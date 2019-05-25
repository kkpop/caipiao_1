
import datetime

# 获取每一个url对应的竞彩数据
def get_eachtime_info(js_data):
    get_eachtime_info_list = []
    js_data_list = []  # json格式内是类似字典类型，直接取键得值
    js_data_list.append(js_data['win'])  # 胜 赔率
    js_data_list.append(js_data['draw'])  # 平 赔率
    js_data_list.append(js_data['lost'])  # 负 赔率
    js_data_list.append(js_data['winamount'])  # 胜 交易总量
    js_data_list.append(js_data['drawamount'])  # 平 交易总量
    js_data_list.append(js_data['lostamount'])  # 负 交易总量
    js_data_list.append(js_data['winyk'])  # 胜 交易盈亏
    js_data_list.append(js_data['drawyk'])  # 平 交易盈亏
    js_data_list.append(js_data['lostyk'])  # 负 交易盈亏
    NowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 当前时间
    js_data_list.append(NowTime)
    get_eachtime_info_list.append(js_data_list)  # 注意:此处如果不另起一个get_eachtime_info_list而只调用
    return get_eachtime_info_list                # js_data_list 的话，保存到csv的数据是一个元素占一行，
