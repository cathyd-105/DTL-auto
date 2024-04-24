from selenium import webdriver
from pageobject.page_createFormula import createFormulaPage
import pytest


class TestmyVmPage():
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Edge()

    def test_goto_dtl_page(self):
        tgdp = createFormulaPage(self.driver)
        tgdp.goto_dtl_page()

    # def test_create_for(self):
    #     tcv = createFormulaPage(self.driver)
    #     tcv.create_for()

    # def test_choose_base(self):
    #     tcb = createFormulaPage(self.driver)
    #     tcb.choose_base()

    # def test_create_forvm(self):
    #     tcf = createFormulaPage(self.driver)
    #     tcf.create_forvm()

    def test_update_for(self):
        tuf = createFormulaPage(self.driver)
        tuf.update_for()


if __name__ == '__main__':
    pytest.main(['-s', 'DTL_test/test_createFormulaPage.py'])