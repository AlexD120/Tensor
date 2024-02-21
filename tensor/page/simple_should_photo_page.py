import allure
from selene import browser, have, by
from selene.support.shared.jquery_style import s, ss
from tensor.helpers import base
from tensor.helpers import dates


class SimpleShouldPhotoPage:
    def __init__(self):
        self.contact = s('.sbisru-Header__container').s(by.text('Контакты'))
        self.tensor_logo = s('#contacts_clients').s('.sbisru-Contacts__logo-tensor')
        self.should_block_strength = s('.tensor_ru-Index__block4-bg')
        self.button_more_detailed = s('.tensor_ru-Index__block4-bg').s(
            '.tensor_ru-link'
        )
        self.photo_working = ss('.tensor_ru-About__block3-image-wrapper')

    @allure.step('Открыть главную страницу')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Открыть контакты и перейти на сайт "tensor"')
    def open_contact_and_transition(self):
        self.contact.click()
        self.tensor_logo.execute_script('element.target = "_self"')
        self.tensor_logo.click()

    @allure.step('Проверить блок и открыть подробнее')
    def open_tensor_website(self):
        self.should_block_strength.should(have.text('Сила в людях'))
        self.button_more_detailed.should(have.text('Подробнее')).press_enter()

    @allure.step('Проверка URL и параметров фото')
    def should_param_photo(self):
        base.current_and_should_url_page(dates.URL_TENSOR_ABOUT)
        self.photo_working.element(have.attribute('width', dates.WIDTH))
        self.photo_working.element(have.attribute('height', dates.HEIGHT))
