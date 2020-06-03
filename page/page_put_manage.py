import page
import time
from base.base import Base


class PagePutManage(Base):
    """
        我的入库单新增
    """

    # 点击仓储管理
    def page_storage_manage_click(self):
        self.base_click(page.storage_manage_click)

    # 点击入库管理
    def page_put_manage_click(self):
        self.base_click(page.put_manage_click)

    # 点击我的入库单
    def page_mine_put_bill_click(self):
        self.base_click(page.mine_put_bill_click)

    # 点击新增
    def page_mine_put_bill_insert_click(self):
        self.base_click(page.public_insert_button)

    # 输入入库单名称
    def page_mine_put_bill_insert_put_part_name(self):
        self.base_input(page.public_name_input, page.public_value)

    # 点击类型
    def page_mine_put_bill_type_click(self):
        self.base_click(page.mine_put_bill_type_click)

    # 选择类型
    def page_mine_put_bill_type_select(self):
        self.base_click(page.mine_put_bill_type_select)

    # 输入申请理由
    def page_mine_put_bill_inser_apply_reason_input(self):
        self.base_input(page.public_applyReason_input, page.public_value)

    # 点击添加备件清单
    def page_mine_put_bill_insert_part_bill(self):
        self.base_click(page.mine_put_bill_insert_part_bill)

    # 点击选择备件型号icon
    def page_mine_put_bill_insert_part_bill_icon(self):
        self.base_click(page.mine_put_bill_insert_part_bill_icon)

    # 选择备件型号radio
    def page_mine_put_bill_insert_part_bill_radio(self):
        self.base_click(page.public_radio)

    # 点击确定
    def page_mine_put_bill_insert_sure_button(self):
        self.base_click(page.mine_put_bill_insert_part_bill_sure_button)

    # 输入备件数量
    def page_mine_put_bill_insert_part_num_input(self):
        self.base_input(page.public_part_num_input, page.public_order_num)

    # 输入采购单价
    def page_mine_put_bill_insert_part_price_input(self):
        self.base_input(page.public_part_price_input, page.public_order_num)

    # 输入采购单位
    def page_mine_put_bill_insert_part_unit_input(self):
        self.base_input(page.public_part_unit_input, page.public_value_num2)

    # 点击保存
    def page_mine_put_bill_insert_save_button(self):
        self.base_click(page.public_insert_save_button)

    # 点击待审批入库单
    def page_wait_approval_put_bill_click(self):
        self.base_click(page.wait_approval_put_bill_click)

    # 输入待审批入库单-名称
    def page_wait_approval_put_bill_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 输入待审批入库单-点击状态
    def page_wait_approval_put_bill_type_click(self):
        self.base_click(page.wait_approval_put_bill_type_click)

    # 输入待审批入库单-选择状态
    def page_wait_approval_put_bill_type_select(self):
        self.base_click(page.wait_approval_put_bill_type_select)

    # 点击查询
    def page_wait_approval_put_bill_search_button(self):
        self.base_click(page.public_search_button)

    # 点击审批
    def page_wait_approval_put_bill_approval_button(self):
        self.base_click(page.public_one_row_button)

    # 输入审批意见
    def page_wait_approval_device_input(self):
        self.base_click(page.public_apprival_device_input)

    # 点击通过
    def page_wait_approval_device_through(self):
        self.base_click(page.public_apprival_through_button)

    # 点击待执行入库单
    def page_wait_excute_bill_click(self):
        self.base_click(page.wait_excute_put_bill_click)

    # 输入待执行入库单-名称
    def page_wait_excute_bill_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 点击待执行入库单-状态
    def page_wait_excute_put_bill_type_click(self):
        self.base_click(page.wait_excute_put_bill_type_click)

    # 选择待执行入库单-状态
    def page_wait_excute_put_bill_type_select(self):
        self.base_click(page.wait_excute_put_bill_type_select)

    # 点击查询
    def page_wait_excute_put_bill_search_button(self):
        self.base_click(page.public_search_button)

    # 点击入库
    def page_wait_excute_put_bill_put_button(self):
        self.base_click(page.public_one_row_button)

    # 点击执行
    def page_wait_excute_put_bill_excute_button(self):
        self.base_click(page.wait_excute_put_bill_excute_button)

    """
        入库单管理新增、查询、审批、入库
    """

    # 点击入库单管理
    def page_put_bill_manage_click(self):
        self.base_click(page.put_bill_manage_click)

    # 点击新增
    def page_put_bill_manage_insert_click(self):
        self.base_click(page.public_insert_button)

    # 输入入库单名称
    def page_put_bill_manage_insert_put_bill_name_input(self):
        self.base_input(page.public_name_input, page.public_value)
    # 输入入库单名称2
    def page_put_bill_manage_insert_put_bill_name2_input(self):
        self.base_input(page.public_name_input, page.public_value_num2)
    # 点击类型
    def page_put_bill_manage_type_click(self):
        self.base_click(page.put_bill_manage_type_click)

    # 选择类型
    def page_put_bill_manage_type_select(self):
        self.base_click(page.put_bill_manage_type_select)

    # 输入申请留有
    def page_put_bill_manage_applyReason_input(self):
        self.base_input(page.public_applyReason_input, page.public_value)

    # 点击添加备件清单
    def page_put_bill_manage_part_unit_click(self):
        self.base_click(page.put_bill_manage_part_unit_click)

    # 点击添加备件清单icon
    def page_put_bill_manage_part_unit_icon(self):
        self.base_click(page.put_bill_manage_part_unit_icon)

    # 选择添加备件清单radio
    def page_put_bill_manage_part_unit_radio(self):
        self.base_click(page.public_radio)
    # 点击确定
    def page_put_bill_manage_insert_sure_button(self):
        self.base_click(page.public_sure_button)

    # 输入备件数量
    def page_put_bill_manage_insert_part_num_input(self):
        self.base_input(page.public_part_num_input, page.public_order_num)

    # 输入采购单价
    def page_put_bill_manage_insert_part_price_input(self):
        self.base_input(page.public_part_price_input, page.public_order_num)

    # 输入采购单位
    def page_put_bill_manage_insert_part_unit_input(self):
        self.base_input(page.public_part_unit_input, page.public_value_num2)

    # 点击保存
    def page_put_bill_manage_insert_save_button(self):
        self.base_click(page.put_bill_manage_insert_save_button)

    """
        入库管理查询
    """

    # 输入入库单名称
    def page_put_bill_manage_search_name_input(self):
        self.base_input(page.public_name_input, page.public_value)

    # 点击状态
    def page_put_bill_manage_part_unit_type_click(self):
        self.base_click(page.put_bill_manage_part_unit_type_click)

    # 选择状态-待审批
    def page_put_bill_manage_part_unit_type_select_approval(self):
        self.base_click(page.put_bill_manage_part_unit_type_select_approval)

    # 选择状态-待入库
    def page_put_bill_manage_part_unit_type_select_put(self):
        self.base_click(page.put_bill_manage_part_unit_type_select_put)

    # 选择状态-完成入库
    def page_put_bill_manage_part_unit_type_select_finish_put(self):
        self.base_click(page.put_bill_manage_part_unit_type_select_finish_put)
    # 点击查询
    def page_put_bill_manage_search_button(self):
        self.base_click(page.public_search_button)

    # 点击审批
    def page_put_bill_manage_approval_button(self):
        self.base_click(page.public_two_row_button)

    # 输入审批意见
    def page_put_bill_manage_approval_device_input(self):
        self.base_input(page.public_apprival_device_input, page.public_value)

    # 点击通过
    def page_put_bill_manage_through_button(self):
        self.base_click(page.public_apprival_through_button)

    # 点击入库
    def page_put_bill_manage_put_button(self):
        self.base_click(page.public_three_row_button)

    # 点击执行
    def page_put_bill_manage_excute_button(self):
        self.base_click(page.put_bill_manage_excute_button)

    """
        入库单查看
    """

    # 点击查看
    def page_put_bill_manage_watch_button(self):
        self.base_click(page.put_bill_manage_watch_button)

    """
        组装业务方法
    """

    # 我的入库单新增
    def mine_put_bill_insert(self):
        self.page_storage_manage_click()
        self.page_put_manage_click()
        self.page_mine_put_bill_click()
        self.page_mine_put_bill_insert_click()
        self.page_mine_put_bill_insert_put_part_name()
        self.page_mine_put_bill_type_click()
        self.page_mine_put_bill_type_select()
        self.page_mine_put_bill_inser_apply_reason_input()
        self.page_mine_put_bill_insert_part_bill()
        self.page_mine_put_bill_insert_part_bill_icon()
        self.page_mine_put_bill_insert_part_bill_radio()
        self.page_mine_put_bill_insert_sure_button()
        self.page_mine_put_bill_insert_part_num_input()
        self.page_mine_put_bill_insert_part_price_input()
        self.page_mine_put_bill_insert_part_unit_input()
        self.page_mine_put_bill_insert_save_button()
        time.sleep(2)

    # 待审批入库单查询
    def wait_approval_put_bill_search(self):
        self.page_wait_approval_put_bill_click()
        self.page_wait_approval_put_bill_name_input()
        self.page_wait_approval_put_bill_type_click()
        self.page_wait_approval_put_bill_type_select()
        self.page_wait_approval_put_bill_search_button()
        time.sleep(2)

    # 待审批入库单审批
    def wait_approval_put_bill_approval(self):
        self.wait_approval_put_bill_search()
        self.page_wait_approval_put_bill_approval_button()
        self.page_wait_approval_device_input()
        self.page_wait_approval_device_through()
        time.sleep(2)

    # 待执行入库单查询
    def wait_approval_put_bill_excute_search(self):
        self.page_wait_excute_bill_click()
        self.page_wait_excute_bill_name_input()
        self.page_wait_excute_put_bill_type_click()
        self.page_wait_excute_put_bill_type_select()
        self.page_wait_excute_put_bill_search_button()
        time.sleep(2)

    # 待执行入库单入库
    def wait_approval_put_bill_put(self):
        self.mine_put_bill_insert()
        self.wait_approval_put_bill_search()
        self.wait_approval_put_bill_approval()
        self.wait_approval_put_bill_excute_search()
        self.page_wait_excute_put_bill_put_button()
        self.page_wait_excute_put_bill_excute_button()
        time.sleep(2)

    # 入库单管理的新增
    def put_bill_manage_insert(self):
        self.page_put_bill_manage_click()
        self.page_put_bill_manage_insert_click()
        self.page_put_bill_manage_insert_put_bill_name2_input()
        self.page_put_bill_manage_type_click()
        self.page_put_bill_manage_type_select()
        self.page_put_bill_manage_applyReason_input()
        self.page_put_bill_manage_part_unit_click()
        self.page_put_bill_manage_part_unit_icon()
        self.page_put_bill_manage_part_unit_radio()
        self.page_put_bill_manage_insert_sure_button()
        self.page_put_bill_manage_insert_part_num_input()
        self.page_put_bill_manage_insert_part_price_input()
        self.page_put_bill_manage_insert_part_unit_input()
        self.page_put_bill_manage_insert_save_button()
        time.sleep(2)

    # 入库单管理的查询-待审批
    def put_bill_manage_search_approval(self):
        self.page_put_bill_manage_insert_put_bill_name2_input()
        self.page_put_bill_manage_part_unit_type_click()
        self.page_put_bill_manage_part_unit_type_select_approval()
        self.page_put_bill_manage_search_button()
        time.sleep(2)

    # 入库单管理的查询-待入库
    def put_bill_manage_search_put(self):
        self.page_put_bill_manage_insert_put_bill_name2_input()
        self.page_put_bill_manage_part_unit_type_click()
        self.page_put_bill_manage_part_unit_type_select_put()
        self.page_put_bill_manage_search_button()
        time.sleep(2)

    # 入库单管理的查询-完成入库
    def put_bill_manage_search_finish_put(self):
        self.page_put_bill_manage_insert_put_bill_name2_input()
        self.page_put_bill_manage_part_unit_type_click()
        self.page_put_bill_manage_part_unit_type_select_finish_put()
        self.page_put_bill_manage_search_button()
        time.sleep(2)
    # 入库单管理的审批
    def put_bill_manage_approval(self):
        self.page_put_bill_manage_approval_button()
        self.page_put_bill_manage_approval_device_input()
        self.page_put_bill_manage_through_button()
        time.sleep(2)

    # 入库单管理的入库
    def put_bill_manage_put(self):
        self.put_bill_manage_insert()
        self.put_bill_manage_search_approval()
        self.put_bill_manage_approval()
        self.put_bill_manage_search_put()
        self.page_put_bill_manage_put_button()
        self.page_put_bill_manage_excute_button()
        time.sleep(2)

    # 入库单管理的查看
    def put_bill_manage_watch(self):
        self.put_bill_manage_search_finish_put()
        self.page_put_bill_manage_watch_button()
        self.base_refresh()
        time.sleep(2)
