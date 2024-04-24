from time import sleep
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


class myVmPage(BasePage):
    # 元素定位
    create_vm_button = (By.XPATH, '//div[@aria-label="Create a virtual machine"]')
    azure_vm = (By.XPATH, '//div[@aria-label="Azure virtual machine"]')
    vm_name = (By.XPATH, '//input[@type="text"]')
    region1 = (By.XPATH, '//div[@role="combobox"]')
    region2 = (By.XPATH, '//span[text()="(US) East US 2 EUAP"]')
    availability_zone = (By.XPATH, '//div[@role="combobox"]')
    zone1 = (By.XPATH, '//span[text()="Zone 1"]')
    zone3 = (By.XPATH, '//span[text()="Zone 3"]')
    image1 = (By.XPATH, '//span[@aria-label="Toggle"]')
    image2 = (By. XPATH, '//span[text()="Ubuntu Server 22.04 LTS - x64 Gen2"]')
    image_text = (By.XPATH, '//label[text()="Image"]')
    radio = (By.XPATH, '//span[@class="azc-radio-circle"]')
    input_uname = (By.XPATH, '//input[@type="text"]')
    input_pw = (By.XPATH, '//input[@type="password"]')
    next_disk = (By.XPATH, '//div[@title="Next : Disks >"]')
    next_network = (By.XPATH, '//div[@title="Next : Networking >"]')
    next_management = (By.XPATH, '//div[@title="Next : Management >"]')
    shutdown_text = (By.XPATH, '//label[text()="Patch orchestration options"]')
    enable_shut = (By.XPATH, '//div[@role="checkbox"]')
    shut_time = (By.XPATH, '//input[@placeholder="h:mm:ss AM/PM"]')
    time_zone = (By.XPATH, '//span[@aria-label="Toggle"]')
    china_zone = (By.XPATH, '//span[text()="(UTC+08:00) Beijing, Chongqing, Hong Kong, Urumqi"]')
    create1 = (By.XPATH, '//div[@title="Review + create"]')
    validate_pass = (By.XPATH, '//span[text()="Validation passed"]')
    create2 = (By.XPATH, '//div[@title="Create"]')
    goto_resourse_button = (By.XPATH, '//span[text()="Go to resource"]')
    auto_shutdown = (By.XPATH, '//div[@data-telemetryname="Menu-autoStop"]')
    send_note_ornot = (By.XPATH, '//span[@class="azc-radio-circle"]')
    save_button = (By.XPATH, '//div[text()="Save"]')
    overview_text = (By.XPATH, '//div[text()="Overview"]')
    refresh_button = (By.XPATH, '//div[@title="Refresh"]')
    url = 'https://ms.portal.azure.com/?feature.msaljs=false#browse/Microsoft.Compute%2FVirtualMachines'
    url1 = 'https://ms.portal.azure.com/?feature.msaljs=false#@microsoft.onmicrosoft.com/resource/subscriptions/ac77c8bc-f7c9-4592-9682-c9b0f643f0c9/resourceGroups/ding-myVm_group_08301544/providers/Microsoft.Compute/virtualMachines/ding-myVm/overview'
    
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 打开页面并最大化
    def goto_dtl_page(self):
        self.open_url(self.url)
        self.driver.maximize_window()

    def create_vm(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.create_vm_button)))
        self.click_element(*self.create_vm_button)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.azure_vm)))
        self.click_element(*self.azure_vm)
    
    def type_parameter(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='DevTest Labs - Testing - CTI']")), 'DevTest Labs - Testing - CTI'))
        vm_name = self.locate_elements(*self.vm_name)
        vm_name[5].send_keys('ding-myVm')
        sleep(5)
        region1 = self.locate_elements(*self.region1)
        region1[5].click()
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.region2)))
        self.click_element(*self.region2)
        sleep(5)
        ava_zone1 = self.locate_elements(*self.availability_zone)
        ava_zone1[7].click()
        self.click_element(*self.zone1)
        self.click_element(*self.zone3)
        sleep(2)
        target1 = self.locate_element(*self.image_text)
        self.driver.execute_script('arguments[0].scrollIntoView();', target1)
        sleep(5)
        image1 = self.locate_elements(*self.image1)
        image1[13].click()
        sleep(2)
        self.click_element(*self.image2)
        pw_radio = self.locate_elements(*self.radio)
        pw_radio[7].click()
        username_input = self.locate_elements(*self.input_uname)
        username_input[10].send_keys('vyuhanding')
        pw_input = self.locate_elements(*self.input_pw)
        pw_input[0].send_keys('Dyh19981222@')
        pw_confirm = self.locate_elements(*self.input_pw)
        pw_confirm[2].send_keys('Dyh19981222@')
        sleep(3)
        no_radio = self.locate_elements(*self.radio)
        no_radio[8].click()
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.next_disk)))
        self.click_element(*self.next_disk)
        # WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.next_network)))
        sleep(5)
        self.click_element(*self.next_network)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.next_management)))
        self.click_element(*self.next_management)

    def management_time(self):
        sleep(2)
        target2 = self.locate_element(*self.shutdown_text)
        self.driver.execute_script('arguments[0].scrollIntoView();', target2)
        enable_shutdown = self.locate_elements(*self.enable_shut)
        enable_shutdown[17].click()
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.shut_time)))
        self.clear_text(*self.shut_time)
        # sleep(2)
        self.type_text('10:00:00 AM', *self.shut_time)
        sleep(5)
        timezone = self.locate_elements(*self.time_zone)
        timezone[34].click()
        sleep(2)
        pyautogui.doubleClick(755, 550)
        pyautogui.doubleClick(755, 550)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.china_zone)))
        self.click_element(*self.china_zone)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.create1)))
        self.click_element(*self.create1)
        # sleep(14)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.validate_pass)))
        self.click_element(*self.create2)
        WebDriverWait(self.driver, 300, 0.5).until(EC.element_to_be_clickable((self.goto_resourse_button)))
        self.click_element(*self.goto_resourse_button)      
    
    def change_time(self):
        sleep(5)
        target3 = self.locate_element(*self.auto_shutdown)
        self.driver.execute_script('arguments[0].scrollIntoView();', target3)
        # WebDriverWait(self.driver, 50, 0.5).until(EC.element_to_be_clickable((self.auto_shutdown)))
        self.click_element(*self.auto_shutdown)
        sleep(5)
        
        send_note = self.locate_elements(*self.send_note_ornot)
        send_note[3].click()
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.shut_time)))
        self.clear_text(*self.shut_time)
        self.type_text('10:05:00 AM', *self.shut_time)
        pyautogui.click(600, 600)
        WebDriverWait(self.driver, 50, 0.5).until(EC.element_to_be_clickable((self.save_button)))
        self.click_element(*self.save_button)
        WebDriverWait(self.driver, 50, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Update of schedule successful']")), 'Update of schedule successful'))
        target4 = self.locate_element(*self.overview_text)
        self.driver.execute_script('arguments[0].scrollIntoView();', target4)
        self.click_element(*self.overview_text)
        sleep(300)
        self.click_element(*self.refresh_button)


        






        


