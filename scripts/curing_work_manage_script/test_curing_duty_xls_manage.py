import unittest
from page.page_curing_work_manage.page_curing_duty_xls_manage import PageCuringDutyXlsManage
from base.get_driver import GetDriver


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pcdxm = PageCuringDutyXlsManage(cls.driver)
        cls.pcdxm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试养护职责模板管理新增、查询、编辑
    def test_curing_duty_cls_manage_edit(self):
        self.pcdxm.curing_duty_cls_manage_edit()

    # 测试重置
    def test_curing_duty_cls_manage_reset(self):
        self.pcdxm.curing_duty_cls_manage_reset()

    # 测试查看
    def test_curing_duty_cls_manage_watch(self):
        self.pcdxm.curing_duty_cls_manage_watch()


if __name__ == '__main__':
    unittest.main()
