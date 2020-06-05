import unittest
from page.page_curing_work_manage.page_curing_item_manage import PageCuringItemManage
from base.get_driver import GetDriver


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pcim = PageCuringItemManage(cls.driver)
        cls.pcim.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试养护项目管理新增、查看、编辑
    def test_curing_item_manage_edit(self):
        self.pcim.curing_item_manage_edit()

    # 测试重置
    def test_curing_item_manage_reset(self):
        self.pcim.curing_item_manage_reset()

    # 测试查看
    def test_curing_item_manage_watch(self):
        self.pcim.curing_item_manage_watch()


if __name__ == '__main__':
    unittest.main()
