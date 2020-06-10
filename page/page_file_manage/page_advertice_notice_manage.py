import page
import time
from base.base import Base


class PageAdverticeNoticeManage(Base):
    # 点击资料档案管理
    def page_file_manage_click(self):
        self.base_click(page.file_manage_click)

    """
        我的宣传公告新增
    """
    # 点击宣传公告管理
    def page_advertice_notice_manage_click(self):
        self.base_click(page.advertice_notice_manage_click)
    # 点击我的宣传公告
    def page_mind_advertice_notice_click(self):
        self.base_click(page.mind_advertice_notice_click)
    # 点击新增
    def page_mind_advertice_notice_insert_click(self):
        self.base_click(page.mind_advertice_notice_insert_click)
    # 输入名称
    def page_mind_advertice_notice_insert_name_input(self):
        self.base_input(page.mind_advertice_notice_insert_name_input,page.public_value)
    # 输入名称
    def page_mind_advertice_notice_insert_name2_input(self):
        self.base_input(page.mind_advertice_notice_insert_name_input, page.public_value2)
    # 输入描述
    def page_mind_advertice_notice_insert_desc_input(self):
        self.base_input(page.mind_advertice_notice_insert_desc_input,page.public_value)
    # 上传附件
    def page_mind_advertice_notice_insert_upload_file(self):
        self.base_click(page.mind_advertice_notice_insert_upload_file)
        self.base_upload()
    # 点击保存
    def page_mind_advertice_notice_insert_save_button(self):
        self.base_click(page.mind_advertice_notice_insert_save_button)
    """
        宣传公告审批查询
    """
    # 点击宣传公告审批
    def page_advertice_notice_approval_click(self):
        self.base_click(page.advertice_notice_approval_click)
    # 输入名称
    def page_advertice_notice_approval_search_name_input(self):
        self.base_input(page.advertice_notice_approval_search_name_input,page.public_value)

    # 输入名称
    def page_advertice_notice_approval_search_name2_input(self):
        self.base_input(page.advertice_notice_approval_search_name_input, page.public_value2)
    # 输入描述
    def page_advertice_notice_approval_search_desc_input(self):
        self.base_input(page.advertice_notice_approval_search_desc_input,page.public_value)
    # 点击状态
    def page_advertice_notice_approval_search_status_click(self):
        self.base_click(page.advertice_notice_approval_search_status_click)
    # 选择状态
    def page_advertice_notice_approval_search_status_select(self):
        self.base_click(page.advertice_notice_approval_search_status_select)
    # 点击查询
    def page_advertice_notice_approval_search_button(self):
        self.base_click(page.advertice_notice_approval_search_button)
    """
        宣传公告审批审批
    """
    # 点击审批
    def page_advertice_notice_approval_approval_click(self):
        self.base_click(page.advertice_notice_approval_approval_click)
    # 输入审批意见
    def page_advertice_notice_approval_device_input(self):
        self.base_input(page.advertice_notice_approval_device_input,page.public_value)
    # 点击通过
    def page_advertice_notice_approval_device_through(self):
        self.base_click(page.advertice_notice_approval_device_through)
    """
        宣传公告管理新增
    """
    # 点击宣传公告管理(子)
    def page_advertice_notice_son_click(self):
        self.base_click(page.advertice_notice_son_click)
    # 点击新增
    # 输入名称
    # 输入描述
    # 上传附件
    # 点击保存

    """
        宣传公告管理查询
    """
    # 输入名称
    # 输入描述
    # 点击状态
    # 选择状态
    # 点击查询
    """
        宣传公告管理审批
    """
    # 点击审批
    def page_advertice_notice_son_approval_approval_click(self):
        self.base_click(page.advertice_notice_son_approval_approval_click)
    # 输入审批意见
    # 点击通过

    """
        组装业务方法
    """
    # 我的宣传公告新增
    def mind_advertice_notice_insert(self):
        self.page_file_manage_click()
        self.page_advertice_notice_manage_click()
        self.page_mind_advertice_notice_click()
        self.page_mind_advertice_notice_insert_click()
        self.page_mind_advertice_notice_insert_name_input()
        self.page_mind_advertice_notice_insert_desc_input()
        self.page_mind_advertice_notice_insert_upload_file()
        self.page_mind_advertice_notice_insert_save_button()
        time.sleep(2)

    # 宣传公告审批查询
    def advertice_notice_approval_search(self):
        self.page_advertice_notice_approval_click()
        self.page_advertice_notice_approval_search_name_input()
        self.page_advertice_notice_approval_search_desc_input()
        self.page_advertice_notice_approval_search_status_click()
        self.page_advertice_notice_approval_search_status_select()
        self.page_advertice_notice_approval_search_button()
        time.sleep(2)

    # 宣传公告审批审批
    def advertice_notice_approval_approval(self):
        self.page_advertice_notice_approval_approval_click()
        self.page_advertice_notice_approval_device_input()
        self.page_advertice_notice_approval_device_through()
        time.sleep(2)

    # 宣传公告新增到审批
    def mind_advertice_notice_ISA(self):
        self.mind_advertice_notice_insert()
        self.advertice_notice_approval_search()
        self.advertice_notice_approval_approval()

    # 宣传公告管理新增
    def advertice_notice_manage_son_insert(self):
        self.page_advertice_notice_son_click()
        self.page_mind_advertice_notice_insert_click()
        self.page_mind_advertice_notice_insert_name2_input()
        self.page_mind_advertice_notice_insert_desc_input()
        self.page_mind_advertice_notice_insert_upload_file()
        self.page_mind_advertice_notice_insert_save_button()
        time.sleep(2)

    # 宣传公告管理查询
    def advertice_notice_manage_son_search(self):
        self.page_advertice_notice_approval_search_name2_input()
        self.page_advertice_notice_approval_search_desc_input()
        self.page_advertice_notice_approval_search_status_click()
        self.page_advertice_notice_approval_search_status_select()
        self.page_advertice_notice_approval_search_button()
        time.sleep(2)

    # 宣传公告管理审批
    def advertice_notice_manage_son_approval(self):
        self.page_advertice_notice_son_approval_approval_click()
        self.page_advertice_notice_approval_device_input()
        self.page_advertice_notice_approval_device_through()
        time.sleep(2)

    # 宣传公告管理新增到审批
    def advertice_notice_manage_son_ISA(self):
        self.advertice_notice_manage_son_insert()
        self.advertice_notice_manage_son_search()
        self.advertice_notice_manage_son_approval()
