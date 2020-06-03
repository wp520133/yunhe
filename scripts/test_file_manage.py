import unittest
from page.page_study_data_manage import PageStudyDataManage
from base.get_driver import GetDriver


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

    # 测试我的学习资料新增
    def test_mine_study_data_insert(self):
        self.psdm.mine_study_data_insert()

if __name__ == '__main__':
    unittest.main()