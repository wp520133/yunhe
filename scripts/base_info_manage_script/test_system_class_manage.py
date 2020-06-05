import unittest
from page.page_base_info_mange.page_system_class_manage import PageSystemClassManage
from base.get_driver import GetDriver


class TestSystemClassManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pscm = PageSystemClassManage(cls.driver)
        cls.pscm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 同时实现新增、查询、编辑
    def test_system_class_manage_edit(self):
        self.pscm.system_class_manage_edit()

    # 实现重置
    def test_system_class_manage_reset(self):
        self.pscm.system_class_manage_reset()


if __name__ == '__main__':
    unittest.main()
