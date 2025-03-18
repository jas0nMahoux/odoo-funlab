{
    'name': 'Session Manager',
    'version': '1.0',
    'summary': 'Gère les sessions de musi-quizz',
    'category': 'Tools',
    'author': 'Jason MAHOUX',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/session_views.xml',
        'data/cron_jobs.xml'
    ],
    'installable': True,
    'application': True,
}