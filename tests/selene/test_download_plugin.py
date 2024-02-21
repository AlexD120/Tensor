from tensor.helpers.application import app
import allure


@allure.title('')
@allure.feature('')
@allure.story('')
@allure.label('UI')
@allure.tag('smoke')
@allure.severity('')
@allure.label("owner", "Davydov")
def test_download_plugin_file(browser_config):
    # ARRANGE
    app.simple_should_download_plugin.open()

    # ACT
    app.simple_should_download_plugin.open_download_and_choice_category()
    app.simple_should_download_plugin.download_plugin()

    # ASSERT
    app.simple_should_download_plugin.should_size_plugin()
