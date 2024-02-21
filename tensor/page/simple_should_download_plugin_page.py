import allure
from selene import browser, have, by, be, query
from selene.support.shared.jquery_style import s, ss
from tensor.helpers import base


class SimpleShouldDownloadPluginPage:
    def __init__(self):
        self.button_download_version = s('.sbisru-Footer__container').s(
            by.text('Скачать локальные версии')
        )
        self.category_plugin = s('[data-id="plugin"]')
        self.choice_os = s('[data-id="default"]')
        self.link_to_plugin = ss('.sbis_ru-DownloadNew-loadLink__link')

    @allure.step('Открыть главную страницу')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Перейти в загрузку, выбрать категорию и OS')
    def open_download_and_choice_category(self):
        self.button_download_version.should(be.visible).press_enter()
        self.category_plugin.should(be.clickable).press_enter()
        self.choice_os.should(have.text('Windows')).click()

    @allure.step('Загрузка плагина')
    def download_plugin(self):
        base.download_file(
            self.link_to_plugin.element_by(have.text('Скачать (Exe 7.02 МБ)')).get(
                query.attribute("href")
            )
        )

    @allure.step('Проверка размера файла')
    def should_size_plugin(self):
        base.size_file('./tensor/file/file.exe', 7000000, 8000000)
