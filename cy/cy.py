import re
import asyncio
import aiohttp
headers = {"User-Agent": '1'}
headers_ = {"Referer": "http://wx.weather.com.cn", "User-Agent": ''}
def runCy(s):
    def printf(text):
        s.wfile.write(('<p style="color:blue">' + text + '</p>').encode() if "热" in text else ('<p>'+text+'</p>').encode())
    async def cy(zz, url, headers=headers):
        try:
            async with aiohttp.request(method='GET', url=url, headers=headers, timeout=aiohttp.ClientTimeout(total=30)) as z:
                printf(re.sub(r'[ -SU-~]+','-',re.sub(r'\s+', '', re.search(zz,await z.text("utf-8", 'ignore')).group(1)))+'!')
                s.wfile.write('</br>')
        except:
            s.wfile.write('<p style="color:green">' + url + '</p>')
    async def cyu(zz, url):
        try:
            async with aiohttp.request(method='GET', url=url, headers=headers, timeout=aiohttp.ClientTimeout(total=5)) as z:
                printf(re.sub(r'[ -SU-~]+','-',re.search(zz,await z.text()).group(1).encode('utf-8').decode('unicode_escape'))+'!')
                s.wfile.write('</br>')
        except:
            s.wfile.write('<p style="color:green">' + url + '</p>')
    async def cypost(zz, url):
        try:
            async with aiohttp.request(method='POST', url=url, json={"cityId":"284767"}, headers=headers, timeout=aiohttp.ClientTimeout(total=5)) as z:
                printf(re.sub(r'[ -SU-~]+','-',re.search(zz,await z.text()).group(1))+'!')
                s.wfile.write('</br>')
        except:
            s.wfile.write('<p style="color:green">' + url + '</p>')
    url1= "https://www.qweather.com/indices/nangang-101050115.html"
    url2= "https://api.caiyunapp.com/v2/Y2FpeXVuX25vdGlmeQ==/126.631248,45.743664/forecast"
    url3= "http://api.help.bj.cn/apis/life29/?id=101050101"
    url4= "https://weathernew.pae.baidu.com/weathernew/pc?query=%E5%8D%97%E5%B2%97%E5%A4%A9%E6%B0%94&srcid=4982"
    url5= "https://tianqi.2345.com/life/2-71467.htm"
    url6= "https://d1.weather.com.cn/zs_index/101050115.html"
    # url7= "https://m.tianqi.com/chuanyi-nangangqu.html"
    url7_= "https://m.tianqi.com/haerbin/life.html"
    url8= "http://www.yytianqi.com/search/CH050101.html"
    url9= "https://m.baidu.com/sf?county_id=101050115&dspName=iphone&from_sf=1&openapi=1&pd=life_compare_weather&resource_id=4599&word=nangang"
    url10= "https://d1.weather.com.cn/wap_40d/101050115.html"
    url11= "http://nanning.welife100.com/PIndex/getnnIndexdata?areaid=101050115"
    url12= "http://aider.meizu.com/app/weather/listWeather?cityIds=101050101"
    url13= "https://api.msn.cn/weather/overview?apikey=j5i4gDqHL6nGYwx5wi5kRhXjtf2c5qgFX9fzfk0TOo&cuthour=true&feature=lifeday&lifeModes=50&days=1&locale=zh-cn&lat=45.760101318359375&lon=126.66900634765625"
    # url13= "https://www.msn.cn/zh-cn/weather/forecast/in-%E9%BB%91%E9%BE%99%E6%B1%9F%E7%9C%81,%E5%93%88%E5%B0%94%E6%BB%A8%E5%B8%82,%E5%8D%97%E5%B2%97%E5%8C%BA"
    url14= "https://tianqi.so.com/weather/101050115"
    url15= "https://weather.mipang.com/tianqi-20135"
    # url16= "https://www.yangshitianqi.com/haerbin.html"
    url17= "https://v.api.aa1.cn/api/tianqi-zs/index.php?id=101050101"
    url18= "https://cdn.weather.hao.360.cn/sed_api_weather_info.php?code=101050115"
    # url19= "https://h5ctywhr.api.moji.com/indexDetail"
    # :"(.{1,3})","indexType":"穿
    url20= "https://www.69tianqi.com/sight-101050101-haerbin151-60921.html"
    url21= "https://yiketianqi.com/api?version=v1&city=%E5%8D%97%E5%B2%97&appid=85841439&appsecret=EKCDLT4I"
    url22= "https://api.seniverse.com/v3/life/suggestion.json?key=SCYrvkytJze9qyzOh&location=haerbin"
    url23= "https://way.jd.com/he/freeweather?city=CN101050115&appkey=da39dce4f8aa52155677ed8cd23a6470"
    url24= "https://h5ctywhr.api.moji.com/indexMoreDetail"
    url25= "https://you.ctrip.com/weather/haerbin151/5065390.html"
    # url25_= "https://gs.ctrip.com/html5/you/weather/Harbin151/5065390.html"
    url26= "https://www.114369.cn/cri40/tianqi.html"
    # "https://d1.weather.com.cn/weather_index/101050115.html"
    # url6:t_hint":"(.*?)",".._name
    cyhrb=[cy(r'lDress[\s\S]*?-.">([\s\S]*?)<[\s\S]*?</d', url1),cy('sing.*?c":"(.*?)"', url2),cy('衣指数","type":"(.*?)"}', url3),cy(r'数：([\s\S]*?)</dd', url15),cy('sin.*?ary":"(.*?)"', url13),cyu('3: (.*?)"', url4),cy('e">(.*?)<', url5),cy('t_hint":"(.*?)","p', url6, headers_),cy('衣<em>(.*?)</p', url7_),cy(r'>空调[\s\S]*?a >([\s\S]*?)</span>[\s]{2}</l', url8),cy('op">(.*?)<', url9),cy('衣指数","i3":"","i4":"(.*?)","i6', url10, headers_),cyu('02","i3":"","i4":"(.*?)","i6', url11),cy('content":"(.*?)","n', url12),cy('>穿衣指数：(.*?)。">', url14),cy('衣指数","type":"(.*?)"}', url17),cyu(r'i":\["(.*?)"\]', url18),cypost('([^ -~]*.{37}[^ -~]*).{15}穿衣', url24),cy('数：</span>(.*?)<', url20),cyu(r'3\\u6307\\u6570","level":"(.*?)"}', url21),cy('sing":{"brief":"(.*?)"', url22),cy('g":{"brf":"(.*?)"}', url23),cy(r'衣[\s\S]*?g>([\s\S]*?)</p', url25),cy('衣指数：(.*?)</p', url26)]
    # cy('v class="fr">(.*?)</', url16),
    # cy(r'_h">([\s\S]*?)<', url7),
    # asyncio.get_event_loop().run_until_complete(asyncio.wait([asyncio.ensure_future(i) for i in cyhrb]))
    async def runWeatheraios():
        await asyncio.wait([asyncio.ensure_future(i) for i in cyhrb])
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(runWeatheraios())