# Page urls
LOGIN_PAGE_URL = '/login'
PERSONS_PAGE_URL = '/persons'

# API urls
CSRF_END_POINT = '/api/v1/set-csrf'
LOGIN_END_POINT = '/api/v1/auth/login'
PERSONS_GET_END_POINT = '/api/v1/persons?offset=0&limit=1'  # выводим только одну запись
PERSON_CREATE_END_POINT = '/api/v1/persons'


def persons_update_end_point(person_id):
    return f'/api/v1/persons/{person_id}'
