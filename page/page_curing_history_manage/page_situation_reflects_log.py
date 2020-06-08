import page
import time
from base.base import Base
import allure


class PageSituationReflectsLog(Base):
    """
        养护历史管理
    """
    """
        故障维修日志
    """

    # 点击养护历史管理
    def page_curing_history_manage_click(self):
        self.base_click(page.curing_history_manage_click)

    # 点击故障维修日志
    def page_situation_reflects_service_log_click(self):
        self.base_click(page.situation_reflects_log_click)

    # 点击系统类别
    def page_situation_reflects_system_class_click(self):
        self.base_click(page.situation_reflects_log_system_class_click)

    # 选择系统类别
    def page_situation_reflects_system_class_select(self):
        self.base_click(page.situation_reflects_log_system_class_select)

    # 点击部件类别
    def page_situation_reflects_component_class_click(self):
        self.base_click(page.situation_reflects_log_component_class_click)

    # 选择部件类别
    def page_situation_reflects_component_class_select(self):
        self.base_click(page.situation_reflects_log_component_class_select)

    # 点击部件型号
    def page_situation_reflects_component_type_click(self):
        self.base_click(page.situation_reflects_log_component_type_click)

    # 选择部件型号
    def page_situation_reflects_component_type_select(self):
        self.base_click(page.situation_reflects_log_component_type_select)

    # 点击选择时间段
    def page_situation_reflects_time_quantum_click(self):
        self.base_click(page.situation_reflects_log_time_quantum_click)

    # 选择前半段时间
    def page_situation_reflects_time_quantum_select_before(self):
        self.base_click(page.situation_reflects_log_time_quantum_select_before)

    # 选择后半段时间
    def page_situation_reflects_time_quantum_select_after(self):
        self.base_click(page.situation_reflects_log_time_quantum_select_after)

    # 点击查询
    def page_situation_reflects_log_search_button(self):
        self.base_click(page.situation_reflects_log_search_button)

    # 点击重置
    def page_situation_reflects_log_reset_button(self):
        self.base_click(page.situation_reflects_log_reset_button)

    # 点击查看

    def page_situation_reflects_log_watch_button(self):
        self.base_click(page.situation_reflects_log_watch_button)

    # 点击查看退出icon
    def page_situation_reflects_log_watch_exct_icon(self):
        self.base_click(page.situation_reflects_log_watch_exct_icon)

    """
        组装业务方法
    """

    # 查询

    def situation_reflects_log_search(self):
        self.page_curing_history_manage_click()
        self.page_situation_reflects_service_log_click()
        self.page_situation_reflects_system_class_click()
        self.page_situation_reflects_system_class_select()
        self.page_situation_reflects_component_class_click()
        self.page_situation_reflects_component_class_select()
        self.page_situation_reflects_component_type_click()
        self.page_situation_reflects_component_type_select()
        self.page_situation_reflects_time_quantum_click()
        self.page_situation_reflects_time_quantum_select_before()
        self.page_situation_reflects_time_quantum_select_after()
        self.page_situation_reflects_log_search_button()
        time.sleep(2)

    # 重置
    def situation_reflects_log_reset(self):
        self.situation_reflects_log_search()
        self.page_situation_reflects_log_reset_button()
        time.sleep(2)

    # 查看
    def situation_reflects_log_watch(self):
        self.page_situation_reflects_log_watch_button()
        self.page_situation_reflects_log_watch_exct_icon()
        time.sleep(2)
