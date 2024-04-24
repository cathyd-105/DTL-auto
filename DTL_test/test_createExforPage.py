from selenium import webdriver
from pageobject.page_createExfor import createExforPage
from logs.Logger import log
import pytest


class TestcreatePrVmPage():
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Edge()
        log.logger.info('测试创建vm页面')

    def test_goto_dtl_page(self):
        tgdp = createExforPage(self.driver)
        tgdp.goto_dtl_page()
    
    def test_open_lab(self):
        tol = createExforPage(self.driver)
        tol.open_lab()

    def test_create_exvmw(self):
        tcew = createExforPage(self.driver)
        tcew.create_exvmw()

    def test_basic_set(self):
        tbs = createExforPage(self.driver)
        tbs.basic_set()
    
    def test_advanced_set(self):
        tas = createExforPage(self.driver)
        tas.advanced_set()

    def test_create_forw(self):
        tcf = createExforPage(self.driver)
        tcf.create_forw()

    def test_create_forvmw(self):
        tcfw = createExforPage(self.driver)
        tcfw.create_forvmw()

    def test_create_exvml(self):
        tcel = createExforPage(self.driver)
        tcel.create_exvml()

    def test_basic_set2(self):
        tbs2 = createExforPage(self.driver)
        tbs2.basic_set2()

    def test_advanced_set2(self):
        tas2 = createExforPage(self.driver)
        tas2.advanced_set2()
  
  
if __name__ == '__main__':
    pytest.main(['-s', 'DTL_test/test_createExforPage.py'])