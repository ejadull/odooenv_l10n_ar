# -*- encoding: utf-8 -*-
{
    'name': 'Reportes y funciones para CTMIL',
    'version': '8.0.1.1',
    'category': 'Generic Modules',
    'description': """
    """,
    'author': 'Coop. Trab. Moldeo Interactive Lim.',
    'website': 'http://www.moldeointeractive.com.ar',
    'depends': [
        'account',
        'l10n_ar_invoice',
    ],
    'init_xml': [
    ],
    'update_xml': [
        'reports.xml',
        'security/ctmil_security.xml',
    ],
    'demo_xml': [
    ],
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
