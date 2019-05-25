import os
import requests

def chaxun_fenshu(filename_1, filename_2, headers):
    path = './{}/{}/'.format(filename_1, filename_2)
    file_list = os.listdir(path)
    for each in file_list:
        file = open('./{}/{}/{}'.format(filename_1, filename_2, each), 'r', encoding='utf_8_sig')
        s = file.read().split(',')
        file.close()
        res = requests.get(s[1], headers)
        status = res.json()['data']['status']

        if status == '4':
            hteamname = res.json()['data']['hteamname']
            ateamname = res.json()['data']['ateamname']
            hteam_score = res.json()['data']['hscore']
            ateam_score = res.json()['data']['ascore']
            ahalfscore = res.json()['data']['ahalfscore']
            hhalfscore = res.json()['data']['hhalfscore']
            file_score = open('./{}/{}.csv'.format(filename_1, s[0]), 'a', encoding= 'utf_8_sig')
            score = '{} vs {} 半场比分：{}:{}  最终比分：{}:{}'.format(hteamname, ateamname, hhalfscore, ahalfscore, hteam_score, ateam_score)
            file_score.write(score)
            file_score.close()
