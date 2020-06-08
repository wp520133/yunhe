import page
import time
from base.base import Base
import allure


class PageFacilityCuringLog(Base):
    """
        养护历史管理
    """
    """
        设备养护日志
    """

    # 点击养护历史管理
    def page_curing_history_manage_click(self):
        self.base_click(page.curing_history_manage_click)

    # 点击设备养护日志
    def page_facility_curing_log_click(self):
        self.base_click(page.facility_curing_log_click)

    # 点击系统类别
    def page_facility_curing_system_class_click(self):
        self.base_click(page.facility_curing_log_system_class_click)

    # 选择系统类别
    def page_facility_curing_system_class_select(self):
        self.base_click(page.facility_curing_log_system_class_select)

    # 点击部件类别
    def page_facility_curing_component_class_click(self):
        self.base_click(page.facility_curing_log_component_class_click)

    # 选择部件类别
    def page_facility_curing_component_class_select(self):
        self.base_click(page.facility_curing_log_component_class_select)

    # 点击部件型号
    def page_facility_curing_component_type_click(self):
        self.base_click(page.facility_curing_log_component_type_click)

    # 选择部件型号
    def page_facility_curing_component_type_select(self):
        self.base_click(page.facility_curing_log_component_type_select)

    # 点击选择时间段
    def page_facility_curing_time_quantum_click(self):
        self.base_click(page.facility_curing_log_time_quantum_click)

    # 选择前半段时间
    def page_facility_curing_time_quantum_select_before(self):
        self.base_click(page.facility_curing_log_time_quantum_select_before)

    # 选择后半段时间
    def page_facility_curing_time_quantum_select_after(self):
        self.base_click(page.facility_curing_log_time_quantum_select_after)

    # 点击评估结果
    def page_facility_curing_assessment_resoult_click(self):
        self.base_click(page.facility_curing_log_assessment_resoult_click)

    # 选择评估结果
    def page_facility_curing_assessment_resoult_select(self):
        self.base_click(page.facility_curing_log_assessment_resoult_select)

    # 点击查询
    def page_facility_curing_log_search_button(self):
        self.base_click(page.facility_curing_log_search_button)

    # 点击重置
    def page_facility_curing_log_reset_button(self):
        self.base_click(page.facility_curing_log_reset_button)

    # 点击养护记录
    def page_facility_curing_curing_record_click(self):
        self.base_click(page.curing_record_click)

    # 点击返回icon
    def page_facility_curing_log_return_icon(self):
        self.base_click(page.facility_curing_log_return_icon)

    """
        组合业务方法
    """

    # 设备养护日志查询
    def facility_curing_log_search(self):
        self.page_curing_history_manage_click()
        self.page_facility_curing_log_click()
        self.page_facility_curing_system_class_click()
        self.page_facility_curing_system_class_select()
        self.page_facility_curing_component_class_click()
        self.page_facility_curing_component_class_select()
        self.page_facility_curing_component_type_click()
        self.page_facility_curing_component_type_select()
        self.page_facility_curing_time_quantum_click()
        self.page_facility_curing_time_quantum_select_before()
        self.page_facility_curing_time_quantum_select_after()
        self.page_facility_curing_assessment_resoult_click()
        self.page_facility_curing_assessment_resoult_select()
        self.page_facility_curing_log_search_button()
        time.sleep(2)

    # 设备养护日志重置
    @allure.step(title="设备养护日志查询与重置")
    def facility_curing_log_reset(self):
        self.facility_curing_log_search()
        self.page_facility_curing_log_reset_button()
        time.sleep(2)

    # 设备养护日志→查看养护记录
    @allure.step(title="设备养护日志养护记录查看")
    def facility_curing_log_watch(self):
        self.page_facility_curing_curing_record_click()
        self.page_facility_curing_log_return_icon()
        time.sleep(2)
