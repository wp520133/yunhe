import unittest
from page.page_storage_manage.page_out_manage import PageOutManage
from base.get_driver import GetDriver
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pom = PageOutManage(cls.driver)
        cls.pom.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试我的报废单的新增、到查询审批
    @pytest.mark.run(order=1)
    def test_wait_excute_scrap_bill_out(self):
        self.pom.wait_excute_scrap_bill_out()

    # 测试我的领用单的新增、到查询审批
    @pytest.mark.run(order=2)
    def test_wait_excute_mind_receive_bill_out(self):
        self.pom.wait_excute_mind_receive_bill_out()


if __name__ == '__main__':
    pytest.main()
