from selenium import webdriver
from pageobject.page_autoShutdown import autoShutdownPage
from logs.Logger import log
import pytest


class TestautoShutdownPage():
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Edge()

    def test_goto_dtl_page(self):
        tgdp = autoShutdownPage(self.driver)
        tgdp.goto_dtl_page()
    
    def test_set_autoshutdown(self):
        tcv = autoShutdownPage(self.driver)
        tcv.set_autoshutdown()

    def test_set_emailshutdown(self):
        tse = autoShutdownPage(self.driver)
        tse.set_emailshutdown()

    def test_set_webhook(self):
        tsw = autoShutdownPage(self.driver)
        tsw.set_webhook()


if __name__ == '__main__':
    pytest.main(['DTL_test/test_autoShutdownPage.py'])