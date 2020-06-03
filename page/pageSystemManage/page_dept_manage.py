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
    def page_dept_manage_input_dept_name(self):
        self.base_input(page.public_name_input, page.public_value)

    # 点击父级节点
    def page_dept_manage_click_parent_node(self):
        self.base_click(page.dept_manage_click_insert_parent_click)

    # 选择父级节点
    def page_dept_manage_select_parent_node(self):
        self.base_click(page.dept_manage_click_insert_parent_select)

    # 输入部门编号
    def page_dept_manage_input_dept_num(self):
        self.base_input(page.public_code_input, page.public_order_num)

    # 输入部门编号其他
    def page_dept_manage_input_dept_num_other(self):
        self.base_input(page.public_code_input, page.public_order_num_other)

    # 输入部门职责
    def page_dept_manage_input_dept_desc_duty(self):
        self.base_input(page.public_dept_duty_input, page.public_value)

    # 输入联系人
    def page_dept_manage_input_link_person_name(self):
        self.base_input(page.public_link_person_name_input, page.public_value)

    # 输入联系电话
    def page_dept_manage_input_link_phone(self):
        self.base_input(page.public_link_phone_input, page.public_moile_phone)

    # 输入负责人
    def page_dept_manage_input_manage_persion_name(self):
        self.base_input(page.public_manage_persion_name_input, page.public_value)

    # 输入排序
    def page_dept_manage_input_order(self):
        self.base_input(page.public_order_input, page.public_order_num)

    # 点击新增保存
    def page_dept_manage_insert_save(self):
        self.base_click(page.public_insert_save_button)

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
    def dept_manage_insert(self):
        self.page_dept_manage_click_button()
        self.page_dept_manage_insert_button_click()
        self.page_dept_manage_input_dept_name()
        self.page_dept_manage_click_parent_node()
        self.page_dept_manage_select_parent_node()
        self.page_dept_manage_input_dept_num()
        self.page_dept_manage_input_dept_desc_duty()
        self.page_dept_manage_input_link_person_name()
        self.page_dept_manage_input_link_phone()
        self.page_dept_manage_input_manage_persion_name()
        self.page_dept_manage_input_order()
        self.page_dept_manage_insert_save()
        time.sleep(2)

    # 实现部门管理编辑
    def dept_manage_edit(self):
        self.page_dept_manage_click_button()
        self.page_dept_manage_edit_button()
        self.page_dept_manage_input_dept_name()
        self.page_dept_manage_click_parent_node()
        self.page_dept_manage_select_parent_node()
        self.page_dept_manage_input_dept_num_other()
        self.page_dept_manage_input_dept_desc_duty()
        self.page_dept_manage_input_link_person_name()
        self.page_dept_manage_input_link_phone()
        self.page_dept_manage_input_manage_persion_name()
        self.page_dept_manage_input_order()
        self.page_dept_manage_insert_save()
        time.sleep(2)

    # 实现部门查看
    def dept_manage_watch(self):
        self.page_dept_manage_click_button()
        self.page_dept_manage_watch_button()
        self.page_refresh()
        time.sleep(2)
