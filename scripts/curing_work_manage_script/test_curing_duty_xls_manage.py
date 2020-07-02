import unittest
from page.page_curing_work_manage.page_curing_duty_xls_manage import PageCuringDutyXlsManage
from base.get_driver import GetDriver
from parameterized import parameterized
from tools.read_txt import read_txt
import page
import allure
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pcdxm = PageCuringDutyXlsManage(cls.driver)
        cls.pcdxm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    @allure.step(title="养护职责模板管理点击")
    def test_curing_duty_cls_manage_click(self):
        self.pcdxm.curing_duty_cls_manage_click()

    @parameterized.expand(read_txt("curing_work_manage/curing_duty_xls.txt"))
    @allure.step(title="养护职责模板管理异常数据新增")
    def test_curing_duty_cls_manage_insert(self,cls_name,success):
        self.pcdxm.curing_duty_cls_manage_insert(cls_name)
        if success:
            try:
                self.pcdxm.page_curing_duty_cls_manage_return_click()
            except:
                self.pcdxm.base_get_image()

    # 测试养护职责模板管理新增、查询、编辑
    @allure.step(title="养护职责模板管理新增、查询到编辑")
    def test_curing_duty_cls_manage_edit(self):
        self.pcdxm.curing_duty_cls_manage_edit(page.public_value)

    # 测试重置
    @allure.step(title="养护职责模板管理重置")
    def test_curing_duty_cls_manage_reset(self):
        self.pcdxm.curing_duty_cls_manage_reset()

    # 测试查看
    @allure.step(title="养护职责模板管理查看")
    def test_curing_duty_cls_manage_watch(self):
        self.pcdxm.curing_duty_cls_manage_watch()


if __name__ == '__main__':
    unittest.main()
