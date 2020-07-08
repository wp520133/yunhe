import unittest
from page.page_curing_work_manage.page_curing_urgency_task import PageCuringUrgencyTask
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
        cls.pcut = PageCuringUrgencyTask(cls.driver)
        cls.pcut.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试紧急养护点击
    def test_curing_urgency_task_click(self):
        self.pcut.curing_urgency_task_click()

    # 测试异常新增输入
    @parameterized.expand(read_txt("/"))
    def test_curing_urgency_task_insert(self, task_name, content, remark):
        self.pcut.curing_urgency_task_insert(task_name, content, remark)

    # 测试新增到编辑
    def test_curing_urgency_task_edit(self):
        self.pcut.curing_urgency_task_edit(page.public_value, page.public_value, page.public_value, page.public_value,
                                           page.public_value2)


if __name__ == '__main__':
    pytest.main()
