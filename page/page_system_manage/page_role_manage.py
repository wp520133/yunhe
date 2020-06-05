import page
import time
from base.base import Base


class PageRoleManage(Base):
    """
        角色管理新增
    """

    # 点击角色管理
    def page_role_manage_click_button(self):
        self.base_click(page.role_manage_click_button)

    # 新增角色
    def page_role_manage_click_insert(self):
        self.base_click(page.role_manage_insert_click_button)

    # 角色名称输入
    def page_role_manage_input_role_name(self):
        self.base_input(page.public_role_name_input, page.public_value)

    # 角色名称编辑输入
    def page_role_manage_edit_input_role_name(self):
        self.base_input(page.public_role_name_input, page.public_value2)

    # 角色标识输入
    def page_role_manage_input_role_code(self):
        self.base_input(page.public_role_code_input, page.public_value)

    # 角色描述输入
    def page_role_manage_input_role_desc(self):
        self.base_input(page.public_role_desc_input, page.public_value)

    # 角色保存
    def page_role_manage_input_role_save(self):
        self.base_click(page.public_insert_save_button)

    """
        角色管理查看
    """

    # 点击查看
    def page_role_manage_click_watch(self):
        self.base_click(page.public_watch_four_line_click)

    # 刷新
    def page_role_manage_refresh_watch(self):
        self.base_refresh()

    """
        角色管理权限
    """

    # 点击权限
    def page_role_manage_power_button(self):
        self.base_click(page.role_manage_power_four_line_click)

    # 点击复选框
    def page_role_manage_power_checkbox(self):
        self.base_click(page.role_manage_power_checkbox)

    # 点击下拉图标
    def page_role_manage_power_down_icon(self):
        self.base_click(page.role_manage_power_down_icon)

    # 点击选中权限按钮
    def page_role_manage_power_save(self):
        self.base_click(page.role_manage_power_save_button)

    """
        角色管理编辑
    """

    # 点击角色管理编辑
    def page_role_manage_edit_button(self):
        self.base_click(page.public_edit_four_line_click)

    # 组装业务方法
    # 测试角色新增
    def role_manage_insert(self):
        self.page_role_manage_click_button()
        self.page_role_manage_click_insert()
        self.page_role_manage_input_role_name()
        self.page_role_manage_input_role_code()
        self.page_role_manage_input_role_desc()
        self.page_role_manage_input_role_save()
        time.sleep(2)

    # 测试角色查看
    def role_manage_watch(self):
        self.page_role_manage_click_button()
        self.page_role_manage_click_watch()
        self.page_role_manage_refresh_watch()
        time.sleep(2)

    # 测试角色权限
    def role_manage_power(self):
        self.page_role_manage_click_button()
        self.page_role_manage_power_button()
        self.page_role_manage_power_checkbox()
        self.page_role_manage_power_down_icon()
        self.page_role_manage_power_save()
        time.sleep(2)

    # 测试角色编辑修改
    def role_manage_edit(self):
        self.page_role_manage_click_button()
        self.page_role_manage_edit_button()
        self.page_role_manage_edit_input_role_name()
        self.page_role_manage_input_role_desc()
        self.page_role_manage_input_role_save()
        time.sleep(2)
