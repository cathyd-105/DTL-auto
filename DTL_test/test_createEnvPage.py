from selenium import webdriver
from pageobject.page_createEnv import createEnvPage
from logs.Logger import log
import pytest


class TestcreateEnvPage():
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Edge()
        log.logger.info('测试创建env页面')

    def test_goto_dtl_page(self):
        tgdp = createEnvPage(self.driver)
        tgdp.goto_dtl_page()
        log.logger.info('打开lab页面')
    
    def test_create_env(self):
        tcv = createEnvPage(self.driver)
        tcv.create_env()
        log.logger.info('打开add')

    def test_type_parameter(self):
        ttp = createEnvPage(self.driver)
        ttp.type_parameter()
        log.logger.info('输入值')

    def test_open_new(self):
        ton = createEnvPage(self.driver)
        ton.open_new()
        
    def test_copy_value(self):
        tcv = createEnvPage(self.driver)
        tcv.copy_value()

    # 只创建一个环境注释掉以下三个
    def test_change_identity(self):
        ci = createEnvPage(self.driver)
        ci.change_identity()

    def test_create_env2(self):
        tce2 = createEnvPage(self.driver)
        tce2.create_env2()
        
    def test_view_log(self):
        tvl = createEnvPage(self.driver)
        tvl.view_log()

    def test_delete_en(self):
        tde = createEnvPage(self.driver)
        tde.delete_en()


    
if __name__ == '__main__':
    pytest.main(['DTL_test/test_createEnvPage.py'])