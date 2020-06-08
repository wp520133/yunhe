import page
import time
from base.base import Base


class PageOutManage(Base):
    """
        出库管理→报废单管理→我的报废单新增
    """

    # 点击仓储管理
    def page_storage_manage_click(self):
        self.base_click(page.storage_manage_click)

    # 点击出库管理
    def page_out_manage_click(self):
        self.base_click(page.out_manage_click)

    # 点击报废单管理
    def page_scrap_bill_manage_click(self):
        self.base_click(page.scrap_bill_manage_click)

    # 点击我的报废单
    def page_mind_scrap_bill_click(self):
        self.base_click(page.mind_scrap_bill_click)

    # 点击新增
    def page_public_scrap_bill_insert_click(self):
        self.base_click(page.public_scrap_bill_insert_click)

    # 输入报废单名称
    def page_public_scrap_bill_insert_name_input(self):
        self.base_input(page.public_scrap_bill_name_input, page.public_value)

    # 点击类型
    def page_public_scrap_bill_type_click(self):
        self.base_click(page.public_scrap_bill_type_click)

    # 选择类型
    def page_public_scrap_bill_type_select(self):
        self.base_click(page.public_scrap_bill_type_select)

    # 输入申请理由
    def page_public_scrap_bill_insert_excute_input(self, ):
        self.base_input(page.public_scrap_bill_excute_input, page.public_value)

    # 点击添加备件清单
    def page_public_scrap_bill_insert_part_bill_click(self):
        self.base_click(page.public_scrap_bill_insert_part_bill_click)

    # 点击选择备件型号icon
    def page_public_scrap_bill_insert_part_bill_icon(self):
        self.base_click(page.public_scrap_bill_insert_part_bill_icon)

    # 点击选择备件型号radio
    def page_public_scrap_bill_insert_part_bill_radio(self):
        self.base_click(page.public_scrap_bill_insert_part_bill_radio)

    # 点击确定
    def page_public_scrap_bill_insert_sure_button(self):
        self.base_click(page.public_scrap_bill_insert_sure_button)

    # 输入备件数量
    def page_public_scrap_bill_insert_num_input(self):
        self.base_input(page.public_scrap_bill_insert_repair_num_input, page.public_order_num)

    # 点击保存
    def page_public_scrap_bill_insert_save_button(self):
        self.base_click(page.public_scrap_bill_insert_save_button)

    # 点击待审批报废单
    def page_public_wait_approval_scrap_bill_click(self):
        self.base_click(page.wait_approval_scrap_bill_click)

    # 输入报废单名称
    # 点击状态
    def page_public_scrap_bill_status_click(self):
        self.base_click(page.public_scrap_bill_status_click)

    # 选择状态
    def page_public_scrap_bill_status_select(self):
        self.base_click(page.public_scrap_bill_status_select)

    # 点击查询
    def page_public_scrap_bill_search_button(self):
        self.base_click(page.public_scrap_bill_search_button)

    # 点击审批
    def page_public_scrap_bill_approval_button(self):
        self.base_click(page.public_scrap_bill_approval_click)

    # 输入审批意见
    def page_public_scrap_bill_approval_device_input(self):
        self.base_input(page.public_scrap_bill_approval_device_input, page.public_value)

    # 点击通过
    def page_public_scrap_bill_approval_through_button(self):
        self.base_click(page.public_scrap_bill_approval_through_button)

    # 点击待执行的出库单
    def page_wait_excute_out_bill_click(self):
        self.base_click(page.wait_excute_out_bill_click)

    # 输入出库单名称(报废单名称)
    # 点击状态
    # 选择状态
    # 点击类型
    def page_wait_excute_out_bill_type_click(self):
        self.base_click(page.wait_excute_out_bill_type_click)

    # 选择类型(报废出库)
    def page_wait_excute_out_bill_select_nth2(self):
        self.base_click(page.wait_excute_out_bill_select_nth2)

    # 点击查询
    # 点击出库
    def page_wait_excute_out_bill_out_click(self):
        self.base_click(page.wait_excute_out_bill_out_click)
    # 点击执行
    def page_wait_excute_out_bill_out_excute_click(self):
        self.base_click(page.wait_excute_out_bill_out_excute_click)

    """
        我的报废单新增→待审批报废单审批→待执行的出库单出库
    """
    # 我的报废单新增
    def mind_scrap_bill_insert(self):
        self.page_storage_manage_click()
        self.page_out_manage_click()
        self.page_scrap_bill_manage_click()
        self.page_mind_scrap_bill_click()
        self.page_public_scrap_bill_insert_click()
        self.page_public_scrap_bill_insert_name_input()
        self.page_public_scrap_bill_type_click()
        self.page_public_scrap_bill_type_select()
        self.page_public_scrap_bill_insert_excute_input()
        self.page_public_scrap_bill_insert_part_bill_click()
        self.page_public_scrap_bill_insert_part_bill_icon()
        self.page_public_scrap_bill_insert_part_bill_radio()
        self.page_public_scrap_bill_insert_sure_button()
        self.page_public_scrap_bill_insert_num_input()
        self.page_public_scrap_bill_insert_save_button()
        time.sleep(2)

    # 待审批报废单查询
    def wait_approval_scrap_bill_search(self):
        self.page_public_wait_approval_scrap_bill_click()
        self.page_public_scrap_bill_insert_name_input()
        self.page_public_scrap_bill_status_click()
        self.page_public_scrap_bill_status_select()
        self.page_public_scrap_bill_search_button()
        time.sleep(2)

    # 待审批报废单审批
    def wait_approval_scrap_bill_approval(self):
        self.wait_approval_scrap_bill_search()
        self.page_public_scrap_bill_approval_button()
        self.page_public_scrap_bill_approval_device_input()
        self.page_public_scrap_bill_approval_through_button()
        time.sleep(2)

    # 待执行的出库单出库
    def wait_excute_scrap_bill_out(self):
        self.mind_scrap_bill_insert()
        self.wait_approval_scrap_bill_approval()
        self.page_wait_excute_out_bill_click()
        self.page_public_scrap_bill_insert_name_input()
        self.page_public_scrap_bill_status_click()
        self.page_public_scrap_bill_status_select()
        self.page_wait_excute_out_bill_type_click()
        self.page_wait_excute_out_bill_select_nth2()
        self.page_public_scrap_bill_search_button()
        self.page_wait_excute_out_bill_out_click()
        self.page_wait_excute_out_bill_out_excute_click()
        time.sleep(2)