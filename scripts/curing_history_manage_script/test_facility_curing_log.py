import unittest
from page.page_curing_history_manage.page_facility_curing_log import PageFacilityCuringLog
from base.get_driver import GetDriver
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pfcl = PageFacilityCuringLog(cls.driver)
        cls.pfcl.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试设备养护日志查询与重置
    @pytest.mark.run(order=1)
    def test_facility_curing_log_reset(self):
        self.pfcl.facility_curing_log_reset()

    # 设备养护日志记录查看
    @pytest.mark.run(order=2)
    def test_facility_curing_log_watch(self):
        self.pfcl.facility_curing_log_watch()


if __name__ == '__main__':
    pytest.main()
