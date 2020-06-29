import page
import time
from base.base import Base


class PageRepairClassManage(Base):
    """
        备件类别管理新增
    """

    # 点击基础信息管理
    def page_base_info_manage_click(self):
        self.base_click(page.base_info_manage_click)

    """
        备件类别管理新增
    """

    # 点击备件管理
    def page_repair_class_manage_click(self):
        self.base_click(page.repair_class_manage_click)

    # 点击新增
    def page_repair_class_manage_insert_click(self):
        self.base_click(page.repair_class_manage_insert_click)

    # 点击上级备件类别
    def page_repair_class_manage_super_repair_class_click(self):
        self.base_click(page.repair_class_manage_super_repair_class_click)

    # 选择上级备件类别
    def page_repair_class_manage_super_repair_class_select(self):
        self.base_click(page.repair_class_manage_super_repair_class_select)

    # 输入备件类别名称
    def page_repair_class_manage_repair_class_name_input(self, repair_name):
        self.base_input(page.public_name_input, repair_name)

    # 输入描述
    def page_repair_class_manage_desc_input(self, desc):
        self.base_input(page.public_desc_input, desc)

    # 点击保存
    def page_repair_class_manage_save_button(self):
        self.base_click(page.public_insert_save_button)

    # 点击返回
    def page_repair_class_manage_return_button(self):
        self.base_click(page.public_return_click)
    """
        备件类别管理查询
    """

    # 输入备件类别名称
    def page_repair_class_manage_search_repair_class_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 输入创建人
    def page_repair_class_manage_search_creatby_input(self):
        self.base_input(page.public_createBy_input, page.public_createBy)

    # 点击查询
    def page_repair_class_manage_search_button(self):
        self.base_click(page.public_search_button)

    """
        备件类别管理编辑
    """

    # 点击编辑
    def page_repair_class_manage_edit_button(self):
        self.base_click(page.public_one_row_button)

    """
        备件类别管理重置
    """

    # 点击重置
    def page_repair_class_manage_reset_button(self):
        self.base_click(page.public_reset_button)

    # 刷新
    def page_repair_class_manage_refresh(self):
        self.base_refresh()

    """
        组装业务方法
    """

    # 点击备件类别管理
    def repair_class_manage_click(self):
        self.page_base_info_manage_click()
        self.page_repair_class_manage_click()
        time.sleep(2)

    # 新增
    def repair_class_manage_insert(self, repair_name, desc):
        self.page_repair_class_manage_insert_click()
        self.page_repair_class_manage_super_repair_class_click()
        self.page_repair_class_manage_super_repair_class_select()
        self.page_repair_class_manage_repair_class_name_input(repair_name)
        self.page_repair_class_manage_desc_input(desc)
        self.page_repair_class_manage_save_button()
        time.sleep(2)

    # 查询
    def repair_class_manage_search(self):
        self.page_repair_class_manage_search_repair_class_name_input()
        self.page_repair_class_manage_search_creatby_input()
        self.page_repair_class_manage_search_button()
        time.sleep(2)

    # 编辑
    def repair_class_manage_edit(self, repair_name, desc):
        self.repair_class_manage_insert(repair_name, desc)
        self.repair_class_manage_search()
        self.page_repair_class_manage_edit_button()
        self.page_repair_class_manage_repair_class_name_input(repair_name)
        self.page_repair_class_manage_desc_input(desc)
        self.page_repair_class_manage_save_button()
        time.sleep(2)

    # 重置
    def repair_class_manage_reset(self):
        self.repair_class_manage_search()
        self.page_repair_class_manage_reset_button()
        self.page_repair_class_manage_refresh()
        time.sleep(2)
