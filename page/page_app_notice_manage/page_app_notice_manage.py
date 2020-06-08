import page
import time
from base.base import Base
import allure


class PageAppNoticeManage(Base):
    """
        点击app公告管理
    """

    # 点击app公告管理
    @allure.step(title="点击app公告管理")
    def page_app_notice_manage_click(self):
        self.base_click(page.app_notice_manage_click)

    """
        app公告管理新增
    """

    # 点击新增
    def page_app_notice_manage_insert_click(self):
        self.base_click(page.app_notice_manage_insert_click)

    # 输入公告标题
    def page_app_notice_manage_insert_title_input(self, title):
        self.base_input(page.public_title_input, title)

    # 获取输入公告提示
    def page_app_notice_manage_insert_title_hint(self):
        self.base_get_html(page.app_notice_manage_insert_title_hint)

    # 输入公告内容
    def page_app_notice_manage_insert_content_input(self, content):
        self.base_input(page.public_content_input, content)

    # 输入公告内容提示
    def page_app_notice_manage_insert_content_hint(self):
        self.base_get_html(page.app_notice_manage_insert_content_hint)

    # 点击公告类型
    def page_app_notice_manage_insert_type_click(self):
        self.base_click(page.app_notice_manage_insert_type_click)

    # 选择公告类型
    def page_app_notice_manage_insert_type_select(self):
        self.base_click(page.app_notice_manage_insert_type_select)

    # 输入公告类型提示
    def page_app_notice_manage_insert_type_hint(self):
        self.base_get_html(page.app_notice_manage_insert_type_hint)

    # 点击确定
    def page_app_notice_manage_insert_sure_button(self):
        self.base_click(page.public_sure_button)

    # 点击x
    def page_app_notice_manage_insert_cross(self):
        self.base_click(page.app_notice_manage_insert_cross)

    """
        app公告管理查询
    """

    # 点击类型
    def page_app_notice_manage_search_type_click(self):
        self.base_click(page.app_notice_manage_search_type_click)

    # 选择类型
    def page_app_notice_manage_search_type_select(self):
        self.base_click(page.app_notice_manage_search_type_select)

    # 点击查询
    def page_app_notice_manage_search_button(self):
        self.base_click(page.public_search_button)

    """
        app公告管理重置
    """

    # 点击重置
    def page_app_notice_manage_reset_button(self):
        self.base_click(page.public_reset_button)

    """
        组装业务方法
    """

    # 新增
    def app_notice_manage_insert(self, title, content):
        self.page_app_notice_manage_click()
        self.page_app_notice_manage_insert_click()
        self.page_app_notice_manage_insert_title_input(title)
        self.page_app_notice_manage_insert_content_input(content)
        self.page_app_notice_manage_insert_type_click()
        self.page_app_notice_manage_insert_type_select()
        self.page_app_notice_manage_insert_sure_button()
        time.sleep(2)

    # 查询
    def app_notice_manage_search(self):
        self.page_app_notice_manage_search_type_click()
        self.page_app_notice_manage_search_type_select()
        self.page_app_notice_manage_search_button()
        time.sleep(2)

    # 重置
    def app_notice_manage_reset(self):
        self.app_notice_manage_search()
        self.page_app_notice_manage_reset_button()
        time.sleep(2)
