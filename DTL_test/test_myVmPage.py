from selenium import webdriver
from pageobject.page_myVm import myVmPage
import pytest


class TestmyVmPage():
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Edge()

    def test_goto_dtl_page(self):
        tgdp = myVmPage(self.driver)
        tgdp.goto_dtl_page()

    def test_create_vm(self):
        tcv = myVmPage(self.driver)
        tcv.create_vm()

    def test_type_parameter(self):
        ttp = myVmPage(self.driver)
        ttp.type_parameter()

    def test_management_time(self):
        tmt = myVmPage(self.driver)
        tmt.management_time()

    def test_change_time(self):
        tst = myVmPage(self.driver)
        tst.change_time()


if __name__ == '__main__':
    pytest.main(['-s', 'DTL_test/test_myVmPage.py'])