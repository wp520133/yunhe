import page
import time
from base.base import Base


class PageCuringRequestManage(Base):

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    """
        养护计划管理
    """
    