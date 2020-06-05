import unittest
from page.page_curing_work_manage.page_curing_inference_manage import PageCuringInferenceManage
from base.get_driver import GetDriver


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pcim = PageCuringInferenceManage(cls.driver)
        cls.pcim.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试新增、查询、编辑
    def test_curing_inference_manage_edit(self):
        self.pcim.curing_inference_manage_edit()

    # 测试重置
    def test_curing_inference_manage_reset(self):
        self.pcim.curing_inference_manage_reset()


if __name__ == '__main__':
    unittest.main()
