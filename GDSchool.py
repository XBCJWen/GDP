import sys

import requests
from fake_useragent import UserAgent
from pyquery import PyQuery as pq
from school_api.check_code import CHECK_CODE


class GDSchool(object):
    def __init__(self):
        ua=UserAgent()
        self.headers={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Language':'Accept-Language',
            'Host':'61.142.209.20:9090',
            'Accept-Encoding':'gzip, deflate',
            'UserAgent':ua.random
                      }
        self.number=input('请输入学号:')
        self.password=input('请输入密码:')

    def main(self):
        self.rssions=requests.session()
        url='http://61.142.209.20:9090'
        self.rssions.get(url=url)
        url_login='http://61.142.209.20:9090/default2.aspx'
        par=self.response_data()
        code=self.resonse_image()
        data={
            '__VIEWSTATE':par['VIEWSTATE'],
            '__EVENTVALIDATION':par['EVENTVALIDATION'],
            'TextBox1':self.number,
            'TextBox2':self.password,
            'TextBox3':code,
            'RadioButtonList1':'(unable to decode value)',
            'Button1':''
        }
        log_response=self.rssions.post(url=url_login,headers=self.headers,data=data)
        print(log_response)

    def resonse_image(self):
        try:
            response=self.rssions.get('http://61.142.209.20:9090/CheckCode.aspx',stream=True)
            code=CHECK_CODE.verify(response.content)
            # with open(code+'.gif','wb') as fp:
            #     fp.write(response.content)
            return code
        except Exception as e:
            print(e)

    def response_data(self):
        try:
            response=requests.get('http://61.142.209.20:9090')
            html=pq(response.text)
            VIEWSTATE=html('#form1 #__VIEWSTATE').attr('value')
            EVENTVALIDATION=html('#form1 #__EVENTVALIDATION').attr('value')
            return {'VIEWSTATE':VIEWSTATE,'EVENTVALIDATION':EVENTVALIDATION}
        except Exception as e:
            print(e)


if __name__ == '__main__':
    gd=GDSchool()
    gd.main()