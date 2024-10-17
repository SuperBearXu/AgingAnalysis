from datetime import datetime

import openpyxl
import pandas as pd
from openpyxl.styles import Alignment, PatternFill, Border, Side

from global_setting import GS
from gui.logic.import_data_dialog_logic import global_temp_data
from utils.my_logger import my_logger as logger
from utils.my_utils import data_frame_add_title, open_file, check_file_exists, get_time_now


def calculate_aging(data):
    enterprise = data['企业']
    origin_value = data['初始值']
    debit_credit = data['借贷']

    n = 1
    list_debit = [origin_value]
    sum_credit = 0

    for dc in debit_credit:
        debit = dc[0]
        credit = dc[1]
        list_debit.append(debit)
        sum_credit += int(credit)

    for i in range(len(list_debit)):
        result = int(list_debit[i]) - sum_credit
        if result > 0:
            list_debit[i] = str(result)
            sum_credit = 0
            break
        elif result < 0:
            if i == len(list_debit) - 1:
                list_debit[i] = str(result)
                break
            sum_credit = sum_credit - int(list_debit[i])
            list_debit[i] = '0'
        else:
            list_debit[i] = '0'
            break

    last_list = list(reversed(list_debit))
    logger.debug(f"{enterprise} 最终分析结果为：{last_list}")

    excel_list = []
    over_three_sum = 0
    for i in range(len(last_list)):
        if i > 2:
            over_three_sum += int(last_list[i])
            continue
        excel_list.append(last_list[i])
    len_last_list = len(last_list)
    while True:
        if len(last_list) < 3:
            excel_list.append('-')
            last_list.append('-')
        elif len(last_list) >= 3 > len_last_list:
            excel_list.append('-')
            break
        elif len(last_list) >= 3:
            excel_list.append(str(over_three_sum))
            break
    # logger.info(f"{enterprise} 最终Excel导出结果为：{excel_list}")
    # sum_excel_row = sum(map(int, excel_list))
    # 过滤并转换列表中的元素
    # print("excel_list", excel_list)
    valid_numbers = [int(num) if num.replace('-', '', 1).isdigit() else 0 for num in excel_list]
    # print("valid_numbers", valid_numbers)
    # 计算和
    sum_excel_row = sum(valid_numbers)
    # print("sum_excel_row", sum_excel_row)
    excel_list.append(str(sum_excel_row))
    excel_list.insert(0, enterprise)
    # logger.info(f"{enterprise} 返回结果为：{excel_list}")
    return excel_list


def data_to_excel(data):
    enterprise_list = []
    one_years_list = []
    two_years_list = []
    three_years_list = []
    over_three_list = []
    sum_list = []

    for d in data:
        enterprise_list.append(d[0])
        one_years_list.append(d[1])
        two_years_list.append(d[2])
        three_years_list.append(d[3])
        over_three_list.append(d[4])
        sum_list.append(d[5])

    last_enterprise = "合计"
    last_one_years = sum(map(int, one_years_list))
    last_two_years = sum(map(int, two_years_list))
    last_three_years = sum(map(int, three_years_list))
    last_over_three = sum(map(int, over_three_list))
    last_sum = sum(map(int, sum_list))

    enterprise_list.append(last_enterprise)
    one_years_list.append(last_one_years)
    two_years_list.append(last_two_years)
    three_years_list.append(last_three_years)
    over_three_list.append(last_over_three)
    sum_list.append(last_sum)

    data_frame = {
        '单位名称': enterprise_list,
        '一年内': one_years_list,
        '1-2年': two_years_list,
        '2-3年': three_years_list,
        '3年及以上': over_three_list,
        '合计': sum_list
    }

    df = pd.DataFrame(data_frame)

    df.to_excel(f'{GS.excel_name}', index=False)
    # 创建一个 ExcelWriter 对象，指定文件名和使用 openpyxl 引擎
    with pd.ExcelWriter(f'{GS.excel_name}', engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

        # 加载生成的工作簿
        workbook = writer.book
        worksheet = workbook['Sheet1']

        excel_name = "应收账款账龄分析表"
        data_frame_add_title(worksheet, excel_name, "A1:F1")

        # 设置样式
        alignment = Alignment(horizontal='center', vertical='center')  # 文本居中

        border = Border(left=Side(border_style='thin'), right=Side(border_style='thin'), top=Side(border_style='thin'), bottom=Side(border_style='thin'))

        for row in worksheet.iter_rows(min_row=2, max_row=len(df) + 2, min_col=1, max_col=len(df.columns)):
            for cell in row:
                cell.alignment = alignment  # 应用居中样式
                cell.border = border  # 应用边框样式


def analysis_data():
    try:
        if len(global_temp_data) == 0:
            logger.info("当前未导入借贷数据，请先添加数据后再次点击！")
            return
        excel_data = []
        for data in global_temp_data:
            excel_data.append(calculate_aging(data))
        now = get_time_now()
        GS.set_excel_name(now)
        data_to_excel(excel_data)
        open_excel()
    except Exception as e:
        logger.error(f"分析失败：{e}")
        return



def open_excel():
    if check_file_exists(GS.excel_name):
        open_file(GS.excel_name)
        return

