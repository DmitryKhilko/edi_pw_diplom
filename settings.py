# settings.py
import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = os.environ.get('BASE_URL')

LOGIN_AIB = os.environ.get('LOGIN_AIB')
PASSWORD_AIB = os.environ.get('PASSWORD_AIB')
EMAIL_ACCOUNT_AIB = os.environ.get('EMAIL_ACCOUNT_AIB')

LOGIN_AIS = os.environ.get('LOGIN_AIS')
PASSWORD_AIS = os.environ.get('PASSWORD_AIS')
EMAIL_ACCOUNT_AIS = os.environ.get('EMAIL_ACCOUNT_AIS')

LOGIN_ASH = os.environ.get('LOGIN_ASH')
PASSWORD_ASH = os.environ.get('PASSWORD_ASH')
EMAIL_ACCOUNT_ASH = os.environ.get('EMAIL_ACCOUNT_ASH')

LOGIN_PSH = os.environ.get('LOGIN_PSH')
PASSWORD_PSH = os.environ.get('PASSWORD_PSH')
EMAIL_ACCOUNT_PSH = os.environ.get('EMAIL_ACCOUNT_PSH')

LOGIN_AMNS = os.environ.get('LOGIN_AMNS')
PASSWORD_AMNS = os.environ.get('PASSWORD_AMNS')
EMAIL_ACCOUNT_AMNS = os.environ.get('EMAIL_ACCOUNT_AMNS')

LOGIN_OAMNS = os.environ.get('LOGIN_OAMNS')
PASSWORD_OAMNS = os.environ.get('PASSWORD_OAMNS')
EMAIL_ACCOUNT_OAMNS = os.environ.get('EMAIL_ACCOUNT_OAMNS')

LOGIN_RAMNS = os.environ.get('LOGIN_RAMNS')
PASSWORD_RAMNS = os.environ.get('PASSWORD_RAMNS')
EMAIL_ACCOUNT_RAMNS = os.environ.get('EMAIL_ACCOUNT_RAMNS')

LOGIN_PMNS = os.environ.get('LOGIN_PMNS')
PASSWORD_PMNS = os.environ.get('PASSWORD_PMNS')
EMAIL_ACCOUNT_PMNS = os.environ.get('EMAIL_ACCOUNT_PMNS')

LOGIN_AGTK = os.environ.get('LOGIN_AGTK')
PASSWORD_AGTK = os.environ.get('PASSWORD_AGTK')
EMAIL_ACCOUNT_AGTK = os.environ.get('EMAIL_ACCOUNT_AGTK')

LOGIN_PGTK = os.environ.get('LOGIN_PGTK')
PASSWORD_PGTK = os.environ.get('PASSWORD_PGTK')
EMAIL_ACCOUNT_PGTK = os.environ.get('EMAIL_ACCOUNT_PGTK')
