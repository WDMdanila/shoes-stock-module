{
    'name': 'Shoes',
    'version': '0.0.1',
    'summary': """Odoo""",
    'description': 'Shoes module',
    'category': 'Stock',
    'author': 'Gennadii Semenyshyn',
    'company': '',
    'website': "",
    'depends': ['mail'],
    'data': [
        'views/shoes_shoe.xml',
        'views/shoes_brand.xml',
        'views/shoes_model.xml',
        'views/shoes_model_type.xml',
        'views/shoes_size.xml',
        'views/shoes_place.xml',
        'views/shoes_status.xml',
        'views/shoes_menu.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
