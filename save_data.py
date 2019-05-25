import requests
import time
import re
import pandas as pd
import os
from get_data import get_eachtime_info

def save_as_csv(i, urls, A, headers, filename_1,filename_2):
    url = urls[i]
    xingqi_ = A['{}'.format(url)]
    number = re.findall(r'c=odds&a=betfair&fid=(.*)', url)[0]
    #构造urltemp,为了获取比赛的主客队名
    urltemp = 'http://www.qqshidao.com/index.php?c=live&a=fixtureinfo&fid={}'.format(number)

    response1 = requests.get(url, headers=headers)
    response2 = requests.get(urltemp, headers=headers)

    res = response1.json()['data']['jincai']

    hteamname = response2.json()['data']['hteamname']
    ateamname = response2.json()['data']['ateamname']

    paths_1 = './{}/{}{} vs {}.csv'.format(filename_1, xingqi_, hteamname, ateamname)
    paths_2 = './{}/{}/{} vs {}.txt'.format(filename_1,filename_2,hteamname,ateamname)

    if os.path.exists(paths_2) == 0:
        file = open('./{}/{}/{}{} vs {}.txt'.format(filename_1,filename_2,xingqi_,hteamname,ateamname),'w',encoding='utf_8_sig')
        file.write(xingqi_+'{} vs {}'.format(hteamname,ateamname)+','+urltemp)
        file.close()


    if os.path.exists(paths_1) == 0:
        #若文件不存在,DataFrame 添加columns,生成第一行的信息
        df = pd.DataFrame(data=None, columns=['胜赔', '平赔', '负赔', '胜总量', '平总量', '负总量', '胜盈亏', '平盈亏', '负盈亏', '时间'])
        df.to_csv('./{}/{}{} vs {}.csv'.format(filename_1, xingqi_, hteamname, ateamname), index=False,
                  encoding="utf_8_sig")

    eachtime_info = get_eachtime_info(res)
    #使用pandas存储
    df = pd.DataFrame(data=eachtime_info, columns=None)

    df.to_csv('./{}/{}{} vs {}.csv'.format(filename_1, xingqi_, hteamname, ateamname), mode='a', index=False,
              header=False)

    time.sleep(5)
