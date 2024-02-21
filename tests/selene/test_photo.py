from tensor.helpers.application import app
import allure


@allure.title("Тестирование параметров фото на сайте Tensor")
@allure.feature("Главная страница")
@allure.story("Проверка параметров фото сотрудников")
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('minor')
@allure.label("owner", "Davydov")
def test_photo_parameters(browser_config):
    # ARRANGE
    app.simple_should_param_photo.open()

    # ACT
    app.simple_should_param_photo.open_contact_and_transition()
    app.simple_should_param_photo.open_tensor_website()

    # ASSERT
    app.simple_should_param_photo.should_param_photo()
