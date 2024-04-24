from time import sleep
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pyautogui

class winArtifactsPage(BasePage):
    # 元素定位
    labname = (By.LINK_TEXT, 'ding1020-e-1')
    win_vm = (By.LINK_TEXT, 'ding-win')
    artifacts_button = (By.XPATH, '//div[@title="Artifacts"]')
    apply_artifacts = (By.XPATH, '//div[@title="Apply artifacts"]')
    artifact_list = (By.XPATH, '//span[text()="[Deprecated] Active Directory Domain Join"]')
    input_art = (By.XPATH, '//input[@placeholder="Search to filter available artifacts"]')
    reset_vm_pw = (By.XPATH, '//span[text()="Reset VM Password"]')
    add_artifact = (By.XPATH, '//li[@title="Add artifact"]')
    type_password = (By.XPATH, '//input[@type="password"]')
    saved_pw_bt = (By.XPATH, '//span[@class="azc-fill-text azc-validation-border azc-checkBox-unchecked"]')
    pick_pw = (By.XPATH, '//div[@aria-haspopup="dialog"]')
    close_fork = (By.XPATH, '//button[@title="Close"]')
    password1 = (By.XPATH, '//span[text()="ding"]')
    reset_vm_add = (By.XPATH, '//div[text()="Reset VM Password"]')
    chrome = (By.XPATH,'//span[text()="Chrome"]')
    firefox = (By.XPATH, '//span[text()="Firefox"]')
    add_ok = (By.XPATH , '//div[@aria-label="OK"]')
    left_button = (By.XPATH, '//div[@aria-label="Click to open context menu"]')
    delete_art = (By.XPATH, '//li[@aria-posinset="2"]')
    install = (By.XPATH, '//div[@title="Install"]')
    applyed_text =(By.XPATH, '//span[text()="Succeeded"')
    refresh_button =(By.XPATH, '//div[text()="Refresh"]')
    connect_button = (By.XPATH, '//div[@title="Connect"]')
    shutdown1 = (By.XPATH, '//div[@title="Click to open context menu"]')
    shutdown2 = (By.XPATH, '//div[text()="Stop"]')
    notice = (By.XPATH, '//div[text()="Apply artifacts feature is currently unavailable. This can occur when the virtual machine is stopped or the agent is unresponsive. If the issue persists, refer to the "]')
    url = 'https://ms.portal.azure.com/#browse/Microsoft.DevTestLab%2Flabs'

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_dtl_page(self):
        self.open_url(self.url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.labname)))
        self.click_element(*self.labname)

    def goto_winvm(self, extra_wait=None):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.win_vm)))
        self.click_element(*self.win_vm)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.artifacts_button)))
        self.click_element(*self.artifacts_button)
        # mes = 'Artifacts按钮'
        # try:
        #     WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located(self.artifacts_button))
        #     if extra_wait:
        #         sleep(extra_wait)
        #     print(f"{mes}可见")
        #     return True
        # except Exception as e:
        #     print(f"{mes}不可见.{e}")
        #     return False
        try:
            assert self.locate_element(*self.artifacts_button).is_displayed()==False
            print('test pass')
        except Exception as e:
            print('test fail', format(e))
        sleep(5)
        self.click_element(*self.apply_artifacts)
        sleep(1)
        try:
            assert self.locate_element(*self.apply_artifacts).is_displayed()==False
            print('test pass')
        except Exception as e:
            print('test fail', format(e))
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.artifact_list)))
        self.type_text('Reset VM Password', *self.input_art)
        try:
            assert self.locate_element(*self.reset_vm_pw).is_displayed()==True
            print("Test Parameter Types” in artifact list")
        except Exception as e:
            print('test fail', format(e))
        sleep(2)
        self.click_element(*self.add_artifact)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.type_password)))
        self.type_text('123456', *self.type_password)
        pw = self.locate_elements(*self.saved_pw_bt)
        pw[2].click()
        sleep(2)
        pick = self.locate_elements(*self.pick_pw)
        pick[3].click()
        sleep(2)
        self.click_element(*self.password1)
        close_button = self.locate_elements(*self.close_fork)
        close_button[5].click()
        sleep(2)
        pyautogui.click(870, 165)# 确认键 165
        sleep(1)
        pyautogui.click(870, 165)

    def apply_art(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.reset_vm_pw)))
        self.clear_text(*self.input_art)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.artifact_list)))
        self.type_text('Chrome', *self.input_art)
        sleep(2)
        self.click_element(*self.add_artifact)
        self.click_element(*self.add_ok)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.chrome)))
        self.clear_text(*self.input_art)
        sleep(1)
        try:
            assert self.locate_element(*self.chrome).is_displayed()==True
            print("test pass")
        except Exception as e:
            print('test fail', format(e))    
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.artifact_list)))
        self.type_text('Firefox', *self.input_art)
        sleep(2)
        self.click_element(*self.add_artifact)
        self.click_element(*self.add_ok)
        sleep(2)
        left_circle = self.locate_elements(*self.left_button)
        left_circle[24].click()
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.delete_art)))
        self.click_element(*self.delete_art)
        sleep(1)
        try:
            self.locate_element(*self.chrome)
            print('test failed')
        except NoSuchElementException:
            print('Chrome deleted test pass')    #     return False
        sleep(1)
        self.click_element(*self.install)
        WebDriverWait(self.driver, 200, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//span[text()="Succeeded"]')), 'Succeeded'))
        sleep(3)
        close_button2 = self.locate_elements(*self.close_fork)
        close_button2[3].click()

    def connect(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.win_vm)))
        self.click_element(*self.win_vm)
        sleep(2)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.connect_button)))
        self.click_element(*self.connect_button)
        sleep(5)
        pyautogui.click(1155,165, duration=2)
        pyautogui.click(1140,145, duration=2)
        pyautogui.click(950,545, duration=2)
        sleep(2)
        pyautogui.typewrite('Dyh19981222')
        sleep(2)
        pyautogui.click(700,580, duration=2)
        sleep(4)
        pyautogui.click(850,600, duration=2)# yes
        sleep(25)
        pyautogui.click(1280,750, duration=2)# next
        pyautogui.click(1280,750, duration=2)# accept
        sleep(5)
        pyautogui.click(700,880, duration=2)# 点击输入框
        pyautogui.typewrite('contro')
        sleep(1)
        pyautogui.click(750,280, duration=2)
        pyautogui.click(700,520, duration=2)
        pyautogui.click(650,280, duration=2)# 安装项目列表
        sleep(6)
        pyautogui.click(850,475, duration=2)# 关闭
        sleep(3)
        pyautogui.click(1420,140, duration=2)

    def auto_shutdown(self):
        close_button3 = self.locate_elements(*self.close_fork)
        close_button3[2].click()
        circle = self.locate_elements(*self.shutdown1)
        circle[21].click()
        self.click_element(*self.shutdown2)
        WebDriverWait(self.driver, 120, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//div[text()="Stopped virtual machine"]')), 'Stopped virtual machine'))
        self.click_element(*self.win_vm)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.artifacts_button)))
        self.click_element(*self.artifacts_button)
        sleep(1)
        try:
            assert self.locate_element(*self.notice).is_displayed()==True
            print("Stoped test pass")
        except Exception as e:
            print('test fail', format(e))