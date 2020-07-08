import page
import time
from base.base import Base


class PageCuringByMeApproval(Base):

    # 点击养护作业管理
    def page_curing_work_manage_click(self):
        self.base_click(page.curing_work_manage_click)

    # 点击养护任务管理
    def page_curing_tesk_manage_click(self):
        self.base_click(page.curing_tesk_manage_click)

    # 点击由我审批的任务
    def page_curing_by_me_approval_click(self):
        self.base_click(page.curing_by_me_approval_click)

    # 点击详情
    def page_curing_by_me_approval_details_click(self):
        self.base_click(page.curing_by_me_approval_details_click)

    # 点击审批
    def page_curing_by_me_approval_approval_click(self):
        self.base_click(page.curing_by_me_approval_approval_click)

    # 输入审批意见
    def page_curing_by_me_approval_device(self, device):
        self.base_input(page.curing_by_me_approval_device, device)

    # 点击通过
    def page_curing_by_me_approval_through(self):
        self.base_click(page.curing_by_me_approval_through)

    """
        组装业务方法
    """
    # 点击由我审批的任务
    def curing_by_me_approval(self):
        self.page_curing_work_manage_click()
        self.page_curing_tesk_manage_click()
        self.page_curing_by_me_approval_click()
        time.sleep(2)

    # 详情
    def curing_by_me_approval_details(self):
        self.page_curing_by_me_approval_details_click()
        self.base_refresh()

    # 审批
    def curing_by_me_approval_approval(self,device):
        self.page_curing_by_me_approval_approval_click()
        self.page_curing_by_me_approval_device(device)
        self.page_curing_by_me_approval_through()