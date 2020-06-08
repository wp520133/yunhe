import unittest
from page.page_curing_history_manage.page_situation_reflects_log import PageSituationReflectsLog
from base.get_driver import GetDriver
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.psrt = PageSituationReflectsLog(cls.driver)
        cls.psrt.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 查询与重置
    @pytest.mark.run(order=1)
    def test_situation_reflects_log_reset(self):
        self.psrt.situation_reflects_log_reset()

    # 查看
    @pytest.mark.run(order=2)
    def test_situation_reflects_log_watch(self):
        self.psrt.situation_reflects_log_watch()


if __name__ == '__main__':
    pytest.main()
