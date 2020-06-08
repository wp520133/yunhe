import unittest
from page.page_curing_history_manage.page_breakdown_service_log import PageBreakdownServiceLog
from base.get_driver import GetDriver
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pbsl = PageBreakdownServiceLog(cls.driver)
        cls.pbsl.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试故障维修日志的查询与重置
    @pytest.mark.run(order=1)
    def test_breakdown_service_log_reset(self):
        self.pbsl.breakdown_service_log_reset()

    # 测试故障维修日志的查看
    @pytest.mark.run(order=2)
    def test_breakdown_service_log_watch(self):
        self.pbsl.breakdown_service_log_watch()


if __name__ == '__main__':
    pytest.main()
