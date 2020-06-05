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
    def page_firm_info_manage_click(self):
        self.base_click(page.firm_infor_manage_click)

    # 点击新增
    def page_firm_info_manage_insert_click(self):
        self.base_click(page.firm_infor_manage_insert_click)

    # 输入企业名称
    def page_public_firm_info_manage_insert_firm_name_input(self, firmName):
        self.base_input(page.public_firm_infor_manage_insert_firm_name_input, firmName)
    # 编辑输入企业名称
    def page_public_firm_info_manage_insert_firm_name_edit_input(self, editfirmName):
        self.base_input(page.public_firm_infor_manage_insert_firm_name_input, editfirmName)

    # 点击企业类型
    def page_public_firm_info_manage_insert_firm_type_click(self):
        self.base_click(page.public_firm_infor_manage_insert_firm_type_click)

    # 选择企业类型
    def page_public_firm_info_manage_insert_firm_type_select(self):
        self.base_click(page.public_firm_infor_manage_insert_firm_type_select)

    # 输入负责人
    def page_public_firm_info_manage_insert_charge_name_input(self, chargeName):
        self.base_input(page.public_firm_infor_manage_insert_charge_name_input, chargeName)

    # 输入联系人
    def page_public_firm_info_manage_insert_link_name_input(self, linkName):
        self.base_input(page.public_firm_infor_manage_insert_link_name_input, linkName)

    # 输入联系电话
    def page_public_firm_info_manage_insert_link_phone_input(self, linkPhone):
        self.base_input(page.public_firm_infor_manage_insert_link_phone_input, linkPhone)

    # 输入座机电话
    def page_public_firm_info_manage_insert_tele_phone_input(self, telePhone):
        self.base_input(page.public_firm_infor_manage_insert_tele_phone_input, telePhone)

    # 输入邮箱
    def page_public_firm_info_manage_insert_email_input(self, email):
        self.base_input(page.public_firm_infor_manage_insert_email_input, email)

    # 输入地址
    def page_public_firm_info_manage_insert_site_input(self, site):
        self.base_input(page.public_firm_infor_manage_insert_site_input, site)

    # 点击保存
    def page_public_firm_info_manage_insert_save_button(self):
        self.base_click(page.public_firm_infor_manage_insert_save_button)

    """
        企业信息列表查询
    """
    # 选择厂家类型
    # 输入厂家名称
    # 输入负责人
    # 输入联系人
    # 点击查询
    def page_firm_info_manage_search_button(self):
        self.base_click(page.firm_infor_manage_search_button)
    # 点击编辑
    def page_firm_info_manage_edit_button(self):
        self.base_click(page.firm_infor_manage_edit_button)
    # 点击查看
    def page_firm_info_manage_watch_button(self):
        self.base_click(page.firm_infor_manage_watch_button)
    """
        组装业务方法
    """

    # 新增
    def firm_info_manage_insert(self, firmName, chargeName, linkName, linkPhone, telePhone, email, site):
        self.page_address_manage_click()
        self.page_firm_info_manage_click()
        self.page_firm_info_manage_insert_click()
        self.page_public_firm_info_manage_insert_firm_name_input(firmName)
        self.page_public_firm_info_manage_insert_firm_type_click()
        self.page_public_firm_info_manage_insert_firm_type_select()
        self.page_public_firm_info_manage_insert_charge_name_input(chargeName)
        self.page_public_firm_info_manage_insert_link_name_input(linkName)
        self.page_public_firm_info_manage_insert_link_phone_input(linkPhone)
        self.page_public_firm_info_manage_insert_tele_phone_input(telePhone)
        self.page_public_firm_info_manage_insert_email_input(email)
        self.page_public_firm_info_manage_insert_site_input(site)
        self.page_public_firm_info_manage_insert_save_button()
        time.sleep(2)

        # 查询
    def firm_info_manage_search(self,firmName,chargeName,linkName):
        self.page_public_firm_info_manage_insert_firm_type_click()
        self.page_public_firm_info_manage_insert_firm_type_select()
        self.page_public_firm_info_manage_insert_firm_name_input(firmName)
        self.page_public_firm_info_manage_insert_charge_name_input(chargeName)
        self.page_public_firm_info_manage_insert_link_name_input(linkName)
        self.page_firm_info_manage_search_button()
        time.sleep(2)


    # 编辑
    def firm_info_manage_edit(self,firmName, chargeName, linkName, linkPhone, telePhone, email, site,editfirmName):
        self.firm_info_manage_insert(firmName, chargeName, linkName, linkPhone, telePhone, email, site)
        self.firm_info_manage_search(firmName,chargeName,linkName)
        self.page_firm_info_manage_edit_button()
        self.page_public_firm_info_manage_insert_firm_name_edit_input(editfirmName)
        self.page_public_firm_info_manage_insert_firm_type_click()
        self.page_public_firm_info_manage_insert_firm_type_select()
        self.page_public_firm_info_manage_insert_charge_name_input(chargeName)
        self.page_public_firm_info_manage_insert_link_name_input(linkName)
        self.page_public_firm_info_manage_insert_link_phone_input(linkPhone)
        self.page_public_firm_info_manage_insert_tele_phone_input(telePhone)
        self.page_public_firm_info_manage_insert_email_input(email)
        self.page_public_firm_info_manage_insert_site_input(site)
        self.page_public_firm_info_manage_insert_save_button()
        time.sleep(2)

    # 查看
    def firm_info_manage_watch(self,firmName, chargeName, linkName):
        self.firm_info_manage_search(firmName, chargeName, linkName)
        self.page_firm_info_manage_watch_button()
        self.base_refresh()
        time.sleep(2)

