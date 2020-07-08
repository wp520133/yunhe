import unittest
from page.page_curing_work_manage.page_curing_by_me_approval import PageCuringByMeApproval
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
        cls.pcbma = PageCuringByMeApproval(cls.driver)
        cls.pcbma.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 点击由我审批的任务
    def test_curing_by_me_approval(self):
        self.pcbma.curing_by_me_approval()

    # 详情
    def test_curing_by_me_approval_details(self):
        self.pcbma.curing_by_me_approval_details()

    # 审批
    def test_curing_by_me_approval_approval(self):
        self.pcbma.curing_by_me_approval_approval(page.public_value)


if __name__ == '__main__':
    pytest.main()
