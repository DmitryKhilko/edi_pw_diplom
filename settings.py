import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = os.environ.get('BASE_URL')

DATABASE = os.environ.get('DATABASE')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')

ROLE_NAME_AIB = os.environ.get('ROLE_NAME_AIB')
FIO_AIB = os.environ.get('FIO_AIB')
ORGANIZATION_AIB = os.environ.get('ORGANIZATION_AIB')
LOGIN_AIB = os.environ.get('LOGIN_AIB')
PASSWORD_AIB = os.environ.get('PASSWORD_AIB')
EMAIL_ACCOUNT_AIB = os.environ.get('EMAIL_ACCOUNT_AIB')

ROLE_NAME_AIS = os.environ.get('ROLE_NAME_AIS')
FIO_AIS = os.environ.get('FIO_AIS')
ORGANIZATION_AIS = os.environ.get('ORGANIZATION_AIS')
LOGIN_AIS = os.environ.get('LOGIN_AIS')
PASSWORD_AIS = os.environ.get('PASSWORD_AIS')
EMAIL_ACCOUNT_AIS = os.environ.get('EMAIL_ACCOUNT_AIS')

ROLE_NAME_ASH = os.environ.get('ROLE_NAME_ASH')
FIO_ASH = os.environ.get('FIO_ASH')
ORGANIZATION_ASH = os.environ.get('ORGANIZATION_ASH')
LOGIN_ASH = os.environ.get('LOGIN_ASH')
PASSWORD_ASH = os.environ.get('PASSWORD_ASH')
EMAIL_ACCOUNT_ASH = os.environ.get('EMAIL_ACCOUNT_ASH')

ROLE_NAME_PSH = os.environ.get('ROLE_NAME_PSH')
FIO_PSH = os.environ.get('FIO_PSH')
ORGANIZATION_PSH = os.environ.get('ORGANIZATION_PSH')
LOGIN_PSH = os.environ.get('LOGIN_PSH')
PASSWORD_PSH = os.environ.get('PASSWORD_PSH')
EMAIL_ACCOUNT_PSH = os.environ.get('EMAIL_ACCOUNT_PSH')

ROLE_NAME_AMNS = os.environ.get('ROLE_NAME_AMNS')
FIO_AMNS = os.environ.get('FIO_AMNS')
ORGANIZATION_AMNS = os.environ.get('ORGANIZATION_AMNS')
LOGIN_AMNS = os.environ.get('LOGIN_AMNS')
PASSWORD_AMNS = os.environ.get('PASSWORD_AMNS')
EMAIL_ACCOUNT_AMNS = os.environ.get('EMAIL_ACCOUNT_AMNS')

ROLE_NAME_OAMNS = os.environ.get('ROLE_NAME_OAMNS')
FIO_OAMNS = os.environ.get('FIO_OAMNS')
ORGANIZATION_OAMNS = os.environ.get('ORGANIZATION_OAMNS')
LOGIN_OAMNS = os.environ.get('LOGIN_OAMNS')
PASSWORD_OAMNS = os.environ.get('PASSWORD_OAMNS')
EMAIL_ACCOUNT_OAMNS = os.environ.get('EMAIL_ACCOUNT_OAMNS')

ROLE_NAME_RAMNS = os.environ.get('ROLE_NAME_RAMNS')
FIO_RAMNS = os.environ.get('FIO_RAMNS')
ORGANIZATION_RAMNS = os.environ.get('ORGANIZATION_RAMNS')
LOGIN_RAMNS = os.environ.get('LOGIN_RAMNS')
PASSWORD_RAMNS = os.environ.get('PASSWORD_RAMNS')
EMAIL_ACCOUNT_RAMNS = os.environ.get('EMAIL_ACCOUNT_RAMNS')

ROLE_NAME_PMNS = os.environ.get('ROLE_NAME_PMNS')
FIO_PMNS = os.environ.get('FIO_PMNS')
ORGANIZATION_PMNS = os.environ.get('ORGANIZATION_PMNS')
LOGIN_PMNS = os.environ.get('LOGIN_PMNS')
PASSWORD_PMNS = os.environ.get('PASSWORD_PMNS')
EMAIL_ACCOUNT_PMNS = os.environ.get('EMAIL_ACCOUNT_PMNS')

ROLE_NAME_AGTK = os.environ.get('ROLE_NAME_AGTK')
FIO_AGTK = os.environ.get('FIO_AGTK')
ORGANIZATION_AGTK = os.environ.get('ORGANIZATION_AGTK')
LOGIN_AGTK = os.environ.get('LOGIN_AGTK')
PASSWORD_AGTK = os.environ.get('PASSWORD_AGTK')
EMAIL_ACCOUNT_AGTK = os.environ.get('EMAIL_ACCOUNT_AGTK')

ROLE_NAME_PGTK = os.environ.get('ROLE_NAME_PGTK')
FIO_PGTK = os.environ.get('FIO_PGTK')
ORGANIZATION_PGTK = os.environ.get('ORGANIZATION_PGTK')
LOGIN_PGTK = os.environ.get('LOGIN_PGTK')
PASSWORD_PGTK = os.environ.get('PASSWORD_PGTK')
EMAIL_ACCOUNT_PGTK = os.environ.get('EMAIL_ACCOUNT_PGTK')
