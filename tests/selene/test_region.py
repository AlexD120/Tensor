from tensor.helpers.application import app
import allure


@allure.title("Тестирование смены региона на сайте СБИС")
@allure.feature("Контакты")
@allure.story("Смена региона на Камчатский край")
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('minor')
@allure.label("owner", "Davydov")
def test_region(browser_config):
    # ARRANGE
    app.simple_should_region_page.open()

    # ACT
    app.simple_should_region_page.open_contact_and_check_region()
    app.simple_should_region_page.change_the_region()

    # ASSERT
    app.simple_should_region_page.should_region()
