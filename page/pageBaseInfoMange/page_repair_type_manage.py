import page
import time
from base.base import Base


class PageRepairTypeManage(Base):
    """
        备件型号管理
    """

    # 点击基础信息管理
    def page_base_info_manage_click(self):
        self.base_click(page.base_info_manage_click)

    """
        备件型号管理新增
    """

    # 点击备件型号管理
    def page_repair_type_manage_click(self):
        self.base_click(page.repair_type_manage_click)

    # 点击新增
    def page_page_repair_type_manage_insert_click(self):
        self.base_click(page.public_insert_button)

    # 点击所属备件类别
    def page_repair_type_manage_repair_type_click(self):
        self.base_click(page.repair_type_manage_repair_type_click)

    # 选择所属备件类别
    def page_repair_type_manage_repair_type_select(self):
        self.base_click(page.repair_type_manage_repair_type_select)

    # 点击上级备件型号
    def page_repair_type_manage_super_repair_type_click(self):
        self.base_click(page.repair_type_manage_super_repair_type_click)

    # 选择上级备件型号
    def page_repair_type_manage_super_repair_type_select(self):
        self.base_click(page.repair_type_manage_super_repair_type_select)

    # 输入备件型号名称
    def page_repair_type_manage_repair_type_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 输入计数单位
    def page_repair_type_manage_cu_input(self):
        self.base_input(page.public_countUnit_input, page.public_order_num)

    # 点击厂商名称
    def page_repair_type_manage_shop_name_click(self):
        self.base_click(page.repair_type_manage_shop_name_click)

    # 选择厂商名称
    def page_repair_type_manage_shop_name_select(self):
        self.base_click(page.repair_type_manage_shop_name_select)

    # 输入品牌名
    def page_repair_type_manage_brand_name_input(self):
        self.base_input(page.public_brand_name_input, page.public_value)

    # 输入有效期
    def page_repair_type_manage_vd_input(self):
        self.base_input(page.public_effective_time_input, page.public_order_num)

    # 点击有效单位
    def page_repair_type_manage_eu_click(self):
        self.base_click(page.repair_type_manage_eu_click)

    # 选择有效单位
    def page_repair_type_manage_eu_select(self):
        self.base_click(page.repair_type_manage_eu_select)

    # 输入保修期
    def page_repair_type_guarantee_num_input(self):
        self.base_input(page.public_guarantee_num_input, page.public_order_num)

    # 点击上市时间
    def page_repair_type_manage_ttm_click(self):
        self.base_click(page.repair_type_manage_ttm_click)

    # 选择上市时间
    def page_repair_type_manage_ttm_select(self):
        self.base_click(page.repair_type_manage_ttm_select)

    # 输入描述
    def page_repair_type_manage_desc_input(self):
        self.base_input(page.public_desc_input, page.public_value)

    # 点击保存
    def page_repair_type_manage_save_button(self):
        self.base_click(page.public_insert_save_button)

    """
        备件管理查询
    """

    # 输入备件型号名称
    def page_repair_type_manage_search_repair_type_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 输入品牌名
    def page_repair_type_manage_search_brand_name_input(self):
        self.base_input(page.public_brand_name_input, page.public_value)

    # 输入编号(随机的,不做查询)
    # 点击查询
    def page_repair_type_manage_search_button(self):
        self.base_click(page.public_search_button)

    """
        备件管理编辑
    """

    # 点击编辑
    def page_repair_type_manage_edit_button(self):
        self.base_click(page.public_one_row_button)

    """
        备件管理重置
    """

    # 点击重置
    def page_repair_type_manage_reset_button(self):
        self.base_click(page.public_reset_button)

    """
        备件管理查看
    """

    # 点击查看
    def page_repair_type_manage_watch_button(self):
        self.base_click(page.public_two_row_button)

    # 回退
    def page_repair_type_manage_back(self):
        self.base_back()

    """
        组装业务方法
    """

    # 备件管理新增
    def repair_type_manage_insert(self):
        self.page_base_info_manage_click()
        self.page_repair_type_manage_click()
        self.page_page_repair_type_manage_insert_click()
        self.page_repair_type_manage_repair_type_click()
        self.page_repair_type_manage_repair_type_select()
        self.page_repair_type_manage_super_repair_type_click()
        self.page_repair_type_manage_super_repair_type_select()
        self.page_repair_type_manage_repair_type_name_input()
        self.page_repair_type_manage_cu_input()
        self.page_repair_type_manage_shop_name_click()
        self.page_repair_type_manage_shop_name_select()
        self.page_repair_type_manage_brand_name_input()
        self.page_repair_type_manage_vd_input()
        self.page_repair_type_manage_eu_click()
        self.page_repair_type_manage_eu_select()
        self.page_repair_type_guarantee_num_input()
        self.page_repair_type_manage_ttm_click()
        self.page_repair_type_manage_ttm_select()
        self.page_repair_type_manage_desc_input()
        self.page_repair_type_manage_save_button()
        time.sleep(2)

    # 备件管理查询
    def repair_type_manage_search(self):
        self.page_repair_type_manage_search_repair_type_name_input()
        self.page_repair_type_manage_search_brand_name_input()
        self.page_repair_type_manage_search_button()
        time.sleep(2)

    # 备件管理编辑
    def repair_type_manage_edit(self):
        self.repair_type_manage_insert()
        self.repair_type_manage_search()
        self.page_repair_type_manage_edit_button()
        self.page_repair_type_manage_repair_type_name_input()
        self.page_repair_type_manage_cu_input()
        self.page_repair_type_manage_shop_name_click()
        self.page_repair_type_manage_shop_name_select()
        self.page_repair_type_manage_brand_name_input()
        self.page_repair_type_manage_vd_input()
        self.page_repair_type_manage_eu_click()
        self.page_repair_type_manage_eu_select()
        self.page_repair_type_guarantee_num_input()
        self.page_repair_type_manage_ttm_click()
        self.page_repair_type_manage_ttm_select()
        self.page_repair_type_manage_desc_input()
        self.page_repair_type_manage_save_button()
        time.sleep(2)

    # 备件管理重置
    def repair_type_manage_reset(self):
        self.repair_type_manage_search()
        self.page_repair_type_manage_reset_button()
        time.sleep(2)

    # 备件管理查看
    def repair_type_manage_watch(self):
        self.repair_type_manage_search()
        self.page_repair_type_manage_watch_button()
        self.page_repair_type_manage_back()
        time.sleep(2)
