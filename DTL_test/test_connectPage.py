from selenium import webdriver
from pageobject.page_connect import connectPage
from logs.Logger import log
import pytest


class TestconnectPage():
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Edge()

    def test_goto_dtl_page(self):
        tgdp = connectPage(self.driver)
        tgdp.goto_dtl_page()
    
    def test_open_lab(self):
        tol = connectPage(self.driver)
        tol.open_lab()

    def test_connect_win(self):
        tcw = connectPage(self.driver)
        tcw.connect_win()

    def test_connect_pr(self):
        tcpr = connectPage(self.driver)
        tcpr.connect_pr()

    def test_connect_pu(self):
        tcpu = connectPage(self.driver)
        tcpu.connect_pu()

    def test_connect_wci(self):
        tci = connectPage(self.driver)
        tci.connect_wci()


if __name__ == '__main__':
    pytest.main(['-s', 'DTL_test/test_connectPage.py'])