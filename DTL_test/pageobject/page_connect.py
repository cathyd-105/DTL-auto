from time import sleep
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


class connectPage(BasePage):
    labname = (By.LINK_TEXT, 'ding1120-e-1')
    vm_win = (By.LINK_TEXT, 'ding-win')
    vm_pr = (By.LINK_TEXT, 'ding-pr000')
    vm_pu = (By.LINK_TEXT, 'ding-pu000')
    vm_wci = (By.LINK_TEXT, 'ding-winci')
    connect_button = (By.XPATH, '//div[@title="Connect"]')
    close_button = (By.XPATH, '//button[@title="Close"]')
    url = 'https://ms.portal.azure.com/?feature.msaljs=false#browse/Microsoft.DevTestLab%2Flabs' 

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 打开页面并最大化
    def goto_dtl_page(self):
        self.open_url(self.url)
        self.driver.maximize_window()

    def open_lab(self):
        # 点击创建的lab
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(self.labname))
        self.click_element(*self.labname)

    def connect_win(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(self.vm_win))
        self.click_element(*self.vm_win)
        # 点击连接
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(self.connect_button))
        self.click_element(*self.connect_button)
        sleep(5)
        pyautogui.click(1150, 165, duration=2)
        pyautogui.click(1130, 145, duration=2)
        pyautogui.click(950, 545, duration=2)
        sleep(2)
        pyautogui.typewrite('Dyh19981222')
        sleep(2)
        pyautogui.click(700, 580, duration=2)
        sleep(4)
        pyautogui.click(850, 600, duration=2)
        sleep(3)
        pyautogui.click(1050, 5, duration=2)
        # pyautogui.click(850, 475, duration=2)# 弹框
        sleep(6)
        close = self.locate_elements(self.close_button)
        close[2].click()

    def connect_pr(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(self.vm_pr))
        self.click_element(*self.vm_pr)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(self.connect_button))
        self.click_element(*self.connect_button)
        sleep(5)
        pyautogui.click(1150,165, duration=2)
        pyautogui.click(1130,145, duration=2)
        pyautogui.click(950,545, duration=2)# 点击connect
        sleep(16)
        pyautogui.click(1005,490, duration=2)    
        sleep(5)
        close = self.locate_elements(self.close_button)
        close[2].click()

    def connect_pu(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(self.vm_pu))
        self.click_element(*self.vm_pu)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(self.connect_button))
        self.click_element(*self.connect_button)
        sleep(5)
        pyautogui.click(1150,165, duration=2)
        pyautogui.click(1130,145, duration=2)
        pyautogui.click(950,545, duration=2)# 点击连接
        sleep(2)
        pyautogui.typewrite('Dyh19981222')
        sleep(2)
        pyautogui.click(700,580, duration=2)
        sleep(4)
        pyautogui.click(850,600, duration=2)
        sleep(3)
        pyautogui.click(1050,5, duration=2)# 关闭
        # sleep(1)
        # pyautogui.click(850,475, duration=2)
        sleep(8)
        close = self.locate_elements(self.close_button)
        close[2].click()

    def connect_wci(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(self.vm_wci))
        self.click_element(*self.vm_wci)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.connect_button)))
        self.click_element(*self.connect_button)
        sleep(5)
        pyautogui.click(1150,165, duration=2)
        pyautogui.click(1130,145, duration=2)
        pyautogui.click(950,545, duration=2)
        sleep(2)
        pyautogui.typewrite('Dyh19981222')
        sleep(2)
        pyautogui.click(700,580, duration=2)
        sleep(4)
        pyautogui.click(850,600, duration=2)# yes
        sleep(3)
        pyautogui.click(1050,5, duration=2)# 关闭
        # pyautogui.click(850,475, duration=2)
        # sleep(3)
        # pyautogui.click(1420,140, duration=2)
        sleep(8)
        close = self.locate_elements(self.close_button)
        close[2].click()