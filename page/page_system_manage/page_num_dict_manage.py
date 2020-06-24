import page
import time
from base.base import Base


class PageNumDictManage(Base):

    # 点击数字字典管理
    def page_num_dict_manage_click_button(self):
        self.base_click(page.num_dict_manage_click_button)

    """
        数字字典管理新增
    """

    # 点击新增
    def page_num_dict_manage_insert_click_button(self):
        self.base_click(page.num_dict_manage_insert_click_button)

    # 输入描述
    def page_num_dict_manage_desc_input(self, desc):
        self.base_input(page.public_desc_input, desc)

    # 点击是否系统字典
    def page_num_dict_manage_insert_isno_dict_click(self):
        self.base_click(page.num_dict_manage_insert_isno_dict_click)

    # 选择是否系统字典
    def page_num_dict_manage_insert_isno_dict_select(self):
        self.base_click(page.num_dict_manage_insert_isno_dict_select)

    # 输入类型
    def page_num_dict_manage_type_input(self, type):
        self.base_input(page.public_type_input, type)

    # 输入类型其他
    def page_num_dict_manage_type_input_other(self, type_other):
        self.base_input(page.public_type_input, type_other)

    # 输入备注信息
    def page_num_dict_manage_remarks_input(self, mark_info):
        self.base_input(page.public_remarks_input, mark_info)

    # 点击保存
    def page_num_dict_manage_insert_save_button(self):
        self.base_click(page.public_insert_save_button)
    
    """
        数字字典管理修改
    """

    # 点击四行修改
    def page_num_dict_manage_four_line_edit_button(self):
        self.base_click(page.num_dict_manage_four_line_edit_button)

    # 点击四行字典项
    def page_num_dict_manage_four_line_dict_nape_button(self):
        self.base_click(page.num_dict_manage_four_line_dict_nape_button)

    """
        字典项新增
    """

    # 点击字典项新增
    def page_num_dict_manage_four_line_dict_nape_insert_button(self):
        self.base_click(page.num_dict_manage_four_line_dict_nape_insert_button)

    # 输入数据值
    def page_num_dict_manage_four_line_value_input(self, data):
        self.base_input(page.public_value_input, data)

    # 输入标签名
    def page_num_dict_manage_four_line_label_input(self, tag):
        self.base_input(page.public_label_input, tag)

    # 输入描述
    def page_num_dict_manage_four_line_desc_input(self, desc):
        self.base_input(page.public_desc_input, desc)

    # 输入排序
    def page_num_dict_manage_four_line_sort_input(self, order):
        self.base_input(page.public_sort_input, order)

    # 输入备注信息
    def page_num_dict_manage_four_line_remarks_input(self, mark_info):
        self.base_input(page.public_remarks_input, mark_info)

    # 点击保存
    def page_num_dict_manage_four_line_insert_button(self):
        self.base_click(page.public_insert_save_button)

    """
        字典项四行编辑
    """

    # 点击编辑
    def page_num_dict_manage_four_line_nape_edit_button(self):
        self.base_click(page.num_dict_manage_four_line_dict_nape_edit_button)

    """
        组装业务方法
    """

    # 数字字典管理新增
    def page_num_dict_manage_insert(self, desc, type_other, mark_info):
        self.page_num_dict_manage_click_button()
        self.page_num_dict_manage_insert_click_button()
        self.page_num_dict_manage_desc_input(desc)
        self.page_num_dict_manage_insert_isno_dict_click()
        self.page_num_dict_manage_insert_isno_dict_select()
        self.page_num_dict_manage_type_input_other(type_other)
        self.page_num_dict_manage_remarks_input(mark_info)
        self.page_num_dict_manage_insert_save_button()
        time.sleep(2)

    # 数字字典管理编辑
    def page_num_dict_manage_edit(self, desc, type, mark_info):
        self.page_num_dict_manage_click_button()
        self.page_num_dict_manage_four_line_edit_button()
        self.page_num_dict_manage_desc_input(desc)
        self.page_num_dict_manage_insert_isno_dict_click()
        self.page_num_dict_manage_insert_isno_dict_select()
        self.page_num_dict_manage_type_input(type)
        self.page_num_dict_manage_remarks_input(mark_info)
        self.page_num_dict_manage_insert_save_button()
        time.sleep(2)

    # 数字字典四行字典项新增
    def page_num_dict_manage_four_line_nape_insert(self, data, tag, desc, order, mark_info):
        self.page_num_dict_manage_click_button()
        self.page_num_dict_manage_four_line_dict_nape_button()
        self.page_num_dict_manage_four_line_dict_nape_insert_button()
        self.page_num_dict_manage_four_line_value_input(data)
        self.page_num_dict_manage_four_line_label_input(tag)
        self.page_num_dict_manage_four_line_desc_input(desc)
        self.page_num_dict_manage_four_line_sort_input(order)
        self.page_num_dict_manage_four_line_remarks_input(mark_info)
        self.page_num_dict_manage_four_line_insert_button()
        time.sleep(2)

    # 数字字典四行字典项编辑
    def page_num_dict_manage_four_line_nape_edit(self, data, tag, desc, order, mark_info):
        self.page_num_dict_manage_click_button()
        self.page_num_dict_manage_four_line_dict_nape_button()
        self.page_num_dict_manage_four_line_nape_edit_button()
        self.page_num_dict_manage_four_line_value_input(data)
        self.page_num_dict_manage_four_line_label_input(tag)
        self.page_num_dict_manage_four_line_desc_input(desc)
        self.page_num_dict_manage_four_line_sort_input(order)
        self.page_num_dict_manage_four_line_remarks_input(mark_info)
        self.page_num_dict_manage_four_line_insert_button()
        time.sleep(2)
