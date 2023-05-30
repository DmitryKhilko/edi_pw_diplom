import allure
from pytest import mark

from conftest import login_service, persons_service
from data.persons_data_api import test_data_can_get_persons, test_data_can_not_get_persons, \
    test_data_can_add_person_valid_param_inside_limits, test_data_can_not_add_person_valid_param_inside_limits, \
    test_data_can_not_add_person_empty_param_required_aib, test_data_can_add_person_valid_param_at_limits, \
    test_data_can_not_add_person_invalid_param_aib, test_data_can_add_person_param_out_of_limits_aib


@allure.label('owner', 'khilko')
@allure.label('layer', 'api')
@allure.label('module', 'Физические лица')
@allure.feature('Список физических лиц')
@allure.link('https://ivc-adsp.ivcmf.by/DefaultCollection/ISEB/_wiki/wikis/ISEB.wiki/32/'
             '%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0-%D1%80%D0%BE%D0%BB%D0%B5%D0%B9', '', 'Матрица ролей')
class TestAPIGetPersons:
    @mark.parametrize('user, message', test_data_can_get_persons)
    @allure.description(
        'Проверка возможности получения списка физических лиц с помощью API-запроса (GET) '
        'для ролей пользователей, которым разрешено получать данный список '
    )
    @allure.id("1362")
    @allure.title('api_Получение списка физ.лиц (у роли есть права)')
    def test_api_can_qet_persons(self, user, message):
        csrftoken, sessionid = login_service.login(user, user[0])
        persons_service.can_get_persons(csrftoken, sessionid, message)

    @mark.parametrize('user, message', test_data_can_not_get_persons)
    @allure.description(
        'Проверка отказа в получении списка физических лиц с помощью API-запроса (GET) '
        'для ролей пользователей, которым запрещено получать данный список'
    )
    @allure.id("1355")
    @allure.title('api_Отказ в получении списка физ.лиц (у роли нет прав)')
    def test_api_can_not_qet_persons(self, user, message):
        csrftoken, sessionid = login_service.login(user, user[0])
        persons_service.can_not_get_persons(csrftoken, sessionid, message)


@allure.label('owner', 'khilko')
@allure.label('layer', 'api')
@allure.label('module', 'Физические лица')
@allure.feature('Создание физического лица')
@allure.link('https://ivc-adsp.ivcmf.by/DefaultCollection/ISEB/_wiki/wikis/ISEB.wiki/32/'
             '%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0-%D1%80%D0%BE%D0%BB%D0%B5%D0%B9', '', 'Матрица ролей')
class TestAPICreatePerson:
    @mark.parametrize('user, data, message', test_data_can_add_person_valid_param_inside_limits)
    @allure.description(
        'Проверка возможности создания физического лица с помощью API-запроса (POST) для ролей пользователей, '
        'которым разрешено создание физического лица . Для создания физического лица используются комбинации '
        'валидных значений параметров, которые по длине находятся внутри нижней и верхней границы значений '
        'параметра'
    )
    @allure.id("1361")
    @allure.title('api_Создание физ.лица (у роли есть права; валидные значения параметров внутри границ)')
    def test_api_can_add_person_valid_param_inside_limits(self, user, data, message, sql_delete_person):
        csrftoken, sessionid = login_service.login(user, user[0])
        persons_service.can_add_person_valid_param(csrftoken, sessionid, data, message)

    @mark.parametrize('user, data, message', test_data_can_add_person_valid_param_at_limits)
    @allure.description(
        'Проверка возможности создания физического лица с помощью API-запроса (POST) для ролей пользователей, '
        'которым разрешено создание физического лица. Для создания физического лица используются комбинации '
        'валидных значений параметров, которые по длине находятся на нижней (а так же нижняя + 1) и верхней '
        '( а так же верхняя - 1) границах значений параметра'
    )
    @allure.id("1367")
    @allure.title('api_Создание физ.лица (у роли есть права; валидные значения параметров на границах)')
    def test_api_can_add_person_valid_param_at_limits(self, user, data, message, sql_delete_person):
        csrftoken, sessionid = login_service.login(user, user[0])
        persons_service.can_add_person_valid_param(csrftoken, sessionid, data, message)

    @mark.parametrize('user, data, message', test_data_can_not_add_person_valid_param_inside_limits)
    @allure.description(
        'Проверка отказа в создании физического лица с помощью API-запроса (POST) для пользователей '
        'с ролями, которым запрещено создание физического лица. Для попытки создания физического лица '
        'используются комбинации валидных значений параметров, которые по длине находятся внутри нижней и '
        'верхней границы значений параметра'
    )
    @allure.id("1356")
    @allure.title('api_Отказ в создании физ.лица (у роли нет прав; валидные значения параметров внутри границ)')
    def test_api_can_not_add_person_valid_param_inside_limits(self, user, data, message, sql_delete_person):
        csrftoken, sessionid = login_service.login(user, user[0])
        persons_service.can_not_add_person_valid_param(csrftoken, sessionid, data, message)

    @mark.parametrize('user, data, message', test_data_can_not_add_person_empty_param_required_aib)
    @allure.description(
        'Проверка отказа в создании физического лица с помощью API-запроса (POST) под ролью АИБ '
        'при использовании пустых значений параметров, которые обязательны для заполнения'
    )
    @allure.id("1363")
    @allure.title('api_Отказ в создании физ.лица (роль АИБ; пустые значения обязательных параметров)')
    def test_api_can_not_add_person_empty_param_required_aib(self, user, data, message, sql_delete_person):
        csrftoken, sessionid = login_service.login(user, user[0])
        persons_service.can_not_add_person_empty_param_required(csrftoken, sessionid, data, message)

    @mark.parametrize('user, data, message', test_data_can_not_add_person_invalid_param_aib)
    @allure.description(
        'Проверка отказа в создании физического лица с помощью API-запроса (POST) под ролью АИБ '
        'при использовании не валидных значений параметров, которые по длине находятся внутри нижней и '
        'верхней границы значений параметра'
    )
    @allure.id("1368")
    @allure.title('api_Отказ в создании физ.лица (роль АИБ; не валидные значения параметров)')
    def test_api_can_not_add_person_invalid_param_aib(self, user, data, message, sql_delete_person):
        csrftoken, sessionid = login_service.login(user, user[0])
        persons_service.can_not_add_person_invalid_param(csrftoken, sessionid, data, message)

    @mark.parametrize('user, data, message', test_data_can_add_person_param_out_of_limits_aib)
    @allure.description(
        'Проверка отказа в создании физического лица с помощью API-запроса (POST) под ролью АИБ '
        'при использовании комбинаций значений параметров, состоящих из валидных или не валидных символов, '
        'которые по длине вышли за нижнюю или верхнюю границу параметра'
    )
    @allure.id("1369")
    @allure.title('api_Отказ в создании физ.лица (роль АИБ; значения параметров вне границ)')
    def test_api_can_not_add_person_param_out_of_limits_aib(self, user, data, message, sql_delete_person):
        csrftoken, sessionid = login_service.login(user, user[0])
        persons_service.can_not_add_person_param_out_of_limits(csrftoken, sessionid, data, message)