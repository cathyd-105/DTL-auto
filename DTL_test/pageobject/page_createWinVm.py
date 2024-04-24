from time import sleep
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


class createWinVmPage(BasePage):
    # 元素定位
    labname = (By.LINK_TEXT, 'ding1127-e-1')
    add = (By.XPATH, '//div[@aria-label="Add"]')
    input_box = (By.XPATH, '//input[@placeholder="Search to filter available bases"]')
    win_base = (By.LINK_TEXT, 'Windows 11 Enterprise (x64) (Microsoft Dev Box Compatible)')
    vm_name = (By.XPATH, '//input[@aria-label="Virtual machine name"]')
    secret_saved = (By.XPATH, '//span[@class="azc-fill-text azc-validation-border azc-checkBox-unchecked"]')
    secret_list = (By.XPATH, '//div[@aria-autocomplete="none"]')
    password = (By.XPATH, '//div[@role="treeitem"]')
    vm_size = (By.XPATH, '//span[text()="Change Size"]')
    select_size = (By.XPATH, '//span[text()="B2ms"]')
    select_button = (By.XPATH, '//div[@title="Select"]')
    create_button = (By.XPATH, '//span[text()="Create"]')
    notification = (By.XPATH, '//a[@aria-label="Notifications"]')
    win_vm = (By.XPATH, '//a[text()="Created virtual machine ding-win"]') 
    refresh_button = (By.XPATH, '//div[text()="Refresh"]')
    connect_button = (By.XPATH, '//div[@title="Connect"]')
    essentials = (By.XPATH, '//div[text()="Essentials"]')
    resource_group = (By.XPATH, '//button[@class="msportalfx-text-primary fxc-essentials-value fxs-portal-text fxs-fxclick"]')
    vm_button = (By.LINK_TEXT, 'ding-win')
    extension = (By.XPATH, '//div[text()="Extensions + applications"]')
    cse = (By.XPATH, '//button[text()="CustomScriptExtension"]')
    close_button = (By.XPATH, '//button[@title="Close"]')
    iframe = (By.XPATH, '//iframe[@name="ApplicationAndExtensionResource.ReactView"]')
    url = 'https://ms.portal.azure.com/?feature.msaljs=false#browse/Microsoft.DevTestLab%2Flabs'
        
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 打开页面并最大化
    def goto_dtl_page(self):
        self.open_url(self.url)
        self.driver.maximize_window()

    def create_vm(self):
        # 点击创建的lab
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.labname)))
        self.click_element(*self.labname)
        # 定位add并点击
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.add)))
        self.click_element(*self.add)

    def choose_base(self):
        # 在搜索框输入常用base：win，并点击
        WebDriverWait(self.driver, 60, 0.5).until(EC.presence_of_element_located((self.win_base)))
        target1 = self.locate_element(*self.win_base)
        self.driver.execute_script('arguments[0].scrollIntoView();', target1)
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.win_base)))
        self.click_element(*self.win_base)

    def basic_set(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//span[text()='Basic_A3']")), 'Basic_A3'))
        self.clear_text(*self.vm_name)
        # 输入vm名
        self.type_text('ding-win', *self.vm_name)
        # 点击已保存密码库选项
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.secret_saved)))
        ss = self.locate_elements(*self.secret_saved)
        ss[2].click() 
        # 点击下拉框
        sleep(1)
        pw = self.locate_elements(*self.secret_list)
        pw[3].click()
        sleep(1)
        # 点击密码
        drop_down_boxes2 = self.locate_elements(*self.password)
        drop_down_boxes2[0].click()
        # 选择vm的size
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.vm_size)))
        self.click_element(*self.vm_size)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.select_size)))
        self.click_element(*self.select_size)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.select_button)))
        self.click_element(*self.select_button)
        # 最后点击创建
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.create_button)))
        self.click_element(*self.create_button)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.notification)))
        self.click_element(*self.notification)
        WebDriverWait(self.driver, 1500, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Created virtual machine ding-win']")), 'Created virtual machine ding-win'))
        self.click_element(*self.win_vm)

    # def connect(self):
    #     WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.connect_button)))
    #     self.click_element(*self.connect_button)
    #     sleep(5)
    #     pyautogui.click(1150, 165, duration=2)
    #     pyautogui.click(1130, 145, duration=2)
    #     pyautogui.click(950, 545, duration=2)
    #     sleep(2)
    #     pyautogui.typewrite('Dyh19981222')
    #     sleep(2)
    #     pyautogui.click(700, 580, duration=2)
    #     sleep(4)
    #     pyautogui.click(850, 600, duration=2)
    #     sleep(3)
    #     pyautogui.click(1050, 5, duration=2)
    #     pyautogui.click(850, 475, duration=2)

    def view_resource(self):
        sleep(4)
        self.click_element(*self.essentials)
        # es[1].click()
        sleep(2)
        rg = self.locate_elements(*self.resource_group)
        rg[0].click()
        sleep(3)
        vm = self.locate_elements(*self.vm_button)
        vm[1].click()
        sleep(3)
        target = self.locate_element(*self.extension)
        self.driver.execute_script('arguments[0].scrollIntoView();', target)
        self.click_element(*self.extension)
        sleep(2)
        self.switch_iframe(*self.iframe)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.cse)))
        try:
            self.locate_element(*self.cse)
            print("test pass")
        except Exception as e:
            print('test fail', format(e))