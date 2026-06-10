
from odoo import fields, models, _
from odoo.exceptions import UserError, ValidationError


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'
    
    def _prepare_line_values(self, line, account_id, date, debit, credit):
        res = super()._prepare_line_values(line, account_id, date, debit, credit)
        partner = self.employee_id.work_contact_id
        # Get the company currency and check if the line has a different currency
        currency_id=line.currency_id.id
        company_currency = self.company_id.currency_id
        line_currency = self.env['res.currency'].browse(currency_id)
        # Update the result dictionary with the converted values

         # If the line has a different currency, convert the amount to the company's currency
        if line_currency != company_currency:
            converted_debit = line_currency._convert(debit, company_currency, self.company_id, date)
            converted_credit = line_currency._convert(credit, company_currency, self.company_id, date)
        else:
            # If the currency is the same as the company's, no conversion is needed
            converted_debit = debit
            converted_credit = credit
        res.update({
            # 'amount_currency': line.total,
            'partner_id': partner.id,
            'debit': converted_debit,
            'credit': converted_credit,
            'amount_currency': debit - credit,  # Amount in the line's currency
            'currency_id': line_currency.id if line_currency != company_currency else company_currency.id,
        })
        
        return res
    
    
    
   
    def _prepare_adjust_line(self, line_ids, adjust_type, debit_sum, credit_sum, date):
        acc_id = self.sudo().journal_id.default_account_id.id
        partner =  self.employee_id.work_contact_id
        # Get the company currency and the line currency
        currency_id =self.line_ids.currency_id.id
        company_currency = self.env.user.company_id.currency_id
        line_currency = self.env['res.currency'].browse(currency_id)
        if not acc_id:
            raise UserError(_('The Expense Journal "%s" has not properly configured the default Account!', self.journal_id.name))
        existing_adjustment_line = (
            line_id for line_id in line_ids if line_id['name'] == _('Adjustment Entry')
        )
        adjust_credit = next(existing_adjustment_line, False)

        # If the line has a different currency, convert the amounts to the company's currency
        if line_currency != company_currency:
            debit_converted = line_currency._convert(credit_sum - debit_sum if adjust_type == 'debit' else 0.0, company_currency, self.env.user.company_id, date)
            credit_converted = line_currency._convert(debit_sum - credit_sum if adjust_type == 'credit' else 0.0, company_currency, self.env.user.company_id, date)
        else:
            debit_converted = credit_sum - debit_sum if adjust_type == 'debit' else 0.0
            credit_converted = debit_sum - credit_sum if adjust_type == 'credit' else 0.0

        if not adjust_credit:
            adjust_credit = {
                'name': _('Adjustment Entry'),
                'partner_id': partner.id,
                'account_id': acc_id,
                'journal_id': self.journal_id.id,
                'date': date,
                'debit': debit_converted,
                'credit': credit_converted,
                'amount_currency': credit_sum - debit_sum if adjust_type == 'debit' else debit_sum - credit_sum,  # Amount in the line's original currency
                'currency_id': line_currency.id if line_currency != company_currency else company_currency.id,


            }
            line_ids.append(adjust_credit)
        else:
            adjust_credit['credit'] = debit_sum - credit_sum

  