import unittest
from page.page_curing_plan_mange import PageCuringPlanManage
from base.get_driver import GetDriver


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pcpm = PageCuringPlanManage(cls.driver)
        cls.pcpm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试养护计划管理的新增、查询、编辑
