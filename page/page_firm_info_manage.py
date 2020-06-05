import page
import time
from base.base import Base


class PageFirmInfoManage(Base):
    """
        企业信息列表新增
    """
    # 点击通讯录管理
    def page_address_manage_click(self):
        self.base_click(page.address_manage_click)
    # 点击企业信息列表
    def page_firm_infor_manage_click(self):
        self.base_click(page.firm_infor_manage_click)
    # 点击新增
    def page_firm_infor_manage_insert_click(self):
        self.base_click(page.firm_infor_manage_insert_click)
    # 输入企业名称
    def page_public_firm_infor_manage_insert_firm_name_input(self):
        self.base_input(page.public_firm_infor_manage_insert_firm_name_input,page.public_value)
    # 点击企业类型
    def page_public_firm_infor_manage_insert_firm_type_click(self):
        self.base_click(page.public_firm_infor_manage_insert_firm_type_click)
    # 选择企业类型
    def page_public_firm_infor_manage_insert_firm_type_select(self):
        self.base_click(page.public_firm_infor_manage_insert_firm_type_select)
    # 输入负责人
    def page_public_firm_infor_manage_insert_charge_name_input(self):
        self.base_input(page.public_firm_infor_manage_insert_charge_name_input,page.public_value)
    # 输入联系人
    def page_public_firm_infor_manage_insert_link_name_input(self):
        self.base_input(page.public_firm_infor_manage_insert_link_name_input,page.public_value_num2)
    # 输入联系电话
    def page_public_firm_infor_manage_insert_link_phone_input(self):
        self.base_input(page.public_firm_infor_manage_insert_link_phone_input,page.public_moile_phone)
    # 输入座机电话
    def page_public_firm_infor_manage_insert_tele_phone_input(self):
        self.base_input(page.public_firm_infor_manage_insert_tele_phone_input,page.public_land_line_phone)
    # 输入邮箱
    def page_public_firm_infor_manage_insert_email_input(self):
        self.base_input(page.public_firm_infor_manage_insert_email_input,page.public_email)
    # 输入地址

    # 点击保存

    """
        企业信息列表查询
    """
    # 选择厂家类型

    # 输入厂家名称

    # 输入负责人

    # 输入联系人

    # 点击查询

    # 点击编辑

    # 点击查看
