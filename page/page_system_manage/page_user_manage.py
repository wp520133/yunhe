import page
import time
from base.base import Base


class TestPageUserManage(Base):
    """
        系统管理→用户管理的查询
    """

    # 输入用户名
    def page_user_manage_input_username(self):
        self.base_input(page.public_username_input, page.public_value)
    # 判断用户名提示语是否存在
    def page_user_manage_input_is_username(self):
        self.base_element_is_exist(page.user_manage_insert_username_title)
    # 点击返回
    def page_user_manage_insert_return_button(self):
        self.base_click(page.user_manage_insert_return_button)
    # 点击状态
    def page_user_manage_click_status(self):
        self.base_click(page.user_manage_status_click)

    # 选择状态
    def page_user_manage_select_status(self):
        self.base_click(page.user_manage_status_select)

    # 点击查询
    def page_user_manage_search(self):
        self.base_click(page.user_manage_search_button)

    """
        系统管理→用户管理的重置
    """

    # 点击重置
    def page_user_manage_reset(self):
        self.base_click(page.public_reset_button)

    """
        系统管理→用户管理的禁用
    """

    # 点击禁用按钮
    def page_user_manage_ban(self):
        self.base_click(page.user_manage_ban_button)

    # 点击确认禁用按钮
    def page_user_manage_sure_ban(self):
        self.base_click(page.user_manage_ban_sure_button)

    """
       系统管理→用户管理的新增 
    """

    # 点击新增
    def page_user_manage_insert(self):
        self.base_click(page.user_manage_insert_click)

    # 判断是否新增
    def page_user_manage_is_insert(self):
        self.base_element_is_exist(page.user_manage_insert_click)
    # 输入用户名
    def page_user_manage_insert_username(self,username):
        self.base_input(page.public_username_input, username)

    # 输入新密码
    def page_user_manage_insert_new_password(self, password):
        self.base_input(page.public_password_input, password)

    # 输入确认密码
    def page_user_manage_insert_confirm_password(self, sure_password):
        self.base_input(page.public_confirm_input, sure_password)

    # 点击角色
    def page_user_manage_insert_click_role(self):
        self.base_click(page.user_manage_insert_role_click)

    # 选择角色
    def page_user_manage_insert_select_role(self):
        self.base_click(page.user_manage_insert_role_select)

    # 点击用户名(解决选择角色后取消下框)
    def page_user_manage_click_username(self):
        self.base_click(page.public_username_input)

    # 点击关联人员图标
    def page_user_manage_insert_rv_icon(self):
        self.base_click(page.user_manage_insert_rv_icon)

    # 单选人员
    def page_user_manage_insert_rv_radio(self):
        self.base_click(page.public_radio)

    # 点击确定
    def page_user_manage_insert_sure_button(self):
        self.base_click(page.public_sure_button)

    # 点击保存
    def page_user_manage_save_button(self):
        self.base_click(page.public_insert_save_button)

    """
        系统管理→用户管理的编辑
    """

    def page_user_manage_edit_button(self):
        self.base_click(page.public_one_row_button)

    # 组装业务方法

    # 组装用户管理查询
    def user_manage_search(self):
        self.page_user_manage_input_username()
        self.page_user_manage_click_status()
        self.page_user_manage_select_status()
        self.page_user_manage_search()
        time.sleep(2)

    # 组装用户管理重置
    def user_manage_reset(self):
        self.user_manage_search()
        self.page_user_manage_reset()
        time.sleep(2)

    # 组装用户管理新增
    def user_manage_insert(self,username,password,sure_password):
        self.page_user_manage_insert()
        self.page_user_manage_insert_username(username)
        self.page_user_manage_insert_new_password(password)
        self.page_user_manage_insert_confirm_password(sure_password)
        self.page_user_manage_insert_click_role()
        self.page_user_manage_insert_select_role()
        self.page_user_manage_click_username()
        self.page_user_manage_insert_rv_icon()
        self.page_user_manage_insert_rv_radio()
        self.page_user_manage_insert_sure_button()
        self.page_user_manage_save_button()
        time.sleep(2)

    # 组装用户管理编辑(通过新增、查询、编辑)
    def user_manage_edit(self,username,password,sure_password):
        self.user_manage_insert(username,password,sure_password)
        self.user_manage_search()
        self.page_user_manage_edit_button()
        self.page_user_manage_insert_new_password(password)
        self.page_user_manage_insert_confirm_password(sure_password)
        self.page_user_manage_save_button()
        time.sleep(2)

    # 组装用户管理的禁用(通过新增、查询、禁用)
    def user_manage_ban(self,username,password,sure_password):
        self.user_manage_insert(username,password,sure_password)
        self.user_manage_search()
        self.page_user_manage_ban()
        self.page_user_manage_sure_ban()
        time.sleep(2)
