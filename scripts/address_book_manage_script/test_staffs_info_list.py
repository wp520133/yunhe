import unittest
from page.page_adress_book_manage.page_staffs_info_list import PageStaffsInfoList
import page
from base.get_driver import GetDriver
import allure
import pytest


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

    def test_staffs_info_insert(self):
        self.psil.staffs_info_insert()

if __name__ == '__main__':
    pytest.main()
