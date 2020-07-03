import page
import time
from base.base import Base


class PageCuringPlanManage(Base):

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    """
        养护计划管理
    """

    # 点击养护计划管理
    def page_curing_plan_manage_click(self):
        self.base_click(page.curing_plan_manage_click)

    # 点击新增
    def page_curing_plan_manage_insert_click(self):
        self.base_click(page.curing_plan_manage_insert_click)

    # 点击导出文档模板
    def page_curing_plan_manage_insert_export_click(self):
        self.base_click_enter(page.curing_plan_manage_insert_export_click)

    # 选择导出文档模板
    def page_curing_plan_manage_insert_export_select(self):
        self.base_click_enter(page.curing_plan_manage_insert_export_click)

    # 输入养护计划名称
    def page_curing_plan_manage_insert_plan_name(self, plan_name):
        self.base_input(page.curing_plan_manage_insert_plan_name, plan_name)

    def page_curing_plan_manage_insert_plan_name_search(self, name):
        self.base_input(page.curing_plan_manage_insert_plan_name_search, name)

    # 点击执行等级
    def page_curing_plan_manage_insert_excute_order_click(self):
        self.base_click(page.curing_plan_manage_insert_excute_order_click)

    # 选择执行等级
    def page_curing_plan_manage_insert_excute_order_select(self):
        self.base_click_enter(page.curing_plan_manage_insert_excute_order_click)

    # 点击有效时间范围
    def page_curing_plan_manage_insert_time_click(self):
        self.base_click_enter(page.curing_plan_manage_insert_time_click)

    # 点击前半部时间
    def page_curing_plan_manage_insert_time_befor_select(self):
        self.base_click(page.curing_plan_manage_insert_time_befor_select)

    # 点击后半部时间
    def page_curing_plan_manage_insert_time_after_select(self):
        self.base_click(page.curing_plan_manage_insert_time_after_select)

    # 点击下次生成时间
    def page_curing_plan_manage_insert_next_create_time_click(self):
        self.base_click_enter(page.curing_plan_manage_insert_next_create_time_click)

    # 选择生成时间
    def page_curing_plan_manage_insert_next_create_time_select(self):
        self.base_click(page.curing_plan_manage_insert_next_create_time_select)

    # 点击是否自动审核:是
    def page_curing_plan_manage_insert_if_auto_audit_click(self):
        self.base_click(page.curing_plan_manage_insert_if_auto_audit_click)

    # 点击闸号
    def page_curing_plan_manage_insert_get_no_click(self):
        self.base_click(page.curing_plan_manage_insert_get_no_click)

    # 选择闸号
    def page_curing_plan_manage_insert_get_no_select(self):
        self.base_click_enter(page.curing_plan_manage_insert_get_no_click)

    # 点击负责人icon
    def page_curing_plan_manage_insert_principal_click(self):
        self.base_click(page.curing_plan_manage_insert_principal_click)

    # 选择负责人radio
    def page_curing_plan_manage_insert_principal_radio(self):
        self.base_click(page.curing_plan_manage_insert_principal_radio)

    # 点击确定
    def page_curing_plan_manage_insert_principal_sure(self):
        self.base_click(page.curing_plan_manage_insert_principal_sure)

    # 输入执行内容
    def page_curing_plan_manage_insert_excute_content(self, content):
        self.base_input(page.public_content_input, content)

    # 输入备注
    def page_uring_plan_manage_insert_remark(self, remark):
        self.base_input(page.public_remark_input, remark)

    # 点击下一步
    def page_curing_plan_manage_insert_next_click(self):
        self.base_click(page.curing_plan_manage_insert_next_click)

    def page_curing_plan_manage_delete_duty_icon(self):
        self.base_click(page.curing_plan_manage_delete_duty_icon)

    # 点击返回
    def page_curing_plan_manage_insert_return_click(self):
        self.base_click(page.public_return_click)

    # 添加一条职责
    def page_curing_plan_manage_insert_one_duty_click(self):
        self.base_click(page.curing_plan_manage_insert_one_duty_click)

    # 点击养护职责icon
    def page_curing_plan_manage_insert_curing_duty_icon_click(self):
        self.base_click(page.curing_plan_manage_insert_curing_duty_icon_click)

    # 选择养护职责radio
    def page_curing_plan_manage_insert_curing_duty_radio(self):
        self.base_click(page.public_radio)

    # 养护职责确定
    def page_curing_plan_manage_insert_curing_duty_sure(self):
        self.base_click(page.public_sure_button)

    # 点击是否为养护小组
    def page_curing_plan_manage_insert_curing_team_click(self):
        self.base_click(page.curing_plan_manage_insert_curing_team_click)

    # 选择是否为养护小组
    def page_curing_plan_manage_insert_curing_team_select(self):
        self.base_click_enter(page.curing_plan_manage_insert_curing_team_click)

    # 点击养护小组icon
    def page_curing_plan_manage_insert_curing_team_icon(self):
        self.base_click(page.curing_plan_manage_insert_member_icon_click)

    # 点击养护小组raido
    def page_curing_plan_manage_insert_curing_team_radio(self):
        self.base_click(page.public_radio)

    # 点击确定
    def page_curing_plan_manage_insert_curing_team_sure(self):
        self.base_click(page.public_sure_button)

    # 点击完成
    def page_curing_plan_manage_insert_finish_click(self):
        self.base_click(page.curing_plan_manage_insert_finish_click)

    # 输入计划名称
    # 点击状态
    def page_curing_plan_manage_search_type_click(self):
        self.base_click(page.curing_plan_manage_search_type_click)

    # 选择状态(开启)
    def page_curing_plan_manage_search_type_select(self):
        self.base_click(page.curing_plan_manage_search_type_select)

    # 选择禁用
    def page_curing_plan_manage_search_type_select2(self):
        self.base_click(page.curing_plan_manage_search_type_select2)

    # 查询
    def page_curing_plan_manage_search_button(self):
        self.base_click(page.public_search_button)

    # 编辑
    def page_curing_plan_manage_edit_button(self):
        self.base_click(page.curing_plan_manage_edit_click)

    # 查看
    def page_curing_plan_manage_watch_click(self):
        self.base_click(page.curing_plan_manage_watch_click)

    # 点击养护记录详情
    def page_curing_plan_manage_details(self):
        self.base_click(page.curing_plan_manage_details)

    # 点击返回
    def page_curing_plan_manage_return_click(self):
        self.base_click(page.public_return_click)

    # 点击禁用
    # 点击延时
    def page_curing_plan_manage_delay(self):
        self.base_click(page.curing_plan_manage_delay)

    # 输入延迟时间
    def page_curing_plan_manage_delay_day(self, delay_day):
        self.base_input(page.curing_plan_manage_delay_day, delay_day)

    # 点击确定
    def page_curing_plan_manage_delay_sure_button(self):
        self.base_click(page.curing_plan_manage_delay_sure_button)

    """
        组合方法
    """

    def curing_plan_manage_click(self):
        self.page_curing_work_manage_click()
        self.page_curing_plan_manage_click()
        time.sleep(2)

    # 新增异常数据
    def curing_plan_manage_except_insert(self, plan_name, content, remark):
        self.page_curing_plan_manage_insert_click()
        self.page_curing_plan_manage_insert_export_click()
        self.page_curing_plan_manage_insert_export_select()
        self.page_curing_plan_manage_insert_plan_name(plan_name)
        self.page_curing_plan_manage_insert_excute_order_click()
        self.page_curing_plan_manage_insert_excute_order_select()
        self.page_curing_plan_manage_insert_time_click()
        self.page_curing_plan_manage_insert_time_befor_select()
        self.page_curing_plan_manage_insert_time_after_select()
        self.page_curing_plan_manage_insert_next_create_time_click()
        self.page_curing_plan_manage_insert_next_create_time_select()
        self.page_curing_plan_manage_insert_if_auto_audit_click()
        self.page_curing_plan_manage_insert_get_no_click()
        self.page_curing_plan_manage_insert_get_no_select()
        # self.page_curing_plan_manage_insert_principal_click()
        # self.page_curing_plan_manage_insert_principal_radio()
        # self.page_curing_plan_manage_insert_principal_sure()
        self.page_curing_plan_manage_insert_excute_content(content)
        self.page_uring_plan_manage_insert_remark(remark)
        self.page_curing_plan_manage_insert_next_click()

    # 新增
    def curing_plan_manage_insert(self, plan_name, content, remark):
        self.page_curing_plan_manage_insert_click()
        self.page_curing_plan_manage_insert_export_click()
        self.page_curing_plan_manage_insert_export_select()
        self.page_curing_plan_manage_insert_plan_name(plan_name)
        self.page_curing_plan_manage_insert_excute_order_click()
        self.page_curing_plan_manage_insert_excute_order_select()
        self.page_curing_plan_manage_insert_time_click()
        self.page_curing_plan_manage_insert_time_befor_select()
        self.page_curing_plan_manage_insert_time_after_select()
        self.page_curing_plan_manage_insert_next_create_time_click()
        self.page_curing_plan_manage_insert_next_create_time_select()
        self.page_curing_plan_manage_insert_if_auto_audit_click()
        self.page_curing_plan_manage_insert_get_no_click()
        self.page_curing_plan_manage_insert_get_no_select()
        # self.page_curing_plan_manage_insert_principal_click()
        # self.page_curing_plan_manage_insert_principal_radio()
        # self.page_curing_plan_manage_insert_principal_sure()
        self.page_curing_plan_manage_insert_excute_content(content)
        self.page_uring_plan_manage_insert_remark(remark)
        self.page_curing_plan_manage_insert_next_click()
        self.page_curing_plan_manage_insert_one_duty_click()
        self.page_curing_plan_manage_insert_curing_duty_icon_click()
        self.page_curing_plan_manage_insert_curing_duty_radio()
        self.page_curing_plan_manage_insert_curing_duty_sure()
        self.page_curing_plan_manage_insert_curing_team_click()
        self.page_curing_plan_manage_insert_curing_team_select()
        self.page_curing_plan_manage_insert_curing_team_icon()
        self.page_curing_plan_manage_insert_curing_team_radio()
        self.page_curing_plan_manage_insert_curing_team_sure()
        self.page_curing_plan_manage_insert_finish_click()
        time.sleep(2)

    # 查询
    def curing_plan_manage_search(self, name):
        self.page_curing_plan_manage_insert_plan_name_search(name)
        self.page_curing_plan_manage_search_type_click()
        self.page_curing_plan_manage_search_type_select()
        self.page_curing_plan_manage_search_button()
        time.sleep(2)

    # 编辑
    def curing_plan_manage_edit(self, plan_name, content, remark, name):
        self.curing_plan_manage_insert(plan_name, content, remark)
        self.curing_plan_manage_search(name)
        self.page_curing_plan_manage_edit_button()
        self.page_curing_plan_manage_insert_export_click()
        self.page_curing_plan_manage_insert_export_select()
        self.page_curing_plan_manage_insert_plan_name(plan_name)
        self.page_curing_plan_manage_insert_excute_order_click()
        self.page_curing_plan_manage_insert_excute_order_select()
        self.page_curing_plan_manage_insert_time_click()
        self.page_curing_plan_manage_insert_time_befor_select()
        self.page_curing_plan_manage_insert_time_after_select()
        self.page_curing_plan_manage_insert_next_create_time_click()
        self.page_curing_plan_manage_insert_next_create_time_select()
        self.page_curing_plan_manage_insert_if_auto_audit_click()
        self.page_curing_plan_manage_insert_get_no_click()
        self.page_curing_plan_manage_insert_get_no_select()
        # self.page_curing_plan_manage_insert_principal_click()
        # self.page_curing_plan_manage_insert_principal_radio()
        # self.page_curing_plan_manage_insert_principal_sure()
        self.page_curing_plan_manage_insert_excute_content(content)
        self.page_uring_plan_manage_insert_remark(remark)
        self.page_curing_plan_manage_insert_next_click()
        self.page_curing_plan_manage_delete_duty_icon()
        self.page_curing_plan_manage_insert_one_duty_click()
        self.page_curing_plan_manage_insert_curing_duty_icon_click()
        self.page_curing_plan_manage_insert_curing_duty_radio()
        self.page_curing_plan_manage_insert_curing_duty_sure()
        self.page_curing_plan_manage_insert_curing_team_click()
        self.page_curing_plan_manage_insert_curing_team_select()
        self.page_curing_plan_manage_insert_curing_team_icon()
        self.page_curing_plan_manage_insert_curing_team_radio()
        self.page_curing_plan_manage_insert_curing_team_sure()
        self.page_curing_plan_manage_insert_finish_click()
        time.sleep(2)

    # 查看
    def curing_plan_manage_watch(self, name):
        self.page_curing_plan_manage_insert_plan_name_search(name)
        self.page_curing_plan_manage_search_type_click()
        self.page_curing_plan_manage_search_type_select()
        self.page_curing_plan_manage_search_button()
        self.page_curing_plan_manage_watch_click()
        self.page_curing_plan_manage_details()
        self.page_curing_plan_manage_return_click()
        time.sleep(2)

    # 禁用
    def curing_plan_manage_disable(self, name):
        self.page_curing_plan_manage_insert_plan_name_search(name)
        self.page_curing_plan_manage_search_type_click()
        self.page_curing_plan_manage_search_type_select()
        self.page_curing_plan_manage_search_button()
        self.base_click(page.public_disable_click)
        time.sleep(2)

    # 延迟
    def curing_plan_manage_delay(self, name, delay_day):
        self.page_curing_plan_manage_insert_plan_name_search(name)
        self.page_curing_plan_manage_search_type_click()
        self.page_curing_plan_manage_search_type_select2()
        self.page_curing_plan_manage_search_button()
        self.page_curing_plan_manage_delay()
        self.page_curing_plan_manage_delay_day(delay_day)
        self.page_curing_plan_manage_delay_sure_button()
        time.sleep(2)
