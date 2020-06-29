import page
import time
from base.base import Base


class PageUnitsManage(Base):
    # 点击基础信息管理
    def page_base_info_manage_click(self):
        self.base_click(page.base_info_manage_click)

    """
        部件管理新增
    """

    # 点击部件管理
    def page_units_manage_click(self):
        self.base_click(page.units_manage_click)

    # 点击新增
    def page_units_manage_insert_click(self):
        self.base_click(page.public_insert_button)

    # 点击所属系统类别
    def page_units_manage_system_class_click(self):
        self.base_click(page.units_manage_system_class_click)

    # 选择所属系统类别
    def page_units_manage_system_class_select(self):
        self.base_click(page.units_manage_system_class_select)

    # 点击所属部件类别
    def page_units_manage_units_class_click(self):
        self.base_click(page.units_manage_units_class_click)

    # 选择所属部件类别
    def page_units_manage_units_class_select(self):
        self.base_click(page.units_manage_units_class_selefct)

    # 点击所属部件型号
    def page_units_manage_units_type_click(self):
        self.base_click(page.units_manage_units_type_click)
        # self.base_click_enter(page.units_manage_units_type_click)
    # 选择所属部件型号
    def page_units_manage_units_type_select(self):
        # self.base_click(page.units_manage_units_type_select)
        # self.base_click_enter(page.units_manage_units_type_click)
        # self.base_click_down(page.units_manage_units_type_select)
        # self.base_click_enter(page.units_manage_units_type_select)
        self.base_click_enter(page.units_manage_units_type_click)

    # 输入部件名称
    def page_units_manage_units_name_input(self, units_name):
        self.base_input(page.public_name_input, units_name)

    # 输入序列号
    def page_units_manage_sn_input(self, sn):
        self.base_input(page.public_sn_input, sn)

    # 点击生产日期
    def page_units_manage_pd_time_click(self):
        self.base_click(page.units_manage_pd_time_click)

    # 选择生产日期
    def page_units_manage_pd_time_select(self):
        self.base_click(page.units_manage_pd_time_select)

    # 点击报废日期
    def page_units_manage_sp_time_click(self):
        self.base_click(page.units_manage_sp_time_click)

    # 选择报废日期
    def page_units_manage_sp_time_select(self):
        self.base_click(page.units_manage_sp_time_select)

    # 点击保修截止日期
    def page_units_manage_gt_time_click(self):
        self.base_click(page.units_manage_gt_time_click)

    # 选择保修截止日期
    def page_units_manage_gt_time_select(self):
        self.base_click(page.units_manage_gt_time_select)

    # 输入备注
    def page_units_manage_remark_input(self, remark):
        self.base_input(page.public_remark_input, remark)

    # 输入描述
    def page_units_manage_desc_input(self, desc):
        self.base_input(page.public_desc_input, desc)

    # 点击保存
    def page_units_manage_save(self):
        self.base_click(page.public_insert_save_button)

    # 点击返回
    def page_units_manage_return_click(self):
        self.base_click(page.public_return_click)

    """
        部件管理查询
    """

    # 输入部件名称
    def page_units_manage_search_units_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 输入序列号
    def page_units_manage_search_sn_input(self):
        self.base_input(page.public_sn_input, page.public_order_num)

    # 点击查询
    def page_units_manage_search_button(self):
        self.base_click(page.public_search_button)

    """
        部件管理重置
    """

    # 点击重置按钮
    def page_units_manage_reset_button(self):
        self.base_click(page.public_reset_button)

    """
        部件管理编辑
    """

    # 点击部件管理编辑
    def page_units_manage_edit_button(self):
        self.base_click(page.public_one_row_button)

    """
        部件管理查看
    """

    # 点击部件管理查看
    def page_units_manage_watch_button(self):
        self.base_click(page.public_two_row_button)

    # 刷新
    def page_units_manage_refresh(self):
        self.base_refresh()

    """
        组装业务方法
    """

    # 部件管理点击
    def units_manage_click(self):
        self.page_base_info_manage_click()
        self.page_units_manage_click()
        time.sleep(2)

    # 新增
    def units_manage_insert(self, units_name, sn, remark, desc):
        self.page_units_manage_insert_click()
        self.page_units_manage_system_class_click()
        self.page_units_manage_system_class_select()
        self.page_units_manage_units_class_click()
        self.page_units_manage_units_class_select()
        self.page_units_manage_units_type_click()
        self.page_units_manage_units_type_select()
        self.page_units_manage_units_name_input(units_name)
        self.page_units_manage_sn_input(sn)
        self.page_units_manage_pd_time_click()
        self.page_units_manage_pd_time_select()
        self.page_units_manage_sp_time_click()
        self.page_units_manage_sp_time_select()
        self.page_units_manage_gt_time_click()
        self.page_units_manage_gt_time_select()
        self.page_units_manage_remark_input(remark)
        self.page_units_manage_desc_input(desc)
        self.page_units_manage_save()
        time.sleep(2)

    # 查询
    def units_manage_search(self):
        self.page_units_manage_search_units_name_input()
        self.page_units_manage_search_sn_input()
        self.page_units_manage_search_button()
        time.sleep(2)

    # 编辑
    def units_manage_edit(self, units_name, sn, remark, desc):
        self.units_manage_insert(units_name, sn, remark, desc)
        self.units_manage_search()
        self.page_units_manage_edit_button()
        self.page_units_manage_units_name_input(units_name)
        self.page_units_manage_sn_input(sn)
        self.page_units_manage_pd_time_click()
        self.page_units_manage_pd_time_select()
        self.page_units_manage_sp_time_click()
        self.page_units_manage_sp_time_select()
        self.page_units_manage_gt_time_click()
        self.page_units_manage_gt_time_select()
        self.page_units_manage_remark_input(remark)
        self.page_units_manage_desc_input(desc)
        self.page_units_manage_save()
        time.sleep(2)

    # 查看
    def units_manage_watch(self):
        self.units_manage_search()
        self.page_units_manage_watch_button()
        self.page_units_manage_refresh()
        time.sleep(2)

    # 重置
    def units_manage_reset(self):
        self.units_manage_search()
        self.page_units_manage_reset_button()
        time.sleep(2)
