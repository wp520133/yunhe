import unittest
from page.page_storage_manage.page_put_manage import PagePutManage
from base.get_driver import GetDriver
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.ppm = PagePutManage(cls.driver)
        cls.ppm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试入库
    @pytest.mark.run(order=1)
    def test_wait_approval_put_bill_put(self):
        self.ppm.wait_approval_put_bill_put()

    # 测试入库单管理入库
    @pytest.mark.run(order=2)
    def test_put_bill_manage_put(self):
        self.ppm.put_bill_manage_put()

    # 测试入库单管理查看
    @pytest.mark.run(order=3)
    def test_put_bill_manage_watch(self):
        self.ppm.put_bill_manage_watch()


if __name__ == '__main__':
    pytest.main()
