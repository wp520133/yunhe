import unittest
from page.page_curing_work_manage.page_curing_tesk_son_manage import PageCuringTeskSonManage
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
        cls.pctsm = PageCuringTeskSonManage(cls.driver)
        cls.pctsm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试养护任务点击
    def test_curing_tesk_son_manage_click(self):
        self.pctsm.curing_tesk_son_manage_click()

    # 测试养护任务管理编辑
    def test_curing_tesk_son_manage_edit(self):
        self.pctsm.curing_tesk_son_manage_edit(page.public_value, page.public_value, page.public_value,
                                               page.public_value)

    # 养护任务管理查看
    def test_curing_tesk_son_manage_watch(self):
        self.pctsm.curing_tesk_son_manage_watch()

    # 养护任务管理催办
    def test_curing_tesk_son_manage_press(self):
        self.pctsm.curing_tesk_son_manage_press()

    # 养护任务管理延时
    def test_curing_tesk_son_manage_delayed(self):
        self.pctsm.curing_tesk_son_manage_delayed(page.public_order_num)


if __name__ == '__main__':
    unittest.main()
