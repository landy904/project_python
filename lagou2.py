# -*- coding:utf-8 -*-
 
import requests,json,xlwt
kd = 'linux'
items = []
 
def get_content(pn):
    #url和data通过F12查看Network->XHR->Headers->Request URL和Form Data
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    data = {'first':'true',
            'pn':pn,
            'kd':kd}
 
    #url发送一个post请求，把data数据发送过去
    html = requests.post(url,data).text  #获取文本
    html = json.loads(html)  #json格式字符串解码转换成python字典对象
    #print html
 
    for i in range(14):  #每页15项职位
        item = []
        #下面参数通过F12查看Network->XHR->Preview->content->positionResult->result
        item.append(html['content']['positionResult']['result'][i]['positionName'])
        item.append(html['content']['positionResult']['result'][i]['companyFullName'])
        item.append(html['content']['positionResult']['result'][i]['salary'])
        item.append(html['content']['positionResult']['result'][i]['city'])
        item.append(html['content']['positionResult']['result'][i]['positionAdvantage'])
        item.append(html['content']['positionResult']['result'][i]['companyLabelList'])
        item.append(html['content']['positionResult']['result'][i]['firstType'])
        items.append(item)
        #print items
    return items
 
def excel_write(items):
    newTable = 'test.xls'
    wb = xlwt.Workbook(encoding='utf-8')  #创建表格文件
    ws = wb.add_sheet('test1')  #创建表
    headData = ['招聘职位','公司','薪资','地区','福利','提供条件','工作类型']   #定义表格首行信息
    for hd in range(0,7):
        ws.write(0,hd,headData[hd],xlwt.easyxf('font: bold on'))  #0行 hd列
 
    #写数据
    index = 1 #从第二行开始写
    for item in items:
        for i in range(0,7):
            print item[i]
            ws.write(index,i,item[i])
        index +=1
        #print index
        wb.save(newTable)  #保存数据
 
if __name__ == "__main__":
    for pn in range(1,5): #爬取1-5页职位
        items = get_content(pn)
        excel_write(items)