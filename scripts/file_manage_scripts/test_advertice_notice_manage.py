import unittest
from page.page_file_manage.page_advertice_notice_manage import PageAdverticeNoticeManage
from base.get_driver import GetDriver
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.panm = PageAdverticeNoticeManage(cls.driver)
        cls.panm.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试我的宣传公告新增到审批
    @pytest.mark.run(order=1)
    def test_mind_advertice_notice_ISA(self):
        self.panm.mind_advertice_notice_ISA()

    # 测试宣传公告管理的新增到审批
    @pytest.mark.run(order=2)
    def test_advertice_notice_manage_son_ISA(self):
        self.panm.advertice_notice_manage_son_ISA()


if __name__ == '__main__':
    pytest.main()
