import unittest
from page.page_curing_work_manage.page_curing_by_me import PageCuringByMe
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
        cls.pcbm = PageCuringByMe(cls.driver)
        cls.pcbm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 点击由我执行的任务
    def test_curing_by_me(self):
        self.pcbm.curing_by_me()

    # 测试养护记录
    def test_curing_by_me_cord(self):
        self.pcbm.curing_by_me_cord()

    # 测试详情
    def test_curing_by_me_details(self):
        self.pcbm.curing_by_me_details()


if __name__ == '__main__':
    pytest.main()
