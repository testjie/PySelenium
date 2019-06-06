"""
    selenium的二次封装了
"""
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class PySelenium():
    
    def __init__(self, browser="chrome", url=None, exe_driver="./driver/chromedriver.exe"):
        """
            初始化Driver并打开浏览器
        """
        browser = browser.lower()# 把所有大小的字母转换成小写

        # 1. 打开浏览器并获取到selenium的浏览器对象
        if browser == "chrome" or browser == "ch":
            self._driver = webdriver.Chrome(executable_path=exe_driver) # 把浏览器对象存在成员变量里，方便我们多个成员方法之间调用
        if browser == "firefox" or browser == "ff":
            self._driver = webdriver.Firefox(executable_path=exe_driver)
        if browser == "internet explorer" or browser == "ie":
            self._driver = webdriver.Ie(executable_path=exe_driver)
        if browser == "edge" or browser == "ed":
            self._driver = webdriver.Edge(executable_path=exe_driver)

        # 2. 打开网页
        try:
            self._driver.get(url)
        except:
            print("打开浏览器失败!")
        
    def get_origin_driver(self):
        """
            获取webdriver初始化的driver
        """
        return self._driver

    def find_element(self, locator):
        """
            查找单个元素
                参数：locator=("id", "123")
                类型：
                ID = "id"
                XPATH = "xpath"
                LINK_TEXT = "link text"
                PARTIAL_LINK_TEXT = "partial link text"
                NAME = "name"
                TAG_NAME = "tag name"
                CLASS_NAME = "class name"
                CSS_SELECTOR = "css selector"
        """
        if not isinstance(locator, tuple):
            raise Exception("输入的格式必须是(by, value)格式!")

        # 动态等待当前元素10s,10s超时报错
        try:
            element = WebDriverWait(self._driver, 10).until(lambda s: s.find_element(*locator))
            return element
        except:
            raise Exception("未找到元素{}！".format(locator))

    def find_elements(self, locator):
        """
            批量查找多个元素
                参数：locator=("id", "123")
                类型：
                ID = "id"
                XPATH = "xpath"
                LINK_TEXT = "link text"
                PARTIAL_LINK_TEXT = "partial link text"
                NAME = "name"
                TAG_NAME = "tag name"
                CLASS_NAME = "class name"
                CSS_SELECTOR = "css selector"
        """
        if not isinstance(locator, tuple):
            raise Exception("输入的格式必须是(by, value)格式!")

        # 动态等待当前元素10s,10s超时报错
        try:
            element = WebDriverWait(self._driver, 10).until(lambda s: s.find_element(*locator))
            return element
        except:
            raise Exception("未找到元素{}！".format(locator))

    def type(self, locator, text):
        """
            查找元素并输入文本
        """
        self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        """
            获取元素文本
        """
        return self.find_element(locator).text

    def get_attribute(self, locator, attribute):
        """
            获取元素属性
        """
        self.find_element(locator).get_attribute(attribute)

    def click(self, locator):
        """
            查找元素并点击元素
        """
        self.find_element(locator).click()

    def refresh(self):
        """
            刷新
        """
        self._driver.refresh()

    def wait(self, timeout=10):
        """
            隐性等待
        """
        self._driver.implicitly_wait(timeout)

    def switch_to_frame(self, locator):
        """
            切换到iframe
        """
        self._driver.switch_to_frame(self.find_element(locator))

    def switch_to_deault_content(self, locator):
        """
            切换回默认的页面
        """
        self._driver.switch_to.default_content()

    def close(self):
        """
            关闭浏览器
        """
        self._driver.close()

    def quit(self):
        """
            退出selenium
        """
        self._driver.quit()


if __name__ == "__main__":
    dr = PySelenium(url="https://www.baidu.com/")

    # dr.find_element(("id", "kw")).send_keys("123") # id
    # dr.find_element(("xpath", "//*[@id='kw']")).send_keys("123") # xpath

    # locator = ("id", "kw")
    # locator = ("xpath", "//*[@id='kw']")
    # dr.find_element(locator).send_keys("123")

    # locator = ("link text", "新闻")
    # dr.find_element(locator).click()

    # link text中包含一部分文本就行了
    # locator = ("partial link text", "hao")
    # print(dr.find_element(locator).text)

    # locator = ("name", "wd")
    # dr.find_element(locator).send_keys("123")

    # locator = ("tag name", "title")
    # print(dr.find_element(locator))

    # locator = ("class name", "s_ipt")
    # # dr.find_element(locator).send_keys("123")

    # tpye
    # locator = ("class name", "s_ipt")
    # dr.type(locator, "123")

    # 点击
    # locator = ("id", "su")
    # dr.click(locator)
    # dr.click(locator)


    time.sleep(3)
    dr.quit()