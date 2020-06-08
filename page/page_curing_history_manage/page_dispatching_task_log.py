import page
import time
from base.base import Base
import allure


class PageDispatchingTaskLog(Base):
    """
        养护历史管理
    """
    """
        派工与任务日志
    """

    # 点击养护历史管理
    def page_curing_history_manage_click(self):
        self.base_click(page.curing_history_manage_click)

    # 点击派工与养护日志
    def page_dispatching_task_log_click(self):
        self.base_click(page.dispatching_task_log_click)

    # 输入创建人
    def page_dispatching_task_log_search_create_by_input(self,create_by):
        self.base_input(page.dispatching_task_log_search_create_by_input,create_by)

    # 点击选择时间段
    def page_dispatching_task_time_quantum_click(self):
        self.base_click(page.dispatching_task_log_time_quantum_click)

    # 选择前半段时间
    def page_dispatching_task_time_quantum_select_before(self):
        self.base_click(page.dispatching_task_log_time_quantum_select_before)

    # 选择后半段时间
    def page_dispatching_task_time_quantum_select_after(self):
        self.base_click(page.dispatching_task_log_time_quantum_select_after)

    # 点击查询
    def page_dispatching_task_log_search_button(self):
        self.base_click(page.dispatching_task_log_search_button)

    # 点击重置
    def page_dispatching_task_log_reset_button(self):
        self.base_click(page.dispatching_task_log_reset_button)

    # 点击查看

    def page_dispatching_task_log_watch_button(self):
        self.base_click(page.dispatching_task_log_watch_button)

    # 点击工作内容
    def page_dispatching_task_log_work_content_click(self):
        self.base_click(page.dispatching_task_log_work_content_click)

    # 点击操作记录
    def page_dispatching_task_log_operating_record_click(self):
        self.base_click(page.dispatching_task_log_operating_record_click)

    # 点击返回
    def page_dispatching_task_log_return_click(self):
        self.base_click(page.dispatching_task_log_return_click)
    """
        组合业务方法
    """
    # 查询
    def dispatching_task_log_search(self,create_by):
        self.page_curing_history_manage_click()
        self.page_dispatching_task_log_click()
        self.page_dispatching_task_log_search_create_by_input(create_by)
        self.page_dispatching_task_time_quantum_click()
        self.page_dispatching_task_time_quantum_select_before()
        self.page_dispatching_task_time_quantum_select_after()
        self.page_dispatching_task_log_search_button()
        time.sleep(2)

    # 重置
    def dispatching_task_log_reset(self,create_by):
        self.dispatching_task_log_search(create_by)
        self.page_dispatching_task_log_reset_button()
        time.sleep(2)

    # 查看
    def dispatching_task_log_watch(self):
        self.page_dispatching_task_log_watch_button()
        self.page_dispatching_task_log_work_content_click()
        self.page_dispatching_task_log_operating_record_click()
        self.page_dispatching_task_log_return_click()
        time.sleep(2)