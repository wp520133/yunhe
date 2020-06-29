import unittest
from page.page_system_manage.page_dept_manage import PageDeptManage
from base.get_driver import GetDriver
from parameterized import parameterized
from tools.read_txt import read_txt
import page
import pytest
import allure


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pd = PageDeptManage(cls.driver)
        cls.pd.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试部门管理新增
    @allure.step(title="测试部门管理正常数据新增")
    # @pytest.mark.run(order=1)
    def test_dept_manage_insert(self):
        self.pd.dept_manage_insert(page.public_value, page.public_password, page.public_value, page.public_value,
                                   page.public_moile_phone, page.public_value, page.public_password)

    # 测试部门管理新增异常数据
    @parameterized.expand(read_txt("system_manage/system_dept.txt"))
    @allure.step(title="测试部门管理异常数据新增")
    # @pytest.mark.run(order=2)
    def test_dept_manage_except_insert(self, dept_name, dept_number, desc_duty, line_persion_name, line_phone,
                                       manage_persion_name, order, success):
        self.pd.dept_manage_insert(dept_name, dept_number, desc_duty, line_persion_name, line_phone,
                                   manage_persion_name, order)
        if success:
            try:
                self.pd.page_dept_manage_insert_return()
            except:
                self.pd.base_get_image()

    # 测试部门管理编辑
    @allure.step(title="测试部门管理正常数据编辑")
    # @pytest.mark.run(order=3)
    def test_dept_manage_edit(self):
        self.pd.dept_manage_edit(page.public_value, page.public_value, page.public_value, page.public_moile_phone,
                                 page.public_value, page.public_password)

    # 测试部门管理查看
    @allure.step(title="测试部门管理查看")
    # @pytest.mark.run(order=4)
    def test_dept_manage_watch(self):
        self.pd.dept_manage_watch()


if __name__ == '__main__':
    pytest.main()
