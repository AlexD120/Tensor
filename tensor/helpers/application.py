from tensor.page.simple_should_photo_page import SimpleShouldPhotoPage
from tensor.page.simple_should_region_page import SimpleShouldRegionPage
from tensor.page.simple_should_download_plugin_page import (
    SimpleShouldDownloadPluginPage,
)


class ApplicationUa:
    def __init__(self):
        self.simple_should_param_photo = SimpleShouldPhotoPage()
        self.simple_should_region_page = SimpleShouldRegionPage()
        self.simple_should_download_plugin = SimpleShouldDownloadPluginPage()


app = ApplicationUa()
