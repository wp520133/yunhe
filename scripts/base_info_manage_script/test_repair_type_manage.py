import unittest
from page.page_base_info_mange.page_repair_type_manage import PageRepairTypeManage
from base.get_driver import GetDriver


class TestSystemClassManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.prtm = PageRepairTypeManage(cls.driver)
        cls.prtm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试新增、查询、编辑
    def test_repair_type_manage_edit(self):
        self.prtm.repair_type_manage_edit()

    # 测试重置
    def test_repair_type_manage_reset(self):
        self.prtm.repair_type_manage_reset()

    # 测试查看
    def test_repair_type_manage_watch(self):
        self.prtm.repair_type_manage_watch()


if __name__ == '__main__':
    unittest.main()
