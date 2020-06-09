import unittest
from page.page_storage_manage.page_storage_each_manage import PageStorageEachManage
from base.get_driver import GetDriver
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.psem = PageStorageEachManage(cls.driver)
        cls.psem.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    def test_storage_each_task_approval(self):
        self.psem.storage_each_task_approval()


if __name__ == '__main__':
    pytest.main()
