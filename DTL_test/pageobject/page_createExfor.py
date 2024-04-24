from time import sleep
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


class createExforPage(BasePage):
    # 元素定位
    labname = (By.LINK_TEXT, 'ding1124-e-1')
    add = (By.XPATH, '//div[@aria-label="Add"]')
    input_box = (By.XPATH, '//input[@placeholder="Search to filter available bases"]')
    win_base = (By.LINK_TEXT, 'Windows 11 Enterprise (x64) (Microsoft Dev Box Compatible)')
    suse_base = (By.LINK_TEXT, 'SUSE Enterprise Linux 15 SP4 +24x7 Support')
    vm_name = (By.XPATH, '//input[@aria-label="Virtual machine name"]')
    secret_saved = (By.XPATH, '//span[@class="azc-fill-text azc-validation-border azc-checkBox-unchecked"]')
    secret_list = (By.XPATH, '//div[@aria-autocomplete="none"]')
    password = (By.XPATH, '//div[@role="treeitem"]')
    vm_size = (By.XPATH, '//span[text()="Change Size"]')
    select_size1 = (By.XPATH, '//span[text()="B2ms"]')
    select_size2 = (By.XPATH, '//span[text()="D2s_v3"]')
    select_button = (By.XPATH, '//div[@title="Select"]')
    advance_setting = (By.XPATH, '//span[text()="Advanced Settings"]')
    basic_setting = (By.XPATH, '//span[text()="Basic Settings"]')
    ex_date = (By.XPATH, '//input[@placeholder="Will not expire"]')
    ex_time = (By.XPATH, '//input[@placeholder="h:mm:ss AM/PM"]')
    create_button = (By.XPATH, '//span[text()="Create"]')
    refresh_button = (By.XPATH, '//div[text()="Refresh"]')
    ex_win = (By.LINK_TEXT, 'ding-expire-w')
    ex_suse = (By.LINK_TEXT, 'ding-expire-l')
    create_for_button = (By.XPATH, '//div[text()="Create formula (reusable base)"]')
    ok_button = (By.XPATH, '//div[@title="OK"]')
    for_name = (By.XPATH, '//input[@type="text"]')
    description = (By.XPATH, '//textarea[@type="text"]')
    failed_mes = (By.XPATH, '//span[text()="Name can only include alphanumeric characters, underscores, hyphens, and parentheses."]')
    close_button = (By.XPATH, '//button[@title="Close"]')
    win_for = (By.LINK_TEXT, 'for-w')
    suse_for = (By.LINK_TEXT, 'for-l')
    url = 'https://ms.portal.azure.com/?feature.msaljs=false#browse/Microsoft.DevTestLab%2Flabs'
    # url = 'https://ms.portal.azure.com/?feature.msaljs=false#view/Microsoft_Azure_DevTestLab/LabVirtualMachineMenuBlade/~/virtualMachine/id/%2Fsubscriptions%2Fac77c8bc-f7c9-4592-9682-c9b0f643f0c9%2Fresourcegroups%2Fding1123-rg-1%2Fproviders%2Fmicrosoft.devtestlab%2Flabs%2Fding1123-e-1%2Fvirtualmachines%2Fding-expire-w'
    
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 打开页面并最大化
    def goto_dtl_page(self):
        self.open_url(self.url)
        self.driver.maximize_window()

    def open_lab(self):
        # 点击创建的lab
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.labname)))
        self.click_element(*self.labname)

    def create_exvmw(self):
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.add)))
        self.click_element(*self.add)
        WebDriverWait(self.driver, 60, 0.5).until(EC.presence_of_element_located((self.win_base)))
        target1 = self.locate_element(*self.win_base)
        self.driver.execute_script('arguments[0].scrollIntoView();', target1)
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.win_base)))
        self.click_element(*self.win_base)

    def basic_set(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//span[text()='Basic_A3']")), 'Basic_A3'))
        self.clear_text(*self.vm_name)
        # 输入vm名
        self.type_text('ding-expire-w', *self.vm_name)
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
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.select_size1)))
        self.click_element(*self.select_size1)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.select_button)))
        self.click_element(*self.select_button)

    def advanced_set(self):
        # 高级设置
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.advance_setting)))
        self.click_element(*self.advance_setting)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.ex_date)))
        self.type_text('11/24/2023', *self.ex_date)
        self.click_element(*self.ex_time)
        self.clear_text(*self.ex_time)
        self.type_text('17:30:00 PM', *self.ex_time)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.basic_setting)))
        self.click_element(*self.basic_setting)
        # 最后点击创建
        # WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.create_button)))
        sleep(2)
        self.click_element(*self.create_button)
        WebDriverWait(self.driver, 2500, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Created virtual machine ding-expire-w']")), 'Created virtual machine ding-expire-w'))
        refresh = self.locate_elements(*self.refresh_button)
        refresh[1].click()
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.ex_win)))
        self.click_element(*self.ex_win)

    def create_forw(self):
        sleep(4)
        self.click_element(*self.create_for_button)
        WebDriverWait(self.driver, 50, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//label[text()='Name']")), 'Name'))
        fname = self.locate_elements(*self.for_name)
        fname[10].send_keys('a b')
        sleep(1)
        try:
            assert self.locate_element(*self.failed_mes).is_displayed()==True
            print("test pass")
        except Exception as e:
            print('test fail', format(e))  
        sleep(2)  
        fname[10].clear()
        fname[10].send_keys('for-w')
        sleep(1)
        self.type_text('base ding-expire-w', *self.description)
        sleep(3)
        self.click_element(*self.ok_button)
        WebDriverWait(self.driver, 100, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Created Formula for-w']")), 'Created Formula for-w'))
        sleep(5)
        close = self.locate_elements(*self.close_button)
        close[2].click()   

    def create_forvmw(self):
        sleep(1)
        pyautogui.click(65, 40)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.add)))
        self.click_element(*self.add)
        WebDriverWait(self.driver, 100, 0.5).until(EC.presence_of_element_located((self.win_for)))
        self.click_element(*self.win_for)
        WebDriverWait(self.driver, 50, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//span[text()="Standard_B2ms"]')), 'Standard_B2ms'))
        self.click_element(*self.create_button)

    def create_exvml(self):
        sleep(5)
        self.click_element(*self.add)
        WebDriverWait(self.driver, 60, 0.5).until(EC.presence_of_element_located((self.suse_base)))
        target1 = self.locate_element(*self.suse_base)
        self.driver.execute_script('arguments[0].scrollIntoView();', target1)
        WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((self.suse_base)))
        self.click_element(*self.suse_base)

    def basic_set2(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//span[text()='Basic_A3']")), 'Basic_A3'))
        self.clear_text(*self.vm_name)
        # 输入vm名
        self.type_text('ding-expire-l', *self.vm_name)
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
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.select_size2)))
        self.click_element(*self.select_size2)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.select_button)))
        self.click_element(*self.select_button)

    def advanced_set2(self):
        # 高级设置
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.advance_setting)))
        self.click_element(*self.advance_setting)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.ex_date)))
        self.type_text('11/24/2023', *self.ex_date)
        self.click_element(*self.ex_time)
        self.clear_text(*self.ex_time)
        self.type_text('17:30:00 PM', *self.ex_time)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.basic_setting)))
        self.click_element(*self.basic_setting)
        # 最后点击创建
        sleep(2)
        self.click_element(*self.create_button)
        WebDriverWait(self.driver, 2500, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Created virtual machine ding-expire-l']")), 'Created virtual machine ding-expire-l'))
        refresh = self.locate_elements(*self.refresh_button)
        refresh[1].click()
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.ex_suse)))
        self.click_element(*self.ex_suse)

    def create_forl(self):
        sleep(4)
        self.click_element(*self.create_for_button)
        WebDriverWait(self.driver, 50, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//label[text()='Name']")), 'Name'))
        fname = self.locate_elements(*self.for_name)
        fname[10].send_keys('a b')
        sleep(1)
        try:
            assert self.locate_element(*self.failed_mes).is_displayed()==True
            print("test pass")
        except Exception as e:
            print('test fail', format(e))  
        sleep(2)  
        fname[10].clear()
        fname[10].send_keys('for-l')
        sleep(1)
        self.type_text('base ding-expire-l', *self.description)
        sleep(3)
        self.click_element(*self.ok_button)
        WebDriverWait(self.driver, 100, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Created Formula for-l']")), 'Created Formula for-l'))
        sleep(5)
        close = self.locate_elements(*self.close_button)
        close[2].click()   
    
    def create_forvml(self):
        sleep(1)
        pyautogui.click(65, 40)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.add)))
        self.click_element(*self.add)
        WebDriverWait(self.driver, 100, 0.5).until(EC.presence_of_element_located((self.suse_for)))
        self.click_element(*self.suse_for)
        WebDriverWait(self.driver, 50, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//span[text()="Standard_D2s_v3"]')), 'Standard_D2s_v3'))
        self.click_element(*self.create_button)

