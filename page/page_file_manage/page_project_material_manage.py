import page
import time
from base.base import Base


class PageProjectMaterialManage(Base):
    # 点击资料档案管理
    def page_file_manage_click(self):
        self.base_click(page.file_manage_click)

    """
        我的项目材料新增
    """

    # 点击项目材料管理
    def page_project_material_click(self):
        self.base_click(page.project_material_click)

    # 点击我的项目材料
    def page_mind_material_click(self):
        self.base_click(page.mind_material_click)

    # 点击新增
    def page_mind_material_insert_click(self):
        self.base_click(page.mind_material_insert_click)

    # 输入名称
    def page_mind_material_insert_name_input(self):
        self.base_input(page.mind_material_insert_name_input, page.public_value)

    # 点击选择工程icon
    def page_mind_material_insert_project_icon(self):
        self.base_click(page.mind_material_insert_project_icon)

    # 选择工程radio
    def page_mind_material_insert_project_radio(self):
        self.base_click(page.mind_material_insert_project_radio)

    # 点击确定
    def page_mind_material_insert_sure_button(self):
        self.base_click(page.mind_material_insert_sure_button)

    # 输入描述
    def page_mind_material_insert_desc_input(self):
        self.base_input(page.mind_material_insert_desc_input, page.public_value)

    # 点击上传附件
    def page_mind_material_insert_upload_file(self):
        self.base_click(page.mind_material_insert_upload_file)
        self.base_upload()

    # 点击保存
    def page_mind_material_insert_save_button(self):
        self.base_click(page.mind_material_insert_save_button)

    """
        项目材料审批查询
    """

    # 点击项目材料审批
    def page_project_approval_click(self):
        self.base_click(page.project_approval_click)

    # 输入名称
    def page_project_approval_search_name_input(self):
        self.base_input(page.project_approval_search_name_input, page.public_value)

    # 输入描述
    def page_project_approval_search_desc_input(self):
        self.base_input(page.project_approval_search_desc_input, page.public_value)

    # 点击状态
    def page_project_approval_search_status_click(self):
        self.base_click(page.project_approval_search_status_click)

    # 选择状态
    def page_project_approval_search_status_select(self):
        self.base_click(page.project_approval_search_status_select)

    # 点击查询
    def page_project_approval_search_button(self):
        self.base_click(page.project_approval_search_button)

    """
        项目材料审批查询后审批
    """

    # 点击审批
    def page_project_approval_approval_click(self):
        self.base_click(page.project_approval_approval_click)

    # 输入审批意见
    def page_project_approval_approval_device_input(self):
        self.base_input(page.project_approval_approval_device_input, page.public_value)

    # 点击通过
    def page_project_approval_approval_device_through(self):
        self.base_click(page.project_approval_approval_device_through)

    """
        项目材料管理新增
    """

    # 点击项目材料管理
    def page_project_material_son_click(self):
        self.base_click(page.project_material_son_click)

    # 点击新增
    # 输入名称
    # 点击选择工程icon
    # 选择工程radio
    # 点击确定
    # 输入描述
    # 点击上传附件
    # 点击保存
    """
        项目材料管理查询
    """
    # 输入名称
    # 输入描述
    # 点击状态
    # 选择状态
    # 点击查询
    """
        项目材料管理审批
    """

    # 点击审批
    def page_project_material_son_approval_click(self):
        self.base_click(page.project_material_son_approval_click)

    # 输入审批意见
    # 点击通过
    """
        工程项目管理新增
    """

    # 点击工程项目管理
    def page_engineering_project_manage_click(self):
        self.base_click(page.engineering_project_manage_click)

    # 点击新增
    def page_engineering_project_manage_insert_click(self):
        self.base_click(page.engineering_project_manage_insert_click)

    # 输入名称
    def page_engineering_project_manage_insert_name_input(self):
        self.base_input(page.engineering_project_manage_insert_name_input, page.public_value)

    # 点击状态
    def page_engineering_project_manage_insert_status_click(self):
        self.base_click(page.engineering_project_manage_insert_status_click)

    # 选择状态
    def page_engineering_project_manage_insert_status_select(self):
        self.base_click(page.engineering_project_manage_insert_status_select)

    # 输入造价
    def page_engineering_project_manage_insert_price_input(self):
        self.base_input(page.engineering_project_manage_insert_price_input, page.public_order_num)

    # 输入造价单位
    def page_engineering_project_manage_insert_price_unit(self):
        self.base_input(page.engineering_project_manage_insert_price_unit, page.public_value_num2)

    # 点击选择时间
    def page_engineering_project_manage_insert_time_click(self):
        self.base_click(page.engineering_project_manage_insert_time_click)

    # 选择前时间
    def page_engineering_project_manage_insert_before_time_click(self):
        self.base_click(page.engineering_project_manage_insert_before_time_click)

    # 选择后时间
    def page_engineering_project_manage_insert_after_time_click(self):
        self.base_click(page.engineering_project_manage_insert_after_time_click)

    # 输入描述
    def page_engineering_project_manage_insert_desc_input(self):
        self.base_input(page.engineering_project_manage_insert_desc_input, page.public_value)

    # 点击保存
    def page_engineering_project_manage_insert_save_button(self):
        self.base_click(page.engineering_project_manage_insert_save_button)

    """
        组装业务方法
    """

    # 我的项目材料新增
    def mind_material_insert(self):
        self.page_file_manage_click()
        self.page_project_material_click()
        self.page_mind_material_click()
        self.page_mind_material_insert_click()
        self.page_mind_material_insert_name_input()
        self.page_mind_material_insert_project_icon()
        self.page_mind_material_insert_project_radio()
        self.page_mind_material_insert_sure_button()
        self.page_mind_material_insert_desc_input()
        self.page_mind_material_insert_upload_file()
        self.page_mind_material_insert_save_button()
        time.sleep(2)

    # 项目材料审批查询
    def project_approval_search(self):
        self.page_project_approval_click()
        self.page_project_approval_search_name_input()
        self.page_project_approval_search_desc_input()
        self.page_project_approval_search_status_click()
        self.page_project_approval_search_status_select()
        self.page_project_approval_search_button()
        time.sleep(2)

    # 项目材料审批审批
    def project_approval_approval(self):
        self.page_project_approval_approval_click()
        self.page_project_approval_approval_device_input()
        self.page_project_approval_approval_device_through()
        time.sleep(2)

    # 测试我的项目材料新增到审批
    def mind_material_ISA(self):
        self.mind_material_insert()
        self.project_approval_search()
        self.project_approval_approval()

    # 项目材料管理的新增到审批
    def project_material_son_ISA(self):
        self.page_mind_material_insert_click()
        self.page_mind_material_insert_name_input()
        self.page_mind_material_insert_project_icon()
        self.page_mind_material_insert_project_radio()
        self.page_mind_material_insert_sure_button()
        self.page_mind_material_insert_desc_input()
        self.page_mind_material_insert_upload_file()
        self.page_mind_material_insert_save_button()
        time.sleep(2)
        self.page_project_approval_search_name_input()
        self.page_project_approval_search_desc_input()
        self.page_project_approval_search_status_click()
        self.page_project_approval_search_status_select()
        self.page_project_approval_search_button()
        time.sleep(2)
        self.page_project_material_son_approval_click()
        self.page_project_approval_approval_device_input()
        self.page_project_approval_approval_device_through()
        time.sleep(2)

    # 工程项目管理新增
    def engineering_project_manage_insert(self):
        self.page_engineering_project_manage_click()
        self.page_engineering_project_manage_insert_click()
        self.page_engineering_project_manage_insert_name_input()
        self.page_engineering_project_manage_insert_status_click()
        self.page_engineering_project_manage_insert_status_select()
        self.page_engineering_project_manage_insert_price_input()
        self.page_engineering_project_manage_insert_price_unit()
        self.page_engineering_project_manage_insert_time_click()
        self.page_engineering_project_manage_insert_before_time_click()
        self.page_engineering_project_manage_insert_after_time_click()
        self.page_engineering_project_manage_insert_desc_input()
        self.page_engineering_project_manage_insert_save_button()
        time.sleep(2)