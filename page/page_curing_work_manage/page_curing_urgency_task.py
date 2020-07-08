import page
import time
from base.base import Base


class PageCuringUrgencyTask(Base):
    """
        养护作业管理→养护职责管理→养护小组管理新增
    """

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    # 点击养护任务管理
    def page_curing_tesk_manage_click(self):
        self.base_click(page.curing_tesk_manage_click)

    """
        紧急养护任务新增
    """

    # 点击紧急养护任务
    def page_curing_urgency_task_click(self):
        self.base_click(page.curing_urgency_task_click)

    # 点击新增
    def page_curing_urgency_task_insert_click(self):
        self.base_click(page.curing_urgency_task_insert_click)

    # 输入养护名称
    def page_curing_urgency_task_insert_name(self, task_name):
        self.base_input(page.curing_urgency_task_insert_name, task_name)

    # 输入养护名称2
    def page_curing_urgency_task_insert_name2(self, task_name2):
        self.base_input(page.curing_urgency_task_insert_name, task_name2)

    # 点击选择时间
    def page_curing_urgency_task_insert_select_name(self):
        self.base_click(page.curing_urgency_task_insert_select_name)

    # 选择前时间
    def page_curing_urgency_task_insert_select_before_name(self):
        self.base_click(page.curing_urgency_task_insert_select_before_name)

    # 选择后时间
    def page_curing_urgency_task_insert_select_after_name(self):
        self.base_click(page.curing_urgency_task_insert_select_after_name)

    # 点击是否为养护小组
    def page_curing_urgency_task_insert_is_team_click(self):
        self.base_click(page.curing_urgency_task_insert_is_team_click)

    # 选择是否为养护小组
    def page_curing_urgency_task_insert_is_team_select(self):
        self.base_click(page.curing_urgency_task_insert_is_team_select)

    # 点击养护人icon
    def page_curing_urgency_task_insert_curing_persion_icon(self):
        self.base_click(page.curing_urgency_task_insert_curing_persion_icon)

    # 选择养护人radio
    def page_curing_urgency_task_insert_radio(self):
        self.base_click(page.curing_urgency_task_insert_radio)

    # 点击确定
    def page_curing_urgency_task_insert_sure_button(self):
        self.base_click(page.curing_urgency_task_insert_sure_button)

    # 输入执行内容
    def page_curing_urgency_task_insert_excute_content(self, content):
        self.base_input(page.curing_urgency_task_insert_excute_content, content)

    # 点击是否自动审核
    def page_curing_urgency_task_insert_is_approval(self):
        self.base_click(page.curing_urgency_task_insert_is_approval)

    # 输入备注
    def page_curing_urgency_task_insert_remark(self, remark):
        self.base_input(page.curing_urgency_task_insert_remark, remark)

    # 点击保存
    def page_curing_urgency_task_insert_save(self):
        self.base_click(page.curing_urgency_task_insert_save)

    """
        紧急养护任务查询
    """

    # 输入名称
    def page_curing_urgency_task_search_name(self, name):
        self.base_input(page.curing_urgency_task_search_name, name)

    # 点击状态
    def page_curing_urgency_task_search_status_click(self):
        self.base_click(page.curing_urgency_task_search_status_click)

    # 选择状态
    def page_curing_urgency_task_search_status_select(self):
        self.base_click(page.curing_urgency_task_search_status_select)

    # 点击查询
    def page_curing_urgency_task_search_button(self):
        self.base_click(page.curing_urgency_task_search_button)

    # 点击重置
    def page_curing_urgency_task_reset_button(self):
        self.base_click(page.curing_urgency_task_reset_button)

    # 点击查看
    def page_curing_urgency_task_watch_button(self):
        self.base_click(page.curing_urgency_task_watch_button)

    # 点击编辑
    def page_curing_urgency_task_edit_button(self):
        self.base_click(page.curing_urgency_task_edit_button)

    """
        组装业务方法
    """

    # 测试紧急养护点击
    def curing_urgency_task_click(self):
        self.page_curing_work_manage_click()
        self.page_curing_tesk_manage_click()
        self.page_curing_urgency_task_click()
        time.sleep(2)

    # 新增
    def curing_urgency_task_insert(self, task_name, content, remark):
        self.curing_urgency_task_click()
        self.page_curing_urgency_task_insert_click()
        self.page_curing_urgency_task_insert_name(task_name)
        self.page_curing_urgency_task_insert_select_name()
        self.page_curing_urgency_task_insert_select_before_name()
        self.page_curing_urgency_task_insert_select_after_name()
        self.page_curing_urgency_task_insert_is_team_click()
        self.page_curing_urgency_task_insert_is_team_select()
        self.page_curing_urgency_task_insert_curing_persion_icon()
        self.page_curing_urgency_task_insert_radio()
        self.page_curing_urgency_task_insert_sure_button()
        self.page_curing_urgency_task_insert_excute_content(content)
        self.page_curing_urgency_task_insert_is_approval()
        self.page_curing_urgency_task_insert_remark(remark)
        self.page_curing_urgency_task_insert_save()
        time.sleep(2)

    # 查询
    def curing_urgency_task_search(self, name):
        self.page_curing_urgency_task_search_name(name)
        self.page_curing_urgency_task_search_status_click()
        self.page_curing_urgency_task_search_status_select()
        self.page_curing_urgency_task_search_button()
        time.sleep(2)

    # 编辑
    def curing_urgency_task_edit(self, task_name, content, remark, name, task_name2):
        self.curing_urgency_task_insert(task_name, content, remark)
        self.curing_urgency_task_search(name)
        self.page_curing_urgency_task_edit_button()
        self.page_curing_urgency_task_insert_name2(task_name2)
        self.page_curing_urgency_task_insert_select_name()
        self.page_curing_urgency_task_insert_select_before_name()
        self.page_curing_urgency_task_insert_select_after_name()
        self.page_curing_urgency_task_insert_is_team_click()
        self.page_curing_urgency_task_insert_is_team_select()
        self.page_curing_urgency_task_insert_curing_persion_icon()
        self.page_curing_urgency_task_insert_radio()
        self.page_curing_urgency_task_insert_sure_button()
        self.page_curing_urgency_task_insert_excute_content(content)
        self.page_curing_urgency_task_insert_is_approval()
        self.page_curing_urgency_task_insert_remark(remark)
        self.page_curing_urgency_task_insert_save()
        time.sleep(2)

    # 重置
    def curing_urgency_task_reset(self, name):
        self.curing_urgency_task_search(name)
        self.page_curing_urgency_task_reset_button()
        time.sleep(2)

    # 查看
    def curing_urgency_task_watch(self, name):
        self.curing_urgency_task_search(name)
        self.page_curing_urgency_task_watch_button()
        time.sleep(2)
