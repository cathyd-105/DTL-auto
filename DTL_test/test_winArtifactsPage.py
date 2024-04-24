from selenium import webdriver
from pageobject.page_winArtifacts import winArtifactsPage
from logs.Logger import log
import pytest


class TestautoShutdownPage():
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Edge()

    def test_goto_dtl_page(self):
        tgdp = winArtifactsPage(self.driver)
        tgdp.goto_dtl_page()
    
    # def test_goto_winvm(self):
    #     tpl = winArtifactsPage(self.driver)
    #     tpl.goto_winvm()

    # def test_apply_art(self):
    #     taa = winArtifactsPage(self.driver)
    #     taa.apply_art()

    def test_connect(self):
        tc = winArtifactsPage(self.driver)
        tc.connect()

if __name__ == '__main__':
    pytest.main(["-s", "DTL_test/test_winArtifactsPage.py"])