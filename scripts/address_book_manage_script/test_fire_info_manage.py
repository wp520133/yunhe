import unittest
from page.page_adress_book_manage.page_firm_info_list import PageFirmInfoManage
import page
from base.get_driver import GetDriver
import allure
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pfim = PageFirmInfoManage(cls.driver)
        cls.pfim.system_login("admin", 123456)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    @pytest.mark.run(order=1)
    @allure.step(title="企业信息列表新增、查询、编辑")
    def test_firm_info_manage_edit(self):
        self.pfim.firm_info_manage_edit(page.public_value, page.public_value, page.public_value,
                                        page.public_moile_phone, page.public_land_line_phone, page.public_email,
                                        page.public_value, page.public_value2)

    @pytest.mark.run(order=2)
    @allure.step(title="企业信息列表查看")
    def test_firm_info_manage_watch(self):
        self.pfim.firm_info_manage_watch(page.public_value2, page.public_value, page.public_value)


if __name__ == '__main__':
    pytest.main()
