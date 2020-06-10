import unittest
from page.page_file_manage.page_file_data_manage import PageFileDataManage
from base.get_driver import GetDriver
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pfdm = PageFileDataManage(cls.driver)
        cls.pfdm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试我的档案新增查询到审批
    @pytest.mark.run(order=1)
    def test_mind_file_ISA(self):
        self.pfdm.mind_file_ISA()

    # 测试档案管理新增查询到审批
    @pytest.mark.run(order=2)
    def test_file_manage_ISA(self):
        self.pfdm.file_manage_ISA()


if __name__ == '__main__':
    pytest.main()
