from time import sleep
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

class pinandValidPage(BasePage):
    labname = (By.LINK_TEXT, 'ding0925-e-2')
    pin_blade = (By.XPATH, '//button[@title="Pin blade to dashboard"]')
    dashboard_select = (By.XPATH, '//div[@aria-label="Select dashboard"]')
    my_dash = (By.XPATH, '//div[@aria-posinset="3"]')
    pin_button = (By.XPATH, '//div[@title="Pin"]')
    home_page = (By.LINK_TEXT, 'Home')
    navigate_text = (By.XPATH, '//h3[text()="Navigate"]')
    dashboard = (By.LINK_TEXT, 'Dashboard')
    lab_button = (By.XPATH, '//div[@role="group"]')
    add = (By.XPATH, '//div[@aria-label="Add"]')
    input_box = (By.XPATH, '//input[@placeholder="Search to filter available bases"]')
    win_base = (By.LINK_TEXT, 'Windows 11 Enterprise (x64) (Microsoft Dev Box Compatible)')
    vm_name = (By.XPATH, '//input[@aria-label="Virtual machine name"]')
    username = (By.XPATH, '//input[@type="text"]')
    secret_saved = (By.XPATH, '/html/body/div[1]/div[4]/main/div[3]/div[2]/section[3]/div[1]/div[1]/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[5]/div[3]/div[2]/div/div/span')
    secret_list = (By.XPATH, '//span[@role="button"]')
    password = (By.XPATH, '//div[@role="treeitem"]')
    type_password = (By.XPATH, '//input[@placeholder="Password"]')
    close_fork = (By.XPATH, '//button[@title="Close"]')
    suse_base = (By.LINK_TEXT, 'SUSE Enterprise Linux 15 SP4 +24x7 Support')
    url = 'https://ms.portal.azure.com/#browse/Microsoft.DevTestLab%2Flabs'

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_dtl_page(self):
        self.open_url(self.url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.labname)))
        self.click_element(*self.labname)

    def pin_lab(self):
        WebDriverWait(self.driver, 50, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//div[text()="Add"]')), 'Add'))
        pin = self.locate_elements(*self.pin_blade)
        pin[1].click()
        sleep(2)
        self.click_element(*self.dashboard_select)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.my_dash)))
        self.click_element(*self.my_dash)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.pin_button)))
        self.click_element(*self.pin_button)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.home_page)))
        self.click_element(*self.home_page)
        sleep(3)
        pyautogui.click(1525, 700)
        self.click_element(*self.dashboard)
        WebDriverWait(self.driver, 50, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//div[text()="Create"]')), 'Create'))
        self.click_element(*self.lab_button)

    def parameter_valid(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.add)))
        self.click_element(*self.add)
        WebDriverWait(self.driver, 100, 0.5).until(EC.presence_of_element_located((self.win_base)))
        self.type_text('win', *self.input_box)
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.win_base)))
        self.click_element(*self.win_base)
        WebDriverWait(self.driver, 30, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//span[text()='Basic_A3']")), 'Basic_A3'))
        self.clear_text(*self.vm_name)
        # 输入vm名
        self.type_text('1', *self.vm_name)
        sleep(1)
        self.clear_text(*self.vm_name)
        self.type_text('a b', *self.vm_name)
        sleep(1)
        self.clear_text(*self.vm_name)
        self.type_text('a$', *self.vm_name)
        sleep(1)
        self.clear_text(*self.vm_name)
        self.type_text('a-', *self.vm_name)
        sleep(1)
        self.clear_text(*self.vm_name)
        self.type_text('a234567890123456', *self.vm_name)
        self.clear_text(*self.vm_name)
        # 有效的vm名
        sleep(2)
        self.type_text('aaa', *self.vm_name)
        sleep(1)
        self.clear_text(*self.vm_name)
        self.type_text('a-b', *self.vm_name)
        sleep(1)
        self.clear_text(*self.vm_name)
        self.type_text('1a1', *self.vm_name)
        sleep(1)
        self.clear_text(*self.vm_name)
        self.type_text('a23456789012345', *self.vm_name)
        # 无效的用户名
        sleep(2)
        user_name = self.locate_elements(*self.username)
        user_name[10].clear()
        user_name[10].send_keys('a')
        sleep(1)
        user_name[10].clear()
        user_name[10].send_keys('user')
        sleep(1)
        user_name[10].clear()
        user_name[10].send_keys('admin')
        sleep(1)
        user_name[10].clear()
        user_name[10].send_keys('david')
        sleep(1)
        user_name[10].clear()
        user_name[10].send_keys('abcdefghijklmnopqrstu')
        user_name[10].clear()
        # 有效的用户名
        sleep(2)
        user_name[10].send_keys('ab')
        sleep(1)
        user_name[10].clear()
        user_name[10].send_keys('local')
        sleep(1)
        user_name[10].clear()
        user_name[10].send_keys('abcdefghijklmnopqrst')
        sleep(3)
        self.click_element(*self.secret_saved) 
        # 点击下拉框
        # WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.secret_list)))
        s = self.locate_elements(*self.secret_list)
        s[3].click()
        # 点击密码
        drop_down_boxes2 = self.locate_elements(*self.password)
        drop_down_boxes2[0].click()
        sleep(2)
        self.click_element(*self.secret_saved) 
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.type_password)))
        # 无效的密码
        self.type_text('a', *self.type_password)
        sleep(1)
        self.clear_text(*self.type_password)
        self.type_text('password', *self.type_password)
        sleep(1)
        self.clear_text(*self.type_password)
        self.type_text('A', *self.type_password)
        sleep(1)
        self.clear_text(*self.type_password)
        self.type_text('A2345678', *self.type_password)
        sleep(1)
        self.clear_text(*self.type_password)
        self.type_text('b2345678', *self.type_password)
        sleep(1)
        self.clear_text(*self.type_password)
        self.type_text('.2345678', *self.type_password)
        # 有效的密码
        sleep(2)
        self.clear_text(*self.type_password)
        self.type_text('Ab345678', *self.type_password)
        sleep(1)
        self.clear_text(*self.type_password)
        self.type_text('A.345678', *self.type_password)
        sleep(1)
        self.clear_text(*self.type_password)
        self.type_text('Ab######', *self.type_password)

        # linux检验参数
        sleep(2)
        close_button = self.locate_elements(*self.close_fork)
        close_button[2].click()
        sleep(2)
        pyautogui.click(940, 165)
        sleep(1)
        pyautogui.click(940, 165)# 取消键
        sleep(1)
        close_button = self.locate_elements(*self.close_fork)
        close_button[2].click()
        pyautogui.click(860, 165)
        sleep(1)
        pyautogui.click(860, 165)# 确认键
        target = self.locate_element(*self.input_box)
        self.driver.execute_script('arguments[0].scrollIntoView();', target)
        self.clear_text(*self.input_box)
        self.type_text('suse', *self.input_box)
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.suse_base)))
        self.click_element(*self.suse_base)
        WebDriverWait(self.driver, 30, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//span[text()='Basic_A3']")), 'Basic_A3'))
        # 输入无效的linux名
        self.clear_text(*self.vm_name)
        self.type_text('asdfasdfasdfasdfafasdfasdfasfdasfdsadfasdfasdfasdfasasdfaaasdfa', *self.vm_name)
        sleep(1)
        self.clear_text(*self.vm_name)
        self.type_text('asdfasdfasdfasdfafasdfasdfasfdasfdsadfasdfasdfasdfasasdfaaasdf', *self.vm_name)
        sleep(1)
        # 输入无效的用户名
        user_name = self.locate_elements(*self.username)
        user_name[10].clear()
        user_name[10].send_keys('abcdefghijklmnopqrstuasdfasdfasdfasdfasdfasdfasdfasdfasddfasdfasa')
        sleep(1)
        user_name[10].clear()
        user_name[10].send_keys('abcdefghijklmnopqrstuasdfasdfasdfasdfasdfasdfasdfasdfasddfasdfas')










        