{
    'name': "Gic",

    'summary': """Vente des fruits et legumes""",

    'description': """Apps de vente de fruits et legumes""",

    'author': "Gabriel ndjieudja ",
    'website': "http://gabrielhack.pythonanywhere.com",

    'application': '1',
    'version': '0.1',

    'depends': ['base', 'mail', 'stock'],
    'images': ['images/icon.png'],

    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'reports/rapport.xml',
    ],

}
