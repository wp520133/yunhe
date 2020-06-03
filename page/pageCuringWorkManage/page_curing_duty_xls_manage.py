import page
import time
from base.base import Base


class PageCuringDutyXlsManage(Base):
    """
        养护作业管理→养护职责管理→养护职责模板管理新增
    """

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    # 点击养护职责管理
    def page_curing_duty_manage_click(self):
        self.base_click(page.curing_duty_manage_click)

    """
        养护职责模板管理新增
    """

    # 点击养护职责模板管理
    def page_curing_duty_cls_manage_click(self):
        self.base_click(page.curing_duty_cls_manage_click)

    # 点击新增
    def page_curing_duty_cls_manage_insert_click(self):
        self.base_click(page.curing_duty_cls_manage_insert_click)

    # 输入职责模板名称
    def page_curing_duty_cls_manage_insert_duty_cls_name_input(self):
        self.base_input(page.public_standard_duty_name_input, page.public_value)

    # 点击职责模板名称
    def page_curing_duty_cls_manage_insert_duty_cls_name_click(self):
        self.base_click(page.public_standard_duty_name_input)

    # 点击养护等级
    def page_curing_duty_cls_manage_insert_curing_order_click(self):
        self.base_click(page.curing_duty_cls_manage_insert_curing_order_click)

    # 选择养护等级
    def page_curing_duty_cls_manage_insert_curing_order_select(self):
        self.base_click(page.curing_duty_cls_manage_insert_curing_order_select)

    # 点击部件型号icon
    def page_curing_duty_cls_manage_insert_repair_type_icon_click(self):
        self.base_click(page.curing_duty_cls_manage_insert_repair_type_icon_click)

    # 选择部件型号radio
    def page_curing_duty_cls_manage_insert_repair_type_radio_select(self):
        self.base_click(page.public_radio)

    # 点击确定
    def page_curing_duty_cls_manage_insert_repair_type_sure_button(self):
        self.base_click(page.public_sure_button)

    # 点击养护要求
    def page_curing_duty_cls_manage_insert_curing_request_click(self):
        self.base_click(page.curing_duty_cls_manage_insert_curing_request_click)

    # 选择养护要求
    def page_curing_duty_cls_manage_insert_curing_request_select(self):
        self.base_click(page.curing_duty_cls_manage_insert_curing_request_select)

    # 点击保存
    def page_curing_duty_cls_manage_insert_save_button(self):
        self.base_click(page.public_insert_save_button)

    """
        养护职责模板管理查询
    """

    # 输入模板名称
    def page_curing_duty_cls_manage_search_duty_cls_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 点击查询
    def page_curing_duty_cls_manage_search_button(self):
        self.base_click(page.public_search_button)

    """
        养护职责模板管理编辑
    """

    # 点击编辑
    def page_curing_duty_cls_manage_edit_button(self):
        self.base_click(page.public_two_row_button)

    """
        养殖职责模板管理重置
    """

    # 点击重置
    def page_curing_duty_cls_manage_reset_button(self):
        self.base_click(page.public_reset_button)

    """
        养护职责模板管理查看
    """

    # 点击查看
    def page_curing_duty_cls_manage_watch_button(self):
        self.base_click(page.public_one_row_button)

    # 回退
    def page_curing_duty_cls_manage_back(self):
        self.base_back()
    """
        组装业务方法
    """

    # 新增
    def curing_duty_cls_manage_insert(self):
        self.page_curing_work_manage_click()
        self.page_curing_duty_manage_click()
        self.page_curing_duty_cls_manage_click()
        self.page_curing_duty_cls_manage_insert_click()
        self.page_curing_duty_cls_manage_insert_duty_cls_name_input()
        self.page_curing_duty_cls_manage_insert_curing_order_click()
        self.page_curing_duty_cls_manage_insert_curing_order_select()
        self.page_curing_duty_cls_manage_insert_repair_type_icon_click()
        self.page_curing_duty_cls_manage_insert_repair_type_radio_select()
        self.page_curing_duty_cls_manage_insert_repair_type_sure_button()
        self.page_curing_duty_cls_manage_insert_curing_request_click()
        self.page_curing_duty_cls_manage_insert_curing_request_select()
        self.page_curing_duty_cls_manage_insert_duty_cls_name_click()
        self.page_curing_duty_cls_manage_insert_save_button()
        time.sleep(2)

    # 查询
    def curing_duty_cls_manage_search(self):
        self.page_curing_duty_cls_manage_search_duty_cls_name_input()
        self.page_curing_duty_cls_manage_search_button()
        time.sleep(2)

    # 编辑
    def curing_duty_cls_manage_edit(self):
        self.curing_duty_cls_manage_insert()
        self.curing_duty_cls_manage_search()
        self.page_curing_duty_cls_manage_edit_button()
        self.page_curing_duty_cls_manage_insert_duty_cls_name_input()
        self.page_curing_duty_cls_manage_insert_curing_order_click()
        self.page_curing_duty_cls_manage_insert_curing_order_select()
        self.page_curing_duty_cls_manage_insert_repair_type_icon_click()
        self.page_curing_duty_cls_manage_insert_repair_type_radio_select()
        self.page_curing_duty_cls_manage_insert_repair_type_sure_button()
        self.page_curing_duty_cls_manage_insert_curing_request_click()
        self.page_curing_duty_cls_manage_insert_curing_request_select()
        self.page_curing_duty_cls_manage_insert_curing_request_select()
        self.page_curing_duty_cls_manage_insert_duty_cls_name_click()
        self.page_curing_duty_cls_manage_insert_save_button()
        time.sleep(2)

    # 重置
    def curing_duty_cls_manage_reset(self):
        self.curing_duty_cls_manage_search()
        self.page_curing_duty_cls_manage_reset_button()
        time.sleep(2)

    # 查看
    def curing_duty_cls_manage_watch(self):
        self.curing_duty_cls_manage_search()
        self.page_curing_duty_cls_manage_watch_button()
        self.page_curing_duty_cls_manage_back()
        time.sleep(2)
