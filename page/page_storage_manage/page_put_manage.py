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
        self.base_click(page.public_put_bill_insert_click)

    # 输入入库单名称
    def page_mine_put_bill_insert_put_part_name(self, put_part):
        self.base_input(page.public_put_bill_name_input, put_part)

    # 点击类型
    def page_mine_put_bill_type_click(self):
        self.base_click(page.public_put_bill_type_click)

    # 选择类型
    def page_mine_put_bill_type_select(self):
        self.base_click(page.public_put_bill_type_select)

    # 输入申请理由
    def page_mine_put_bill_inser_apply_reason_input(self, apply_reason):
        self.base_input(page.public_put_bill_apply_reason_input, apply_reason)

    # 点击添加备件清单
    def page_mine_put_bill_insert_part_bill(self):
        self.base_click(page.public_put_bill_insert_part_bill)

    # 点击选择备件型号icon
    def page_mine_put_bill_insert_part_bill_icon(self):
        self.base_click(page.public_put_bill_insert_part_bill_icon)

    # 选择备件型号radio
    def page_mine_put_bill_insert_part_bill_radio(self):
        self.base_click(page.public_put_bill_insert_art_bill_radio)

    # 点击确定
    def page_mine_put_bill_insert_sure_button(self):
        self.base_click(page.public_put_bill_insert_part_bill_sure_button)

    # 输入备件数量
    def page_mine_put_bill_insert_part_num_input(self, part_num):
        self.base_input(page.public_put_bill_insert_part_bill_num_input, part_num)

    # 输入采购单价
    def page_mine_put_bill_insert_part_price_input(self, price):
        self.base_input(page.public_put_bill_insert_part_bill_price_input, price)

    # 输入采购单位
    def page_mine_put_bill_insert_part_unit_input(self, part_unit):
        self.base_input(page.public_put_bill_insert_part_bill_unit_input, part_unit)

    # 点击保存
    def page_mine_put_bill_insert_save_button(self):
        self.base_click(page.public_put_bill_insert_part_bill_save_button)

    # 点击返回
    def page_mine_put_bill_insert_return_button(self):
        self.base_click(page.public_return_click)

    # 点击待审批入库单
    def page_wait_approval_put_bill_click(self):
        self.base_click(page.wait_approval_put_bill_click)

    # 输入待审批入库单-名称
    def page_wait_approval_put_bill_name_input(self):
        self.base_input(page.public_put_bill_name_input, page.public_value)

    # 输入待审批入库单-点击状态
    def page_wait_approval_put_bill_type_click(self):
        self.base_click(page.public_put_bill_status_click)

    # 输入待审批入库单-选择状态
    def page_wait_approval_put_bill_type_select(self):
        self.base_click(page.public_put_bill_status_select)

    # 点击查询
    def page_wait_approval_put_bill_search_button(self):
        self.base_click(page.public_put_bill_search_button)

    # 点击审批
    def page_wait_approval_put_bill_approval_button(self):
        self.base_click(page.public_put_bill_approval_button)

    # 输入审批意见
    def page_wait_approval_device_input(self):
        self.base_input(page.public_put_bill_apprival_device_input, page.public_value)

    # 点击通过
    def page_wait_approval_device_through(self):
        self.base_click(page.public_put_bill_apprival_through_button)

    # 点击待执行入库单
    def page_wait_excute_bill_click(self):
        self.base_click(page.wait_excute_put_bill_click)

    # 输入待执行入库单-名称
    def page_wait_excute_bill_name_input(self):
        self.base_input(page.public_put_bill_name_input, page.public_value)

    # 点击待执行入库单-状态
    def page_wait_excute_put_bill_type_click(self):
        self.base_click(page.public_put_bill_status_click)

    # 选择待执行入库单-状态
    def page_wait_excute_put_bill_type_select(self):
        self.base_click(page.public_put_bill_status_select)

    # 点击查询
    def page_wait_excute_put_bill_search_button(self):
        self.base_click(page.public_put_bill_search_button)

    # 点击入库
    def page_wait_excute_put_bill_put_button(self):
        self.base_click(page.public_put_bill_put_click)

    # 点击执行
    def page_wait_excute_put_bill_excute_button(self):
        self.base_click(page.public_wait_excute_put_bill_excute_button)

    """
        入库单管理新增、查询、审批、入库
    """

    # 点击入库单管理
    def page_put_bill_manage_click(self):
        self.base_click(page.put_bill_manage_click)

    # 点击新增
    def page_put_bill_manage_insert_click(self):
        self.base_click(page.public_put_bill_insert_click)

    # 输入入库单名称
    def page_put_bill_manage_insert_put_bill_name_input(self):
        self.base_input(page.public_put_bill_name_input, page.public_value)

    # 点击类型
    def page_put_bill_manage_type_click(self):
        self.base_click(page.public_put_bill_type_click)

    # 选择类型
    def page_put_bill_manage_type_select(self):
        self.base_click(page.public_put_bill_type_select)

    # 输入申请留有
    def page_put_bill_manage_applyReason_input(self,apply_reason):
        self.base_input(page.public_put_bill_apply_reason_input,apply_reason)

    # 点击添加备件清单
    def page_put_bill_manage_part_unit_click(self):
        self.base_click(page.public_put_bill_insert_part_bill)

    # 点击添加备件清单icon
    def page_put_bill_manage_part_unit_icon(self):
        self.base_click(page.public_put_bill_insert_part_bill_icon)

    # 选择添加备件清单radio
    def page_put_bill_manage_part_unit_radio(self):
        self.base_click(page.public_put_bill_insert_art_bill_radio)

    # 点击确定
    def page_put_bill_manage_insert_sure_button(self):
        self.base_click(page.public_put_bill_insert_part_bill_sure_button)

    # 输入备件数量
    def page_put_bill_manage_insert_part_num_input(self,part_num):
        self.base_input(page.public_put_bill_insert_part_bill_num_input, part_num)

    # 输入采购单价
    def page_put_bill_manage_insert_part_price_input(self,price):
        self.base_input(page.public_put_bill_insert_part_bill_price_input, price)

    # 输入采购单位
    def page_put_bill_manage_insert_part_unit_input(self,part_unit):
        self.base_input(page.public_put_bill_insert_part_bill_unit_input, part_unit)

    # 点击保存
    def page_put_bill_manage_insert_save_button(self):
        self.base_click(page.public_put_bill_insert_part_bill_save_button)

    """
        入库管理待审批入库单查询
    """

    # 输入入库单名称
    def page_put_bill_manage_search_name_input(self):
        self.base_input(page.public_put_bill_name_input, page.public_value)

    def page_put_bill_manage_insert_put_bill_name2_input(self,put_part):
        self.base_input(page.public_put_bill_name_input, put_part)

    # 点击状态
    def page_put_bill_manage_part_unit_type_click(self):
        self.base_click(page.public_put_bill_status_click)

    # 选择状态-待审批
    def page_put_bill_manage_part_unit_type_select_approval(self):
        self.base_click(page.put_bill_manage_part_unit_type_select_approval)

    # 选择状态-待入库
    def page_put_bill_manage_part_unit_type_select_put(self):
        self.base_click(page.put_bill_manage_part_unit_type_select_put)

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
        组装业务方法
    """

    # 点击入库管理
    def mine_put_bill_click(self):
        self.page_storage_manage_click()
        self.page_put_manage_click()
        time.sleep(2)

    # 我的入库单新增
    def mine_put_bill_insert(self, put_part, apply_reason, part_num, price, part_unit):
        self.page_mine_put_bill_click()
        self.page_mine_put_bill_insert_click()
        self.page_mine_put_bill_insert_put_part_name(put_part)
        self.page_mine_put_bill_type_click()
        self.page_mine_put_bill_type_select()
        self.page_mine_put_bill_inser_apply_reason_input(apply_reason)
        self.page_mine_put_bill_insert_part_bill()
        self.page_mine_put_bill_insert_part_bill_icon()
        self.page_mine_put_bill_insert_part_bill_radio()
        self.page_mine_put_bill_insert_sure_button()
        self.page_mine_put_bill_insert_part_num_input(part_num)
        self.page_mine_put_bill_insert_part_price_input(price)
        self.page_mine_put_bill_insert_part_unit_input(part_unit)
        self.page_mine_put_bill_insert_save_button()
        time.sleep(2)

    # 我的入库单查询
    def mine_put_bill_search(self, put_part, apply_reason, part_num, price, part_unit):
        self.mine_put_bill_insert(put_part, apply_reason, part_num, price, part_unit)
        self.page_wait_excute_bill_name_input()
        self.page_wait_excute_put_bill_type_click()
        self.page_wait_excute_put_bill_type_select()
        self.page_wait_excute_put_bill_search_button()
        time.sleep(2)

    # 待审批入库单查询
    def wait_approval_put_bill_search(self):
        self.page_wait_approval_put_bill_click()
        self.page_wait_approval_put_bill_name_input()
        self.page_wait_approval_put_bill_type_click()
        self.page_wait_approval_put_bill_type_select()
        self.page_wait_approval_put_bill_search_button()
        time.sleep(2)

    # # 待审批入库单审批
    # def wait_approval_put_bill_approval(self):
    #     self.wait_approval_put_bill_search()
    #     self.page_wait_approval_put_bill_approval_button()
    #     self.page_wait_approval_device_input()
    #     self.page_wait_approval_device_through()
    #     time.sleep(2)

    # 待执行入库单查询
    def wait_approval_put_bill_excute_search(self):
        self.page_wait_excute_bill_click()
        self.page_wait_excute_bill_name_input()
        self.page_wait_excute_put_bill_type_click()
        self.page_wait_excute_put_bill_type_select()
        self.page_wait_excute_put_bill_search_button()
        time.sleep(2)

    # 待执行入库单入库
    def wait_approval_put_bill_put(self, put_part, apply_reason, part_num, price, part_unit):
        self.mine_put_bill_insert(put_part, apply_reason, part_num, price, part_unit)
        # self.wait_approval_put_bill_approval()
        self.wait_approval_put_bill_excute_search()
        self.page_wait_excute_put_bill_put_button()
        self.page_wait_excute_put_bill_excute_button()
        time.sleep(2)

    # 入库单管理的新增
    def put_bill_manage_insert(self, put_part, apply_reason, part_num, price, part_unit):
        self.page_put_bill_manage_click()
        self.page_put_bill_manage_insert_click()
        self.page_put_bill_manage_insert_put_bill_name2_input(put_part)
        self.page_put_bill_manage_type_click()
        self.page_put_bill_manage_type_select()
        self.page_put_bill_manage_applyReason_input(apply_reason)
        self.page_put_bill_manage_part_unit_click()
        self.page_put_bill_manage_part_unit_icon()
        self.page_put_bill_manage_part_unit_radio()
        self.page_put_bill_manage_insert_sure_button()
        self.page_put_bill_manage_insert_part_num_input(part_num)
        self.page_put_bill_manage_insert_part_price_input(price)
        self.page_put_bill_manage_insert_part_unit_input(part_unit)
        self.page_put_bill_manage_insert_save_button()
        time.sleep(2)

    # 入库单管理的查询-待审批
    def put_bill_manage_search_approval(self,put_part):
        self.page_put_bill_manage_insert_put_bill_name2_input(put_part)
        self.page_put_bill_manage_part_unit_type_click()
        self.page_put_bill_manage_part_unit_type_select_approval()
        self.page_put_bill_manage_search_button()
        time.sleep(2)

    # 入库单管理的查询-待入库
    def put_bill_manage_search_put(self,put_part):
        self.page_put_bill_manage_insert_put_bill_name2_input(put_part)
        self.page_put_bill_manage_part_unit_type_click()
        self.page_put_bill_manage_part_unit_type_select_put()
        self.page_put_bill_manage_search_button()
        time.sleep(2)

    # # 入库单管理的审批
    # def put_bill_manage_approval(self):
    #     self.page_put_bill_manage_approval_button()
    #     self.page_put_bill_manage_approval_device_input()
    #     self.page_put_bill_manage_through_button()
    #     time.sleep(2)

    # 入库单管理的入库
    def put_bill_manage_put(self,put_part, apply_reason, part_num, price, part_unit):
        self.put_bill_manage_insert(put_part, apply_reason, part_num, price, part_unit)
        self.put_bill_manage_search_approval(put_part)
        # self.put_bill_manage_approval()
        self.put_bill_manage_search_put(put_part)
        self.page_put_bill_manage_put_button()
        self.page_put_bill_manage_excute_button()
        time.sleep(2)
