import page
import time
from base.base import Base


class PageCuringItemManage(Base):
    """
        养护作业管理→养护职责管理→养护项目管理
    """

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    # 点击养护职责管理
    def page_curing_duty_manage_click(self):
        self.base_click(page.curing_duty_manage_click)

    """
        养护项目管理新增
    """

    # 点击养护项目管理
    def page_curing_item_manage_click(self):
        self.base_click(page.curing_item_manage_click)

    # 点击养护项目管理新增
    def page_curing_item_manage_insert_click(self):
        self.base_click(page.curing_item_manage_insert_click)

    # 点击部件icon
    def page_curing_item_manage_insert_units_icon_click(self):
        self.base_click(page.curing_item_manage_insert_units_icon_click)

    # 选择部件
    def page_curing_item_manage_insert_units_radio_click(self):
        self.base_click(page.public_radio)

    # 点击确定
    def page_curing_item_manage_insert_units_radio_sure_click(self):
        self.base_click(page.public_sure_button)

    # 输入项目名称
    def page_curing_item_manage_insert_units_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 输入最大保养周期
    def page_curing_item_manage_insert_required_max_period_input(self):
        self.base_input(page.public_required_max_period_input, page.public_order_num)

    # 点击最大保养周期单位
    def page_curing_item_manage_insert_max_unit_click(self):
        self.base_click(page.curing_item_manage_insert_max_unit_click)

    # 选择最大保养周期单位
    def page_curing_item_manage_insert_max_unit_select(self):
        self.base_click(page.curing_item_manage_insert_max_unit_select)

    # 输入建议保养周期
    def page_curing_item_manage_insert_recommended_main_period_input(self):
        self.base_input(page.public_recommended_main_period_input, page.public_order_num)

    # 点击建议保养周期单位
    def page_curing_item_manage_insert_offer_unit_click(self):
        self.base_click(page.curing_item_manage_insert_offer_unit_click)

    # 选择建议保养周期单位
    def page_curing_item_manage_insert_offer_unit_select(self):
        self.base_click(page.curing_item_manage_insert_offer_unit_select)

    # 输入位置描述
    def page_curing_item_manage_insert_positon_desc_input(self):
        self.base_input(page.public_positon_desc_input, page.public_value)

    # 输入备注
    def page_curing_item_manage_insert_remark_input(self):
        self.base_input(page.public_remark_input, page.public_value)

    # 点击保存
    def page_curing_item_manage_insert_save_button(self):
        self.base_click(page.public_insert_save_button)

    """
        养护项目管理查询
    """

    # 输入养护项目名称
    def page_curing_item_manage_search_units_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 点击查询
    def page_curing_item_manage_search_button(self):
        self.base_click(page.public_search_button)

    """
        养护项目管理查看
    """
    # 重置
    def page_curing_item_manage_reset_button(self):
        self.base_click(page.public_reset_button)

    # 点击查看
    def page_curing_item_manage_watch_button(self):
        self.base_click(page.public_one_row_button)

    # 网页回退
    def page_curing_item_manage_back(self):
        self.base_back()

    """
        养护项目管理编辑
    """

    # 点击编辑
    def page_curing_item_manage_edit_button(self):
        self.base_click(page.public_two_row_button)


    """
        组装业务方法
    """
    # 新增
    def curing_item_manage_insert(self):
        self.page_curing_work_manage_click()
        self.page_curing_duty_manage_click()
        self.page_curing_item_manage_click()
        self.page_curing_item_manage_insert_click()
        self.page_curing_item_manage_insert_units_icon_click()
        self.page_curing_item_manage_insert_units_radio_click()
        self.page_curing_item_manage_insert_units_radio_sure_click()
        self.page_curing_item_manage_insert_units_name_input()
        self.page_curing_item_manage_insert_required_max_period_input()
        self.page_curing_item_manage_insert_max_unit_click()
        self.page_curing_item_manage_insert_max_unit_select()
        self.page_curing_item_manage_insert_recommended_main_period_input()
        self.page_curing_item_manage_insert_offer_unit_click()
        self.page_curing_item_manage_insert_offer_unit_select()
        self.page_curing_item_manage_insert_positon_desc_input()
        self.page_curing_item_manage_insert_remark_input()
        self.page_curing_item_manage_insert_save_button()
        time.sleep(2)

    # 查询
    def curing_item_manage_search(self):
        self.page_curing_item_manage_search_units_name_input()
        self.page_curing_item_manage_search_button()
        time.sleep(2)

    # 编辑
    def curing_item_manage_edit(self):
        self.curing_item_manage_insert()
        self.curing_item_manage_search()
        self.page_curing_item_manage_edit_button()
        self.page_curing_item_manage_insert_units_name_input()
        self.page_curing_item_manage_insert_required_max_period_input()
        self.page_curing_item_manage_insert_max_unit_click()
        self.page_curing_item_manage_insert_max_unit_select()
        self.page_curing_item_manage_insert_recommended_main_period_input()
        self.page_curing_item_manage_insert_offer_unit_click()
        self.page_curing_item_manage_insert_offer_unit_select()
        self.page_curing_item_manage_insert_positon_desc_input()
        self.page_curing_item_manage_insert_remark_input()
        self.page_curing_item_manage_insert_save_button()
        time.sleep(2)

    # 重置
    def curing_item_manage_reset(self):
        self.curing_item_manage_search()
        self.page_curing_item_manage_reset_button()
        time.sleep(2)

    # 查看
    def curing_item_manage_watch(self):
        self.curing_item_manage_search()
        self.page_curing_item_manage_watch_button()
        self.page_curing_item_manage_back()
        time.sleep(2)