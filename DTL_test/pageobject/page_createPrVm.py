from time import sleep
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


class createPrVmPage(BasePage):
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
    advance_setting = (By.XPATH, '//span[text()="Advanced Settings"]')
    basic_setting = (By.XPATH, '//span[text()="Basic Settings"]')
    private_button = (By.XPATH, '//span[text()="Private"]')
    number_instance = (By.XPATH, '//input[@title="Please match the numeric format"]')
    create_button = (By.XPATH, '//span[text()="Create"]')
    refresh_button = (By.XPATH, '//div[text()="Refresh"]')
    pr_vm1 = (By.LINK_TEXT, 'ding-pr000')
    pr_vm2 = (By.LINK_TEXT, 'ding-pr001')
    connect_button = (By.XPATH, '//div[@title="Connect"]')
    resource_group = (By.XPATH, '//button[@tabindex="0"]')
    close_button = (By.XPATH, '//button[@title="Close"]')
    delete1 = (By.XPATH, '//div[@title="Click to open context menu"]')
    delete2 = (By. XPATH, '//li[@aria-posinset="6"]')
    delete3 = (By.XPATH, '//span[text()="Delete"]')
    cancel_button = (By.XPATH, '//div[@title="Cancel"]')
    url = 'https://ms.portal.azure.com/?feature.msaljs=false#browse/Microsoft.DevTestLab%2Flabs'
    # url = 'https://ms.portal.azure.com/?feature.msaljs=false#@microsoft.onmicrosoft.com/resource/subscriptions/ac77c8bc-f7c9-4592-9682-c9b0f643f0c9/resourceGroups/ding1127-rg-1/providers/Microsoft.DevTestLab/labs/ding1127-e-1/overview'

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
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.add)))
        self.click_element(*self.add)

    def choose_base(self):
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.win_base)))
        target1 = self.locate_element(*self.win_base)
        self.driver.execute_script('arguments[0].scrollIntoView();', target1)
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.win_base)))
        self.click_element(*self.win_base)

    def basic_set(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//span[text()='Basic_A3']")), 'Basic_A3'))
        self.clear_text(*self.vm_name)
        # 输入vm名
        self.type_text('ding-pr', *self.vm_name)
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

    def advanced_set(self):
        # 高级设置
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.advance_setting)))
        self.click_element(*self.advance_setting)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.private_button)))
        self.click_element(*self.private_button)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.number_instance)))
        self.clear_text(*self.number_instance)
        self.type_text('2', *self.number_instance)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.basic_setting)))
        self.click_element(*self.basic_setting)
        # 最后点击创建
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.create_button)))
        self.click_element(*self.create_button)
        WebDriverWait(self.driver, 2500, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Created 2 virtual machines with base name ding-pr']")), 'Created 2 virtual machines with base name ding-pr'))
        refresh = self.locate_elements(*self.refresh_button)
        refresh[1].click()
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.pr_vm1)))
        self.click_element(*self.pr_vm1)

    # def connect(self):
    #     WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.connect_button)))
    #     self.click_element(*self.connect_button)
    #     sleep(5)
    #     pyautogui.click(1150,165, duration=2)
    #     pyautogui.click(1130,145, duration=2)
    #     pyautogui.click(950,545, duration=2)# 点击connect
    #     sleep(16)
    #     pyautogui.click(1005,490, duration=2)      
        # sleep(3)
        # pyautogui.click(1420,140, duration=2)# 点击删除

    def view_resource(self):
        sleep(5)
        rg = self.locate_elements(*self.resource_group)
        rg[5].click()
        sleep(3)
        fork1 = self.locate_elements(*self.close_button)
        fork1[2].click() # 3
        sleep(2)
        fork2 = self.locate_elements(*self.close_button)
        fork2[1].click() #2
        # 点击第二个pr
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.pr_vm2)))
        self.click_element(*self.pr_vm2)
        sleep(5)
        # fork1 = self.locate_elements(*self.close_button)
        # fork1[3].click()
        # sleep(2)
        fork2 = self.locate_elements(*self.close_button)
        fork2[1].click()
        sleep(2)
        circle = self.locate_elements(*self.delete1)
        circle[11].click()# 12
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.delete2)))
        self.click_element(*self.delete2)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.cancel_button)))
        self.click_element(*self.cancel_button)
        # 再点一遍删除
        sleep(2)
        circle = self.locate_elements(*self.delete1)
        circle[11].click()# 12
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.delete2)))
        self.click_element(*self.delete2)
        sleep(5)
        # WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.delete3)))
        self.click_element(*self.delete3)
        WebDriverWait(self.driver, 1000, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Deleted Virtual machine ding-pr000']")), 'Deleted Virtual machine ding-pr000'))
        refresh = self.locate_elements(*self.refresh_button)
        refresh[1].click()
        sleep(1)
        try:
            assert self.locate_element(*self.pr_vm2).is_displayed()==False
            print("test pass")
        except Exception as e:
            print('test fail', format(e))



