# -*- coding: utf-8 -*-
{
    'name': 'Lead Managment Assitant + GPT',
    'summary': """
    Trabajo Final para el curso de TP1
    """,
    'description': """
    Trabajo Final para el curso de TP1
    """,
    'version': '16.0.1.0.0',
    'license': 'LGPL-3',
    'category': 'Productivity/Discuss',
    'author': 'Enzo Livelli - Edison Cabrera',
    'website': 'https://leads-management-landing-hly4.vercel.app/',

    'depends': [
        'base',
        'base_setup',
        'mail_bot',
    ],
    'external_dependencies': {
        'python': ['openai', 'langchain']
    },

    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',

        'views/res_config_settings.xml',
        'views/res_users.xml',

        'views/odoogpt_openai_model.xml',
        'views/odoogpt_openai_log.xml',
        'views/odoogpt_openai_file.xml',
        'views/odoogpt_openai_fine_tune.xml',

        'wizard/odoogpt_openai_model_select_wizard.xml',
        'wizard/odoogpt_openai_file_create_wizard.xml',
        'wizard/odoogpt_openai_fine_tune_create_wizard.xml',

        'views/menu.xml',
    ],

    'assets': {
        'mail.assets_messaging': [
            'odoogpt/static/src/models/*.js',
        ],
    },

    'images': [
        'static/description/cover/odoogpt.png',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
