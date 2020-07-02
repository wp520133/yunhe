import unittest
from page.page_curing_work_manage.page_curing_plan_manage import PageCuringPlanManage
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
        cls.pcpm = PageCuringPlanManage(cls.driver)
        cls.pcpm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 点击养护计划管理
    def test_curing_plan_manage_click(self):
        self.pcpm.curing_plan_manage_click()

    # 养护计划管理新增
    @parameterized.expand(read_txt("curing_work_manage/curing_plan.txt"))
    def test_curing_plan_manage_except_insert(self, plan_name, content, remark, success):
        self.pcpm.curing_plan_manage_insert(plan_name, content, remark)
        if success:
            try:
                self.pcpm.page_curing_plan_manage_insert_return_click()
            except:
                self.pcpm.base_get_image()

    # 养护计划管理编辑
    def test_curing_plan_manage_edit(self):
        self.pcpm.curing_plan_manage_edit(page.public_value, page.public_value, page.public_value, page.public_value)

    # 测试查看
    def test_curing_plan_manage_watch(self):
        self.pcpm.curing_plan_manage_watch(page.public_value)

    # 测试禁用
    def test_curing_plan_manage_disable(self):
        self.pcpm.curing_plan_manage_disable(page.public_value)

    # 测试延迟
    def test_curing_plan_manage_delay(self):
        self.pcpm.curing_plan_manage_delay(page.public_value,page.public_order_num)


if __name__ == '__main__':
    unittest.main()
