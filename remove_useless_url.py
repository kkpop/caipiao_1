import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'www.qqshidao.com',
    'Cookie': '这里添加你自己的cookie哦，我感觉没有cookie也无所谓'
}

# 去掉没有竞彩数据 或者 比赛已经开始了 的比赛url,这样循环检测时就不会重复更新没必要的比赛数据
def Remove_useless_url(urlss):

    for each in urlss[::-1]:

# 逆序遍历，以确保列表删除元素时不会因为元素下标改变而造成元素遗漏
# 普通顺序遍历会在删除元素时少遍历一个移位的元素
# 也可采用递归调用的方式进行顺序遍历

        fid_ = re.findall(r'c=odds&a=betfair&fid=(.*)', each)[0]

        urlstatus = 'http://www.qqshidao.com/index.php?c=live&a=fixtureinfo&fid={}'.format(fid_)
        response1 = requests.get(each, headers=headers)
        response2 = requests.get(urlstatus, headers=headers)
        rr = response1.json()['data']['jincai'] # 当前比赛若没有竞彩数据，即盘口太深，竞彩不开胜平负时，返回的数据类型为list
        rs = response2.json()['data']['status'] # 获取当前比赛的状态，未开赛时状态为'0'

        if type(rr) == list or rs != '0':
            urlss.remove(each)

    return urlss
