# -*- coding: utf-8 -*-
{
    'name': "Payslip Multi Currency",

    'summary': "Payslip multi Currency",

    'description': """
        This module gives multi currency option for payslips
    """,
    'author': "Maryam Mohamed Sobhy",
    'website': "",
    "license": "LGPL-3",
    'category': 'Extra Tools',
    'version': '17.0.0.1',
    'depends': ['hr_contract','hr_payroll'],

    'data': [
        'views/hr_contract.xml',
        'views/report_payslip.xml'
    ],
    
}

