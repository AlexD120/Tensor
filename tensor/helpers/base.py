import requests
from selene import browser
import os


def current_and_should_url_page(value):
    current_url = browser.config.driver.current_url
    key = current_url
    assert key == value


def assert_value(value1, value2):
    assert value1 == value2


def assert_text_in_element(value1, value2):
    assert value1 in value2


def check_attributes(value1, value2, value3):
    for element in value1:
        width_attribute_value = element.get_attribute(value2)
        assert width_attribute_value == value3


def size_file(path, min_size, max_size):
    file_path = path
    file_size = os.path.getsize(file_path)
    min_size = min_size
    max_size = max_size

    assert min_size <= file_size <= max_size


def download_file(link):
    download = link
    current_directory = os.path.dirname(os.path.abspath(__file__))
    relative_path = '../file'
    download_path = os.path.join(current_directory, relative_path, 'file.exe')
    os.makedirs(os.path.dirname(download_path), exist_ok=True)
    response = requests.get(download)
    if response.status_code == 200:
        with open(download_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f'Ошибка при скачивании файла. Код статуса: {response.status_code}')
