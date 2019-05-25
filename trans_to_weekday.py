def trans_to_weekdays(date):

# 已知2019.1.1是周二
# 年数变化后，需要修改下面的A
    b = {
        '0': '周一',
        '1': '周二',
        '2': '周三',
        '3': '周四',
        '4': '周五',
        '5': '周六',
        '6': '周日',
        }

    year = int(date.split('.')[0])

    month = int(date.split('.')[1])

    day = int(date.split('.')[2])

    list1 = [31,28,31,30,31,30,31,31,30,31,30,31] #平年月份天数
    list2 = [31,29,31,30,31,30,31,31,30,31,30,31] #闰年月份天数

    sum_day = 0

    if is_runnian(year):

        for i in range(month-1):

            sum_day += list2[i]
        sum_day += day

    else:
        for i in range(month-1):

            sum_day += list1[i]
        sum_day += day

    number = str((sum_day % 7))

    return b[number]


def is_runnian(year):

    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False
