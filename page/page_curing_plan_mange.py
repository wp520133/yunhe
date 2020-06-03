import page
import time
from base.base import Base


class PageCuringPlanManage(Base):
    """
        养护作业管理→养护计划管理
    """

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    """
        养护计划管理新增
    """

    # 点击养护计划管理
    def page_curing_plan_manage_click(self):
        self.base_click(page.curing_plan_manage_insert_click)

    # 点击新增
    def page_curing_plan_manage_insert_click(self):
        self.base_click(page.public_insert_button)

    # 输入养护计划名称
    def page_curing_plan_manage_plan_name_input(self):
        self.base_input(page.public_plan_name_input, page.public_value)

    # 点击执行等级
    def page_curing_plan_manage_insert_excute_order_click(self):
        self.base_click(page.curing_plan_manage_insert_excute_order_click)

    # 选择执行等级
    def page_curing_plan_manage_insert_excute_order_select(self):
        self.base_click(page.curing_plan_manage_insert_excute_order_select)

    # 点击选择时间
    def page_curing_plan_manage_insert_time_click(self):
        self.base_click(page.curing_plan_manage_insert_time_click)

    # 选择前半部分时间
    def page_curing_plan_manage_insert_time_befor_select(self):
        self.base_click(page.curing_plan_manage_insert_time_befor_select)

    # 选择后半部分时间
    def page_curing_plan_manage_insert_time_after_select(self):
        self.base_click(page.curing_plan_manage_insert_time_after_select)

    # 点击下次生成时间
    def page_curing_plan_manage_insert_next_create_time_click(self):
        self.base_click(page.curing_plan_manage_insert_next_create_time_click)

    # 选择下次生成时间
    def page_curing_plan_manage_insert_next_create_time_select(self):
        self.base_click(page.curing_plan_manage_insert_next_create_time_select)

    # 点击是否自动审核(否)
    def page_curing_plan_manage_insert_if_auto_audit_click(self):
        self.base_click(page.curing_plan_manage_insert_if_auto_audit_click)

    # 输入保养周期
    def page_curing_plan_manage_insert_cycle_input(self):
        self.base_input(page.public_cycle_input, page.public_order_num)

    # 点击保养周期单位
    def page_curing_plan_manage_insert_if_service_cycle_unit_click(self):
        self.base_click(page.curing_plan_manage_insert_if_service_cycle_unit_click)

    # 选择保养周期单位
    def page_curing_plan_manage_insert_if_service_cycle_unit_select(self):
        self.base_click(page.curing_plan_manage_insert_if_service_cycle_unit_select)

    # 输入执行内容
    def page_curing_plan_manage_insert_content_input(self):
        self.base_input(page.public_content_input, page.public_value)

    # 输入备注
    def page_curing_plan_manage_insert_remark_input(self):
        self.base_input(page.public_remark_input, page.public_value)

    # 点击下一步
    def page_curing_plan_manage_insert_next_click(self):
        self.base_click(page.curing_plan_manage_insert_next_click)

    # 点击添加一条职责
    def page_curing_plan_manage_insert_one_duty_click(self):
        self.base_click(page.curing_plan_manage_insert_one_duty_click)

    # 点击养护职责icon
    def page_curing_plan_manage_insert_curing_duty_icon_click(self):
        self.base_click(page.curing_plan_manage_insert_curing_duty_icon_click)

    # 选择养护职责radio
    def page_curing_plan_manage_insert_curing_duty_redio_select(self):
        self.base_click(page.public_radio)

    # 点击确定
    def page_curing_plan_manage_insert_sure_button(self):
        self.base_click(page.public_sure_button)

    # 输入工作内容名称
    def page_curing_plan_manage_insert_work_content_name(self):
        self.base_input(page.curing_plan_manage_insert_work_content_name_input, page.public_value)

    # 点击养护小组/养护人
    def page_curing_plan_manage_insert_curing_team_click(self):
        self.base_click(page.curing_plan_manage_insert_curing_team_click)

    # 选择养护小组/养护人
    def page_curing_plan_manage_insert_curing_team_select(self):
        self.base_click(page.curing_plan_manage_insert_curing_team_select)

    # 点击选择人员icon
    def page_curing_plan_manage_insert_member_icon_click(self):
        self.base_click(page.curing_plan_manage_insert_member_icon_click)

    # 选择人员radio
    def page_curing_plan_manage_insert_member_radio_click(self):
        self.base_click(page.public_radio)

    # 点击确认
    def page_curing_plan_manage_insert_member_sure_button(self):
        self.base_click(page.public_sure_button)

    # 点击完成
    def page_curing_plan_manage_insert_member_finish_button(self):
        self.base_click(page.curing_plan_manage_insert_finish_click)

    """
        养护计划管理查询
    """

    # 输入计划名称
    def page_curing_plan_manage_search_plan_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 点击状态
    def page_curing_plan_manage_search_status_click(self):
        self.base_click(page.public_status_click)

    # 选择状态
    def page_curing_plan_manage_search_status_select(self):
        self.base_click(page.public_status_select)

    # 点击查询
    def page_curing_plan_manage_search_button(self):
        self.base_click(page.public_search_button)

    """
        养护计划管理重置
    """

    # 点击重置
    def page_curing_plan_manage_reset_button(self):
        self.base_click(page.public_reset_button)

    """
        养护计划管理查看
    """

    # 点击查看
    def page_curing_plan_manage_watch_button(self):
        self.base_click(page.public_one_row_button)

    # 回退
    def page_curing_plan_manage_back(self):
        self.base_back()

    """
        养护计划管理编辑
    """

    # 点击编辑
    def page_curing_plan_manage_edit_button(self):
        self.base_click(page.public_two_row_button)

    """
        养护计划禁用
    """

    # 点击禁用与启用
    def page_curing_plan_manage_disable_button(self):
        self.base_click(page.public_four_row_button)

    """
        养护计划延时
    """

    # 点击延时
    def page_curing_plan_manage_delay_button(self):
        self.base_click(page.public_five_row_button)

    # 输入延时天数
    def page_curing_plan_manage_delay_day_input(self):
        self.base_input(page.public_delay_day_input, page.public_order_num)

    # 点击确定
    def page_curing_plan_manage_sure_button(self):
        self.base_click(page.public_sure_button)

    """
        组装业务方法
    """

    # 新增
    def curing_plan_manage_insert(self):
        self.page_curing_work_manage_click()
        self.page_curing_plan_manage_click()
        self.page_curing_plan_manage_insert_click()
        self.page_curing_plan_manage_plan_name_input()
        self.page_curing_plan_manage_insert_excute_order_click()
        self.page_curing_plan_manage_insert_excute_order_select()
        self.page_curing_plan_manage_insert_time_click()
        self.page_curing_plan_manage_insert_time_befor_select()
        self.page_curing_plan_manage_insert_time_after_select()
        self.page_curing_plan_manage_insert_next_create_time_click()
        self.page_curing_plan_manage_insert_next_create_time_select()
        self.page_curing_plan_manage_insert_if_auto_audit_click()
        self.page_curing_plan_manage_insert_cycle_input()
        self.page_curing_plan_manage_insert_if_service_cycle_unit_click()
        self.page_curing_plan_manage_insert_if_service_cycle_unit_select()
        self.page_curing_plan_manage_insert_content_input()
        self.page_curing_plan_manage_insert_remark_input()
        self.page_curing_plan_manage_insert_next_click()
        self.page_curing_plan_manage_insert_one_duty_click()
        self.page_curing_plan_manage_insert_curing_duty_icon_click()
        self.page_curing_plan_manage_insert_curing_duty_redio_select()
        self.page_curing_plan_manage_insert_sure_button()
        self.page_curing_plan_manage_insert_work_content_name()
        self.page_curing_plan_manage_insert_curing_team_click()
        self.page_curing_plan_manage_insert_curing_team_select()
        self.page_curing_plan_manage_insert_member_icon_click()
        self.page_curing_plan_manage_insert_member_radio_click()
        self.page_curing_plan_manage_insert_member_sure_button()
        self.page_curing_plan_manage_insert_member_finish_button()
        time.sleep(2)

    # 查询
    def curing_plan_manage_search(self):
        self.page_curing_plan_manage_search_plan_name_input()
        self.page_curing_plan_manage_search_status_click()
        self.page_curing_plan_manage_search_status_select()
        self.page_curing_plan_manage_search_button()
        time.sleep(2)

    # 编辑
    def curing_plan_manage_edit(self):
        self.curing_plan_manage_insert()
        self.curing_plan_manage_search()
        self.page_curing_plan_manage_edit_button()
        # 待续....

    # 重置
    def curing_plan_manage_reset(self):
        self.curing_plan_manage_search()
        self.page_curing_plan_manage_reset_button()
        time.sleep(2)

    # 查看
    def curing_plan_manage_watch(self):
        self.curing_plan_manage_search()
        self.page_curing_plan_manage_watch_button()
        self.page_curing_plan_manage_back()
        time.sleep(2)

    # 禁用
    def curing_plan_manage_disable(self):
        self.curing_plan_manage_search()
        self.page_curing_plan_manage_disable_button()
        time.sleep(2)

    # 延时
    def curing_plan_manage_delay(self):
        self.curing_plan_manage_search()
        self.page_curing_plan_manage_delay_button()
        self.page_curing_plan_manage_delay_day_input()
        self.page_curing_plan_manage_sure_button()
        time.sleep(2)
