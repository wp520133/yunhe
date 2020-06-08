import page
import time
from base.base import Base
import allure


class PagePartsReplacementLog(Base):
    """
        养护历史管理
    """
    """
        设备养护日志
    """

    # 点击养护历史管理
    def page_curing_history_manage_click(self):
        self.base_click(page.curing_history_manage_click)

    # 点击配件更换日志
    def page_parts_replacement_log_click(self):
        self.base_click(page.parts_replacement_log_click)

    # 点击系统类别
    def page_parts_replacement_system_class_click(self):
        self.base_click(page.parts_replacement_log_system_class_click)

    # 选择系统类别
    def page_parts_replacement_system_class_select(self):
        self.base_click(page.parts_replacement_log_system_class_select)

    # 点击部件类别
    def page_parts_replacement_component_class_click(self):
        self.base_click(page.parts_replacement_log_component_class_click)

    # 选择部件类别
    def page_parts_replacement_component_class_select(self):
        self.base_click(page.parts_replacement_log_component_class_select)

    # 点击部件型号
    def page_parts_replacement_component_type_click(self):
        self.base_click(page.parts_replacement_log_component_type_click)

    # 选择部件型号
    def page_parts_replacement_component_type_select(self):
        self.base_click(page.parts_replacement_log_component_type_select)

    # 点击选择时间段
    def page_parts_replacement_time_quantum_click(self):
        self.base_click(page.parts_replacement_log_time_quantum_click)

    # 选择前半段时间
    def page_parts_replacement_time_quantum_select_before(self):
        self.base_click(page.parts_replacement_log_time_quantum_select_before)

    # 选择后半段时间
    def page_parts_replacement_time_quantum_select_after(self):
        self.base_click(page.parts_replacement_log_time_quantum_select_after)

    # 点击查询
    def page_parts_replacement_log_search_button(self):
        self.base_click(page.parts_replacement_log_search_button)

    # 点击重置
    def page_parts_replacement_log_reset_button(self):
        self.base_click(page.parts_replacement_log_reset_button)

    """
        组装业务方法
    """
    # 查询
    def page_parts_replacement_log_search(self):
        self.page_curing_history_manage_click()
        self.page_parts_replacement_log_click()
        self.page_parts_replacement_system_class_click()
        self.page_parts_replacement_system_class_select()
        self.page_parts_replacement_component_class_click()
        self.page_parts_replacement_component_class_select()
        self.page_parts_replacement_component_type_click()
        self.page_parts_replacement_component_type_select()
        self.page_parts_replacement_time_quantum_click()
        self.page_parts_replacement_time_quantum_select_before()
        self.page_parts_replacement_time_quantum_select_after()
        self.page_parts_replacement_log_search_button()
        time.sleep(2)

    # 重置
    def page_parts_replacement_log_reset(self):
        self.page_parts_replacement_log_search()
        self.page_parts_replacement_log_reset_button()
        time.sleep(2)