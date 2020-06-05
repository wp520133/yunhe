import unittest
from page.page_curing_work_manage.page_curing_work_manage import PageCuringWorkManage
from base.get_driver import GetDriver


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pcwm = PageCuringWorkManage(cls.driver)
        cls.pcwm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试养护小组新增、查看、编辑
    def test_curing_team_manage_edit(self):
        self.pcwm.curing_team_manage_edit()

    # 测试重置
    def test_curing_team_manage_reset(self):
        self.pcwm.curing_team_manage_reset()

    # 测试查看
    def test_curing_team_manage_watch(self):
        self.pcwm.curing_team_manage_watch()


if __name__ == '__main__':
    unittest.main()
