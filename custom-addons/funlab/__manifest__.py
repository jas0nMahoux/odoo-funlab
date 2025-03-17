{
    'name': 'Appointment Manager',
    'version': '1.0',
    'summary': 'Gère les rendez-vous externes',
    'category': 'Tools',
    'author': 'Votre Nom',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/appointment_views.xml',
        'data/cron_jobs.xml'
    ],
    'installable': True,
    'application': True,
}