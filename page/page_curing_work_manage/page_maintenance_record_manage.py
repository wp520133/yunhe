import page
import time
from base.base import Base


class PageMaintenanceRecordManage(Base):
    """
        养护作业管理→养护职责管理→养护小组管理新增
    """

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    # 点击养护任务管理
    def page_curing_tesk_manage_click(self):
        self.base_click(page.curing_tesk_manage_click)

    # 点击维修记录
    def page_maintenance_record_manage_click(self):
        self.base_click(page.maintenance_record_manage_click)

    # 点击新增
    def page_maintenance_record_manage_insert_click(self):
        self.base_click(page.maintenance_record_manage_insert_click)

    # 点击养护名称icon
    def page_maintenance_record_manage_insert_name_icon(self):
        self.base_click(page.maintenance_record_manage_insert_name_icon)

    # 选择养护名称radio
    def page_maintenance_record_manage_insert_name_radio(self):
        self.base_click(page.maintenance_record_manage_insert_name_radio)

    # 点击确定
    def page_maintenance_record_manage_insert_name_sure(self):
        self.base_click(page.maintenance_record_manage_insert_name_sure)

    # 点击损坏类型
    def page_maintenance_record_manage_insert_back_type_click(self):
        self.base_click_enter(page.maintenance_record_manage_insert_back_type_click)

    # 选择损坏类型
    def page_maintenance_record_manage_insert_back_type_select(self):
        self.base_click_enter(page.maintenance_record_manage_insert_back_type_click)

    # 输入损坏原因概述
    def page_maintenance_record_manage_insert_back_content(self, content):
        self.base_input(page.maintenance_record_manage_insert_back_content, content)

    # 点击维修结果
    def page_maintenance_record_manage_insert_service_result_click(self):
        self.base_click(page.maintenance_record_manage_insert_service_result_click)

    # 选择维修结果
    def page_maintenance_record_manage_insert_service_result_select(self):
        self.base_click(page.maintenance_record_manage_insert_service_result_select)

    # 点击维修时间
    def page_maintenance_record_manage_insert_service_time_click(self):
        self.base_click(page.maintenance_record_manage_insert_service_time_click)

    # 选择维修时间
    def page_maintenance_record_manage_insert_service_time_select(self):
        self.base_click(page.maintenance_record_manage_insert_service_time_select)

    # 点击是否选择维修厂家
    def page_maintenance_record_manage_insert_is_shop(self):
        self.base_click(page.maintenance_record_manage_insert_is_shop)

    # 点击维修厂家
    def page_maintenance_record_manage_insert_service_shop_click(self):
        self.base_click(page.maintenance_record_manage_insert_service_shop_click)

    # 选择维修厂家
    def page_maintenance_record_manage_insert_service_shop_select(self):
        self.base_click(page.maintenance_record_manage_insert_service_shop_select)

    # 点击维修人icon
    def page_maintenance_record_manage_insert_service_person_icon(self):
        self.base_click(page.maintenance_record_manage_insert_service_person_icon)

    # 选择维修人raido
    def page_maintenance_record_manage_insert_service_person_radio(self):
        self.base_click(page.maintenance_record_manage_insert_service_person_radio)

    # 点击确定
    def page_maintenance_record_manage_insert_service_sure(self):
        self.base_click(page.maintenance_record_manage_insert_service_sure)

    # 输入维修费用
    def page_maintenance_record_manage_insert_service_price(self, price):
        self.base_input(page.maintenance_record_manage_insert_service_price, price)

    # 输入维修方法描述
    def page_maintenance_record_manage_insert_service_desc(self, desc):
        self.base_input(page.maintenance_record_manage_insert_service_desc, desc)

    # 输入备注
    def page_maintenance_record_manage_insert_service_remark(self, remark):
        self.base_input(page.maintenance_record_manage_insert_service_remark, remark)

    # 点击保存
    def page_maintenance_record_manage_insert_sure(self):
        self.base_click(page.maintenance_record_manage_insert_sure)

    # 点击返回
    def page_maintenance_record_manage_return_click(self):
        self.base_click(page.public_return_click)

    # 点击编辑
    def page_maintenance_record_manage_edit_button(self):
        self.base_click(page.maintenance_record_manage_edit_button)

    # 点击查看
    def page_maintenance_record_manage_watch_button(self):
        self.base_click(page.maintenance_record_manage_watch_button)

    """
        组装业务方法
    """

    # 点击维修记录管理
    def maintenance_record_manage_click(self):
        self.page_curing_work_manage_click()
        self.page_curing_tesk_manage_click()
        self.page_maintenance_record_manage_click()
        time.sleep(2)

    # 新增
    def maintenance_record_manage_insert(self, content, price, desc, remark):
        self.page_maintenance_record_manage_insert_click()
        self.page_maintenance_record_manage_insert_name_icon()
        self.page_maintenance_record_manage_insert_name_radio()
        self.page_maintenance_record_manage_insert_name_sure()
        self.page_maintenance_record_manage_insert_back_type_click()
        self.page_maintenance_record_manage_insert_back_type_select()
        self.page_maintenance_record_manage_insert_back_content(content)
        self.page_maintenance_record_manage_insert_service_result_click()
        self.page_maintenance_record_manage_insert_service_result_select()
        self.page_maintenance_record_manage_insert_service_time_click()
        self.page_maintenance_record_manage_insert_service_time_select()
        self.page_maintenance_record_manage_insert_is_shop()
        self.page_maintenance_record_manage_insert_service_shop_click()
        self.page_maintenance_record_manage_insert_service_shop_select()
        self.page_maintenance_record_manage_insert_service_person_icon()
        self.page_maintenance_record_manage_insert_service_person_radio()
        self.page_maintenance_record_manage_insert_service_sure()
        self.page_maintenance_record_manage_insert_service_price(price)
        self.page_maintenance_record_manage_insert_service_desc(desc)
        self.page_maintenance_record_manage_insert_service_remark(remark)
        self.page_maintenance_record_manage_insert_sure()
        time.sleep(2)

    # 编辑
    def maintenance_record_manage_edit(self, content, price, desc, remark):
        self.page_maintenance_record_manage_edit_button()
        self.page_maintenance_record_manage_insert_name_icon()
        self.page_maintenance_record_manage_insert_name_radio()
        self.page_maintenance_record_manage_insert_name_sure()
        self.page_maintenance_record_manage_insert_back_type_click()
        self.page_maintenance_record_manage_insert_back_type_select()
        self.page_maintenance_record_manage_insert_back_content(content)
        self.page_maintenance_record_manage_insert_service_result_click()
        self.page_maintenance_record_manage_insert_service_result_select()
        self.page_maintenance_record_manage_insert_service_time_click()
        self.page_maintenance_record_manage_insert_service_time_select()
        self.page_maintenance_record_manage_insert_is_shop()
        self.page_maintenance_record_manage_insert_service_shop_click()
        self.page_maintenance_record_manage_insert_service_shop_select()
        self.page_maintenance_record_manage_insert_service_person_icon()
        self.page_maintenance_record_manage_insert_service_person_radio()
        self.page_maintenance_record_manage_insert_service_sure()
        self.page_maintenance_record_manage_insert_service_price(price)
        self.page_maintenance_record_manage_insert_service_desc(desc)
        self.page_maintenance_record_manage_insert_service_remark(remark)
        self.page_maintenance_record_manage_insert_sure()
        time.sleep(2)

    # 查看
    def maintenance_record_manage_watch(self):
        self.page_maintenance_record_manage_watch_button()
        self.base_refresh()
        time.sleep(2)
