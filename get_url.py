from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from lxml import etree
from selenium.webdriver.chrome.service import Service
import time

global A
global xingqi


# 获取urls列表
def get_urls(xingqi,A):

    #由于在后台打开浏览器，因此不能很好的关闭，所以用service.start(),service.close()控制进程开关
    c_service = Service('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    c_service.command_line_args()
    c_service.start()
    #使用谷歌自带的无头浏览器模式，悄无声息地运行
    opt =Options()
    opt.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options = opt)
    wait = WebDriverWait(browser, 10) #设置延迟10秒，等待网页加载
    #
    browser.get('http://www.qqshidao.com/index.php?c=home&a=bifen')
    time.sleep(3)
    submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[6]/div/span[6]')))
    submit.click()
    time.sleep(2)
    js = 'var q=document.documentElement.scrollTop=100000' #设置往下拉网页的长度,设置大点，直接拉到底部
    browser.execute_script(js)  #发现当比赛较多时，往下拉一下后加载新的数据，因此，自动往下拉一下就停了
    time.sleep(1)
    browser.execute_script(js)  #再往下拉一下，加载全部比赛
    time.sleep(2)

    yuanma = browser.page_source

    browser.quit()
    c_service.stop()

    s = etree.HTML(yuanma)
    urls = []
    urls_ =  s.xpath('//*[@id="app"]/div[7]/div/table/tbody/tr[@data-fid]')
    for each in urls_:
        fid = each.attrib['data-fid']

        xingqiji = each.xpath('./td[3]/text()')[0]

        if xingqi in xingqiji:
            url = 'http://www.qqshidao.com/index.php?c=odds&a=betfair&fid={}'.format(fid)
            A['{}'.format(url)] = xingqiji
            urls.append(url)

    return urls
