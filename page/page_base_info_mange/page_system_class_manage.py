import page
import time
from base.base import Base


class PageSystemClassManage(Base):
    """
        系统类别管理新增
    """

    # 点击基础信息管理
    def page_base_info_manage_click(self):
        self.base_click(page.base_info_manage_click)

    # 点击系统类别管理
    def page_system_class_manage_click(self):
        self.base_click(page.system_class_manage_click)

    # 点击新增
    def page_system_class_manage_insert_click(self):
        self.base_click(page.public_insert_button)

    # 点击上级系统类别
    def page_system_class_manage_super_system_class_click(self):
        self.base_click(page.system_class_manage_super_system_class_click)

    # 选择上级系统类别
    def page_system_class_manage_super_system_class_select(self):
        self.base_click(page.system_class_manage_super_system_class_select)

    # 输入系统类别名称
    def page_system_class_manage_system_class_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 输入描述
    def page_system_class_manage_desc_input(self):
        self.base_input(page.public_desc_input, page.public_value)

    # 点击保存
    def page_system_class_manage_insert_save(self):
        self.base_click(page.public_insert_save_button)

    """
        系统类别管理查询
    """

    # 输入系统类别名称
    def page_search_system_class_manage_system_class_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 输入创建人
    def page_search_system_class_manage__createBy_input(self):
        self.base_input(page.public_createBy_input, page.public_createBy)

    # 点击查询
    def page_system_class_manage_seach_button(self):
        self.base_click(page.system_class_manage_search_button)

    """
        系统类别管理重置
    """

    # 点击重置按钮
    def page_system_class_manage_reset_button(self):
        self.base_click(page.public_reset_button)

    """
        系统类别管理编辑
    """

    # 点击编辑
    def page_system_class_manage_edit_button(self):
        self.base_click(page.public_one_row_button)

    """
        组合业务方法
    """

    # 新增
    def system_class_manage_insert(self):
        self.page_base_info_manage_click()
        self.page_system_class_manage_click()
        self.page_system_class_manage_insert_click()
        self.page_system_class_manage_super_system_class_click()
        self.page_system_class_manage_super_system_class_select()
        self.page_system_class_manage_system_class_name_input()
        self.page_system_class_manage_desc_input()
        self.page_system_class_manage_insert_save()
        time.sleep(2)

    # 查询
    def system_class_manage_search(self):
        self.page_search_system_class_manage_system_class_name_input()
        self.page_search_system_class_manage__createBy_input()
        self.page_system_class_manage_seach_button()
        time.sleep(2)

    # 编辑(从新增到查询再到编辑)
    def system_class_manage_edit(self):
        self.system_class_manage_insert()
        self.system_class_manage_search()
        self.page_system_class_manage_edit_button()
        self.page_system_class_manage_system_class_name_input()
        self.page_system_class_manage_desc_input()
        self.page_system_class_manage_insert_save()
        time.sleep(2)

    # 重置按钮
    def system_class_manage_reset(self):
        self.system_class_manage_search()
        self.page_system_class_manage_reset_button()
        time.sleep(2)
