from selenium.webdriver.common.by import By
from xeger import Xeger


url = "http://192.168.102.50:6426/"

value = r'([a-zA-Z]{3,6})'
value2 = r'([a-zA-Z]{1,2})'
password = r'(^\d{6,9}$)'
order = r'(^\d{1,2}$)'
moilePhone = r'(^1[3|5|7|8|]\d{9}$)'
xeger = Xeger()
publicValue = xeger.xeger(value)
publicValue2 = xeger.xeger(value)
publicValue_num_2 = xeger.xeger(value2)
publicPassword = xeger.xeger(password)
publicMoilePhone = xeger.xeger(moilePhone)
publicOrder = xeger.xeger(order)
publicOrder2 = xeger.xeger(order)
public_order_num = publicOrder
public_order_num_other = publicOrder2
public_value = publicValue
public_value2 = publicValue2
public_value_num2=publicValue_num_2
public_password = publicPassword
public_moile_phone = publicMoilePhone

# 公共的用户名输入
public_username_input = By.ID, "username"
# 公共的密码输入
public_password_input = By.ID, "password"
# 公共的名字输入
public_name_input = By.ID, "name"
# 公共的确认密码输入
public_confirm_input = By.ID, "confirm"
# 公共的申请理由输入
public_applyReason_input = By.ID, "applyReason"
# 公共的单选按钮以及确认按钮
public_radio = By.CSS_SELECTOR, "tr.ant-table-row:nth-child(1) > td:nth-child(1) > span:nth-child(1) > label:nth-child(1) > span:nth-child(1) > input"
public_sure_button = By.CSS_SELECTOR, ".ant-modal-footer > div:nth-child(1) > button:nth-child(2)"
# 公共的输入数量
public_num_input = By.ID, "spareNum[0]"
# 公共的添加按钮
public_insert_button = By.CSS_SELECTOR, ".style_titleGroup__3gG29 > div:nth-child(2) > button:nth-child(1)"
# 公共的操作1列按钮
public_one_row_button = By.CSS_SELECTOR, "button.ant-btn-link:nth-child(1)"
# 公共的操作3列按钮
public_three_row_button = By.CSS_SELECTOR, "button.ant-btn-link:nth-child(3)"
# 公共的状态点击及选择
public_status_click = By.CSS_SELECTOR, ".ant-select-selection"
public_status_select = By.CSS_SELECTOR, "li.ant-select-dropdown-menu-item:nth-child(1)"
# 公共的查询按钮
public_search_button = By.CSS_SELECTOR, ".ant-btn-primary"
# 公共的审批意见
public_approval_device_input = By.ID, "auditOpinion"
# 公共的角色名称
public_role_name_input = By.ID, "roleName"
# 公共的角色标识
public_role_code_input = By.ID, "roleCode"
# 公共的角色描述
public_role_desc_input = By.ID, "roleDesc"
# 公共的新增保存按钮
public_insert_save_button = By.CSS_SELECTOR, "button.ant-btn:nth-child(2)"
# 公共的部门职责(输入)
public_dept_duty_input = By.ID, "dutyDesc"
# 公共的联系人
public_link_person_name_input = By.ID, "linkPersonName"
# 公共的联系电话
public_link_phone_input = By.ID, "linkPhone"
# 公共的负责人
public_manage_persion_name_input = By.ID, "managePersonName"
# 公共的排序
public_order_input = By.ID, "order"
# 公共的编号code
public_code_input = By.ID, "code"
# 公共的四行查看
public_watch_four_line_click = By.CSS_SELECTOR, "tr.ant-table-row:nth-child(4) > td:nth-child(6) > div:nth-child(1) > button:nth-child(1)"
# 公共的四行编辑
public_edit_four_line_click = By.CSS_SELECTOR, "tr.ant-table-row:nth-child(4) > td:nth-child(6) > div:nth-child(1) > button:nth-child(2)"
# 公共的描述
public_desc_input = By.ID, "desc"
# 公共的输入类型
public_type_input = By.ID, "type"
# 公有的备注信息
public_remarks_input = By.ID, "remarks"
# 公有的备注
public_remark_input = By.ID, "remark"
# 公有的数据值
public_value_input = By.ID, "value"
# 公有的标签名
public_label_input = By.ID, "label"
# 公有的字典排序
public_sort_input = By.ID, "sort"
# 公有的创建人
public_createBy_input=By.ID,"createBy"
# 公有的创建人value
public_createBy="admin"
# 公有的重置按钮
public_reset_button = By.CSS_SELECTOR, "div.ant-form-item-control-wrapper:nth-child(1) > div:nth-child(1) > span:nth-child(1) > button:nth-child(2)"
# 公有的操作2列
public_two_row_button=By.CSS_SELECTOR, "button.ant-btn-link:nth-child(2)"
# 公有的操作4列
public_four_row_button=By.CSS_SELECTOR, "button.ant-btn-link:nth-child(4)"
# 公有的操作5列
public_five_row_button=By.CSS_SELECTOR, "button.ant-btn-link:nth-child(5)"
# 公有的品牌名
public_brand_name_input=By.ID,"brandName"
# 公有的有效期
public_effective_time_input=By.ID,"effectiveTime"
# 公有的保修期
public_guarantee_num_input=By.ID,"guaranteeNum"
# 公有序列号
public_sn_input=By.ID,"sn"
# 公共计数单位
public_countUnit_input=By.ID,"countUnit"
# 公有队长姓名
public_caption_person_name_input=By.ID,"captionPersonName"
public_caption_person_name="丁四鸣"
# 公有队长用户名
public_caption_user_name_input=By.ID,"captionUsername"
# 公有具体操作方法
public_detail_method_input=By.ID,"detailMethod"
# 公有最大保养周期
public_required_max_period_input=By.ID,"requiredMaximumMaintenancePeriod"
# 公有的建议保养周期
public_recommended_main_period_input=By.ID,"recommendedMaintenancePeriod"
# 公有的位置描述
public_positon_desc_input=By.ID,"positionDesc"
# 公有的职责模板名称
public_standard_duty_name_input=By.ID,"standardDutyName"
# 公有的养护名称
public_duty_name_input=By.ID,"dutyName"
# 公有养护计划名称
public_plan_name_input=By.ID,"planName"
# 公有保养周期
public_cycle_input=By.ID,"cycle"
# 公有的执行内容
public_content_input=By.ID,"content"
# 公有的延时天数
public_delay_day_input=By.ID,"delayDay"
# 公有的标题
public_title_input=By.ID,"title"
# 公有备件数量
public_part_num_input=By.ID,"spareNum[0]"
# 公有采购单价
public_part_price_input=By.ID,"purchasingPrice[0]"
# 公有采购单位
public_part_unit_input=By.ID,"purchasingPriceUnit[0]"
# 输入审批意见
public_apprival_device_input=By.CSS_SELECTOR,"#auditOpinion"
# 点击通过
public_apprival_through_button=By.CSS_SELECTOR,"form.ant-form:nth-child(8) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > button:nth-child(2)"


# 系统登录
system_login_button = By.CSS_SELECTOR, ".ant-btn"
"""
    系统管理的相关变量
"""
system_manage_click=By.CSS_SELECTOR,"#root ul:first-child>li>ul>li:first-child>div"
# 系统管理→用户管理→查询
user_manage_status_click = By.CSS_SELECTOR, ".ant-select-selection"
user_manage_status_select = By.CSS_SELECTOR, "li.ant-select-dropdown-menu-item:nth-child(2)"
user_manage_search_button = By.CSS_SELECTOR, "div.ant-form-item-control-wrapper:nth-child(1) > div:nth-child(1) > span:nth-child(1) > button:nth-child(1)"

# 系统管理→用户管理→重置

# 系统管理→用户管理→禁用
user_manage_ban_button = By.CSS_SELECTOR, "button.ant-btn:nth-child(3)"
user_manage_ban_sure_button = By.CSS_SELECTOR, ".ant-modal-confirm-btns > button:nth-child(2)"
# 系统管理→用户管理新增
user_manage_insert_role_click = By.CSS_SELECTOR, ".ant-select-selection__placeholder"
user_manage_insert_role_select = By.CSS_SELECTOR, "li.ant-select-dropdown-menu-item:nth-child(1)"
user_manage_insert_rv_icon = By.CSS_SELECTOR, ".anticon-user"
# 系统管理→用户管理编辑(公有)

# 系统管理→角色管理新增(公有)

# 系统管理→点击角色管理
role_manage_click_button = By.CSS_SELECTOR, "li.ant-menu-item:nth-child(2) > span:nth-child(2)"
# 系统管理→点击新增按钮
role_manage_insert_click_button = By.CSS_SELECTOR, "button.ant-btn-primary:nth-child(1)"
# 系统管理→角色管理查看(公有)
# 系统管理→角色管理编辑(公有)

# 系统管理→角色管理权限
role_manage_power_four_line_click = By.CSS_SELECTOR, "tr.ant-table-row:nth-child(4) > td:nth-child(6) > div:nth-child(1) > button:nth-child(4)"
role_manage_power_checkbox = By.CSS_SELECTOR, ".ant-tree > li:nth-child(1) > span:nth-child(2)"
role_manage_power_down_icon = By.CSS_SELECTOR, ".ant-tree > li:nth-child(1) > span:nth-child(1) > i:nth-child(1) > svg:nth-child(1)"
role_manage_power_save_button = By.CSS_SELECTOR, ".ant-modal-footer > div:nth-child(1) > button:nth-child(2)"

# 系统管理→部门管理新增
# 点击部门管理
dept_manage_click_button = By.CSS_SELECTOR, "li.ant-menu-item:nth-child(4) > span:nth-child(2)"
# 点击新增
dept_manage_click_insert_button = By.CSS_SELECTOR, "button.ant-btn-primary:nth-child(1)"
# 点击父级节点
dept_manage_click_insert_parent_click = By.CSS_SELECTOR, ".ant-select-selection"
# 选择父级节点
dept_manage_click_insert_parent_select = By.CSS_SELECTOR, ".ant-select-tree > li:nth-child(1) > span:nth-of-type(2)"

# 系统管理→部门管理编辑
dept_manage_click_edit_button = By.CSS_SELECTOR, "tr.ant-table-row:nth-child(4) > td:nth-child(6) > div:nth-child(1) > button:nth-child(2)"

# 系统管理→部门管理查看(公有)
# 点击数字字典管理
num_dict_manage_click_button = By.CSS_SELECTOR, "li.ant-menu-item:nth-child(5) > span:nth-child(2)"
# 数字字典管理→新增
num_dict_manage_insert_click_button = By.CSS_SELECTOR, "button.ant-btn-primary:nth-child(1)"
# 数字字典管理→输入描述(公有)
# 数字字典管理→点击是否系统字典
num_dict_manage_insert_isno_dict_click = By.CSS_SELECTOR, ".ant-select-selection"
# 数字字典管理→选择是否系统字典
num_dict_manage_insert_isno_dict_select = By.CSS_SELECTOR, "li.ant-select-dropdown-menu-item:nth-child(1)"
# 数字字典管理→输入类型(公有)
# 数字字典管理→输入备注信息(公有)
# 数字字典管理→点击保存(公有)
# 数字字典管理修改
# 点击四行修改
num_dict_manage_four_line_edit_button = By.CSS_SELECTOR, "tr.ant-table-row:nth-child(4) > td:nth-child(6) > div:nth-child(1) > button:nth-child(1)"

# 点击四行字典项
num_dict_manage_four_line_dict_nape_button = By.CSS_SELECTOR, "tr.ant-table-row:nth-child(4) > td:nth-child(6) > div:nth-child(1) > button:nth-child(2)"
# 字典项新增
# 点击字典项新增
num_dict_manage_four_line_dict_nape_insert_button = By.CSS_SELECTOR, "button.ant-btn-primary:nth-child(1)"
# 输入数据值(公有)
# 输入标签名(公有)
# 输入描述(公有)
# 输入排序(公有)
# 输入备注信息(公有)
# 点击保存(公有)
# 字典项四行编辑
# 点击编辑
num_dict_manage_four_line_dict_nape_edit_button = By.CSS_SELECTOR, "tr.ant-table-row:nth-child(4) > td:nth-child(7) > div:nth-child(1) > button:nth-child(1)"


"""
    基础信息管理的相关变量
"""
# 点击基础信息管理
base_info_manage_click=By.CSS_SELECTOR,"li.ant-menu-submenu:nth-child(2) > div:nth-child(1) > span:nth-child(1) > span:nth-child(2)"
# 点击系统类别管理
system_class_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(2)>ul>li:first-child"
"""
    系统类别管理新增
"""
# 点击新增(公有)
# 点击上级系统类别
system_class_manage_super_system_class_click=By.CSS_SELECTOR,".ant-select-selection"
# 选择上级系统类别
system_class_manage_super_system_class_select=By.CSS_SELECTOR,".ant-select-tree-node-content-wrapper-close > span:nth-child(1)"
# 输入系统类别名称(公有)
# 输入描述(公有)
# 点击保存(公有)

"""
    系统类别管理查询
"""
# 输入系统类别名称(公有)
# 输入创建人(公有)
# 点击查询
system_class_manage_search_button=By.CSS_SELECTOR,"div.ant-form-item-control-wrapper:nth-child(1) > div:nth-child(1) > span:nth-child(1) > button:nth-child(1)"
"""
    系统类别管理重置
"""
# 点击重置按钮(公有)
"""                                                                     ""
    系统类别管理编辑
"""

# 点击编辑(公有)


"""
    部件类别管理新增
"""
# 点击部件类别管理
units_class_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(2)>ul>li:nth-child(2)"
# 点击新增(公有)
# 点击所属系统类别
units_class_manage_insert_belong_system_class_click=By.CSS_SELECTOR,"span.ant-select-selection"
# 选择所属系统类别
units_class_manage_insert_belong_system_class_select=By.CSS_SELECTOR,".ant-select-tree-node-content-wrapper-close > span:nth-child(1)"
# 点击上级部件类别
units_class_manage_insert_super_units_class_click=By.CSS_SELECTOR,"div.ant-select-selection"
# 选择上级部件类别
units_class_manage_insert_super_units_class_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 输入部件类别名称(公有)
# 输入描述(公有)
# 点击保存(公有)

"""
    部件类别管理查询
"""
# 输入部件类别名称(公有)
# 输入创建人(公有)
# 点击查询按钮(公有)

"""
    部件类别管理编辑
"""
# 点击编辑(公有)

"""
    部件类别管理重置
"""
# 点击重置(公有)


"""
    部件型号管理新增
"""
# 点击部件型号管理
units_type_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(2)>ul>li:nth-child(3)"
# 点击新增按钮(公有)
# 点击所属系统类别
units_type_manage_system_class_click=By.CSS_SELECTOR,"span.ant-select-selection"
# 选择所属系统类别
units_type_manage_system_class_select=By.CSS_SELECTOR,".ant-select-tree-node-content-wrapper-close > span:nth-child(1)"
# 点击所属部件类别
units_type_manage_units_type_click=By.CSS_SELECTOR,"#componentCategoryId > div:nth-child(1)"
# 选择所属部件类别
units_type_manage_units_type_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 点击上级部件型号
units_type_manage_super_units_type_click=By.CSS_SELECTOR,"#pid > div:nth-child(1)"
# 选择上级部件型号
units_type_manage_super_units_type_select=By.CSS_SELECTOR,".ant-select-dropdown-menu-item-active"
# 输入部件型号名称(公有)
# 点击厂商名称
units_type_manage_shop_name_click=By.CSS_SELECTOR,"#companyId > div:nth-child(1)"
# 选择厂商名称
units_type_manage_shop_name_select=By.CSS_SELECTOR,".ant-select-dropdown-menu-item-active"
# 输入品牌名(公有)
# 输入有效期(公有)
# 点击有效单位
units_type_manage_valid_unit_click=By.CSS_SELECTOR,"#effectiveTimeUnit > div:nth-child(1)"
# 选择有效单位
units_type_manage_valid_unit_select=By.CSS_SELECTOR,"body>div:last-child>div>div>div>ul>li:first-child"
# 输入保修期(公有)
# 点击上市时间
units_type_manage_appear_time_click=By.CSS_SELECTOR,".ant-calendar-picker-input"
# 选择上市时间
units_type_manage_appear_time_select=By.CSS_SELECTOR,".ant-calendar-today-btn"
# 输入描述(公有)
# 点击保存(公有)
"""
    部件型号管理查询
"""
# 输入部件型号名称(公有)
# 输入品牌名(公有)
# 输入编号(公有)
# 点击查询(公有)

"""
    部件型号管理编辑
"""
# 点击编辑(公有)

"""
    部件型号管理查看
"""
# 点击查看(公有)

# 页面刷新一次(公有)

"""
    部件型号管理重置
"""
# 点击重置(公有)


"""
    部件管理新增
"""
# 点击部件管理
units_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(2)>ul>li:nth-child(4)"
# 点击新增(公有)
# 点击所属系统类别
units_manage_system_class_click=By.CSS_SELECTOR,"span.ant-select-selection"
# 选择所属系统类别
units_manage_system_class_select=By.CSS_SELECTOR,".ant-select-tree-node-content-wrapper-close > span:nth-child(1)"
# 点击所属部件类别
units_manage_units_class_click=By.CSS_SELECTOR,"#partsCateId > div:nth-child(1)"
# 选择所属部件类别
units_manage_units_class_selefct=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 点击所属部件型号
units_manage_units_type_click=By.CSS_SELECTOR,"#partsTypeId > div:nth-child(1) > div:nth-child(1)"
# 选择所属部件型号
units_manage_units_type_select=By.CSS_SELECTOR,"body>div:nth-of-type(2) ul>li:nth-of-type(2)"
# 输入部件名称(公有)
# 输入序列号(公有)
# 点击生产日期
units_manage_pd_time_click=By.CSS_SELECTOR,"#manufactureDate > div:nth-child(1) > input:nth-child(1)"
# 选择生产日期
units_manage_pd_time_select=By.CSS_SELECTOR,".ant-calendar-today-btn"

# 点击报废日期
units_manage_sp_time_click=By.CSS_SELECTOR,"#retirementDate > div:nth-child(1) > input:nth-child(1)"
# 选择报废日期
units_manage_sp_time_select=By.CSS_SELECTOR,".ant-calendar-today-btn"
# 点击保修截止日期
units_manage_gt_time_click=By.CSS_SELECTOR,"#endGuaranteeDate > div:nth-child(1) > input:nth-child(1)"
# 选择保修截止日期
units_manage_gt_time_select=By.CSS_SELECTOR,".ant-calendar-today-btn"
# 输入备注(公有)
# 输入描述(公有)
# 点击保存(公有)

"""
    部件管理查询
"""
# 输入部件名称(公有)
# 输入序列号(公有)
# 点击查询(公有)
"""
    部件管理重置
"""
# 点击重置按钮(公有)

"""
    部件管理编辑
"""
# 点击部件管理编辑(公有)

"""
    部件管理查看
"""
# 点击部件管理查看(公有)
# 刷新(公有)



"""
    备件类别管理新增
"""

# 点击备件管理
repair_class_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(2)>ul>li:nth-child(5)"
# 点击新增(公有)
# 点击上级备件类别
repair_class_manage_super_repair_class_click=By.CSS_SELECTOR,".ant-select-selection__placeholder"
# 选择上级备件类别
repair_class_manage_super_repair_class_select=By.CSS_SELECTOR,"li.ant-select-tree-treenode-switcher-close:nth-child(1) > span:nth-child(2) > span:nth-child(1)"
# 输入备件类别名称(公有)
# 输入描述(公有)
# 点击保存(公有)

"""
    备件类别管理查询
"""
# 输入备件类别名称(公有)
# 输入创建人(公有)
# 点击查询(公有)

"""
    备件类别管理编辑
"""
# 点击编辑(公有)

"""
    备件类别管理重置
"""
# 点击重置(公有)



"""
    备件型号管理新增
"""

# 点击备件型号管理
repair_type_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(2)>ul>li:nth-child(6)"
# 点击新增(公有)
# 点击所属备件类别
repair_type_manage_repair_type_click=By.CSS_SELECTOR,"span.ant-select-selection__placeholder"
# 选择所属备件类别
repair_type_manage_repair_type_select=By.CSS_SELECTOR,"li.ant-select-tree-treenode-switcher-close:nth-child(1) > span:nth-child(2) > span:nth-child(1)"

# 点击上级备件型号
repair_type_manage_super_repair_type_click=By.CSS_SELECTOR,"#pid > div:nth-child(1) > div:nth-child(1)"

# 选择上级备件型号
repair_type_manage_super_repair_type_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"

# 输入备件型号名称(公有)

# 输入计数单位(公有)

# 点击厂商名称
repair_type_manage_shop_name_click=By.CSS_SELECTOR,"#companyId > div:nth-child(1) > div:nth-child(1)"
# 选择厂商名称
repair_type_manage_shop_name_select=By.CSS_SELECTOR,"body>div:last-child ul>li:first-child"
# 输入品牌名(公有)
# 输入有效期(公有)

# 点击有效单位
repair_type_manage_eu_click=By.CSS_SELECTOR,"#effectiveTimeUnit > div:nth-child(1) > div:nth-child(1)"
# 选择有效单位
repair_type_manage_eu_select=By.CSS_SELECTOR,".ant-select-dropdown-menu-item-active"

# 输入保修期(公有)

# 点击上市时间
repair_type_manage_ttm_click=By.CSS_SELECTOR,".ant-calendar-picker-input"
# 选择上市时间
repair_type_manage_ttm_select=By.CSS_SELECTOR,".ant-calendar-today-btn"

# 输入描述(公有)
# 点击保存(公有)
"""
    备件管理查询
"""
# 输入备件型号名称(公有)
# 输入品牌名(公有)
# 输入编号(公有)
# 点击查询(公有)
"""
    备件管理编辑
"""
# 点击编辑(公有)
"""
    备件管理重置
"""
# 点击重置(公有)
"""
    备件管理查看
"""
# 点击查看(公有)
# 刷新(公有)





"""
    我的入库单新增
"""
# 点击仓储管理
storage_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(3)>div"
# 点击入库管理
put_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(3)>ul>li:first-child>div"
# 点击我的入库单
mine_put_bill_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(3)>ul>li>ul>li:nth-child(1)"
# 点击新增
# 输入入库单名称
# 点击类型
mine_put_bill_type_click=By.CSS_SELECTOR,".ant-select-selection__rendered"
# 选择类型
mine_put_bill_type_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 输入申请理由
# 点击添加备件清单
mine_put_bill_insert_part_bill=By.CSS_SELECTOR,".ant-btn-dashed"
# 点击选择备件型号icon
mine_put_bill_insert_part_bill_icon=By.CSS_SELECTOR,".anticon-setting"
# 选择备件型号radio
# 点击确定
mine_put_bill_insert_part_bill_sure_button=By.CSS_SELECTOR,".ant-modal-footer > div:nth-child(1) > button:nth-child(2)"
# 输入备件数量
# 输入采购单价
# 输入采购单位
# 点击保存
# 点击待审批入库单
wait_approval_put_bill_click=By.CSS_SELECTOR,"li.ant-menu-item:nth-child(2) > span:nth-child(2)"
# 输入待审批入库单-名称
# 输入待审批入库单-点击状态
wait_approval_put_bill_type_click=By.CSS_SELECTOR,".ant-select-selection"
# 输入待审批入库单-选择状态
wait_approval_put_bill_type_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 点击查询
# 点击审批
# 点击待执行入库单
wait_excute_put_bill_click=By.CSS_SELECTOR,"li.ant-menu-item:nth-child(3) > span:nth-child(2)"
# 输入待执行入库单-名称
# 点击待执行入库单-状态
wait_excute_put_bill_type_click=By.CSS_SELECTOR,".ant-select-selection"
# 选择待执行入库单-状态
wait_excute_put_bill_type_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 点击查询
# 点击入库
# 点击执行
wait_excute_put_bill_excute_button=By.CSS_SELECTOR,".detail_detailContainer__3um4P > div:nth-child(7) > button:nth-child(2)"
"""
    入库单管理新增、查询、审批、入库
"""
# 点击入库单管理
put_bill_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(3)>ul>li>ul>li:nth-child(4)"
# 点击新增
# 输入入库单名称
# 点击类型
put_bill_manage_type_click=By.CSS_SELECTOR,".ant-select-selection__rendered"
# 选择类型
put_bill_manage_type_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 输入申请理由
# 点击添加备件清单
put_bill_manage_part_unit_click=By.CSS_SELECTOR,".ant-btn-dashed"
# 点击添加备件清单icon
put_bill_manage_part_unit_icon=By.CSS_SELECTOR,".anticon-setting"
# 选择添加备件清单radio
# 点击确定
# 输入备件数量
# 输入采购单价
# 输入采购单价单位
# 点击保存
put_bill_manage_insert_save_button=By.CSS_SELECTOR,"button.ant-btn:nth-child(2)"

"""
    入库管理查询
"""
# 输入入库单名称
# 点击状态
put_bill_manage_part_unit_type_click=By.CSS_SELECTOR,".ant-select-selection"
# 选择状态-待审批
put_bill_manage_part_unit_type_select_approval=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 选择状态-待入库
put_bill_manage_part_unit_type_select_put=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(2)"
# 选择状态-入库完成
put_bill_manage_part_unit_type_select_finish_put=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(4)"
# 点击查询
# 点击审批

# 点击入库
# 点击执行
put_bill_manage_excute_button=By.CSS_SELECTOR,".detail_detailContainer__3um4P > div:nth-child(7) > button:nth-child(2)"
# 点击查看
put_bill_manage_watch_button=By.CSS_SELECTOR,"tr.ant-table-row:nth-child(1) > td:nth-child(9) > div:nth-child(1) > button:nth-child(5)"


"""
    出库管理→报废单管理→我的报废单新增
"""
# 点击出库管理
out_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(3)>ul>li:nth-child(2)"
# 点击报废单管理
scrap_bill_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(3)>ul>li:nth-child(2)>ul>li:nth-child(1)"
# 点击我的报废单
mind_scrap_bill_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(3)>ul>li:nth-child(2)>ul>li:nth-child(1)>ul>li:nth-child(1)"
# 点击新增
public_scrap_bill_insert_click=By.CSS_SELECTOR,".style_titleGroup__3gG29 > div:nth-child(2) > button:nth-child(1)"
# 输入报废单名称(公有)
# 点击类型
public_scrap_bill_type_click=By.CSS_SELECTOR,".ant-select-selection"
# 选择类型
public_scrap_bill_type_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 输入申请理由(公有)
# 点击添加备件清单
public_scrap_bill_insert_part_bill_click=By.CSS_SELECTOR,".ant-btn-dashed"
# 点击选择备件型号icon
public_scrap_bill_insert_part_bill_icon=By.CSS_SELECTOR,".anticon-setting"
# 点击选择备件型号radio(公有)
# 点击确定(公有)
# 输入备件数量(公有)
# 点击保存
public_scrap_bill_insert_save_button=By.CSS_SELECTOR,"button.ant-btn:nth-child(2)"
# 点击待审批报废单
wait_approval_scrap_bill_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(3)>ul>li:nth-child(2)>ul>li:nth-child(1)>ul>li:nth-child(2)"
# 输入报废单名称
# 点击状态
# 选择状态
# 点击查询
# 点击审批
# 输入审批意见
public_scrap_bill_approval_device_input=By.CSS_SELECTOR,"#auditOpinion"
# 点击通过
public_scrap_bill_approval_through_button=By.CSS_SELECTOR,"button.ant-btn-primary:nth-child(2)"
# 点击报废管理
scrap_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(3)>ul>li:nth-child(2)>ul>li:nth-child(1)>ul>li:nth-child(3)"
# 点击新增
# 输入报废单名称
# 点击类型
# 选择类型
# 输入申请理由
# 点击添加备件清单
# 点击选择备件型号icon
# 点击选择备件型号radio
# 点击确定
# 输入备件数量
# 点击保存
# 输入报废单名称
# 点击状态
# 选择状态
# 点击审批
# 输入审批意见
# 点击通过
scrap_manage_through_button=By.CSS_SELECTOR,"form.ant-form:nth-child(8) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > button:nth-child(2)"








"""
    养护作业管理→养护职责管理→养护小组管理新增
"""
# 点击养护作业管理
curing_work_manage_click=By.CSS_SELECTOR,"li.ant-menu-submenu:nth-child(4) > div:nth-child(1) > span:nth-child(1) > span:nth-child(2)"
# 点击养护职责管理
curing_duty_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(4)>ul>li:first-child"
# 点击养护小组管理
curing_team_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(4)>ul>li>ul>li:first-child"
# 点击新增(公有)
curing_team_manage_insert_click=By.CSS_SELECTOR,".style_btnGroup__1StZF > button:nth-child(1)"
# 输入小组名称(公有)
# 输入描述(公有)
# 点击小组成员新增
curing_team_manage_member_insert_button=By.CSS_SELECTOR,".style_btnGroup__1StZF > button:nth-child(1)"
# 选择人员
curing_team_manage_member_insert_checkbox_select=By.CSS_SELECTOR,"div.style_tableGroup__dOEj2:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > thead:nth-child(2) > tr:nth-child(1) > th:nth-child(1) > span:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)"
# 点击确定
curing_team_manage_member_insert_checkbox_sure_button=By.CSS_SELECTOR,".ant-modal-footer > div:nth-child(1) > button:nth-child(2)"
# 设为队长
curing_team_manage_member_appoint_header_click=By.CSS_SELECTOR,"div.style_tableGroup__dOEj2:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child(1) > td:nth-child(4) > button:nth-child(1)"
# 点击保存
curing_team_manage_member_save_button=By.CSS_SELECTOR,".style_rightAlign__U_IVA > button:nth-child(1)"
"""
    养护小组管理查询
"""
# 输入小组名称(公有)
# 输入队长用户名(公有)
# 输入队长姓名(公有)
# 点击查询(公有)

"""
    养护小组管理编辑
"""
# 点击编辑按钮(公有2列)
"""
    养护小组管理重置
"""
# 点击重置按钮(公有)

"""
    养护小组查看
"""
# 点击查看按钮(公有1列)


"""
    养护结论管理新增
"""
# 点击养护结论管理
curing_inference_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(4)>ul>li>ul>li:nth-child(2)"
# 点击新增
curing_inference_manage_insert_click=By.CSS_SELECTOR,".style_btnGroup__NgT53 > button:nth-child(1)"
# 输入结论名称(公有)
# 点击结果标记
curing_inference_manage_insert_remark_click=By.CSS_SELECTOR,".ant-select-selection__rendered"
# 选择结果标记
curing_inference_manage_insert_remark_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 输入描述(公有)
# 点击保存(公有)

"""
    养护结论管理查询
"""
# 输入结论名称(公有)
# 输入创建人(公有)
# 点击查询(公有)

"""
    养护结论管理重置
"""
# 点击重置(公有)
"""
    养护结论管理编辑
"""
# 点击编辑(公有)



"""
    养护要求管理新增
"""

# 点击养护要求管理
curing_request_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(4)>ul>li>ul>li:nth-child(3)"
# 点击新增
curing_request_manage_insert_click=By.CSS_SELECTOR,".style_btnGroup__3lwLK > button:nth-child(1)"
# 输入养护要求名称(公有)
# 选择是否必须
curing_request_manage_select_if_must=By.CSS_SELECTOR,"label.ant-radio-wrapper:nth-child(1) > span:nth-child(1) > input:nth-child(1)"
# 点击养护结论
curing_request_manage_curing_inference_click=By.CSS_SELECTOR,".ant-select-selection__rendered"
# 选择养护结论
curing_request_manage_curing_inference_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 输入操作方法(公有)
# 点击保存(公有)

"""
    养护要求管理查询
"""
# 输入名称(公有)
# 输入创建人(公有)
# 点击查询(公有)
"""
    养护要求管理编辑
"""
# 点击编辑(公有)


"""
    养护项目管理新增
"""
# 点击养护项目管理
curing_item_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(4)>ul>li>ul>li:nth-child(4)"
# 点击养护项目管理新增
curing_item_manage_insert_click=By.CSS_SELECTOR,".style_btnGroup__1_6Qo > button:nth-child(1)"

# 点击部件icon
curing_item_manage_insert_units_icon_click=By.CSS_SELECTOR,".anticon-setting"
# 选择部件(公有单选)
# 点击确定(公有)
# 输入项目名称(公有)
# 输入最大保养周期(公有)
# 点击最大保养周期单位
curing_item_manage_insert_max_unit_click=By.CSS_SELECTOR,"#requiredMaximumMaintenancePeriodUnit > div:nth-child(1)"
# 选择最大保养周期单位
curing_item_manage_insert_max_unit_select=By.CSS_SELECTOR,"body>div:last-child>div>div>div>ul>li:first-child"
# 输入建议保养周期(公有)
# 点击建议保养周期单位
curing_item_manage_insert_offer_unit_click=By.CSS_SELECTOR,"#recommendedMaintenancePeriodUnit > div:nth-child(1)"
# 选择建议保养周期单位
curing_item_manage_insert_offer_unit_select=By.CSS_SELECTOR,"body>div:nth-of-type(4)>div>div>div>ul>li:first-child"
# 输入位置描述(公有)
# 输入备注(公有)
# 点击保存(公有)
"""
    养护项目管理查询
"""
# 输入养护项目名称(公有)
# 点击查询(公有)
"""
    养护项目管理查看
"""
# 点击查看(公有)
"""
    养护项目管理编辑
"""
# 点击编辑(公有)


"""
    养护职责模板管理新增
"""
# 点击养护职责模板管理
curing_duty_cls_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(4)>ul>li>ul>li:nth-child(5)"
# 点击新增
curing_duty_cls_manage_insert_click=By.CSS_SELECTOR,".style_btnGroup__1wQXj > button:nth-child(1)"

# 输入职责模板名称(公有)

# 点击养护等级
curing_duty_cls_manage_insert_curing_order_click=By.CSS_SELECTOR,".ant-select-selection--single"
# 选择养护等级
curing_duty_cls_manage_insert_curing_order_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 点击部件型号icon
curing_duty_cls_manage_insert_repair_type_icon_click=By.CSS_SELECTOR,".anticon-setting"
# 选择部件型号radio(公有)
# 点击确定(公有)
# 点击养护要求
curing_duty_cls_manage_insert_curing_request_click=By.CSS_SELECTOR,".ant-select-selection--multiple > div:nth-child(1)"
# 选择养护要求
curing_duty_cls_manage_insert_curing_request_select=By.CSS_SELECTOR,".ant-select-dropdown-menu-item-active"
# 点击保存(公有)

"""
    养护职责模板管理查询
"""
# 输入模板名称(公有)
# 点击查询(公有)

"""
    养护职责模板管理编辑
"""
# 点击编辑(公有)

"""
    养殖职责模板管理重置
"""
# 点击重置(公有)

"""
    养护职责模板管理查看
"""
# 点击查看(公有)



"""
    养护职责管理(子)新增
"""
# 点击养护职责管理(子)
curing_duty_son_manage=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(4)>ul>li>ul>li:nth-child(6)"
# 点击新增
curing_duty_son_insert_manage=By.CSS_SELECTOR,".style_btnGroup__Dd_gV > button:nth-child(1)"
# 点击养护项目icon
curing_duty_son_insert_curing_item_icon_click=By.CSS_SELECTOR,".anticon-setting"
# 选择养护项目radio(公有)
# 点击确定(公有)
# 点击养护等级
curing_duty_son_insert_curing_order_click=By.CSS_SELECTOR,"div.ant-select-selection"
# curing_duty_son_insert_curing_order_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 输入养护名称(公有)
# 点击下一步
curing_duty_son_insert_next_click=By.CSS_SELECTOR,"button.ant-btn:nth-child(6)"
# 取消新增的职责模板
curing_duty_son_insert_duty_xls_remove_icon_click=By.CSS_SELECTOR,"i.anticon:nth-child(5) > svg:nth-child(1)"
# 点击选择职责模板
curing_duty_son_insert_duty_xls_click=By.CSS_SELECTOR,"div.ant-row:nth-child(4) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > button:nth-child(1)"
# 选择职责模板radio(公有)
# 点击确定(公有)
# 点击完成
curing_duty_son_insert_finish_button=By.CSS_SELECTOR,"button.ant-btn:nth-child(2)"
"""
    养护职责管理(子)查询
"""
# 输入职责名称(公有)
# 点击查询(公有)

"""
    养护职责管理(子)编辑
"""
# 点击编辑(公有)

"""
    养护职责管理(子)重置
"""
# 点击重置(公有)

"""
    养护职责管理(子)查看
"""
# 点击查看(公有)

# 网页回退




"""
    养护计划管理新增
"""
# 点击养护计划管理
curing_plan_manage_click=By.CSS_SELECTOR,"#root>section>aside>div>div>ul>li>ul>li:nth-child(4)>ul>li:nth-child(2)"
# 点击新增
curing_plan_manage_insert_click=By.CSS_SELECTOR,".style_btnGroup__1m2HV > button:nth-child(1)"
# 输入养护计划名称(公有)
# 点击执行等级
curing_plan_manage_insert_excute_order_click=By.CSS_SELECTOR,"#level > div:nth-child(1)"
# 选择执行等级
curing_plan_manage_insert_excute_order_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 点击选择时间
curing_plan_manage_insert_time_click=By.CSS_SELECTOR,"span.ant-calendar-picker-input"
# 选择前半部分时间
curing_plan_manage_insert_time_befor_select=By.CSS_SELECTOR,".ant-calendar-today > div:nth-child(1)"
# 选择后半部分时间
curing_plan_manage_insert_time_after_select=By.CSS_SELECTOR,"td.ant-calendar-last-day-of-month:nth-child(2) > div:nth-child(1)"
# 点击下次生成时间
curing_plan_manage_insert_next_create_time_click=By.CSS_SELECTOR,"input.ant-calendar-picker-input"
# 选择下次生成时间
curing_plan_manage_insert_next_create_time_select=By.CSS_SELECTOR,".ant-calendar-today-btn"
# 点击是否自动审核(否)
curing_plan_manage_insert_if_auto_audit_click=By.CSS_SELECTOR,"label.ant-radio-wrapper:nth-child(2) > span:nth-child(1) > input:nth-child(1)"
# 输入保养周期(公有)
# 点击保养周期单位
curing_plan_manage_insert_if_service_cycle_unit_click=By.CSS_SELECTOR,"#unit > div:nth-child(1)"
# 选择保养周期单位
curing_plan_manage_insert_if_service_cycle_unit_select=By.CSS_SELECTOR,".ant-select-dropdown-menu-item-active"
# 输入执行内容(公有)
# 输入备注(公有)
# 点击下一步
curing_plan_manage_insert_next_click=By.CSS_SELECTOR,"button.ant-btn:nth-child(10)"
# 点击添加一条职责
curing_plan_manage_insert_one_duty_click=By.CSS_SELECTOR,".ant-btn-dashed"
# 点击养护职责icon
curing_plan_manage_insert_curing_duty_icon_click=By.CSS_SELECTOR,".style_itemGroup__108TA > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > span:nth-child(2) > i:nth-child(1)"
# 选择养护职责radio(公有)
# 点击确定(公有)
# 输入工作内容名称
curing_plan_manage_insert_work_content_name_input=By.CSS_SELECTOR,"#planAndDutyName\[c82ee4e9-6d10-45cf-8777-f996a44fa06a\]"
# 点击养护小组/养护人
curing_plan_manage_insert_curing_team_click=By.CSS_SELECTOR,"div.ant-select-selection"
# 选择养护小组/养护人
curing_plan_manage_insert_curing_team_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 点击选择人员icon
curing_plan_manage_insert_member_icon_click=By.CSS_SELECTOR,"div.ant-row:nth-child(6) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > span:nth-child(2) > i:nth-child(1)"
# 选择人员radio(公有)
# 点击确定(公有)
# 点击完成
curing_plan_manage_insert_finish_click=By.CSS_SELECTOR,"button.ant-btn:nth-child(3)"
"""
    养护计划管理查询
"""
# 输入计划名称(公有)
# 点击状态(公有)
# 选择状态(公有)
# 点击查询(公有)

"""
    养护计划管理重置
"""
# 点击重置(公有)
"""
    养护计划管理查看
"""
# 点击查看(公有)

"""
    养护计划管理编辑
"""
# 点击编辑(公有)

"""
    养护计划禁用
"""
# 点击禁用与启用(公有)

"""
    养护计划延时
"""
# 点击延时(公有)
# 延时天数(公有)
# 确定(公有)





"""
    企业信息列表新增
"""
# 点击通讯录管理
address_manage_click=By.CSS_SELECTOR,"li.ant-menu-submenu:nth-child(6) > div:nth-child(1)"
# 点击企业信息列表
firm_infor_manage_click=By.CSS_SELECTOR,"li.ant-menu-submenu:nth-child(6) > ul>li:nth-child(1)"

# 点击新增
firm_infor_manage_insert_click=By.CSS_SELECTOR,".style_titleGroup__3gG29 > div:nth-child(2) > button:nth-child(1)"
# 输入企业名称
public_firm_infor_manage_insert_firm_name_input=By.ID,"name"
# 点击企业类型
public_firm_infor_manage_insert_firm_type_click=By.CSS_SELECTOR,".ant-select-selection"
# 选择企业类型
public_firm_infor_manage_insert_firm_type_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 输入负责人
public_firm_infor_manage_insert_charge_name_input=By.ID,"chargeName"
# 输入联系人
public_firm_infor_manage_insert_link_name_input=By.ID,"linkName"
# 输入联系电话
public_firm_infor_manage_insert_link_phone_input=By.ID,"linkPhone"
# 输入座机电话
public_firm_infor_manage_insert_tele_phone_input=By.ID,"telephone"
# 输入邮箱
public_firm_infor_manage_insert_email_input=By.ID,"email"
# 输入地址
public_firm_infor_manage_insert_site_input=By.ID,"email"

# 点击保存
public_firm_infor_manage_insert_save_button=By.CSS_SELECTOR,"button.ant-btn:nth-child(2)"
"""
    企业信息列表查询
"""
# 选择厂家类型
# 输入厂家名称
# 输入负责人
# 输入联系人
# 点击查询
# 点击编辑
# 点击查看





















"""
    我的学习资料新增、查看、重置、编辑→学习资料审批查询、审批、查看、重置
"""
"""
    我的学习资料新增
"""
# 点击资料档案管理
file_manage_click=By.CSS_SELECTOR,'li.ant-menu-submenu:nth-child(7) > div:nth-child(1) > span:nth-child(1) > span:nth-child(2)'
# 点击学习资料管理
study_data_manage_click=By.CSS_SELECTOR,'#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(7)>ul>li:first-child>div'
# 点击我的学习资料
mine_study_data_click=By.CSS_SELECTOR,'#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(7)>ul>li:first-child>ul>li:nth-child(3)'
# 点击新增(公有)
# 输入名称
mine_study_data_insert_name_input=By.CSS_SELECTOR,".ant-form-horizontal > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > input:nth-child(1)"
# 输入描述
mine_study_data_insert_desc_input=By.CSS_SELECTOR,"textarea.ant-input"
# 点击上传按钮
mine_study_data_upload_file_button=By.CSS_SELECTOR,"span.ant-upload > button:nth-child(2)"
# 点击保存
mine_study_data_insert_save_button=By.CSS_SELECTOR,".ant-col-xs-offset-0 > div:nth-child(1) > span:nth-child(1) > button:nth-child(2)"

"""
    我的学习资料查询
"""
# 输入名称(公有)
# 输入描述(公有)
# 点击状态(公有)
# 选择状态(公有)
# 点击查询(公有)

"""
    我的学习资料重置
"""
# 点击重置(公有)

"""
    我的学习资料编辑
"""
# 点击编辑(公有)

# 点击查看(公有)

"""
    学习资料审批查询
"""
# 点击学习资料审批
study_data_approval_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(7)>ul>li:first-child>ul>li:nth-child(4)"
# 输入名称(公有)
# 输入描述(公有)
# 点击状态(公有)
# 选择状态(公有)
# 点击查询(公有)
# 点击审批(公有)

"""
    学习资料重置
"""
# 点击重置(公有)

"""
    学习资料查看
"""
# 点击查看(公有)

"""
    学习资料列表查询
"""
# 点击学习资料列表
study_data_list_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(7)>ul>li:first-child>ul>li:nth-child(1)"
# 输入名称(公有)
# 输入描述(公有)
# 点击查询(公有)
"""
    学习资料重置
"""
# 点击重置(公有)

"""
    学习资料查看
"""
# 点击查看(公有)

"""
    学习资料管理(子)新增
"""
# 点击学习资料管理(子)模块
study_data_manage_son_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(7)>ul>li:first-child>ul>li:nth-child(2)"
# 点击新增
study_data_manage_son_insert_click=By.CSS_SELECTOR,".style_titleGroup__3gG29 > div:nth-child(2) > button:nth-child(1)"
# 输入名称
study_data_manage_son_insert_name_input=By.CSS_SELECTOR,".ant-form-horizontal > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > input:nth-child(1)"
# 输入描述
study_data_manage_son_insert_desc_input=By.CSS_SELECTOR,"textarea.ant-input"
# 点击上传附件按钮
study_data_manage_son_updata_click=By.CSS_SELECTOR,"span.ant-upload > button:nth-child(2)"
# 点击保存
study_data_manage_son_save_button=By.CSS_SELECTOR,".ant-col-xs-offset-0 > div:nth-child(1) > span:nth-child(1) > button:nth-child(2)"
"""
    学习资料管理(子)查询
"""
# 输入名称(公有)
# 输入描述(公有)
# 点击状态(公有)
# 选择状态(公有)
# 点击查询(公有)
"""
    学习资料管理(子)编辑
"""
# 点击编辑(公有)
"""
    学习资料管理(子)审批
"""
# 点击审批(公有)

"""
    学习资料管理(子)查看
"""
# 点击查看(公有)
"""
    学习资料管理(子)重置
"""




"""
    我的档案、查看、重置、编辑→档案审批查询、审批、查看、重置
"""
"""
    我的档案新增
"""
# 点击档案管理
record_manage_click=By.CSS_SELECTOR,'#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(7)>ul>li:nth-child(2)>div'
# 点击我的档案
mine_record_click=By.CSS_SELECTOR,'#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(7)>ul>li:nth-child(2)>ul>li:nth-child(3)'
# 点击新增(公有)
# 输入名称
mine_record_insert_name_input=By.CSS_SELECTOR,".ant-form-horizontal > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > input:nth-child(1)"
# 输入描述
mine_record_insert_desc_input=By.CSS_SELECTOR,"textarea.ant-input"
# 点击上传按钮
mine_recorda_upload_file_button=By.CSS_SELECTOR,"span.ant-upload > button:nth-child(2)"
# 点击保存
mine_record_insert_save_button=By.CSS_SELECTOR,".ant-col-xs-offset-0 > div:nth-child(1) > span:nth-child(1) > button:nth-child(2)"

"""
    我的档案查询
"""
# 输入名称(公有)
# 输入描述(公有)
# 点击状态(公有)
# 选择状态(公有)
# 点击查询(公有)

"""
    我的档案重置
"""
# 点击重置(公有)

"""
    我的档案编辑
"""
# 点击编辑(公有)

# 点击查看(公有)

"""
    档案审批查询
"""
# 点击档案审批
record_approval_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(7)>ul>li:nth-child(2)>ul>li:nth-child(4)"
# 输入名称(公有)
# 输入描述(公有)
# 点击状态(公有)
# 选择状态(公有)
# 点击查询(公有)
# 点击审批(公有)

"""
    档案审批重置
"""
# 点击重置(公有)

"""
    档案审批查看
"""
# 点击查看(公有)

"""
    档案列表查询
"""
# 点击档案列表
record_list_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(7)>ul>li:nth-child(2)>ul>li:nth-child(4)"
# 输入名称(公有)
# 输入描述(公有)
# 点击查询(公有)
"""
    档案列表重置
"""
# 点击重置(公有)

"""
    档案列表查看
"""
# 点击查看(公有)

"""
    档案管理(子)新增
"""
# 点击档案管理(子)模块
record_manage_son_click=By.CSS_SELECTOR,"#root>section>aside>div>div:nth-child(2)>ul>li>ul>li:nth-child(7)>ul>li:nth-child(2)>ul>li:nth-child(2)"
# 点击新增
record_manage_son_insert_click=By.CSS_SELECTOR,".style_titleGroup__3gG29 > div:nth-child(2) > button:nth-child(1)"
# 输入名称
record_manage_son_insert_name_input=By.CSS_SELECTOR,".ant-form-horizontal > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > input:nth-child(1)"
# 输入描述
record_manage_son_insert_desc_input=By.CSS_SELECTOR,"textarea.ant-input"
# 点击上传附件按钮
record_manage_son_updata_click=By.CSS_SELECTOR,"span.ant-upload > button:nth-child(2)"
# 点击保存
record_manage_son_save_button=By.CSS_SELECTOR,".ant-col-xs-offset-0 > div:nth-child(1) > span:nth-child(1) > button:nth-child(2)"
"""
    档案管理(子)查询
"""
# 输入名称(公有)
# 输入描述(公有)
# 点击状态(公有)
# 选择状态(公有)
# 点击查询(公有)
"""
    档案管理(子)编辑
"""
# 点击编辑(公有)
"""
    档案管理(子)审批
"""
# 点击审批(公有)

"""
    档案管理(子)查看
"""
# 点击查看(公有)
"""
   档案管理(子)重置
"""


























"""
    点击app公告管理
"""
# 点击app公告管理

app_notice_manage_click=By.CSS_SELECTOR,"li.ant-menu-item:nth-child(8) > span:nth-child(2)"
"""
    app公告管理新增
"""
# 点击新增(公有)
app_notice_manage_insert_click=By.CSS_SELECTOR,".style_btnGroup__1B5uf > button:nth-child(1)"
# 输入公告标题(公有)

# 输入公告内容(公有)

# 点击公告类型
app_notice_manage_insert_type_click=By.CSS_SELECTOR,"div.ant-row:nth-child(3) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1)"
# 选择公告类型
app_notice_manage_insert_type_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 点击确定(公有)
"""
    app公告管理查询
"""
# 点击类型
app_notice_manage_search_type_click=By.CSS_SELECTOR,".ant-select-selection"
# 选择类型
app_notice_manage_search_type_select=By.CSS_SELECTOR,"li.ant-select-dropdown-menu-item:nth-child(1)"
# 点击查询(公有)
"""
    app公告管理重置
"""
# 点击重置(公有)












# # 点击仓储管理
# warehouse_manage_click_button = By.CSS_SELECTOR, "li.ant-menu-submenu-open:nth-child(2) > div:nth-child(1) > span:nth-child(1) > span:nth-child(2)"
# # 点击入库管理
# storage_manage_click_button = By.CSS_SELECTOR, "li.ant-menu-submenu-open:nth-child(2)>ul>li:first-child"
# # 点击我的入库单
# mind_storage_bill_click_button = By.CSS_SELECTOR, "li.ant-menu-item:nth-child(1) > span"
#
# # 仓储管理→入库管理→我的入库单查询(公有)
#
# # 仓储管理→入库管理→我的入库单新增
# mind_storage_bill_insert_type_click = By.CSS_SELECTOR, ".ant-select-selection"
# mind_storage_bill_insert_type_select = By.CSS_SELECTOR, "li.ant-select-dropdown-menu-item:nth-child(1)"
# mind_storage_bill_insert_commpont_bill_click = By.CSS_SELECTOR, ".ant-btn-dashed"
# mind_storage_bill_insert_commpont_bill_icon = ".anticon-setting"
# mind_storage_bill_insert_save = By.CSS_SELECTOR, ".ant-col-xs-offset-0 > div:nth-child(1) > span:nth-child(1) > button:last-child"
#
# # 仓储管理→点击待审批入库单
# wait_approval_storage_bill_button = By.CSS_SELECTOR, "li.ant-menu-item:nth-child(2) > span"
#
# # 仓储管理→待审批入库单查询(公有)
#
# # 仓储管理→待审批入库单审批
# wait_approval_storage_bill_approval_button = By.CSS_SELECTOR, "button.ant-btn-link:nth-child(1)"
# wait_approval_storage_bill_approval_through_button = By.CSS_SELECTOR, "button.ant-btn-primary:nth-child(2)"
#
# # 仓储管理→待审批入库单入库
# wait_approval_storage_bill_put_button = By.CSS_SELECTOR, "button.ant-btn-link:nth-child(1)"
# wait_approval_storage_bill_excute_button = By.CSS_SELECTOR, "button.ant-btn-primary:nth-child(2)"
#
#
# # 仓储管理→点击出库管理
# put_manage_click_button=By.CSS_SELECTOR, ""
# # 仓储管理→点击报废单管理
# mind_scrap_bill_click_button=By.CSS_SELECTOR, ""
