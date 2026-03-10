{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Manage Students and Print Reports',
    'description': 'A module to manage student records and generate PDF certificates.',
    'category': 'Education',
    'author': 'Soufianee',
    'depends': ['base'], 
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/pfe_views.xml',
        'reports/pfe_report.xml',
    ],
    'installable': True,
    'application': True,
}