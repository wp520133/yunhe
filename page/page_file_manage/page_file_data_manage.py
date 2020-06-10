import page
import time
from base.base import Base


class PageFileDataManage(Base):
    # 点击资料档案管理
    def page_file_manage_click(self):
        self.base_click(page.file_manage_click)

    """
        我的档案新增
    """

    # 点击档案管理
    def page_data_manage_click(self):
        self.base_click(page.data_manage_click)

    # 点击我的档案
    def page_mind_data_manage_click(self):
        self.base_click(page.mind_data_manage_click)

    # 点击新增
    def page_mind_data_manage_insert_click(self):
        self.base_click(page.mind_data_manage_insert_click)

    # 输入名称
    def page_mind_data_manage_insert_name_input(self):
        self.base_input(page.mind_data_manage_insert_name_input, page.public_value)

    # 输入名称2
    def page_mind_data_manage_insert_name2_input(self):
        self.base_input(page.mind_data_manage_insert_name_input, page.public_value2)

    # 输入描述
    def page_mind_data_manage_insert_desc_input(self):
        self.base_input(page.mind_data_manage_insert_desc_input, page.public_value)

    # 点击附件
    def page_mind_data_manage_insert_upload_file_click(self):
        self.base_click(page.mind_data_manage_insert_upload_file_click)

    # 点击保存
    def page_mind_data_manage_insert_save_button(self):
        self.base_click(page.mind_data_manage_insert_save_button)

    """
        档案审批查询
    """

    # 点击档案审批
    def page_record_approval_click(self):
        self.base_click(page.record_approval_click)

    # 输入名称
    def page_record_approval_search_name_input(self):
        self.base_input(page.record_approval_search_name_input, page.public_value)

    # 输入名称2
    def page_record_approval_search_name2_input(self):
        self.base_input(page.record_approval_search_name_input, page.public_value2)

    # 输入描述
    def page_record_approval_search_desc_input(self):
        self.base_input(page.record_approval_search_desc_input, page.public_value)

    # 点击状态
    def page_record_approval_search_status_click(self):
        self.base_click(page.record_approval_search_status_click)

    # 选择状态
    def page_record_approval_search_status_select(self):
        self.base_click(page.record_approval_search_status_select)

    # 点击查询
    def page_record_approval_search_button(self):
        self.base_click(page.record_approval_search_button)

    """
        档案审批审批
    """

    # 点击审批
    def page_record_approval_approval_click(self):
        self.base_click(page.record_approval_approval_click)

    # 输入审批意见
    def page_record_approval_approval_device_input(self):
        self.base_input(page.record_approval_approval_device_input, page.public_value)

    # 点击通过
    def page_record_approval_approval_through_button(self):
        self.base_click(page.record_approval_approval_through_button)

    """
        档案管理(子)新增
    """
    # 点击档案管理(子)
    def page_data_manage_son_click(self):
        self.base_click(page.data_manage_son_click)
    # 点击新增
    # 输入名称
    # 输入描述
    # 点击附件
    # 点击保存
    """
        档案管理(子)查询
    """
    # 输入名称
    # 输入描述
    # 点击状态
    # 选择状态
    # 点击查询

    """
        档案管理(子)审批
    """
    # 点击审批
    def page_data_manage_son_approval_click(self):
        self.base_click(page.data_manage_son_approval_click)
    # 输入审批意见
    # 点击通过

    """
        组装业务方法
    """
    # 我的档案新增
    def mind_file_insert(self):
        self.page_file_manage_click()
        self.page_data_manage_click()
        self.page_mind_data_manage_click()
        self.page_mind_data_manage_insert_click()
        self.page_mind_data_manage_insert_name_input()
        self.page_mind_data_manage_insert_desc_input()
        self.page_mind_data_manage_insert_upload_file_click()
        self.base_upload()
        self.page_mind_data_manage_insert_save_button()
        time.sleep(2)

    # 档案审批查询
    def record_approval_search(self):
        self.page_record_approval_click()
        self.page_record_approval_search_name_input()
        self.page_record_approval_search_desc_input()
        self.page_record_approval_search_status_click()
        self.page_record_approval_search_status_select()
        self.page_record_approval_search_button()
        time.sleep(2)

    # 档案审批查询后审批
    def record_approval_approval(self):
        self.page_record_approval_approval_click()
        self.page_record_approval_approval_device_input()
        self.page_record_approval_approval_through_button()
        time.sleep(2)

    # 实现我的档案新增查询到审批
    def mind_file_ISA(self):
        self.mind_file_insert()
        self.record_approval_search()
        self.record_approval_approval()
        time.sleep(2)

    # 档案管理新增查询到审批
    def file_manage_ISA(self):
        self.page_data_manage_son_click()
        self.page_mind_data_manage_insert_click()
        self.page_mind_data_manage_insert_name2_input()
        self.page_mind_data_manage_insert_desc_input()
        self.page_mind_data_manage_insert_upload_file_click()
        self.base_upload()
        self.page_mind_data_manage_insert_save_button()
        time.sleep(2)
        self.page_record_approval_search_name2_input()
        self.page_record_approval_search_desc_input()
        self.page_record_approval_search_status_click()
        self.page_record_approval_search_status_select()
        self.page_record_approval_search_button()
        time.sleep(2)
        self.page_data_manage_son_approval_click()
        self.page_record_approval_approval_device_input()
        self.page_record_approval_approval_through_button()
        time.sleep(2)