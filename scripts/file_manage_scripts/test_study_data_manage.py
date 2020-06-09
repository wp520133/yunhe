import unittest
from page.page_file_manage.page_study_data_manage import PageStudyDataManage
from base.get_driver import GetDriver
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.psdm = PageStudyDataManage(cls.driver)
        cls.psdm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # # 测试我的学习资料新增到编辑(需要做修复)
    # def test_mine_study_data_edit(self):
    #     self.psdm.mine_study_data_edit()

    # 测试我的学习资料新增到审批
    def test_study_data_approval(self):
        self.psdm.study_data_approval()


if __name__ == '__main__':
    pytest.main()
