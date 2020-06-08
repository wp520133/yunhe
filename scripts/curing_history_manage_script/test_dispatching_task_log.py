import unittest
from page.page_curing_history_manage.page_dispatching_task_log import PageDispatchingTaskLog
from base.get_driver import GetDriver
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pdtl = PageDispatchingTaskLog(cls.driver)
        cls.pdtl.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 查询与重置
    def test_dispatching_task_log_reset(self):
        self.pdtl.dispatching_task_log_reset("admin")

    # 查看
    def test_dispatching_task_log_watch(self):
        self.pdtl.dispatching_task_log_watch()


if __name__ == '__main__':
    pytest.main()
