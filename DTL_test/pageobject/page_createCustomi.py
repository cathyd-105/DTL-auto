from time import sleep
from base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


class createCustomiPage(BasePage):
    labname = (By.LINK_TEXT, 'ding1121-e-1')
    vm_button = (By.LINK_TEXT, 'ding-win')
    create_custom_image = (By.XPATH, '//div[text()="Create custom image"]')
    wci = (By.XPATH, '//div[text()="Created Custom image ding-winci"]')
    iname = (By.XPATH, '//input[@type="text"]')
    failed_mes = (By.XPATH, '//span[text()="Name can only include alphanumeric characters, underscores, hyphens, and parentheses."]')
    add = (By.XPATH, '//div[@aria-label="Add"]')
    input_box = (By.XPATH, '//input[@placeholder="Search to filter available bases"]')
    win_customimage = (By.LINK_TEXT, 'ding-winci')
    vm_name = (By.XPATH, '//input[@aria-label="Virtual machine name"]')
    vm_size = (By.XPATH, '//span[text()="Change Size"]')
    select_size = (By.XPATH, '//span[text()="B2ms"]')
    select_button = (By.XPATH, '//div[@title="Select"]')
    create_button = (By.XPATH, '//span[text()="Create"]')
    refresh_button = (By.XPATH, '//div[text()="Refresh"]')
    ding_winci = (By.LINK_TEXT, 'ding-winci')
    connect_button = (By.XPATH, '//div[@title="Connect"]')
    close_button = (By.XPATH, '//button[@title="Close"]')
    configuration = (By.XPATH, '//div[text()="Configuration and policies"]')
    custom_image = (By.XPATH, '//div[text()="Custom images"]')
    my_customimage = (By.XPATH, '//div[text()="ding-winci"]')
    description = (By.XPATH, '//textarea[@type="text"]')
    ok_button = (By.XPATH, '//div[@title="OK"]')
    update_image = (By.XPATH, '//div[text()="Updating custom image ding-winci"]')
    url = 'https://ms.portal.azure.com/?feature.msaljs=false#browse/Microsoft.DevTestLab%2Flabs'

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
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.vm_button)))
        self.click_element(*self.vm_button)

    def create_customimage(self, expected="ding-winci"):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.create_custom_image)))
        self.click_element(*self.create_custom_image)
        WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.ok_button)))
        image_name = self.locate_elements(*self.iname)
        actual = image_name[10].get_attribute("value")
        mes = f'实际值:[{actual}],预期值:[{expected}]'
        try:
            assert expected in actual
            print('test success')
        except AssertionError:
            raise AssertionError(f'{mes};不包含')
        sleep(2)
        image_name[10].clear()
        image_name[10].send_keys('a b')
        sleep(1)
        try:
            assert self.locate_element(*self.failed_mes).is_displayed()==True
            print("test pass")
        except Exception as e:
            print('test fail', format(e))  
        sleep(2)  
        image_name[10].clear()
        image_name[10].send_keys('ding-winci')
        # WebDriverWait(self.driver, 50, 0.5).until(EC.presence_of_element_located((self.ok_button)))
        sleep(3)
        self.click_element(*self.ok_button)
        WebDriverWait(self.driver, 300, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Created Custom image ding-winci']")), 'Created Custom image ding-winci'))
        try:
            self.locate_element(*self.wci)
            print("test pass")
        except Exception as e:
            print('test fail', format(e))
        sleep(2)
        close = self.locate_elements(*self.close_button)
        close[2].click()    
     
    def choose_base(self):
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.add)))
        self.click_element(*self.add)
        WebDriverWait(self.driver, 100, 0.5).until(EC.presence_of_element_located((self.win_customimage)))
        self.click_element(*self.win_customimage)

    def basic_set(self):
        WebDriverWait(self.driver, 50, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ('//span[text()="Basic_A3"]')), 'Basic_A3'))
        self.clear_text(*self.vm_name)
        # 输入vm名
        self.type_text('ding-winci', *self.vm_name)
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
        WebDriverWait(self.driver, 900, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Created virtual machine ding-winci']")), 'Created virtual machine ding-winci'))
        self.click_element(*self.refresh_button)
        sleep(2)
        try:
            self.locate_element(*self.ding_winci)
            print("test pass")
        except Exception as e:
            print('test fail', format(e))
        sleep(1)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.ding_winci)))
        self.click_element(*self.ding_winci)

    # def connect(self):
    #     WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.connect_button)))
    #     self.click_element(*self.connect_button)
    #     sleep(5)
    #     pyautogui.click(1150,165, duration=2)
    #     pyautogui.click(1130,145, duration=2)
    #     pyautogui.click(950,545, duration=2)
    #     sleep(2)
    #     pyautogui.typewrite('Dyh19981222')
    #     sleep(2)
    #     pyautogui.click(700,580, duration=2)
    #     sleep(4)
    #     pyautogui.click(850,600, duration=2)
    #     sleep(3)
    #     pyautogui.click(1050,5, duration=2)
    #     pyautogui.click(850,475, duration=2)
    #     sleep(3)
    #     pyautogui.click(1420,140, duration=2)

    def view_resoure(self):
        sleep(2)
        fork1 = self.locate_elements(*self.close_button)
        fork1[2].click()
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.configuration)))
        self.click_element(*self.configuration)
        sleep(3)
        target = self.locate_element(*self.custom_image)
        self.driver.execute_script('arguments[0].scrollIntoView();', target)
        self.click_element(*self.custom_image)
        sleep(3)
        self.click_element(*self.my_customimage)
        WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located((self.description)))
        self.click_element(*self.description)
        self.type_text('123', *self.description)
        sleep(1)
        self.click_element(*self.ok_button)
        WebDriverWait(self.driver, 900, 0.5).until(EC.text_to_be_present_in_element((By.XPATH, ("//div[text()='Updating custom image ding-winci']")), 'Updating custom image ding-winci'))
        try:
            assert self.locate_element(*self.update_image).is_displayed()==True
            print("test pass")
        except Exception as e:
            print('test fail', format(e))