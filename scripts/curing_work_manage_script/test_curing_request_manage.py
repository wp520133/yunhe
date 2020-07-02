import unittest
from page.page_curing_work_manage.page_curing_request_manage import PageCuringRequestManage
from base.get_driver import GetDriver


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pcrm = PageCuringRequestManage(cls.driver)
        cls.pcrm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试新增、查看、编辑
    def test_curing_request_manage_edit(self):
        self.pcrm.curing_request_manage_edit()

    # 测试重置
    def test_curing_request_manage_reset(self):
        self.pcrm.curing_request_manage_reset()


if __name__ == '__main__':
    unittest.main()
