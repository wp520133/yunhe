import unittest
from page.pageCuringWorkManage.page_curing_duty_son_manage import PageCuringDutySonManage
from base.get_driver import GetDriver


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pcdsm = PageCuringDutySonManage(cls.driver)
        cls.pcdsm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试养护职责管理的新增、查询、编辑
    def test_curing_duty_son_edit(self):
        self.pcdsm.curing_duty_son_edit()

    # 测试重置
    def test_curing_duty_son_reset(self):
        self.pcdsm.curing_duty_son_reset()

    # 测试查看
    def test_curing_duty_son_watch(self):
        self.pcdsm.curing_duty_son_watch()


if __name__ == '__main__':
    unittest.main()
