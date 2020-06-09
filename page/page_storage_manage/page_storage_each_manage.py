import page
import time
from base.base import Base


class PageStorageEachManage(Base):

    # 点击仓储管理
    def page_storage_manage_click(self):
        self.base_click(page.storage_manage_click)

    """
        盘库任务新增、执行到审批
    """

    # 点击盘库管理
    def page_storage_each_manage_click(self):
        self.base_click(page.storage_each_manage_click)

    # 点击盘库任务
    def page_storage_each_task_click(self):
        self.base_click(page.storage_each_task_click)

    # 点击新增
    def page_storage_each_task_insert_click(self):
        self.base_click(page.storage_each_task_insert_click)

    # 输入标题(public)
    def page_public_storage_each_task_insert_title_input(self):
        self.base_input(page.public_storage_each_task_insert_title_input, page.public_value)

    # 点击任务等级(public)
    def page_public_storage_each_task_insert_task_order_click(self):
        self.base_click(page.public_storage_each_task_insert_task_order_click)

    # 选择任务等级(public)
    def page_public_storage_each_task_insert_task_order_select(self):
        self.base_click(page.public_storage_each_task_insert_task_order_select)

    # 输入执行内容
    def page_storage_each_task_insert_excute_content_input(self):
        self.base_input(page.storage_each_task_insert_excute_content_input, page.public_value)

    # 点击选择时间
    def page_storage_each_task_insert_time_click(self):
        self.base_click(page.storage_each_task_insert_time_click)

    # 选择前时间
    def page_storage_each_task_insert_time_before_select(self):
        self.base_click(page.storage_each_task_insert_time_before_select)

    # 选择后时间
    def page_storage_each_task_insert_time_after_select(self):
        self.base_click(page.storage_each_task_insert_time_after_select)

    # 点击执行人icon
    def page_storage_each_task_insert_excute_persion_icon(self):
        self.base_click(page.storage_each_task_insert_excute_persion_icon)

    # 选择执行人radio
    def page_public_storage_each_task_insert_excute_persion_radio(self):
        self.base_click(page.public_storage_each_task_insert_excute_persion_radio)

    # 点击确定
    def page_public_storage_each_task_insert_excute_persion_sure_button(self):
        self.base_click(page.public_storage_each_task_insert_excute_persion_sure_button)

    # 点击其他执行人icon
    def page_storage_each_task_insert_other_excute_persion_icon(self):
        self.base_click(page.storage_each_task_insert_other_excute_persion_icon)

    # 选择其他执行人radio
    # 点击确定
    # 点击添加备件型号
    def page_storage_each_task_insert_component_type_click(self):
        self.base_click(page.storage_each_task_insert_component_type_click)

    # 点击添加备件型号icon
    def page_storage_each_task_insert_component_type_icon(self):
        self.base_click(page.storage_each_task_insert_component_type_icon)

    # 选择添加备件型号radio
    # 点击确定
    # 点击保存
    def page_storage_each_task_insert_save_button(self):
        self.base_click(page.storage_each_task_insert_save_button)

    # 输入标题
    # 点击状态
    def page_public_storage_each_task_status_click(self):
        self.base_click(page.public_storage_each_task_status_click)

    # 选择状态
    def page_public_storage_each_task_status_select(self):
        self.base_click(page.public_storage_each_task_status_select)

    # 点击任务等级
    # 选择任务等级
    def page_public_storage_each_task_search_order_select(self):
        self.base_click(page.public_storage_each_task_search_order_select)

    # 点击查询
    def page_public_storage_each_task_search_button(self):
        self.base_click(page.public_storage_each_task_search_button)

    # 点击执行
    def page_public_storage_each_task_excute_click(self):
        self.base_click(page.public_storage_each_task_excute_click)

    # 输入盘点数量
    def page_public_storage_each_task_check_num(self):
        self.base_input(page.public_storage_each_task_check_num, page.public_order_num)

    # 输入执行描述
    def page_public_storage_each_task_excute_input(self):
        self.base_input(page.public_storage_each_task_excute_input, page.public_value)

    # 输入备注
    def page_public_storage_each_task_remark_input(self):
        self.base_input(page.public_storage_each_task_remark_input, page.public_value)

    # 点击执行
    def page_public_storage_each_task_excute_button(self):
        self.base_click(page.public_storage_each_task_excute_button)

    # 点击待审批的库存修正单
    def page_wait_approval_inventory_correction_order(self):
        self.base_click(page.wait_approval_inventory_correction_order)

    # 输入名称
    def page_public_storage_each_task_name_input(self):
        self.base_input(page.public_storage_each_task_name_input, page.public_value)

    # 点击类型
    def page_public_storage_each_task_type_click(self):
        self.base_click(page.public_storage_each_task_type_click)

    # 选择类型
    def page_public_storage_each_task_type_select(self):
        self.base_click(page.public_storage_each_task_type_select)

    # 点击状态
    def page_public_storage_each_task_status1_click(self):
        self.base_click(page.public_storage_each_task_status1_click)

    # 选择状态
    def page_public_storage_each_task_status1_select(self):
        self.base_click_enter(page.public_storage_each_task_status1_click)

    # 点击查询
    # 点击审批
    def page_storage_each_task_approval_click(self):
        self.base_click(page.storage_each_task_approval_click)

    # 输入审批意见
    def page_public_storage_each_task_approval_device_input(self):
        self.base_input(page.public_storage_each_task_approval_device_input, page.public_value)

    # 点击通过
    def page_public_storage_each_task_approval_through_button(self):
        self.base_click(page.public_storage_each_task_approval_through_button)

    """
        组合业务方法
    """

    # 盘库任务新增
    def storage_each_task_insert(self):
        self.page_storage_manage_click()
        self.page_storage_each_manage_click()
        self.page_storage_each_task_click()
        self.page_storage_each_task_insert_click()
        self.page_public_storage_each_task_insert_title_input()
        self.page_public_storage_each_task_insert_task_order_click()
        self.page_public_storage_each_task_insert_task_order_select()
        self.page_storage_each_task_insert_excute_content_input()
        self.page_storage_each_task_insert_time_click()
        self.page_storage_each_task_insert_time_before_select()
        self.page_storage_each_task_insert_time_after_select()
        self.page_storage_each_task_insert_excute_persion_icon()
        self.page_public_storage_each_task_insert_excute_persion_radio()
        self.page_public_storage_each_task_insert_excute_persion_sure_button()
        self.page_storage_each_task_insert_other_excute_persion_icon()
        self.page_public_storage_each_task_insert_excute_persion_radio()
        self.page_public_storage_each_task_insert_excute_persion_sure_button()
        self.page_storage_each_task_insert_component_type_click()
        self.page_storage_each_task_insert_component_type_icon()
        self.page_public_storage_each_task_insert_excute_persion_radio()
        self.page_public_storage_each_task_insert_excute_persion_sure_button()
        self.page_storage_each_task_insert_save_button()
        time.sleep(2)

    # 盘库任务查询
    def storage_each_task_search(self):
        self.page_public_storage_each_task_insert_title_input()
        self.page_public_storage_each_task_status_click()
        self.page_public_storage_each_task_status_select()
        self.page_public_storage_each_task_insert_task_order_click()
        self.page_public_storage_each_task_search_order_select()
        self.page_public_storage_each_task_search_button()
        time.sleep(2)

    # 盘库任务执行
    def storage_each_task_excute(self):
        self.storage_each_task_search()
        self.page_public_storage_each_task_excute_click()
        self.page_public_storage_each_task_check_num()
        self.page_public_storage_each_task_excute_input()
        self.page_public_storage_each_task_remark_input()
        self.page_public_storage_each_task_excute_button()
        time.sleep(2)

    # 待审批的库存修正单查询
    def wait_approval_inventory_correction_order_search(self):
        self.page_wait_approval_inventory_correction_order()
        self.page_public_storage_each_task_name_input()
        self.page_public_storage_each_task_type_click()
        self.page_public_storage_each_task_type_select()
        self.page_public_storage_each_task_status1_click()
        self.page_public_storage_each_task_status1_select()
        self.page_public_storage_each_task_search_button()
        time.sleep(2)

    # 盘库任务审批
    def storage_each_task_approval(self):
        self.storage_each_task_insert()
        self.storage_each_task_excute()
        self.wait_approval_inventory_correction_order_search()
        self.page_storage_each_task_approval_click()
        self.page_public_storage_each_task_approval_device_input()
        self.page_public_storage_each_task_approval_through_button()
        time.sleep(2)
