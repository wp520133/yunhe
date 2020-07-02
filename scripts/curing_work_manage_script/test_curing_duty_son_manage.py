import unittest
from page.page_curing_work_manage.page_curing_duty_son_manage import PageCuringDutySonManage
from base.get_driver import GetDriver
from parameterized import parameterized
from tools.read_txt import read_txt
import page
import allure
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pcdsm = PageCuringDutySonManage(cls.driver)
        cls.pcdsm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试养护职责子管理点击
    @allure.step(title="养护职责子管理点击")
    def test_curing_duty_son_click(self):
        self.pcdsm.curing_duty_son_click()

    # 测试养护职责子管理新增
    @parameterized.expand(read_txt("curing_work_manage/curing_duty_son.txt"))
    @allure.step(title="养护职责子管理异常数据新增")
    def test_curing_duty_son_insert(self, curing_name, success):
        self.pcdsm.curing_duty_son_except_insert(curing_name)
        if success:
            try:
                self.pcdsm.page_curing_duty_son_return_click()
            except:
                self.pcdsm.base_get_image()

    # 测试养护职责管理的新增、查询、编辑
    @allure.step(title="养护职责子管理新增、查询到编辑")
    def test_curing_duty_son_edit(self):
        self.pcdsm.curing_duty_son_edit(page.public_value)

    # 测试重置
    @allure.step(title="养护职责子管理重置")
    def test_curing_duty_son_reset(self):
        self.pcdsm.curing_duty_son_reset()

    # 测试查看
    @allure.step(title="养护职责子管理查看")
    def test_curing_duty_son_watch(self):
        self.pcdsm.curing_duty_son_watch()


if __name__ == '__main__':
    unittest.main()
