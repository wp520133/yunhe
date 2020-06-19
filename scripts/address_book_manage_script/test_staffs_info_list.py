import unittest
from page.page_adress_book_manage.page_staffs_info_list import PageStaffsInfoList
from parameterized import parameterized
from base.get_driver import GetDriver
from tools.read_txt import read_txt
import allure
import pytest
import page

class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.psil = PageStaffsInfoList(cls.driver)
        cls.psil.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # @parameterized.expand(read_txt(("")))
    def test_staffs_info_insert(self):
        self.psil.staffs_info_insert()

if __name__ == '__main__':
    pytest.main()
