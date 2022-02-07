{
    'name' : 'Reprint POS Receipts',
    'version' : '12.0.1.0.0',
    'author' : 'Dominic Krimmer',
    'license': 'AGPL-3',
    'category' : 'Point Of Sale',
    'summary': 'Reprint POS Receipts in the Backend',
    'description' : """
As in the Odoo 10 this feature was kicked, we re-implement it as we think it is quite essential
    """,
    'website': 'https://github.com/dkrimmer84',
    'depends' : ['point_of_sale'],
    'data': ['report/pos_receipt.xml'],
    'installable': True,
}
