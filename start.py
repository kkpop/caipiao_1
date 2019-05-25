import time
from get_url import get_urls
from create_directory import Create_dir
from remove_useless_url import Remove_useless_url
from save_data import save_as_csv
from trans_to_weekday import trans_to_weekdays
from inquire_score import chaxun_fenshu


#headers 请根据你自己浏览器的配置做更改
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'www.qqshidao.com',
    'Cookie': 'PHPSESSID=rvtklhs6u1fkv9q4066871rbe0; Hm_lvt_1cc6125513403f855d2a2484ef79b3b3=1555830801; Hm_lpvt_1cc6125513403f855d2a2484ef79b3b3=1555830892',
}

'''请在date里修改你当前的日期,示例：'2018.5.23'
做自动填充日期也行，但是会有个问题，例如现在统计14号比赛，但是如果我15号凌晨后重新运行程序，
就会出现统计15号比赛的情况,如果各位有好的办法，请给我留言，感激不尽。。
'''

date = '2018.5.25'
#是否检查完场分数,填写完场分数，只能填写采集过数据的比赛，未在caipiao_*文件夹下有数据的比赛，无法填写完场比分
is_chaxun_fenshu = False

xingqi = trans_to_weekdays(date)
filename_1 = 'caipiao_{}'.format(date)
filename_2 = 'save_inquire_url'
A = dict()
urls_ = get_urls(xingqi, A)
Create_dir(filename_1, filename_2)
if is_chaxun_fenshu:

    chaxun_fenshu(filename_1, filename_2, headers)

else:
    while 1:
        #去掉无用的比赛url
        urls = Remove_useless_url(urls_)
        for i in range(len(urls)):
            #对每场比赛进行数据存储
            save_as_csv(i, urls, A, headers, filename_1, filename_2)

        print('这一轮统计完毕')
        time.sleep(3600) #循环检测，1小时检测一次，也可以添加window定时任务解决，或者挂到服务器上定时运行
