import unittest
from page.page_file_manage.page_project_material_manage import PageProjectMaterialManage
from base.get_driver import GetDriver
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.ppmm = PageProjectMaterialManage(cls.driver)
        cls.ppmm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()
    # 测试我的项目材料新增到审批
    def test_mind_material_ISA(self):
        self.ppmm.mind_material_ISA()

    # 测试项目材料管理(子)新增到审批
    def test_project_material_son_ISA(self):
        self.ppmm.project_material_son_ISA()

    # 测试工程项目管理新增
    def test_engineering_project_manage_insert(self):
        self.ppmm.engineering_project_manage_insert()


if __name__ == '__main__':
    pytest.main()
