import page
import time
from base.base import Base


class PageCuringTeskSonManage(Base):
    """
        养护作业管理→养护职责管理→养护小组管理新增
    """

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)