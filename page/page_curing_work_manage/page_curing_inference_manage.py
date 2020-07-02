import page
import time
from base.base import Base


class PageCuringInferenceManage(Base):
    """
        养护作业管理→养护职责管理→养护结论管理新增
    """

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    # 点击养护职责管理
    def page_curing_duty_manage_click(self):
        self.base_click(page.curing_duty_manage_click)

    """
        养护结论管理新增
    """

    # 点击养护结论管理
    def page_curing_inference_manage_click(self):
        self.base_click(page.curing_inference_manage_click)

    # 点击新增
    def page_curing_inference_manage_insert_click(self):
        self.base_click(page.curing_inference_manage_insert_click)

    # 输入结论名称
    def page_curing_inference_manage_insert_inference_name_input(self, inference):
        self.base_input(page.public_name_input, inference)

    # 点击结果标记
    def page_curing_inference_manage_insert_remark_click(self):
        self.base_click(page.curing_inference_manage_insert_remark_click)

    # 选择结果标记
    def page_curing_inference_manage_insert_remark_select(self):
        self.base_click(page.curing_inference_manage_insert_remark_select)

    # 输入描述
    def page_curing_inference_manage_insert_desc_input(self, desc):
        self.base_input(page.public_desc_input, desc)

    # 点击保存
    def page_curing_inference_manage_insert_save_button(self):
        self.base_click(page.public_insert_save_button)

    # 点击返回
    def page_curing_inference_manage_return_click(self):
        self.base_click(page.public_return_click)
    """
        养护结论管理查询
    """

    # 输入结论名称
    def page_curing_inference_manage_search_inference_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 输入创建人
    def page_curing_inference_manage_search_creatby_name_input(self):
        self.base_input(page.public_createBy_input, page.public_createBy)

    # 点击查询
    def page_curing_inference_manage_search_button(self):
        self.base_click(page.public_search_button)

    """
        养护结论管理重置
    """

    # 点击重置
    def page_curing_inference_manage_reset_button(self):
        self.base_click(page.public_reset_button)

    """
        养护结论管理编辑
    """

    # 点击编辑
    def page_curing_inference_manage_edit_button(self):
        self.base_click(page.public_one_row_button)

    """
        组合业务方法
    """

    # 点击养护结论
    def curing_inference_manage_click(self):
        self.page_curing_work_manage_click()
        self.page_curing_duty_manage_click()
        self.page_curing_inference_manage_click()
        time.sleep(2)

    # 新增
    def curing_inference_manage_insert(self, inference, desc):
        self.page_curing_inference_manage_insert_click()
        self.page_curing_inference_manage_insert_inference_name_input(inference)
        self.page_curing_inference_manage_insert_remark_click()
        self.page_curing_inference_manage_insert_remark_select()
        self.page_curing_inference_manage_insert_desc_input(desc)
        self.page_curing_inference_manage_insert_save_button()
        time.sleep(2)

    # 查询
    def curing_inference_manage_search(self):
        self.page_curing_inference_manage_search_inference_name_input()
        self.page_curing_inference_manage_search_creatby_name_input()
        self.page_curing_inference_manage_search_button()
        time.sleep(2)

    # 重置
    def curing_inference_manage_reset(self):
        self.curing_inference_manage_search()
        self.page_curing_inference_manage_reset_button()
        time.sleep(2)

    # 编辑
    def curing_inference_manage_edit(self, inference, desc):
        self.curing_inference_manage_insert(inference, desc)
        self.curing_inference_manage_search()
        self.page_curing_inference_manage_edit_button()
        self.page_curing_inference_manage_insert_inference_name_input(inference)
        self.page_curing_inference_manage_insert_remark_click()
        self.page_curing_inference_manage_insert_remark_select()
        self.page_curing_inference_manage_insert_desc_input(desc)
        self.page_curing_inference_manage_insert_save_button()
        time.sleep(2)
