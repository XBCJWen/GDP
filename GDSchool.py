import re
import sys

import requests
from fake_useragent import UserAgent
from pyquery import PyQuery as pq
from school_api.check_code import CHECK_CODE

class GDSchool(object):
    def __init__(self):
        self.ua=UserAgent()
        self.headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Language':'Accept-Language',
            'Host':'61.142.209.20:9090',
            'Accept-Encoding':'gzip, deflate',
            'UserAgent':self.ua.random
                      }
        self.number='1711605038'#input('请输入学号:')
        self.password='44162119980817247X'#input('请输入密码:')

    def responseMenu(self,data): #获取菜单链接
        html=pq(data.text)
        mainItems = {}
        menu=html('#headDiv > ul li').items()
        for subItems in menu:
            sub_nextItems = {}
            for nextItems in  subItems('ul li a').items():
                subList = []
                sub_nextItems[nextItems.text()]=nextItems.attr('href')
                subList.append(sub_nextItems)
            mainItems[subItems('.top_link').text()]=subList
        return mainItems

    def resonseImage(self): #用于获取验证码
        try:
            response=self.rssions.get('http://61.142.209.20:9090/CheckCode.aspx',stream=True)
            code=CHECK_CODE.verify(response.content)
            # with open(code+'.gif','wb') as fp:
            #     fp.write(response.content)
            return code
        except Exception as e:
            print(e)

    def responseData(self): #用于获取登录data参数
        try:
            response=requests.get('http://61.142.209.20:9090')
            html=pq(response.text)
            VIEWSTATE=html('#form1 #__VIEWSTATE').attr('value')
            EVENTVALIDATION=html('#form1 #__EVENTVALIDATION').attr('value')
            return {'VIEWSTATE':VIEWSTATE,'EVENTVALIDATION':EVENTVALIDATION}
        except Exception as e:
            print(e)

    # def parseClassTime(self, classre):  #选择课表信息
    #     classUrl='http://61.142.209.20:9090/'+re.sub(self.name,self.nameCode,classre['信息查询'][0]['个人课表查询'],re.S)
    #     dataParam=self.resonsePara()
    #     # data={
    #     #     '__EVENTTARGET':'xqd',
    #     #     '__EVENTARGUMENT':'',
    #     #     '__LASTFOCUS':'',
    #     #     '__VIEWSTATE':
    #     #     'xnd':'2019-2020',
    #     #     'xqd':'1'
    #     #
    #     # }
    #     #
    #     # reClass=self.rssions.post(url=classUrl,headers=self.headers,data=data)

    def resonsePara(self):  #第一次登录时的初始课表信息
        url='http://61.142.209.20:9090/'+self.menu['信息查询'][0]['个人课表查询']
        referer='http://61.142.209.20:9090/xs_main.aspx?xh={xh}'
        xh=re.findall('xh=(.*?)&xm',url,re.S)[0]
        gnmkdm=re.findall('dm=(.*?)$',url,re.S)[0]
        xm=re.findall(r'xm=(.*?)&gn',url,re.S)[0]
        data={
            'xh':xh,
            'xm':xm,
            'gnmkdm':gnmkdm
        }
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Language': 'Accept-Language',
            'Host': '61.142.209.20:9090',
            'Accept-Encoding': 'gzip, deflate',
            'referer':referer.format(xh=xh),
            'UserAgent': self.ua.random
        }
        reClss=self.rssions.get(url='http://61.142.209.20:9090/xskbcx.aspx?',params=data,headers=headers)
        return  reClss


    def main(self):  #主入口
        self.rssions=requests.session()
        url='http://61.142.209.20:9090'
        self.rssions.get(url=url)
        url_login='http://61.142.209.20:9090/default2.aspx'
        para=self.responseData()
        code=self.resonseImage()
        data={
            '__VIEWSTATE':para['VIEWSTATE'],
            '__EVENTVALIDATION':para['EVENTVALIDATION'],
            'TextBox1':self.number,
            'TextBox2':self.password,
            'TextBox3':code,
            'RadioButtonList1':'(unable to decode value)',
            'Button1':''
        }
        log_response=self.rssions.post(url=url_login,headers=self.headers,data=data)
        self.menu=self.responseMenu(log_response)         #菜单链接
        self.name=re.findall(r'xm=(.*?)&gn',self.menu['信息查询'][0]['个人课表查询'],re.S)[0]
        self.nameCode=self.name.encode('unicode_escape').decode().replace('\\u','%u')
        # self.parseClassTime(self.menu)
        fisrClss=self.resonsePara()
        self.parseFClss(fisrClss)

    def parseFClss(self, data):
        print(data.text)


if __name__ == '__main__':
    gd=GDSchool()
    gd.main()
