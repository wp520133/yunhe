import page
import time
from base.base import Base


class PageUnitsClassManage(Base):
    # 点击基础信息管理
    def page_base_info_manage_click(self):
        self.base_click(page.base_info_manage_click)

    """
        部件类别管理新增
    """

    # 点击部件类别管理
    def page_units_class_manage_click(self):
        self.base_click(page.units_class_manage_click)

    # 点击新增
    def page_units_class_manage_insert_click(self):
        self.base_click(page.units_class_manage_insert_click)

    # 点击所属系统类别
    def page_units_class_manage_insert_belong_system_class_click(self):
        self.base_click(page.units_class_manage_insert_belong_system_class_click)

    # 选择所属系统类别
    def page_units_class_manage_insert_belong_system_class_select(self):
        self.base_click(page.units_class_manage_insert_belong_system_class_select)

    # 点击上级部件类别
    def page_units_class_manage_insert_super_units_class_click(self):
        self.base_click(page.units_class_manage_insert_super_units_class_click)

    # 选择上级部件类别
    def page_units_class_manage_insert_super_units_class_select(self):
        self.base_click(page.units_class_manage_insert_super_units_class_select)

    # 输入部件类别名称
    def page_units_class_manage_insert_units_class_name_input(self,units_name):
        self.base_input(page.public_name_input, units_name)

    # 输入描述
    def page_units_class_manage_insert_units_class_desc_input(self,desc):
        self.base_input(page.public_desc_input, desc)

    # 点击保存
    def page_units_class_manage_insert_save_button(self):
        self.base_click(page.public_insert_save_button)

    # 点击返回
    def page_units_class_manage_insert_return_click(self):
        self.base_click(page.units_class_manage_insert_return_click)

    """
        部件类别管理查询
    """

    # 输入部件类别名称
    def page_units_class_manage_search_units_class_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 输入创建人
    def page_units_class_manage_search_createBy_input(self):
        self.base_input(page.public_createBy_input, page.public_createBy)

    # 点击查询按钮
    def page_units_class_manage_search_button(self):
        self.base_click(page.public_search_button)

    """
        部件类别管理编辑
    """

    # 点击编辑
    def page_units_class_manage_edit_button(self):
        self.base_click(page.public_one_row_button)

    """
        部件类别管理重置
    """

    def page_units_class_manage_reset_button(self):
        self.base_click(page.public_reset_button)

    """
        组装业务方法
    """
    # 点击部件类别管理
    def units_class_manage_click(self):
        self.page_base_info_manage_click()
        self.page_units_class_manage_click()
        time.sleep(2)
    # 新增
    def units_class_manage_insert(self,units_name,desc):
        self.page_units_class_manage_insert_click()
        self.page_units_class_manage_insert_belong_system_class_click()
        self.page_units_class_manage_insert_belong_system_class_select()
        self.page_units_class_manage_insert_super_units_class_click()
        self.page_units_class_manage_insert_super_units_class_select()
        self.page_units_class_manage_insert_units_class_name_input(units_name)
        self.page_units_class_manage_insert_units_class_desc_input(desc)
        self.page_units_class_manage_insert_save_button()
        time.sleep(2)

    # 查询
    def units_class_manage_search(self):
        self.page_units_class_manage_search_units_class_name_input()
        self.page_units_class_manage_search_createBy_input()
        self.page_units_class_manage_search_button()
        time.sleep(2)

    # 编辑
    def units_class_manage_edit(self,units_name,desc):
        self.units_class_manage_insert(units_name,desc)
        self.units_class_manage_search()
        self.page_units_class_manage_edit_button()
        self.page_units_class_manage_insert_units_class_name_input(units_name)
        self.page_units_class_manage_insert_units_class_desc_input(desc)
        self.page_units_class_manage_insert_save_button()

    # 重置
    def units_class_manage_reset(self):
        self.units_class_manage_search()
        self.page_units_class_manage_reset_button()
