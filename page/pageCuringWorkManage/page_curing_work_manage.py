import page
import time
from base.base import Base


class PageCuringWorkManage(Base):
    """
        养护作业管理→养护职责管理→养护小组管理新增
    """

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    # 点击养护职责管理
    def page_curing_duty_manage_click(self):
        self.base_click(page.curing_duty_manage_click)

    # 点击养护小组管理
    def page_curing_team_manage_click(self):
        self.base_click(page.curing_team_manage_click)

    # 点击新增
    def page_curing_team_manage_insert_click(self):
        self.base_click(page.curing_team_manage_insert_click)

    # 输入小组名称
    def page_curing_team_manage_insert_team_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 输入描述
    def page_curing_team_manage_insert_desc_input(self):
        self.base_input(page.public_desc_input, page.public_value2)

    # 点击小组成员新增
    def page_curing_team_manage_insert_team_member_click(self):
        self.base_click(page.curing_team_manage_member_insert_button)

    # 选择人员
    def page_curing_team_manage_member_insert_checkbox_select(self):
        self.base_click(page.curing_team_manage_member_insert_checkbox_select)

    # 点击确定
    def page_curing_team_manage_member_insert_checkbox_sure_button(self):
        self.base_click(page.curing_team_manage_member_insert_checkbox_sure_button)

    # 设为队长
    def page_curing_team_manage_member_appoint_header_click(self):
        self.base_click(page.curing_team_manage_member_appoint_header_click)

    # 点击保存
    def page_curing_team_manage_member_save_button(self):
        self.base_click(page.curing_team_manage_member_save_button)

    """
        养护小组管理查询
    """

    # 输入小组名称
    def page_curing_team_manage_search_team_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 输入队长用户名
    def page_curing_team_manage_search_caption__user_name_input(self):
        self.base_input(page.public_caption_user_name_input, page.public_createBy)

    # 输入队长姓名
    def page_curing_team_manage_search_caption_person_name_input(self):
        self.base_input(page.public_caption_person_name_input, page.public_caption_person_name)

    # 点击查询
    def page_curing_team_manage_search_button(self):
        self.base_click(page.public_search_button)

    """
        养护小组管理编辑
    """

    # 点击编辑按钮
    def page_curing_team_manage_edit_button(self):
        self.base_click(page.public_two_row_button)

    """
        养护小组管理重置
    """

    # 点击重置按钮
    def page_curing_team_manage_reset_button(self):
        self.base_click(page.public_reset_button)

    """
        养护小组查看
    """

    # 点击查看按钮
    def page_curing_team_manage_watch_button(self):
        self.base_click(page.public_one_row_button)

    # 网页回退
    def page_curing_team_manage_back(self):
        self.base_back()

    """
        组装业务方法
    """

    # 新增
    def curing_team_manage_insert(self):
        self.page_curing_work_manage_click()
        self.page_curing_duty_manage_click()
        self.page_curing_team_manage_click()
        self.page_curing_team_manage_insert_click()
        self.page_curing_team_manage_insert_team_name_input()
        self.page_curing_team_manage_insert_desc_input()
        self.page_curing_team_manage_insert_team_member_click()
        self.page_curing_team_manage_member_insert_checkbox_select()
        self.page_curing_team_manage_member_insert_checkbox_sure_button()
        time.sleep(2)
        self.page_curing_team_manage_member_appoint_header_click()
        self.page_curing_team_manage_member_save_button()
        time.sleep(2)

    # 查询
    def curing_team_manage_search(self):
        self.page_curing_team_manage_search_team_name_input()
        self.page_curing_team_manage_search_caption__user_name_input()
        self.page_curing_team_manage_search_caption_person_name_input()
        self.page_curing_team_manage_search_button()
        time.sleep(2)

    # 新增、查看、编辑
    def curing_team_manage_edit(self):
        self.curing_team_manage_insert()
        self.curing_team_manage_search()
        self.page_curing_team_manage_edit_button()
        self.page_curing_team_manage_insert_team_name_input()
        self.page_curing_team_manage_insert_desc_input()
        self.page_curing_team_manage_insert_team_member_click()
        self.page_curing_team_manage_member_insert_checkbox_select()
        self.page_curing_team_manage_member_insert_checkbox_sure_button()
        time.sleep(2)
        self.page_curing_team_manage_member_save_button()
        time.sleep(2)
    # 重置
    def curing_team_manage_reset(self):
        self.curing_team_manage_search()
        self.page_curing_team_manage_reset_button()
        time.sleep(2)

    # 查看
    def curing_team_manage_watch(self):
        self.curing_team_manage_search()
        self.page_curing_team_manage_watch_button()
        self.page_curing_team_manage_back()
        time.sleep(2)
