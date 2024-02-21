from tensor.helpers.application import app
import allure


@allure.title('')
@allure.feature('')
@allure.story('')
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('')
@allure.label("owner", "Davydov")
def test_photo_parameters(browser_config):
    # ARRANGE
    app.simple_should_param_photo.open()

    # ACT
    app.simple_should_param_photo.open_contact_and_transition()
    app.simple_should_param_photo.open_tensor_website()

    # ASSERT
    app.simple_should_param_photo.should_param_photo()
