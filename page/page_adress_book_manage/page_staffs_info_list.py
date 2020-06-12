import page
import time
from base.base import Base


class PageStaffsInfoList(Base):

    # 点击通讯录管理
    def page_address_manage_click(self):
        self.base_click(page.address_manage_click)

    """
       员工信息列表新增
    """

    # 点击员工信息列表
    def page_staffs_info_list_click(self):
        self.base_click(page.staffs_info_list_click)

    # 点击新增
    def page_staffs_info_list_insert_click(self):
        self.base_click(page.staffs_info_list_insert_click)

    # 输入姓名
    def page_staffs_info_list_insert_name_input(self):
        self.base_input(page.staffs_info_list_insert_name_input, page.public_value)

    # 点击性别
    def page_staffs_info_list_insert_sex_click(self):
        self.base_click(page.staffs_info_list_insert_sex_click)

    # 选择性别
    def page_staffs_info_list_insert_sex_select(self):
        self.base_click(page.staffs_info_list_insert_sex_select)

    # 点击状态
    def page_staffs_info_list_insert_status_click(self):
        self.base_click(page.staffs_info_list_insert_status_click)

    # 选择状态
    def page_staffs_info_list_insert_status_select(self):
        self.base_click(page.staffs_info_list_insert_status_select)

    # 点击入职时间
    def page_staffs_info_list_insert_time_click(self):
        self.base_click(page.staffs_info_list_insert_time_click)

    # 选择入职时间
    def page_staffs_info_list_insert_time_select(self):
        self.base_click(page.staffs_info_list_insert_time_select)

    # 点击部门
    def page_staffs_info_list_insert_dept_click(self):
        self.base_click(page.staffs_info_list_insert_dept_click)

    # 选择部门
    def page_staffs_info_list_insert_dept_select(self):
        self.base_click(page.staffs_info_list_insert_dept_select)

    # 点击岗位
    def page_staffs_info_list_insert_job_click(self):
        self.base_click(page.staffs_info_list_insert_job_click)

    # 选择岗位
    def page_staffs_info_list_insert_job_select(self):
        self.base_click_enter(page.staffs_info_list_insert_job_click)

    # 点击岗位等级
    def page_staffs_info_list_insert_job_order_click(self):
        self.base_click_enter(page.staffs_info_list_insert_job_order_click)

    # 选择岗位等级
    def page_staffs_info_list_insert_job_order_select(self):
        self.base_click_enter(page.staffs_info_list_insert_job_order_click)

    # 输入联系电话
    def page_staffs_info_list_insert_mobile_phone_input(self):
        self.base_input(page.staffs_info_list_insert_mobile_phone_input, page.public_moile_phone)

    # 输入座机电话
    def page_staffs_info_list_insert_phone_input(self):
        self.base_input(page.staffs_info_list_insert_phone_input, page.public_land_line_phone)

    # 输入微信号
    def page_staffs_info_list_insert_vx_num_input(self):
        self.base_input(page.staffs_info_list_insert_vx_num_input, page.public_value)

    # 输入身份证
    def page_staffs_info_list_insert_idcardno_input(self):
        self.base_input(page.staffs_info_list_insert_idcardno_input, page.public_id_card_no)

    # 输入现住址
    def page_staffs_info_list_insert_addr_input(self):
        self.base_input(page.staffs_info_list_insert_addr_input, page.public_value)

    # 输入户口所在地
    def page_staffs_info_list_insert_registered_permanent_residence_input(self):
        self.base_input(page.staffs_info_list_insert_registered_permanent_residence_input, page.public_value)

    # 输入紧急联系人
    def page_staffs_info_list_insert_emergency_contact_name_input(self):
        self.base_input(page.staffs_info_list_insert_emergency_contact_name_input, page.public_value)

    # 输入紧急联系人电话
    def page_staffs_info_list_insert_emergency_contact_phone_input(self):
        self.base_input(page.staffs_info_list_insert_emergency_contact_phone_input, page.public_moile_phone)

    # 输入婚孕情况
    def page_staffs_info_list_insert_marriage_childbirth_status_input(self):
        self.base_input(page.staffs_info_list_insert_marriage_childbirth_status_input, page.public_value)

    # 输入技术特长
    def page_staffs_info_list_insert_tech_input(self):
        self.base_input(page.staffs_info_list_insert_tech_input, page.public_value)

    # 点击保存
    def page_staffs_info_list_insert_save_button(self):
        self.base_click(page.staffs_info_list_insert_save_button)

    """
        员工信息列表查询
    """
    # 点击人员状态

    # 选择人员状态

    # 输入姓名

    # 点击岗位

    # 选择岗位

    # 点击查询

    """
        组装业务方法 
    """

    # 员工信息新增
    def staffs_info_insert(self):
        self.page_address_manage_click()
        self.page_staffs_info_list_click()
        self.page_staffs_info_list_insert_click()
        self.page_staffs_info_list_insert_name_input()
        self.page_staffs_info_list_insert_sex_click()
        self.page_staffs_info_list_insert_sex_select()
        self.page_staffs_info_list_insert_status_click()
        self.page_staffs_info_list_insert_status_select()
        self.page_staffs_info_list_insert_time_click()
        self.page_staffs_info_list_insert_time_select()
        self.page_staffs_info_list_insert_dept_click()
        self.page_staffs_info_list_insert_dept_select()
        self.page_staffs_info_list_insert_job_click()
        self.page_staffs_info_list_insert_job_select()
        self.page_staffs_info_list_insert_job_order_click()
        self.page_staffs_info_list_insert_job_order_select()
        self.page_staffs_info_list_insert_mobile_phone_input()
        self.page_staffs_info_list_insert_phone_input()
        self.page_staffs_info_list_insert_vx_num_input()
        self.page_staffs_info_list_insert_idcardno_input()
        self.page_staffs_info_list_insert_addr_input()
        self.page_staffs_info_list_insert_registered_permanent_residence_input()
        self.page_staffs_info_list_insert_emergency_contact_name_input()
        self.page_staffs_info_list_insert_emergency_contact_phone_input()
        self.page_staffs_info_list_insert_marriage_childbirth_status_input()
        self.page_staffs_info_list_insert_tech_input()
        self.page_staffs_info_list_insert_save_button()
        time.sleep(2)

    def  insert(self):
        self.page_staffs_info_list_insert_click()
        self.page_staffs_info_list_insert_name_input()
        self.page_staffs_info_list_insert_sex_click()
        self.page_staffs_info_list_insert_sex_select()
        self.page_staffs_info_list_insert_status_click()
        self.page_staffs_info_list_insert_status_select()
        self.page_staffs_info_list_insert_time_click()
        self.page_staffs_info_list_insert_time_select()
        self.page_staffs_info_list_insert_dept_click()
        self.page_staffs_info_list_insert_dept_select()
        self.page_staffs_info_list_insert_job_click()
        self.page_staffs_info_list_insert_job_select()
        self.page_staffs_info_list_insert_job_order_click()
        self.page_staffs_info_list_insert_job_order_select()
        self.page_staffs_info_list_insert_mobile_phone_input()
        self.page_staffs_info_list_insert_phone_input()
        self.page_staffs_info_list_insert_vx_num_input()
        self.page_staffs_info_list_insert_idcardno_input()
        self.page_staffs_info_list_insert_addr_input()
        self.page_staffs_info_list_insert_registered_permanent_residence_input()
        self.page_staffs_info_list_insert_emergency_contact_name_input()
        self.page_staffs_info_list_insert_emergency_contact_phone_input()
        self.page_staffs_info_list_insert_marriage_childbirth_status_input()
        self.page_staffs_info_list_insert_tech_input()
        self.page_staffs_info_list_insert_save_button()
        time.sleep(2)