import unittest
from page.page_curing_work_manage.page_maintenance_record_manage import PageMaintenanceRecordManage
from base.get_driver import GetDriver
from parameterized import parameterized
from tools.read_txt import read_txt
import page
import allure
import pytest


class TestCuringTeamManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pmtrm = PageMaintenanceRecordManage(cls.driver)
        cls.pmtrm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 点击维修记录管理
    def test_maintenance_record_manage_click(self):
        self.pmtrm.maintenance_record_manage_click()

    @parameterized.expand(read_txt("curing_work_manage/maintenance_record.txt"))
    def test_maintenance_record_manage_except_insert(self, content, price, desc, remark, success):
        self.pmtrm.maintenance_record_manage_insert(content, price, desc, remark)
        if success:
            try:
                self.pmtrm.page_maintenance_record_manage_return_click()
            except:
                self.pmtrm.base_get_image()

    # 新增
    def test_maintenance_record_manage_insert(self):
        self.pmtrm.maintenance_record_manage_insert(page.public_value, page.public_order_num, page.public_value,
                                                    page.public_value)

    # 编辑
    def test_maintenance_record_manage_edit(self):
        self.pmtrm.maintenance_record_manage_edit(page.public_value_num2, page.public_order_num, page.public_value_num2,
                                                  page.public_value_num2)

    # 查看
    def test_maintenance_record_manage_watch(self):
        self.pmtrm.maintenance_record_manage_watch()


if __name__ == '__main__':
    pytest.main()
