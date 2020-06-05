import page
import time
from base.base import Base


class PageUnitsTypeManage(Base):
    # 点击基础信息管理
    def page_base_info_manage_click(self):
        self.base_click(page.base_info_manage_click)

    """
        部件型号管理新增
    """

    # 点击部件型号管理
    def page_units_type_manage_click(self):
        self.base_click(page.units_type_manage_click)

    # 点击新增按钮
    def page_units_type_manage_insert_click(self):
        self.base_click(page.public_insert_button)

    # 点击所属系统类别
    def page_units_type_manage_system_class_click(self):
        self.base_click(page.units_type_manage_system_class_click)

    # 选择所属系统类别
    def page_units_type_manage_system_class_select(self):
        self.base_click(page.units_type_manage_system_class_select)

    # 点击所属部件类别
    def page_units_type_manage_units_type_click(self):
        self.base_click(page.units_type_manage_units_type_click)

    # 选择所属系统类别
    def page_units_type_manage_units_type_select(self):
        self.base_click(page.units_type_manage_units_type_select)

    # 点击上级部件型号
    def page_units_type_manage_super_units_type_click(self):
        self.base_click(page.units_type_manage_super_units_type_click)

    # 选择上级部件型号
    def page_units_type_manage_super_units_type_select(self):
        self.base_click(page.units_type_manage_super_units_type_select)

    # 输入部件型号名称
    def page_units_type_manage_units_type_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 点击厂商名称
    def page_units_type_manage_shop_name_click(self):
        self.base_click(page.units_type_manage_shop_name_click)

    # 选择厂商名称
    def page_units_type_manage_shop_name_select(self):
        self.base_click(page.units_type_manage_shop_name_select)

    # 输入品牌名
    def page_units_type_manage_brand_name_input(self):
        self.base_input(page.public_brand_name_input, page.public_value)

    # 输入有效期
    def page_units_type_manage_effective_time_input(self):
        self.base_input(page.public_effective_time_input, page.public_order_num)

    # 点击有效单位
    def page_units_type_manage_valid_unit_click(self):
        self.base_click(page.units_type_manage_valid_unit_click)

    # 选择有效单位
    def page_units_type_manage_valid_unit_select(self):
        self.base_click(page.units_type_manage_valid_unit_select)

    # 输入保修期
    def page_units_type_manage_guarantee_num_input(self):
        self.base_input(page.public_guarantee_num_input, page.public_order_num)

    # 点击上市时间
    def page_units_type_manage_appear_time_click(self):
        self.base_click(page.units_type_manage_appear_time_click)

    # 选择上市时间
    def page_units_type_manage_appear_time_select(self):
        self.base_click(page.units_type_manage_appear_time_select)

    # 输入描述
    def page_units_type_manage_desc_input(self):
        self.base_input(page.public_desc_input, page.public_value)

    # 点击保存
    def page_units_type_manage_save_button(self):
        self.base_click(page.public_insert_save_button)

    """
        部件型号管理查询
    """

    # 输入部件型号名称
    def page_units_type_manage_search_units_type_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 输入品牌名
    def page_units_type_manage_search_brand_name_input(self):
        self.base_input(page.public_brand_name_input, page.public_value)

    # 输入编号
    def page_units_type_manage_search_code_input(self):
        self.base_input(page.public_code_input, page.public_order_num)

    # 点击查询
    def page_units_type_manage_search_button(self):
        self.base_click(page.public_search_button)

    """
        部件型号管理编辑
    """

    # 点击编辑
    def page_units_type_manage_edit_button(self):
        self.base_click(page.public_one_row_button)

    """
        部件型号管理查看
    """

    # 点击查看
    def page_units_type_manage_watch_button(self):
        self.base_click(page.public_two_row_button)

    # 页面刷新一次
    def page_units_type_manage_refresh(self):
        self.base_refresh()

    """
        部件型号管理重置
    """

    # 点击重置
    def page_units_type_manage_reset_button(self):
        self.base_click(page.public_reset_button)

    """
        组装业务方法
    """

    # 新增
    def units_type_manage_insert(self):
        self.page_base_info_manage_click()
        self.page_units_type_manage_click()
        self.page_units_type_manage_insert_click()
        self.page_units_type_manage_system_class_click()
        self.page_units_type_manage_system_class_select()
        self.page_units_type_manage_units_type_click()
        self.page_units_type_manage_units_type_select()
        self.page_units_type_manage_super_units_type_click()
        self.page_units_type_manage_super_units_type_select()
        self.page_units_type_manage_units_type_name_input()
        self.page_units_type_manage_shop_name_click()
        self.page_units_type_manage_shop_name_select()
        self.page_units_type_manage_brand_name_input()
        self.page_units_type_manage_effective_time_input()
        self.page_units_type_manage_valid_unit_click()
        self.page_units_type_manage_valid_unit_select()
        self.page_units_type_manage_guarantee_num_input()
        self.page_units_type_manage_appear_time_click()
        self.page_units_type_manage_appear_time_select()
        self.page_units_type_manage_desc_input()
        self.page_units_type_manage_save_button()
        time.sleep(2)

    # 查询
    def units_type_manage_search(self):
        self.page_units_type_manage_search_units_type_name_input()
        self.page_units_type_manage_search_brand_name_input()
        self.page_units_type_manage_search_code_input()
        self.page_units_type_manage_search_button()
        time.sleep(2)

    # 编辑
    def units_type_manage_edit(self):
        self.units_type_manage_insert()
        self.units_type_manage_search()
        self.page_units_type_manage_edit_button()
        self.page_units_type_manage_units_type_name_input()
        self.page_units_type_manage_shop_name_click()
        self.page_units_type_manage_shop_name_select()
        self.page_units_type_manage_brand_name_input()
        self.page_units_type_manage_effective_time_input()
        self.page_units_type_manage_valid_unit_click()
        self.page_units_type_manage_valid_unit_select()
        self.page_units_type_manage_guarantee_num_input()
        self.page_units_type_manage_appear_time_click()
        self.page_units_type_manage_appear_time_select()
        self.page_units_type_manage_desc_input()
        self.page_units_type_manage_save_button()
        time.sleep(2)

    # 查看
    def units_type_manage_watch(self):
        self.units_type_manage_search()
        self.page_units_type_manage_watch_button()
        self.page_units_type_manage_refresh()
        time.sleep(2)

    # 重置
    def units_type_manage_reset(self):
        self.units_type_manage_search()
        self.page_units_type_manage_reset_button()
        time.sleep(2)
