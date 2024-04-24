from time import sleep
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class createLabPage(BasePage):
    subscription1 = (By.XPATH, '//div[@role="combobox"]')
    subscription2 = (By.XPATH, '//span[text()="DevTest Labs - Testing - CTI"]')
    subscription3 = (By.XPATH, '//a[@title="DevTest Labs - Testing - CTI"]')
    rg1 = (By.LINK_TEXT, 'Create new')
    rg2 = (By.XPATH, '//input[@aria-label="Name of new Resource group"]')
    rg3 = (By.XPATH, '//div[@title="OK"]')
    labname = (By.XPATH, '//input[@placeholder="Enter name for your lab here"]')    
    location1 = (By.XPATH, '//div[@role="combobox"]')
    location2 = (By.XPATH, '//span[text()="East US 2 EUAP"]')
    location3 = (By.XPATH, '//div[@title="eastus2euap"]')
    button1 = (By.XPATH, '//span[text()="Review + create"]')
    validate_pass = (By.XPATH, '//span[text()="Succeeded"]')
    button2 = (By.XPATH, '//span[text()="Create"]')
    goto_resourse_button = (By.XPATH, '//span[text()="Go to resource"]')
    my_secret = (By.XPATH, '//div[text()="My secrets"]')
    my_lab = (By.XPATH, '//div[text()="My Lab"]')
    add = (By.XPATH, '//div[@aria-label="Add"]')
    secret_name1 = (By.XPATH, '//input[@aria-label="Name"]')
    secret1 = (By.XPATH, '//input[@aria-label="Secret"]')
    secret_name2 = (By.XPATH, '//input[@aria-label="Name"]')
    secret2 = (By.XPATH, '//input[@aria-label="Secret"]')
    ok_button = (By.XPATH, '//div[@title="OK"]')
    essentials = (By.XPATH, '//button[@aria-label="Essentials"]')
    refresh_button = (By.XPATH, '//div[text()="Refresh"]')
    resource_group = (By.LINK_TEXT, 'ding1128-rg-1')
    lab_status = (By.XPATH, '//div[@title="Ready"]')
    storage_account = (By.XPATH, '//div[text()="Storage account"]')
    dtl = (By.XPATH, '//div[text()="DevTest Lab"]')
    key_valut = (By.XPATH, '//div[text()="Key vault"]')
    virtual_network = (By.XPATH, '//div[text()="Virtual network"]')
    close_button = (By.XPATH, '//button[@title="Close"]')
    vm_list = (By.XPATH, '//div[text()="My virtual machines"]')
    nothing_vm = (By.XPATH, '//div[text()="Nothing to display"]')
    config = (By.XPATH, '//div[text()="Configuration and policies"]')
    internal_support = (By.LINK_TEXT, 'Internal support')
    enable_intsupport1 = (By.XPATH, '//span[text()="Yes"]')
    enable_intsupport2 = (By.XPATH, '//textarea[@rows="7"]')
    enable_intsupport3 = (By.XPATH, '//div[@title="Save"]')    
    # url = 'https://ms.portal.azure.com/?feature.msaljs=false#create/Microsoft.DevTestLab'
    url = 'https://ms.portal.azure.com/?feature.msaljs=false#@microsoft.onmicrosoft.com/resource/subscriptions/ac77c8bc-f7c9-4592-9682-c9b0f643f0c9/resourcegroups/ding1128-rg-1/providers/Microsoft.DevTestLab/labs/ding1128-e-1/overview'
    
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_createlab_page(self):
        self.open_url(self.url)
        self.driver.maximize_window()

    def select_subscription(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((By.XPATH, '//div[@role="combobox"]')))
        list1 = self.locate_elements(*self.subscription1)
        sleep(2)
        list1[0].click()
        sleep(2)
        target = self.locate_element(*self.subscription2)
        self.driver.execute_script('arguments[0].scrollIntoView();', target)
        try:
            self.click_element(*self.subscription2)
            print('test success')
        except AssertionError:
            raise AssertionError('未点击dtl-ctl')

    def type_rg(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Create new')))
        self.click_element(*self.rg1)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Name of new Resource group"]')))
        self.type_text('ding1128-rg-1', *self.rg2)
        sleep(2)
        self.click_element(*self.rg3)
        
    def type_labname(self, expected = 'ding1128-e-1'):
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.labname)))
        self.type_text('ding1128-e-1', *self.labname)
        name = self.locate_element(*self.labname)
        actual = name.get_attribute("value")
        mes = f'实际值:[{actual}],预期值:[{expected}]'
        try:
            assert expected in actual
            print('test success')
        except AssertionError:
            raise AssertionError(f'{mes};不包含')
            
    def select_location(self):
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.XPATH, '//div[@role="combobox"]')))
        list2 = self.locate_elements(*self.location1)
        sleep(2)
        list2[2].click()
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="East US 2 EUAP"]')))
        try:
            self.click_element(*self.location2)
            print('test success')
        except AssertionError:
            raise AssertionError('未点击eu2e')

    def click_button(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Review + create"]')))
        self.click_element(*self.button1)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.validate_pass)))
        self.click_element(*self.button2)
        WebDriverWait(self.driver, 240, 0.5).until(EC.element_to_be_clickable((self.goto_resourse_button)))
        self.click_element(*self.goto_resourse_button)     

    def validate_resource(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.element_to_be_clickable((self.essentials)))
        self.click_element(*self.essentials)   
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.resource_group)))
        try:
            self.locate_element(*self.resource_group)
            print('test success')
        except AssertionError:
            raise AssertionError('未定位到resource-group')
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.lab_status)))
        try:
            self.locate_element(*self.lab_status)
            print('test success')
        except AssertionError:
            raise AssertionError('未定位到ready状态')
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.location3)))
        try:
            self.locate_element(*self.location3)
            print('test success')
        except AssertionError:
            raise AssertionError('未定位到eu2e')
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.subscription3)))
        try:
            self.locate_element(*self.subscription3)
            print('test success')
        except AssertionError:
            raise AssertionError('未定位到eu2e')
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.resource_group)))
        self.click_element(*self.resource_group)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.storage_account)))
        try:
            self.locate_element(*self.storage_account)
            print('test success')
        except AssertionError:
            raise AssertionError('未定位到storage account')
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.key_valut)))
        try:
            self.locate_element(*self.key_valut)
            print('test success')
        except AssertionError:
            raise AssertionError('未定位到Key vault')
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.virtual_network)))
        try:
            self.locate_element(*self.virtual_network)
            print('test success')
        except AssertionError:
            raise AssertionError('未定位到Virtual network')
        sleep(2)
        fork1 = self.locate_elements(*self.close_button)
        fork1[1].click()
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.vm_list)))
        self.click_element(*self.vm_list)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.nothing_vm)))
        try:
            self.locate_element(*self.nothing_vm)
            print('test success')
        except AssertionError:
            raise AssertionError('有vm存在')
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.config)))
        self.click_element(*self.config)
        WebDriverWait(self.driver, 50, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//div[text()="General"]')), 'General'))
        self.click_element(*self.internal_support)
        WebDriverWait(self.driver, 50, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//label[text()="Support message"]')), 'Support message'))
        self.click_element(*self.enable_intsupport1)
        self.type_text('123', *self.enable_intsupport2)
        sleep(2)
        self.click_element(*self.enable_intsupport3)
        sleep(9)
        fork2 = self.locate_elements(*self.close_button)
        fork2[1].click()  

    def create_secret(self):
        # WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((self.my_lab)))
        # self.click_element(*self.my_lab)
        # 点击‘My secrets’选项
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((self.my_secret)))
        self.click_element(*self.my_secret)
        # 定位add并点击
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.add)))
        self.click_element(*self.add)

    def type_right_parameter(self):
        # 输入name
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.secret_name1)))
        self.type_text('ding', *self.secret_name1)
        # 输入secret
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.secret1)))
        self.type_text('Dyh19981222', *self.secret1)
        # 点击ok
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.ok_button)))
        self.click_element(*self.ok_button)
        
    def type_failed_parameter(self):
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((self.add)))
        self.click_element(*self.add)
        # 输入name
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.secret_name2)))
        self.type_text('failed', *self.secret_name2)
        # 输入secret
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.secret2)))
        self.type_text('123', *self.secret2)
        # 点击ok
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.ok_button)))
        self.click_element(*self.ok_button)