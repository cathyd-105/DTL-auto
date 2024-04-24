from selenium import webdriver
from pageobject.page_pinandValid import pinandValidPage
from logs.Logger import log
import pytest


class TestautoShutdownPage():
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Edge()

    def test_goto_dtl_page(self):
        tgdp = pinandValidPage(self.driver)
        tgdp.goto_dtl_page()
    
    def test_pin_lab(self):
        tpl = pinandValidPage(self.driver)
        tpl.pin_lab()

    def test_parameter_valid(self):
        tgdp = pinandValidPage(self.driver)
        tgdp.parameter_valid()
    


if __name__ == '__main__':
    pytest.main(['DTL_test/test_pinandValidPage.py'])