import unittest
from page.page_system_manage.page_num_dict_manage import PageNumDictManage
from base.get_driver import GetDriver
from parameterized import parameterized
from tools.read_txt import read_txt
import page
import pytest
import allure


class TestNumDictManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pndm = PageNumDictManage(cls.driver)
        cls.pndm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试数字字典管理新增
    @parameterized.expand(read_txt("system_manage/system_num_dict.txt"))
    @allure.step(title="测试数字字典的异常输入新增")
    @pytest.mark.run(order=1)
    def test_num_dict_manage_except_insert(self, desc, type_other, mark_info):
        self.pndm.page_num_dict_manage_insert(desc, type_other, mark_info)

    # 测试数字字典管理新增
    @allure.step(title="测试数字字典的正常输入新增")
    @pytest.mark.run(order=2)
    def test_num_dict_manage_insert(self):
        self.pndm.page_num_dict_manage_insert(page.public_value, page.public_value, page.public_value)

    # 测试数字字典管理编辑
    @allure.step(title="测试数字字典的编辑")
    @pytest.mark.run(order=3)
    def test_num_dict_manage_edit(self, desc, type, mark_info):
        self.pndm.page_num_dict_manage_edit(desc, type, mark_info)

    # 测试数字字典字典项新增
    @parameterized.expand(read_txt("system_manage/system_num_dict_tem.txt"))
    @allure.step(title="测试数字字典项的异常输入新增")
    @pytest.mark.run(order=4)
    def test_num_dict_manage_four_line_nape_insert(self, data, tag, desc, order, mark_info):
        self.pndm.page_num_dict_manage_four_line_nape_insert(data, tag, desc, order, mark_info)

    # 测试数字字典字典项新增
    @allure.step(title="输入数字字典项的正常输入新增")
    @pytest.mark.run(order=5)
    def test_num_dict_manage_four_line_nape_insert(self):
        self.pndm.page_num_dict_manage_four_line_nape_insert(page.public_value, page.public_value, page.public_value,
                                                             page.public_order_num, page.public_value)

    # 测试数字字典字典项编辑
    @allure.step(title="输入数字字典项的编辑")
    @pytest.mark.run(order=6)
    def test_num_dict_manage_four_line_nape_edit(self, data, tag, desc, order, mark_info):
        self.pndm.page_num_dict_manage_four_line_nape_edit(data, tag, desc, order, mark_info)


if __name__ == '__main__':
    unittest.main()
