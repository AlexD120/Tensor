import allure
from selene import browser, have, by
from selene.support.shared.jquery_style import s
from tensor.helpers import base
from tensor.helpers import dates


class SimpleShouldRegionPage:
    def __init__(self):
        self.contact = s('.sbisru-Header__container').s(by.text('Контакты'))
        self.contact_title = s('.sbis_ru-container.sbisru-Contacts__relative')
        self.contacts_of_partners = s('#city-id-2')
        self.partners_name = s('.sbisru-Contacts-List__col')
        self.region_41 = s(by.text('41 Камчатский край'))

    @allure.step('Открыть главную страницу')
    def open(self):
        browser.open('/contacts/26-stavropolskij-kraj?tab=clients')
        return self

    @allure.step('Открыть контакты и выполнить проверку региона')
    def open_contact_and_check_region(self):
        # self.contact.click()
        self.contact_title.should(have.text('Ставропольский край'))
        self.contacts_of_partners.should(have.text('Ставрополь'))
        self.partners_name.should(have.text('СБИС - Ставрополь'))

    @allure.step('Изменить регион на Камчатский край')
    def change_the_region(self):
        self.contact_title.s('.sbis_ru-Region-Chooser__text.sbis_ru-link').click()
        self.region_41.double_click()

    @allure.step('Проверка названия региона и URL')
    def should_region(self):
        self.contact_title.should(have.text('Камчатский край'))
        base.current_and_should_url_page(dates.URL_KAMCH_KRAY)
        self.contacts_of_partners.should(have.text('Петропавловск-Камчатский'))
        self.partners_name.should(have.text('СБИС - Камчатка'))
