# import allure
# from pytest import mark
#
# from pages.login_page import Login
# from pages.persons_add_page import Persons
# from data.persons_add_data import person_parameters_aib
#
#
# # уникальное значение при добавлении физического лица: email + card_id + key_id
#
# class TestAddPerson:
#     @mark.parametrize('p01_login, p02_password, p03_first_name, p04_patronymic, p05_last_name, p06_birthday, p07_sex, p08_phone, p09_email, p10_card_id, p11_key_id', person_parameters_aib)
#     @allure.title(f'Добавление физического лица под ролью АИБ')
#     def test_add_person_aib(self, web_app, p01_login, p02_password, p03_first_name, p04_patronymic, p05_last_name, p06_birthday, p07_sex, p08_phone, p09_email, p10_card_id, p11_key_id):
#         Login(web_app).\
#             login_fast(p01_login, p02_password)
#         Persons(web_app).\
#             navigate().\
#             check_goto_persons().\
#             opening_form_add_person().\
#             check_opening_form_add_person().\
#             add_person(p03_first_name, p04_patronymic, p05_last_name, p06_birthday, p07_sex, p08_phone, p09_email, p10_card_id, p11_key_id).\
#             to_be_visible_in_table_add_person(p09_email)
#
#         # login_page = Login(web_app)
#         # login_page.login_fast(p1_login, p2_password)
#         # person_page = Persons(web_app)
#         # person_page.navigate()
#         # person_page.check_goto_persons()
#         # person_page.opening_form_add_person()
#         # person_page.check_opening_form_add_person()
#         # person_page.add_person(p3_first_name, p4_patronymic, p5_last_name, p6_birthday, p7_sex, p8_phone, p9_email, p10_card_id, p11_key_id)
#         # person_page.to_be_visible_in_table_add_person(p9_email)
#
#
