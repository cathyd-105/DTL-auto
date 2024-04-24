from time import sleep
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class createClaimVmPage(BasePage):
    # 元素定位
    labname = (By.LINK_TEXT, 'ding1127-e-1')
    add = (By.XPATH, '//div[@aria-label="Add"]')
    suse_base = (By.LINK_TEXT, 'SUSE Enterprise Linux 15 SP4 +24x7 Support')
    vm_name = (By.XPATH, '//input[@aria-label="Virtual machine name"]')
    secret_saved = (By.XPATH, '//span[@class="azc-fill-text azc-validation-border azc-checkBox-unchecked"]')
    secret_list = (By.XPATH, '//div[@aria-autocomplete="none"]')
    password = (By.XPATH, '//div[@role="treeitem"]')
    vm_size = (By.XPATH, '//span[text()="Change Size"]')
    select_size = (By.XPATH, '//span[text()="D2s_v3"]')
    select_button = (By.XPATH, '//div[@title="Select"]')
    advance_setting = (By.XPATH, '//span[text()="Advanced Settings"]')
    claim_ornot = (By.XPATH, '//li[@role="radio"]')
    basic_setting = (By.XPATH, '//span[text()="Basic Settings"]')
    create_button = (By.XPATH, '//span[text()="Create"]')
    number_instance = (By.XPATH, '//input[@title="Please match the numeric format"]')
    refresh_button = (By.XPATH, '//div[text()="Refresh"]')
    claim_any = (By.XPATH, '//div[@title="Claim any"]')
    ding_claim1 = (By.LINK_TEXT, 'ding-claim1')
    running_text = (By.XPATH, '//div[@aria-label="Running"]')
    stop_button =(By.XPATH, '//div[@data-telemetryname="Command-Stop"]')
    url = 'https://ms.portal.azure.com/?feature.msaljs=false#browse/Microsoft.DevTestLab%2Flabs'

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 打开页面并最大化
    def goto_dtl_page(self):
        self.open_url(self.url)
        self.driver.maximize_window()

    def create_vm(self):
        # 点击创建的lab
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.labname)))
        self.click_element(*self.labname)
        # 定位add并点击
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.add)))
        self.click_element(*self.add)

    def choose_base(self):
        # 在搜索框输入常用base：suse，并点击
        WebDriverWait(self.driver, 120, 0.5).until(EC.presence_of_element_located((self.suse_base)))
        target1 = self.locate_element(*self.suse_base)
        self.driver.execute_script('arguments[0].scrollIntoView();', target1)
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.suse_base)))
        self.click_element(*self.suse_base)

    def basic_set(self):
        WebDriverWait(self.driver, 50, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//span[text()="Basic_A3"]')), 'Basic_A3'))
        self.clear_text(*self.vm_name)
        # 输入vm名
        self.type_text('ding-claim1', *self.vm_name)
        # 点击已保存密码库选项
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.secret_saved)))
        ss = self.locate_elements(*self.secret_saved)
        ss[2].click() 
        # 点击下拉框
        sleep(1)
        secret_dropbox = self.locate_elements(*self.secret_list)
        secret_dropbox[3].click()
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
        WebDriverWait(self.driver, 30, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//label[text()="Make this machine claimable"]')), 'Make this machine claimable'))
        vm_claim= self.locate_elements(*self.claim_ornot)
        vm_claim[5].click()
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.basic_setting)))
        self.click_element(*self.basic_setting)
        # 最后点击创建
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.create_button)))
        self.click_element(*self.create_button)

    def repeat_create(self):
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.add)))
        self.click_element(*self.add)
        self.choose_base()
        WebDriverWait(self.driver, 50, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//span[text()="Basic_A3"]')), 'Basic_A3'))
        self.clear_text(*self.vm_name)
        # 输入vm名
        self.type_text('ding-claim2', *self.vm_name)
        # 点击已保存密码库选项
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.secret_saved)))
        ss = self.locate_elements(*self.secret_saved)
        ss[2].click() 
        # 点击下拉框
        sleep(1)
        secret_dropbox = self.locate_elements(*self.secret_list)
        secret_dropbox[3].click()
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
        # 高级设置
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.advance_setting)))
        self.click_element(*self.advance_setting)
        WebDriverWait(self.driver, 30, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//label[text()="Make this machine claimable"]')), 'Make this machine claimable'))
        vm_claim= self.locate_elements(*self.claim_ornot)
        vm_claim[5].click()
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.number_instance)))
        self.clear_text(*self.number_instance)
        self.type_text('2', *self.number_instance)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.basic_setting)))
        self.click_element(*self.basic_setting)
        # 最后点击创建
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.create_button)))
        self.click_element(*self.create_button)

    def claim_vm(self):
        WebDriverWait(self.driver, 900, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Created 2 virtual machines with base name ding-claim2']")), 'Created 2 virtual machines with base name ding-claim2'))
        refresh = self.locate_elements(*self.refresh_button)
        refresh[1].click()
        sleep(3)
        self.click_element(*self.claim_any)
        WebDriverWait(self.driver, 300, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Successfully claimed a random virtual machine.']")), 'Successfully claimed a random virtual machine.'))
        refresh = self.locate_elements(*self.refresh_button)
        refresh[1].click()
        sleep(3)
        btn = self.locate_element(By.XPATH, '//div[@title="Claim any"]')
        ActionChains(self.driver).double_click(btn).perform()
        WebDriverWait(self.driver, 300, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Successfully claimed a random virtual machine.']")), 'Successfully claimed a random virtual machine.'))
        refresh = self.locate_elements(*self.refresh_button)
        refresh[1].click()
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.ding_claim1)))
        self.click_element(*self.ding_claim1)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.stop_button)))
        self.click_element(*self.stop_button)
        