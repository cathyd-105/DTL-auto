class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
    
    # 定位元素
    def locate_element(self, *loc):
        return self.driver.find_element(*loc)

    # 定位一组元素
    def locate_elements(self, *loc):
        return self.driver.find_elements(*loc)
    
    # 输入值
    def type_text(self, text, *loc):
        self.locate_element(*loc).send_keys(text)
      
    # 点击元素
    def click_element(self, *loc):
        self.locate_element(*loc).click()

    # 清空元素
    def clear_text(self, *loc):
        self.locate_element(*loc).clear()

    # 表单切换
    def switch_iframe(self, *loc):
        self.driver.switch_to.frame(self.locate_element(*loc))

    # 窗口切换
    def switch_window(self, n):
        self.driver.switch_to.window(self.driver.window_handles[n])


    

    
        
