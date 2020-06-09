import page
import time
from base.base import Base


class PageStudyDataManage(Base):
    """
        我的学习资料新增、查看、重置、编辑→学习资料审批查询、审批、查看、重置
    """
    """
        我的学习资料新增
    """

    # 点击资料档案管理
    def page_file_manage_click(self):
        self.base_click(page.file_manage_click)

    # 点击学习资料管理
    def page_study_data_manage_click(self):
        self.base_click(page.study_data_manage_click)

    # 点击我的学习资料
    def page_mine_study_data_click(self):
        self.base_click(page.mine_study_data_click)

    # 点击新增
    def page_mine_study_data_insert_click(self):
        self.base_click(page.mine_study_data_insert_click)

    # 输入名称
    def page_mine_study_data_insert_name_input(self):
        self.base_input(page.public_mine_study_data_insert_name_input, page.public_value)

    # 输入描述
    def page_mine_study_data_insert_desc_input(self):
        self.base_input(page.public_mine_study_data_insert_desc_input, page.public_value)

    # 点击上传按钮
    def mine_study_data_upload_file_button(self):
        self.base_click(page.public_mine_study_data_upload_file_button)

    # # 点击保存
    def mine_study_data_save_button(self):
        self.base_click(page.public_mine_study_data_insert_save_button)

    """
        我的学习资料查询
    """

    # 输入名称
    def page_mine_study_data_search_name_input(self):
        self.base_input(page.public_mine_study_data_search_name_input, page.public_value)

    # 输入描述
    def page_mine_study_data_search_desc_input(self):
        self.base_input(page.public_mine_study_data_search_desc_input, page.public_value)

    # 点击状态
    def page_mine_study_data_search_status_click(self):
        self.base_click(page.public_mine_study_data_search_type_click)

    # 选择状态
    def page_mine_study_data_search_status_select(self):
        self.base_click(page.public_mine_study_data_search_type_select)

    # 点击查询
    def page_mine_study_data_search_button(self):
        self.base_click(page.public_public_mine_study_data_search_button)

    """
        我的学习资料重置
    """

    # 点击重置
    def page_mine_study_data_reset_button(self):
        self.base_click(page.public_mine_study_data_reset_button)

    """
        我的学习资料编辑
    """

    # 点击编辑
    def page_mine_study_data_edit_button(self):
        self.base_click(page.mine_study_data_edit_button)

    """
        我的学习资料查看
    """

    # 点击查看
    def page_mine_study_data_watch_button(self):
        self.base_click(page.mine_study_data_watch_button)

    """
        我的学习资料审批查询
    """

    # 点击学习资料审批
    def page_study_data_approval_click(self):
        self.base_click(page.study_data_approval_click)

    # 输入名称
    # 输入描述
    # 点击状态
    # 选择状态
    # 点击查询
    # 点击审批
    def page_study_data_approval_excute_click(self):
        self.base_click(page.study_data_approval_excute_click)

    # 输入审批意见
    def page_study_data_approval_excute_device_input(self):
        self.base_input(page.study_data_approval_excute_device_input, page.public_value)

    # 点击通过
    def page_study_data_approval_excute_though_button(self):
        self.base_click(page.study_data_approval_excute_though_button)

    # 学习资料审批查看
    def page_study_data_approval_excute_watch_click(self):
        self.base_click(page.study_data_approval_excute_watch_click)

    """
        学习资料列表查询
    """

    # 点击学习资料列表
    def page_study_data_list_click(self):
        self.base_click(page.study_data_list_click)

    # 输入名称
    # 输入描述
    # 点击查询

    """
        学习资料重置
    """
    # 点击重置
    """
        学习资料查看
    """

    # 点击查看
    def page_study_data_watch_button(self):
        self.base_click(page.study_data_list_watch_click)

    # 点击重置
    """
        学习资料查看
    """

    # 点击查看
    def page_study_data_list_watch_button(self):
        self.base_click(page.public_one_row_button)

    """
        学习资料管理(子)新增
    """

    # 点击学习资料管理(子)模块
    def page_study_data_manage_son_click(self):
        self.base_click(page.study_data_manage_son_click)

    # 点击新增
    # 输入名称
    # 输入描述
    # 点击上传附件按钮
    # 点击保存

    """
        学习资料管理(子)查询
    """
    # 输入名称
    # 输入描述
    # 点击状态
    # 选择状态
    # 点击查询

    """
        学习资料管理(子)编辑
    """

    # 点击编辑
    def page_study_data_manage_son_edit_button(self):
        self.base_click(page.public_four_row_button)

    """
        学习资料管理(子)审批
    """

    # 点击审批
    def page_study_data_manage_son_approval_button(self):
        self.base_click(page.public_three_row_button)

    """
        学习资料管理(子)查看
    """

    # 点击查看
    def page_study_data_manage_son_watch_button(self):
        self.base_click(page.public_one_row_button)

    """
        学习资料管理(子)重置
    """
    # 点击重置

    """
        组装业务方法
    """

    # 我的学习资料新增
    def mine_study_data_insert(self):
        self.page_file_manage_click()
        self.page_study_data_manage_click()
        self.page_mine_study_data_click()
        self.page_mine_study_data_insert_click()
        self.page_mine_study_data_insert_name_input()
        self.page_mine_study_data_insert_desc_input()
        self.mine_study_data_upload_file_button()
        self.base_upload()
        self.mine_study_data_save_button()
        time.sleep(2)

    # 我的学习资料查询
    def mine_study_data_search(self):
        self.page_mine_study_data_search_name_input()
        self.page_mine_study_data_search_desc_input()
        self.page_mine_study_data_search_status_click()
        self.page_mine_study_data_search_status_select()
        self.page_mine_study_data_search_button()
        time.sleep(2)

    # 学习资料审批查询
    def study_data_approval_search(self):
        self.page_study_data_approval_click()
        self.mine_study_data_search()
        time.sleep(2)

    # 我的学习资料编辑
    def mine_study_data_edit(self):
        self.mine_study_data_insert()
        self.mine_study_data_search()
        self.page_mine_study_data_edit_button()
        self.page_mine_study_data_insert_name_input()
        self.page_mine_study_data_insert_desc_input()
        self.mine_study_data_upload_file_button()
        self.base_upload()
        self.mine_study_data_save_button()
        time.sleep(2)

    # 我的学习资料重置
    def mine_study_data_reset(self):
        self.mine_study_data_search()
        self.page_mine_study_data_reset_button()
        time.sleep(2)

    # 我的学习资料查看
    def mine_study_data_watch(self):
        self.mine_study_data_search()
        self.page_mine_study_data_watch_button()
        time.sleep(2)

    # 学习资料审批
    def study_data_approval(self):
        self.mine_study_data_insert()
        self.study_data_approval_search()
        self.page_study_data_approval_excute_click()
        self.page_study_data_approval_excute_device_input()
        self.page_study_data_approval_excute_though_button()
        time.sleep(2)
