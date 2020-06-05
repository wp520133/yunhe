import page
import time
from base.base import Base


class PageCuringRequestManage(Base):
    """
        养护作业管理→养护职责管理→养护要求管理
    """

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    # 点击养护职责管理
    def page_curing_duty_manage_click(self):
        self.base_click(page.curing_duty_manage_click)

    """
        养护要求管理新增
    """

    # 点击养护要求管理
    def page_curing_request_manage_click(self):
        self.base_click(page.curing_request_manage_click)
    # 点击新增
    def page_curing_request_manage_insert_click(self):
        self.base_click(page.curing_request_manage_insert_click)
    # 输入养护要求名称
    def page_curing_request_manage_curing_request_name_input(self):
        self.base_input(page.public_name_input,page.public_value)
    # 选择是否必须
    def page_curing_request_manage_select_if_must(self):
        self.base_click(page.curing_request_manage_select_if_must)
    # 点击养护结论
    def page_curing_request_manage_curing_inference_click(self):
        self.base_click(page.curing_request_manage_curing_inference_click)
    # 选择养护结论
    def page_curing_request_manage_curing_inference_select(self):
        self.base_click(page.curing_request_manage_curing_inference_select)
    # 输入操作方法
    def page_curing_request_manage_detail_method_input(self):
        self.base_input(page.public_detail_method_input,page.public_value)
    # 点击保存
    def page_curing_request_manage_save_button(self):
        self.base_click(page.public_insert_save_button)
    """
        养护要求管理查询
    """
    # 输入名称
    def page_curing_request_manage_search_name_input(self):
        self.base_input(page.public_name_input,page.public_value)
    # 输入创建人
    def page_curing_request_manage_creatby_input(self):
        self.base_input(page.public_createBy_input,page.public_createBy)
    # 点击查询
    def page_curing_request_manage_search_button(self):
        self.base_click(page.public_search_button)

    """
        养护要求管理重置
    """
    # 点击重置
    def page_curing_request_manage_reset_button(self):
        self.base_click(page.public_reset_button)
    """
        养护要求管理编辑
    """
    # 点击编辑
    def page_curing_request_manage_edit_button(self):
        self.base_click(page.public_one_row_button)

    """
        组合业务方法
    """
    # 养护要求管理新增
    def curing_request_manage_insert(self):
        self.page_curing_work_manage_click()
        self.page_curing_duty_manage_click()
        self.page_curing_request_manage_click()
        self.page_curing_request_manage_insert_click()
        self.page_curing_request_manage_curing_request_name_input()
        self.page_curing_request_manage_select_if_must()
        self.page_curing_request_manage_curing_inference_click()
        self.page_curing_request_manage_curing_inference_select()
        self.page_curing_request_manage_select_if_must()
        self.page_curing_request_manage_detail_method_input()
        self.page_curing_request_manage_save_button()
        time.sleep(2)

    # 养护要求管理查询
    def curing_request_manage_search(self):
        self.page_curing_request_manage_search_name_input()
        self.page_curing_request_manage_creatby_input()
        self.page_curing_request_manage_search_button()
        time.sleep(2)

    # 养护要求管理重置
    def curing_request_manage_reset(self):
        self.curing_request_manage_search()
        self.page_curing_request_manage_reset_button()
        time.sleep(2)

    # 养护要求管理编辑
    def curing_request_manage_edit(self):
        self.curing_request_manage_insert()
        self.curing_request_manage_search()
        self.page_curing_request_manage_edit_button()
        self.page_curing_request_manage_curing_request_name_input()
        self.page_curing_request_manage_select_if_must()
        self.page_curing_request_manage_curing_inference_click()
        self.page_curing_request_manage_curing_inference_select()
        self.page_curing_request_manage_curing_inference_select()
        self.page_curing_request_manage_select_if_must()
        self.page_curing_request_manage_detail_method_input()
        self.page_curing_request_manage_save_button()
        time.sleep(2)