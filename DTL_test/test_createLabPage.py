from selenium import webdriver
from pageobject.page_createLab import createLabPage
from logs.Logger import log
import pytest


class TestcreateLabPage():
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Edge()
        log.logger.info('测试创建lab页面')
    
    def test_goto_createlab_page(self):
        tgcp = createLabPage(self.driver)
        tgcp.goto_createlab_page()
    
    # def test_select_subscription(self):
    #     tss = createLabPage(self.driver)
    #     tss.select_subscription()    

    # def test_type_rg(self):
    #     ttr = createLabPage(self.driver)
    #     ttr.type_rg()

    # def test_type_labname(self):
    #     ttl = createLabPage(self.driver)
    #     ttl.type_labname()
        
    # def test_select_location(self):
    #     tsl = createLabPage(self.driver)
    #     tsl.select_location()

    # def test_click_button(self):
    #     tcb = createLabPage(self.driver)
    #     tcb.click_button()
            
    def test_validate_resource(self):
        tvr = createLabPage(self.driver)
        tvr.validate_resource()

    def test_create_secret(self):
        tcs = createLabPage(self.driver)
        tcs.create_secret()

    def test_type_right_parameter(self):
        ttrp = createLabPage(self.driver)
        ttrp.type_right_parameter()
     
    def test_type_failed_parameter(self):
        ttfp = createLabPage(self.driver)
        ttfp.type_failed_parameter()
        

    # @classmethod
    # def teardown_class(self):
    #     self.driver.quit()
    #     log.logger.info('关闭浏览器')


if __name__ == '__main__':
    pytest.main(["-s", "DTL_test/test_createLabPage.py"])
    