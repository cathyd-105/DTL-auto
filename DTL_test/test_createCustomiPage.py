from selenium import webdriver
from pageobject.page_createCustomi import createCustomiPage
from logs.Logger import log
import pytest


class TestcreateCustomiPage():
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Edge()
    
    def test_goto_dtl_page(self):
        tgdp = createCustomiPage(self.driver)
        tgdp.goto_dtl_page()     

    def test_open_lab(self):
        ttl = createCustomiPage(self.driver)
        ttl.open_lab()    

    def test_create_customimage(self):
        tcc = createCustomiPage(self.driver)
        tcc.create_customimage()   

    def test_choose_base(self):
        tsl = createCustomiPage(self.driver)
        tsl.choose_base()

    def test_basic_set(self):
        tcb = createCustomiPage(self.driver)
        tcb.basic_set()

    def test_view_resoure(self):
        tvr = createCustomiPage(self.driver)
        tvr.view_resoure()


if __name__ == '__main__':
    pytest.main(['-s', 'DTL_test/test_createCustomiPage.py'])
    
