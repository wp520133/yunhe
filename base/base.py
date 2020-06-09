from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import os
import page


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法
    def base_find_element(self, loc, timeout=10, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 使用enter确认模拟点击方法
    def base_click_enter(self, loc):
        el = self.base_find_element(loc)
        el.send_keys(Keys.ENTER)

    # 使用向下键确认模拟点击方法
    def base_click_down(self, loc):
        el = self.base_find_element(loc)
        el.send_keys(Keys.DOWN)

    # 输入方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)
    # 获取文本
    def base_get_html(self,loc):
        return self.base_find_element(loc).get_attribute("textContent")

    # 获取文本方法
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 获取value的属性方法
    def base_get_value(self, loc):
        # 使用get_attribute获取指定的元素值
        self.base_find_element(loc).get_attribute("value")

    # 获取截图
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 刷新
    def base_refresh(self):
        self.driver.refresh()

    # 网页回退
    def base_back(self):
        self.driver.back()

    """
        系统管理登录
    """

    # 文件上传

    def base_upload(self):
        os.system(r"C:\其他\file\name.exe")

    # 输入系统登录用户名
    def system_manage_input_username(self, username):
        self.base_input(page.public_username_input, username)

    # 输入系统登录密码
    def system_manage_input_password(self, password):
        self.base_input(page.public_password_input, password)

    # 点击登录
    def system_manage_login_button(self):
        self.base_click(page.system_login_button)

        # 组装主页面系统登录

    def system_login(self, username, password):
        self.system_manage_input_username(username)
        self.system_manage_input_password(password)
        self.system_manage_login_button()
        time.sleep(2)
