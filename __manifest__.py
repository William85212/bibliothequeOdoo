# -*- coding: utf-8 -*-
{
    'name': "bc_bib",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Jabran",
    'website': "http://www.Jabran.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/book.xml',
        'views/bibliotheque.xml',
        'views/etageres.xml',
        'views/piece.xml',
    ],

    'images': ['static/description/icon.png'],

    'application':True,
}
