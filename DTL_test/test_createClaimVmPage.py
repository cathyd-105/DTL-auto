from selenium import webdriver
from pageobject.page_createClaimVm import createClaimVmPage
from logs.Logger import log
import pytest


class TestcreateClaimVmPage():
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Edge()
        log.logger.info('测试创建vm页面')

    def test_goto_dtl_page(self):
        tgdp = createClaimVmPage(self.driver)
        tgdp.goto_dtl_page()
        log.logger.info('打开lab页面')
    
    def test_create_vm(self):
        tcv = createClaimVmPage(self.driver)
        tcv.create_vm()
        log.logger.info('打开add')

    def test_choose_base(self):
        tcb = createClaimVmPage(self.driver)
        tcb.choose_base()
        log.logger.info('选择Linux')

    def test_basic_set(self):
        tbs = createClaimVmPage(self.driver)
        tbs.basic_set()

    def test_advanced_set(self):
        tbs = createClaimVmPage(self.driver)
        tbs.advanced_set()

    def test_repeat_create(self):
        trc = createClaimVmPage(self.driver)
        trc.repeat_create()

    def test_claim_vm(self):
        tcv = createClaimVmPage(self.driver)
        tcv.claim_vm()


if __name__ == '__main__':
    pytest.main(['DTL_test/test_createClaimVmPage.py'])