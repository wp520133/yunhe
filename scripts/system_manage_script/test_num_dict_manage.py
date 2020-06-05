import unittest
from page.page_system_manage.page_num_dict_manage import PageNumDictManage
from base.get_driver import GetDriver


class TestNumDictManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pndm = PageNumDictManage(cls.driver)
        cls.pndm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试数字字典管理新增
    def test_num_dict_manage_insert(self):
        self.pndm.page_num_dict_manage_insert()

    # 测试数字字典管理编辑
    def test_num_dict_manage_edit(self):
        self.pndm.page_num_dict_manage_edit()

    # 测试数字字典字典项新增
    def test_num_dict_manage_four_line_nape_insert(self):
        self.pndm.page_num_dict_manage_four_line_nape_insert()

    # 测试数字字典字典项编辑
    def test_num_dict_manage_four_line_nape_edit(self):
        self.pndm.page_num_dict_manage_four_line_nape_edit()


if __name__ == '__main__':
    unittest.main()
