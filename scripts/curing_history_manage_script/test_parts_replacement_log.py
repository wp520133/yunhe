import unittest
from page.page_curing_history_manage.page_parts_replacement_log import PagePartsReplacementLog
from base.get_driver import GetDriver
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pprl = PagePartsReplacementLog(cls.driver)
        cls.pprl.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 配件更换日志的查询与重置
    def test_page_parts_replacement_log_reset(self):
        self.pprl.page_parts_replacement_log_reset()


if __name__ == '__main__':
    pytest.main()
