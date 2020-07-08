import page
import time
from base.base import Base


class PageCuringTeskSonManage(Base):
    """
        养护作业管理→养护职责管理→养护小组管理新增
    """

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    # 点击养护任务管理
    def page_curing_tesk_manage_click(self):
        self.base_click(page.curing_tesk_manage_click)

    # 点击养护任务子管理
    def page_curing_tesk_son_manage_click(self):
        self.base_click(page.curing_tesk_son_manage_click)

    # 输入名称
    def page_curing_tesk_son_manage_name_input(self, name):
        self.base_input(page.curing_tesk_son_manage_name_input, name)

    # 点击状态
    def page_curing_tesk_son_manage_status_click(self):
        self.base_click(page.curing_tesk_son_manage_status_click)

    # 选择状态(待执行)
    def page_curing_tesk_son_manage_status_select(self):
        self.base_click(page.curing_tesk_son_manage_status_select)

    # 点击查询
    def page_curing_tesk_son_manage_search_button(self):
        self.base_click(page.curing_tesk_son_manage_search_button)

    # 点击查看
    def page_curing_tesk_son_manage_watch_click(self):
        self.base_click(page.curing_tesk_son_manage_watch_click)

    # 点击工作内容
    def page_curing_tesk_son_manage_work_content_click(self):
        self.base_click(page.curing_tesk_son_manage_work_content_click)

    # 点击返回
    def page_curing_tesk_son_manage_return_click(self):
        self.base_click(page.curing_tesk_son_manage_return_click)

    # 点击编辑
    def page_curing_tesk_son_manage_edit_click(self):
        self.base_click(page.curing_tesk_son_manage_edit_click)

    # 输入养护任务名称
    def page_curing_tesk_son_manage_edit_name_input(self, taskname):
        self.base_input(page.curing_tesk_son_manage_edit_name_input, taskname)

    # 点击养护等级
    def page_curing_tesk_son_manage_edit_order_click(self):
        self.base_click(page.curing_tesk_son_manage_edit_order_click)

    # 选择养护等级
    def page_curing_tesk_son_manage_edit_order_select(self):
        self.base_click(page.curing_tesk_son_manage_edit_order_select)

    # 点击时间
    def page_curing_tesk_son_manage_edit_time_click(self):
        self.base_click(page.curing_tesk_son_manage_edit_time_click)

    # 选择前时间
    def page_curing_tesk_son_manage_edit_time_before(self):
        self.base_click(page.curing_tesk_son_manage_edit_time_before)

    # 选择后时间
    def page_curing_tesk_son_manage_edit_time_after(self):
        self.base_click(page.curing_tesk_son_manage_edit_time_after)

    # 输入执行内容
    def page_curing_tesk_son_manage_edit_excute_content(self, content):
        self.base_input(page.curing_tesk_son_manage_edit_excute_content, content)

    # 点击导出文档模板
    def page_curing_tesk_son_manage_edit_data_template_click(self):
        self.base_click(page.curing_tesk_son_manage_edit_data_template_click)

    # 选择导出文档模板
    def page_curing_tesk_son_manage_edit_data_template_select(self):
        self.base_click(page.curing_tesk_son_manage_edit_data_template_select)

    # 点击类型
    def page_curing_tesk_son_manage_edit_type_click(self):
        self.base_click(page.curing_tesk_son_manage_edit_type_click)

    # 选择类型
    def page_curing_tesk_son_manage_edit_type_select(self):
        self.base_click(page.curing_tesk_son_manage_edit_type_click)

    # 点击闸号
    def page_curing_tesk_son_manage_edit_num_click(self):
        self.base_click(page.curing_tesk_son_manage_edit_num_click)

    # 选择闸号
    def page_curing_tesk_son_manage_edit_num_select(self):
        self.base_click(page.curing_tesk_son_manage_edit_num_select)

    # 点击负责人icon
    def page_curing_tesk_son_manage_edit_pc_click(self):
        self.base_click(page.curing_tesk_son_manage_edit_pc_click)

    # 选择负责人radio
    def page_curing_tesk_son_manage_edit_pc_radio(self):
        self.base_click(page.curing_tesk_son_manage_edit_pc_radio)

    # 点击确定
    def page_curing_tesk_son_manage_edit_sure_clck(self):
        self.base_click(page.curing_tesk_son_manage_edit_sure_clck)

    # 输入备注
    def page_curing_tesk_son_manage_edit_remark(self, remark):
        self.base_input(page.curing_tesk_son_manage_edit_remark, remark)

    # 点击下一步
    def page_curing_tesk_son_manage_edit_next(self):
        self.base_click(page.curing_tesk_son_manage_edit_next)

    # 删除养护职责
    def page_curing_tesk_son_manage_edit_delete_duty(self):
        self.base_click(page.curing_tesk_son_manage_edit_delete_duty)

    # 点击添加职责icon
    def page_curing_tesk_son_manage_edit_insert_duty_icon_click(self):
        self.base_click(page.curing_tesk_son_manage_edit_insert_duty_icon_click)

    # 点击养护职责icon
    def page_curing_tesk_son_manage_edit_curing_duty_click(self):
        self.base_click(page.curing_tesk_son_manage_edit_curing_duty_click)

    # 选择养护职责radio
    def page_curing_tesk_son_manage_edit_curing_duty_select(self):
        self.base_click(page.curing_tesk_son_manage_edit_curing_duty_select)

    # 点击确定
    def page_curing_tesk_son_manage_edit_curing_duty_sure(self):
        self.base_click(page.curing_tesk_son_manage_edit_curing_duty_sure)

    # 输入工作内容名称
    def page_curing_tesk_son_manage_edit_work_content_name(self, cont_name):
        self.base_input(page.curing_tesk_son_manage_edit_work_content_name, cont_name)

    # 点击是否为养护小组
    def page_curing_tesk_son_manage_edit_is_team_click(self):
        self.base_click(page.curing_tesk_son_manage_edit_is_team_click)

    # 选择是否为养护小组
    def page_curing_tesk_son_manage_edit_is_team_select(self):
        self.base_click(page.curing_tesk_son_manage_edit_is_team_select)

    # 点击养护小组icon
    def page_curing_tesk_son_manage_edit_curing_team_icon(self):
        self.base_click(page.curing_tesk_son_manage_edit_curing_team_icon)

    # 选择养护小组radio
    def page_curing_tesk_son_manage_edit_curing_team_radio(self):
        self.base_click(page.curing_tesk_son_manage_edit_curing_team_radio)

    # 点击确定
    def page_curing_tesk_son_manage_edit_curing_team_sure_button(self):
        self.base_click(page.curing_tesk_son_manage_edit_curing_team_sure_button)

    # 点击完成
    def page_curing_tesk_son_manage_edit_curing_team_finish(self):
        self.base_click(page.curing_tesk_son_manage_edit_curing_team_finish)

    # 点击催办
    def page_curing_tesk_son_manage_us_click(self):
        self.base_click(page.curing_tesk_son_manage_us_click)

    # 点击确定
    def page_curing_tesk_son_manage_us_sure_click(self):
        self.base_click(page.curing_tesk_son_manage_us_sure_click)

    # 点击延时
    def page_curing_tesk_son_manage_delayed_click(self):
        self.base_click(page.curing_tesk_son_manage_delayed_click)

    # 输入延时天数
    def page_curing_tesk_son_manage_delayed_days_click(self, delayed_days):
        self.base_input(page.curing_tesk_son_manage_delayed_days_click, delayed_days)

    # 点击确定
    def page_curing_tesk_son_manage_delayed_sure_click(self):
        self.base_click(page.curing_tesk_son_manage_delayed_sure_click)

    """
        组装业务方法
    """

    # 点击养护任务管理
    def curing_tesk_son_manage_click(self):
        self.page_curing_work_manage_click()
        self.page_curing_tesk_manage_click()
        self.page_curing_tesk_son_manage_click()

    # 查询
    def curing_tesk_son_manage_search(self):
        self.page_curing_tesk_son_manage_status_click()
        self.page_curing_tesk_son_manage_status_select()
        self.page_curing_tesk_son_manage_search_button()
        time.sleep(2)

    # 养护任务编辑
    def curing_tesk_son_manage_edit(self, taskname, content, remark, cont_name):
        self.curing_tesk_son_manage_search()
        self.page_curing_tesk_son_manage_edit_click()
        self.page_curing_tesk_son_manage_edit_name_input(taskname)
        self.page_curing_tesk_son_manage_edit_order_click()
        self.page_curing_tesk_son_manage_edit_order_select()
        self.page_curing_tesk_son_manage_edit_time_click()
        self.page_curing_tesk_son_manage_edit_time_before()
        self.page_curing_tesk_son_manage_edit_time_after()
        self.page_curing_tesk_son_manage_edit_excute_content(content)
        self.page_curing_tesk_son_manage_edit_data_template_click()
        self.page_curing_tesk_son_manage_edit_data_template_select()
        self.page_curing_tesk_son_manage_edit_type_click()
        self.page_curing_tesk_son_manage_edit_type_select()
        self.page_curing_tesk_son_manage_edit_num_click()
        self.page_curing_tesk_son_manage_edit_num_select()
        self.page_curing_tesk_son_manage_edit_pc_click()
        self.page_curing_tesk_son_manage_edit_pc_radio()
        self.page_curing_tesk_son_manage_edit_sure_clck()
        self.page_curing_tesk_son_manage_edit_remark(remark)
        self.page_curing_tesk_son_manage_edit_next()
        self.page_curing_tesk_son_manage_edit_delete_duty()
        self.page_curing_tesk_son_manage_edit_insert_duty_icon_click()
        self.page_curing_tesk_son_manage_edit_curing_duty_click()
        self.page_curing_tesk_son_manage_edit_curing_duty_select()
        self.page_curing_tesk_son_manage_edit_curing_duty_sure()
        self.page_curing_tesk_son_manage_edit_work_content_name(cont_name)
        self.page_curing_tesk_son_manage_edit_is_team_click()
        self.page_curing_tesk_son_manage_edit_is_team_select()
        self.page_curing_tesk_son_manage_edit_curing_team_icon()
        self.page_curing_tesk_son_manage_edit_curing_team_radio()
        self.page_curing_tesk_son_manage_edit_curing_team_sure_button()
        self.page_curing_tesk_son_manage_edit_curing_team_finish()
        time.sleep(2)

    # 养护任务查看
    def curing_tesk_son_manage_watch(self):
        self.curing_tesk_son_manage_search()
        self.page_curing_tesk_son_manage_watch_click()
        self.page_curing_tesk_son_manage_work_content_click()
        self.page_curing_tesk_son_manage_return_click()
        time.sleep(2)

    # 养护任务催办
    def curing_tesk_son_manage_press(self):
        self.curing_tesk_son_manage_search()
        self.page_curing_tesk_son_manage_us_click()
        self.page_curing_tesk_son_manage_us_sure_click()
        time.sleep(2)

    # 养护任务延时
    def curing_tesk_son_manage_delayed(self,delayed_days):
        self.curing_tesk_son_manage_search()
        self.page_curing_tesk_son_manage_delayed_click()
        self.page_curing_tesk_son_manage_delayed_days_click(delayed_days)
        self.page_curing_tesk_son_manage_delayed_sure_click()
        time.sleep(2)