from odoo import models, fields

""" Category: Payslips Currencies
    Made By: Maryam Mohamed
    TO DO: This allow Multi Currency option for Payslip  """
class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Payslips Multi Currency'
        
    currency_id = fields.Many2one('res.currency',string="Currency", related='',readonly=False,default=lambda self: self._default_currency_id())

    def _default_currency_id(self):
        return self.env.user.company_id.currency_id

   