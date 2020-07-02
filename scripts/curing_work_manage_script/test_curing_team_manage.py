import unittest
from page.page_curing_work_manage.page_curing_team_manage import PageCuringTeamManage
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
        cls.pctm = PageCuringTeamManage(cls.driver)
        cls.pctm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    @allure.step(title="养护小组管理点击")
    def test_curing_team_manage_click(self):
        self.pctm.curing_team_manage_click()

    @parameterized.expand(read_txt(""))
    @allure.step(title="养护小组管理新增")
    def test_curing_team_manage_insert(self, team_name, desc):
        self.pctm.curing_team_manage_insert(team_name, desc)

    # 测试养护小组新增、查看、编辑
    def test_curing_team_manage_edit(self):
        self.pctm.curing_team_manage_edit(page.public_value, page.public_value)

    # 测试重置
    def test_curing_team_manage_reset(self):
        self.pctm.curing_team_manage_reset()

    # 测试查看
    def test_curing_team_manage_watch(self):
        self.pctm.curing_team_manage_watch()


if __name__ == '__main__':
    unittest.main()
