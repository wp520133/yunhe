import unittest
from page.page_curing_work_manage.page_curing_inference_manage import PageCuringInferenceManage
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
        cls.pcim = PageCuringInferenceManage(cls.driver)
        cls.pcim.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    @allure.step(title="养护结论点击")
    def test_curing_inference_manage_click(self):
        self.pcim.curing_inference_manage_click()

    @parameterized.expand(read_txt("curing_work_manage/curing_inference.txt"))
    @allure.step(title="养护结论输入异常数据新增")
    def test_curing_inference_manage_insert(self, inference, desc, success):
        self.pcim.curing_inference_manage_insert(inference, desc)
        if success:
            try:
                self.pcim.page_curing_inference_manage_return_click()
            except:
                self.pcim.base_get_image()

    # 测试新增、查询、编辑
    @allure.step(title="养护结论新增、查询到编辑")
    def test_curing_inference_manage_edit(self):
        self.pcim.curing_inference_manage_edit(page.public_value, page.public_value)

    # 测试重置
    @allure.step(title="养护结论重置")
    def test_curing_inference_manage_reset(self):
        self.pcim.curing_inference_manage_reset()


if __name__ == '__main__':
    unittest.main()
