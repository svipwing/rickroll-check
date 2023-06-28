import requests

def check(web_page):
    a = requests.get(web_page)
    a = a.text
    #print(a)
    ls = ['never gonna','give you up','so do i','never gonna give you up','never gonna let you down','rick','rickroll','你被骗了','诈骗']
    for i in ls:
        if i in a.lower():
            return '发现诈骗'
    return '没有诈骗'
                                                    
while True:
    t = input('请输入需要鉴定的网址：')
    print(check(t))