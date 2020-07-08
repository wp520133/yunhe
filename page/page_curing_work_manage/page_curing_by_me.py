import page
import time
from base.base import Base


class PageCuringByMe(Base):
    """
        养护作业管理→养护职责管理→养护小组管理新增
    """

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    # 点击养护任务管理
    def page_curing_tesk_manage_click(self):
        self.base_click(page.curing_tesk_manage_click)

    # 点击由我执行的任务
    def page_curing_by_me_click(self):
        self.base_click(page.curing_by_me_click)

    # 点击养护记录
    def page_curing_by_me_cord_click(self):
        self.base_click(page.curing_by_me_cord_click)

    # # 点击返回
    def page_curing_by_me_return_click(self):
        self.base_click(page.curing_by_me_return_click)

    # # 点击详情
    def page_curing_by_me_details_click(self):
        self.base_click(page.curing_by_me_details_click)

    """
        组装业务方法
    """

    # 点击由我执行的任务
    def curing_by_me(self):
        self.page_curing_work_manage_click()
        self.page_curing_tesk_manage_click()
        self.page_curing_by_me_click()

    # 养护记录
    def curing_by_me_cord(self):
        self.page_curing_by_me_cord_click()
        self.page_curing_by_me_return_click()
        time.sleep(2)

    # 详情
    def curing_by_me_details(self):
        self.page_curing_by_me_details_click()
        self.base_refresh()
