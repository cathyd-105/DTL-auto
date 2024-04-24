from selenium import webdriver
from pageobject.page_createWinVm import createWinVmPage
from logs.Logger import log
import pytest


class TestcreateWinVmPage():
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Edge()
        log.logger.info('测试创建vm页面')

    def test_goto_dtl_page(self):
        tgdp = createWinVmPage(self.driver)
        tgdp.goto_dtl_page()
        log.logger.info('打开lab页面')
    
    def test_create_vm(self):
        tcv = createWinVmPage(self.driver)
        tcv.create_vm()
        log.logger.info('打开add')

    def test_choose_base(self):
        tcb = createWinVmPage(self.driver)
        tcb.choose_base()
        log.logger.info('选择Windows')

    def test_basic_set(self):
        tbs = createWinVmPage(self.driver)
        tbs.basic_set()

    # def test_connect(self):
    #     tc = createWinVmPage(self.driver)
    #     tc.connect()

    def test_view_resource(self):
        tvr = createWinVmPage(self.driver)
        tvr.view_resource()

  
if __name__ == '__main__':
    pytest.main(["-s", "DTL_test/test_createWinVmPage.py"])