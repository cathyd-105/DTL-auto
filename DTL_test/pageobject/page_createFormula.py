from time import sleep
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


class createFormulaPage(BasePage):
    # 元素定位
    labname = (By.LINK_TEXT, 'ding1123-e-1')
    configuration = (By.XPATH, '//div[text()="Configuration and policies"]')
    formula = (By.XPATH, '//div[text()="Formulas (reusable bases)"]')
    add_button = (By.XPATH, '//div[@aria-label="Add"]')
    nofor_text = (By.XPATH, '//div[text()="No formulas to display"]')
    vs_base = (By.LINK_TEXT, 'Visual Studio 2022 Pro on Windows 10 Enterprise (x64) + Microsoft 365 Apps (Microsoft Dev Box compatible)')
    forname1 = (By.XPATH, '//label[text()="Formula name"]')
    forname2 = (By.XPATH, '//input[@placeholder="Formula"]')
    error_tip = (By.XPATH, '//span[text()="Name can only include alphanumeric characters, underscores, hyphens, and parentheses."]')
    secret1 = (By.XPATH, '//span[@class="azc-fill-text azc-validation-border azc-checkBox-unchecked"]')
    secret2 = (By.XPATH, '//div[@aria-haspopup="dialog"]')
    secret3 = (By.XPATH, '//span[text()="ding"]')
    chosen_secret = (By.XPATH, '//div[text()="ding"]')
    for_advanced_set = (By.XPATH, '//span[text()="Advanced Settings"]')
    for_basic_set = (By.XPATH, '//span[text()="Basic Settings"]')
    yes_button = (By.XPATH, '//span[text()="Yes"]')
    no_button = (By.XPATH, '//span[text()="No"]')
    create_for_btn = (By.XPATH, '//div[@title="Create formula"]')
    refresh_btn = (By.XPATH, '//div[text()="Refresh"]')
    for1 = (By.LINK_TEXT, 'for1')
    close_btn = (By.XPATH, '//button[@title="Close"]')
    add = (By.XPATH, '//div[@aria-label="Add"]')
    user_name = (By.XPATH, '//input[@type="text"]')
    vm_size = (By.XPATH, '//span[text()="Change Size"]')
    select_size = (By.XPATH, '//span[text()="B2ms"]')
    select_button = (By.XPATH, '//div[@title="Select"]')
    create_button = (By.XPATH, '//span[text()="Create"]')
    notification = (By.XPATH, '//a[@aria-label="Notifications"]')
    claim_vm = (By.XPATH, '//div[text()="Claimable virtual machines"]')
    for1vm = (By.LINK_TEXT, 'for1001')
    for_usename = (By.XPATH, '//input[@type="text"]')
    update_formula = (By.XPATH, '//div[@title="Update formula"]')
    url = 'https://ms.portal.azure.com/#browse/Microsoft.DevTestLab%2Flabs'

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 打开页面并最大化
    def goto_dtl_page(self):
        self.open_url(self.url)
        self.driver.maximize_window()

    def create_for(self):
        # 点击创建的lab
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.labname)))
        self.click_element(*self.labname)
        # 定位config并点击
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.configuration)))
        self.click_element(*self.configuration)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.formula)))
        target1 = self.locate_element(*self.formula)
        self.driver.execute_script('arguments[0].scrollIntoView();', target1)
        sleep(1)
        self.click_element(*self.formula)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.nofor_text)))
        # try:
        #     self.locate_element(*self.nofor_text)
        #     # print('test pass')
        # except AssertionError:
        #     raise AssertionError('未定位到无法点击add')
        self.click_element(*self.add_button)

    def choose_base(self):
        WebDriverWait(self.driver, 80, 0.5).until(EC.presence_of_element_located((self.vs_base)))
        target1 = self.locate_element(*self.vs_base)
        self.driver.execute_script('arguments[0].scrollIntoView();', target1)
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.vs_base)))
        self.click_element(*self.vs_base)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.forname1)))
        try:
            assert self.locate_element(*self.forname1).is_displayed()==True
            print("test pass")
        except Exception as e:
            print('test fail', format(e))
        self.type_text('a b', *self.forname2)
        sleep(1)
        try:
            assert self.locate_element(*self.error_tip).is_displayed()==True
            print("test pass")
        except Exception as e:
            print('test fail', format(e))
        self.clear_text(*self.forname2)
        self.type_text('for1', *self.forname2)
        sleep(3)
        click_saved = self.locate_elements(*self.secret1)
        click_saved[2].click()
        click_pw = self.locate_elements(*self.secret2)
        click_pw[3].click()
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.secret3)))
        self.click_element(*self.secret3)
        try:
            self.locate_element(*self.chosen_secret)
            print('test pass')
        except Exception as e:
            print('test fail', format(e))
        sleep(1)
        self.click_element(*self.for_advanced_set)
        # formula_advance = self.locate_elements(*self.for_advanced_set)
        # formula_advance[0].click()
        WebDriverWait(self.driver, 30, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//label[text()="Make this machine claimable"]')), 'Make this machine claimable'))
        self.click_element(*self.yes_button)
        sleep(2)
        self.click_element(*self.for_basic_set)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.create_for_btn)))
        self.click_element(*self.create_for_btn)
        WebDriverWait(self.driver, 30, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//div[text()="Created Formula for1"]')), 'Created Formula for1'))
        refresh = self.locate_elements(*self.refresh_btn)
        refresh[1].click()
        sleep(3)
        try:
            self.locate_element(*self.for1)
            print('test pass')
        except Exception as e:
            print('test fail', format(e))
        sleep(5)
        close_for = self.locate_elements(*self.close_btn)
        close_for[2].click()

    def create_forvm(self):
        sleep(1)
        pyautogui.click(65, 40)
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.add)))
        self.click_element(*self.add)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.for1)))
        self.click_element(*self.for1)
        WebDriverWait(self.driver, 30, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//span[text()='Basic_A3']")), 'Basic_A3'))
        usname1 = self.locate_elements(*self.user_name)
        usname1[9].send_keys("vyuhanding")
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.vm_size)))
        self.click_element(*self.vm_size)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.select_size)))
        self.click_element(*self.select_size)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.select_button)))
        self.click_element(*self.select_button)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.create_button)))
        self.click_element(*self.create_button)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.notification)))
        self.click_element(*self.notification)
        WebDriverWait(self.driver, 2500, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Created virtual machine for1001']")), 'Created virtual machine for1001'))
        self.click_element(*self.claim_vm)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.for1vm)))
        sleep(1)
        try: 
            print('test pass')
        except Exception as e:
            print('test fail', format(e))

    def update_for(self, expected = 'vyuhanding'):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.configuration)))
        self.click_element(*self.configuration)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.formula)))
        target1 = self.locate_element(*self.formula)
        self.driver.execute_script('arguments[0].scrollIntoView();', target1)
        sleep(1)
        self.click_element(*self.formula)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.for1)))
        self.click_element(*self.for1)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.for_advanced_set)))
        usename = self.locate_elements(*self.for_usename)
        usename[5].send_keys('vyuhanding')
        sleep(1)
        self.click_element(*self.for_advanced_set)
        WebDriverWait(self.driver, 30, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//label[text()="Make this machine claimable"]')), 'Make this machine claimable'))
        self.click_element(*self.no_button)
        sleep(2)
        self.click_element(*self.for_basic_set)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.update_formula)))
        self.click_element(*self.update_formula)
        sleep(8)
        close_for = self.locate_elements(*self.close_btn)
        close_for[1].click()
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.add)))
        self.click_element(*self.add)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.for1)))
        self.click_element(*self.for1)
        WebDriverWait(self.driver, 50, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//span[text()="Basic_A3"]')), 'Basic_A3'))
        usname2 = self.locate_elements(*self.user_name)
        actual = usname2[9].get_attribute("value")
        mes = f'实际值:[{actual}],预期值:[{expected}]'
        try:
            assert expected in actual
            print('test success')
        except AssertionError:
            raise AssertionError(f'{mes};不包含')