import page
import time
from base.base import Base


class PageDeptManage(Base):
    """
        部门管理新增
    """

    # 点击部门管理
    def page_dept_manage_click_button(self):
        self.base_click(page.dept_manage_click_button)

    # 点击新增
    def page_dept_manage_insert_button_click(self):
        self.base_click(page.dept_manage_click_insert_button)

    # 输入部门名称
    def page_dept_manage_input_dept_name(self, dept_name):
        self.base_input(page.public_name_input, dept_name)

    # 点击父级节点
    def page_dept_manage_click_parent_node(self):
        self.base_click(page.dept_manage_click_insert_parent_click)

    # 选择父级节点
    def page_dept_manage_select_parent_node(self):
        self.base_click(page.dept_manage_click_insert_parent_select)

    # 输入部门编号
    def page_dept_manage_input_dept_num(self, dept_number):
        self.base_input(page.public_code_input, dept_number)

    # 输入部门编号其他
    def page_dept_manage_input_dept_num_other(self):
        self.base_input(page.public_code_input, page.public_order_num_other)

    # 输入部门职责
    def page_dept_manage_input_dept_desc_duty(self, desc_duty):
        self.base_input(page.public_dept_duty_input, desc_duty)

    # 输入联系人
    def page_dept_manage_input_link_person_name(self, line_persion_name):
        self.base_input(page.public_link_person_name_input, line_persion_name)

    # 输入联系电话
    def page_dept_manage_input_link_phone(self, line_phone):
        self.base_input(page.public_link_phone_input, line_phone)

    # 输入负责人
    def page_dept_manage_input_manage_persion_name(self, manage_persion_name):
        self.base_input(page.public_manage_persion_name_input, manage_persion_name)

    # 输入排序
    def page_dept_manage_input_order(self, order):
        self.base_input(page.public_order_input, order)

    # 点击新增保存
    def page_dept_manage_insert_save(self):
        self.base_click(page.public_insert_save_button)

    # 点击返回
    def page_dept_manage_insert_return(self):
        self.base_click(page.dept_manage_click_insert_return)

    """
        部门管理编辑
    """

    # 点击编辑按钮
    def page_dept_manage_edit_button(self):
        self.base_click(page.dept_manage_click_edit_button)

    """
        部门查看
    """

    # 点击部门查看按钮(四排)
    def page_dept_manage_watch_button(self):
        self.base_click(page.public_watch_four_line_click)

    # 页面刷新
    def page_refresh(self):
        self.base_refresh()

    """
        组装业务方法
    """

    # 实现部门管理新增
    def dept_manage_insert(self, dept_name, dept_number, desc_duty, line_persion_name, line_phone, manage_persion_name,
                           order):
        self.page_dept_manage_click_button()
        self.page_dept_manage_insert_button_click()
        self.page_dept_manage_input_dept_name(dept_name)
        self.page_dept_manage_click_parent_node()
        self.page_dept_manage_select_parent_node()
        self.page_dept_manage_input_dept_num(dept_number)
        self.page_dept_manage_input_dept_desc_duty(desc_duty)
        self.page_dept_manage_input_link_person_name(line_persion_name)
        self.page_dept_manage_input_link_phone(line_phone)
        self.page_dept_manage_input_manage_persion_name(manage_persion_name)
        self.page_dept_manage_input_order(order)
        self.page_dept_manage_insert_save()
        time.sleep(2)

    # 实现部门管理编辑
    def dept_manage_edit(self, dept_name, desc_duty, line_persion_name, line_phone, manage_persion_name, order):
        self.page_dept_manage_click_button()
        self.page_dept_manage_edit_button()
        self.page_dept_manage_input_dept_name(dept_name)
        self.page_dept_manage_click_parent_node()
        self.page_dept_manage_select_parent_node()
        self.page_dept_manage_input_dept_num_other()
        self.page_dept_manage_input_dept_desc_duty(desc_duty)
        self.page_dept_manage_input_link_person_name(line_persion_name)
        self.page_dept_manage_input_link_phone(line_phone)
        self.page_dept_manage_input_manage_persion_name(manage_persion_name)
        self.page_dept_manage_input_order(order)
        self.page_dept_manage_insert_save()
        time.sleep(2)

    # 实现部门查看
    def dept_manage_watch(self):
        self.page_dept_manage_click_button()
        self.page_dept_manage_watch_button()
        self.page_refresh()
        time.sleep(2)
