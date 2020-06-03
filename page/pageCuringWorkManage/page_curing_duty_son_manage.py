import page
import time
from base.base import Base


class PageCuringDutySonManage(Base):
    """
        养护作业管理→养护职责管理→养护职责管理(子)新增
    """

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    # 点击养护职责管理
    def page_curing_duty_manage_click(self):
        self.base_click(page.curing_duty_manage_click)

    """
        养护职责管理(子)新增
    """

    # 点击养护职责管理(子)
    def page_curing_duty_son_manage(self):
        self.base_click(page.curing_duty_son_manage)

    # 点击新增
    def page_curing_duty_son_insert_manage(self):
        self.base_click(page.curing_duty_son_insert_manage)

    # 点击养护项目icon
    def page_curing_duty_son_insert_curing_item_icon_click(self):
        self.base_click(page.curing_duty_son_insert_curing_item_icon_click)

    # 选择养护项目radio
    def page_curing_duty_son_insert_curing_item_radio_click(self):
        self.base_click(page.public_radio)

    # 点击确定
    def page_curing_duty_son_insert_curing_item_button(self):
        self.base_click(page.public_sure_button)

    # 点击养护等级
    def page_curing_duty_son_insert_curing_order_click(self):
        self.base_click_enter(page.curing_duty_son_insert_curing_order_click)

    # 选择养护等级
    def page_curing_duty_son_insert_curing_order_select(self):
        self.base_click_enter(page.curing_duty_son_insert_curing_order_click)

    # 输入养护名称
    def page_curing_duty_son_insert_curing_name_input(self):
        self.base_input(page.public_duty_name_input, page.public_value)

    # 点击下一步
    def page_curing_duty_son_insert_next_click(self):
        self.base_click(page.curing_duty_son_insert_next_click)
    # 取消新增的职责模板
    def page_curing_duty_son_insert_duty_xls_remove_icon_click(self):
        self.base_click(page.curing_duty_son_insert_duty_xls_remove_icon_click)
    # 点击选择职责模板
    def page_curing_duty_son_insert_duty_xls_click(self):
        self.base_click(page.curing_duty_son_insert_duty_xls_click)

    # 选择职责模板radio
    def page_curing_duty_son_insert_duty_xls_radio_click(self):
        self.base_click(page.public_radio)

    # 点击确定
    def page_curing_duty_son_insert_duty_xls_button(self):
        self.base_click(page.public_sure_button)

    # 点击完成
    def page_curing_duty_son_insert_finish_button(self):
        self.base_click(page.curing_duty_son_insert_finish_button)

    """ 
        养护职责管理(子)查询
    """

    # 输入职责名称
    def page_curing_duty_son_search_curing_name_input(self):
        self.base_input(page.public_duty_name_input, page.public_value)

    # 点击查询
    def page_curing_duty_son_search_button(self):
        self.base_click(page.public_search_button)

    """
        养护职责管理(子)编辑
    """

    # 点击编辑
    def page_curing_duty_son_edit_button(self):
        self.base_click(page.public_two_row_button)

    """
        养护职责管理(子)重置
    """

    # 点击重置
    def page_curing_duty_son_reset_button(self):
        self.base_click(page.public_reset_button)

    """
        养护职责管理(子)查看
    """

    # 点击查看
    def page_curing_duty_son_watch_button(self):
        self.base_click(page.public_one_row_button)

    # 网页回退
    def page_curing_duty_son_back(self):
        self.base_back()

    """
        组装业务方法
    """
    # 新增
    def curing_duty_son_insert(self):
        self.page_curing_work_manage_click()
        self.page_curing_duty_manage_click()
        self.page_curing_duty_son_manage()
        self.page_curing_duty_son_insert_manage()
        self.page_curing_duty_son_insert_curing_item_icon_click()
        self.page_curing_duty_son_insert_curing_item_radio_click()
        self.page_curing_duty_son_insert_curing_item_button()
        self.page_curing_duty_son_insert_curing_order_click()
        self.page_curing_duty_son_insert_curing_order_select()
        self.page_curing_duty_son_insert_curing_name_input()
        self.page_curing_duty_son_insert_next_click()
        self.page_curing_duty_son_insert_duty_xls_click()
        self.page_curing_duty_son_insert_duty_xls_radio_click()
        self.page_curing_duty_son_insert_duty_xls_button()
        self.page_curing_duty_son_insert_finish_button()
        time.sleep(2)

    # 查询
    def curing_duty_son_search(self):
        self.page_curing_duty_son_search_curing_name_input()
        self.page_curing_duty_son_search_button()
        time.sleep(2)

    # 编辑
    def curing_duty_son_edit(self):
        self.curing_duty_son_insert()
        self.curing_duty_son_search()
        self.page_curing_duty_son_edit_button()
        self.page_curing_duty_son_insert_curing_item_icon_click()
        self.page_curing_duty_son_insert_curing_item_radio_click()
        self.page_curing_duty_son_insert_curing_item_button()
        time.sleep(2)
        self.page_curing_duty_son_insert_curing_order_click()
        self.page_curing_duty_son_insert_curing_order_select()
        self.page_curing_duty_son_insert_curing_name_input()
        self.page_curing_duty_son_insert_next_click()
        self.page_curing_duty_son_insert_duty_xls_remove_icon_click()
        self.page_curing_duty_son_insert_duty_xls_click()
        self.page_curing_duty_son_insert_duty_xls_radio_click()
        self.page_curing_duty_son_insert_duty_xls_button()
        self.page_curing_duty_son_insert_finish_button()
        time.sleep(2)

    # 重置
    def curing_duty_son_reset(self):
        self.curing_duty_son_search()
        self.page_curing_duty_son_reset_button()
        time.sleep(2)

    # 查看
    def curing_duty_son_watch(self):
        self.curing_duty_son_search()
        self.page_curing_duty_son_watch_button()
        self.page_curing_duty_son_back()
        time.sleep(2)