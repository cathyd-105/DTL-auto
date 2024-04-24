from selenium import webdriver
from pageobject.page_createPrVm import createPrVmPage
from logs.Logger import log
import pytest


class TestcreatePrVmPage():
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Edge()
        log.logger.info('测试创建vm页面')

    def test_goto_dtl_page(self):
        tgdp = createPrVmPage(self.driver)
        tgdp.goto_dtl_page()
        log.logger.info('打开lab页面')
    
    # def test_create_vm(self):
    #     tcv = createPrVmPage(self.driver)
    #     tcv.create_vm()
    #     log.logger.info('打开add')

    # def test_choose_base(self):
    #     tcb = createPrVmPage(self.driver)
    #     tcb.choose_base()
    #     log.logger.info('选择Windows')

    # def test_basic_set(self):
    #     tbs = createPrVmPage(self.driver)
    #     tbs.basic_set()
    
    # def test_advanced_set(self):
    #     tas = createPrVmPage(self.driver)
    #     tas.advanced_set()

    # def test_connection(self):
    #     tc = createPrVmPage(self.driver)
    #     tc.connect()

    def test_view_resource(self):
        tc = createPrVmPage(self.driver)
        tc.view_resource()
  
  
if __name__ == '__main__':
    pytest.main(['-s', 'DTL_test/test_createPrVmPage.py'])