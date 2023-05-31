import asyncio
import aiohttp
import re
headers_ = {"Referer": "http://wx.weather.com.cn", "User-Agent": ''}
headers = {"User-Agent": '1'}
# headers_qq = {"User-Agent": "QQ/8", "Cookie": "uin=o2594508592;skey=M3ILAVr82d"}
def runWeatheraio(s):
    def ff(x, text):
        if float(x) < 17:
            s.wfile.write(('<p style="color:red">' + x + text + '</p>').encode())
        elif float(x) > 20:
            s.wfile.write(('<p style="color:blue">' + x + text + '</p>').encode())
        else:
            s.wfile.write(('<p>'+x + text+'</p>').encode())
    async def f(url, zz, text, headers=headers):
        try:
            async with aiohttp.request(method='GET', url=url, headers=headers, timeout=aiohttp.ClientTimeout(total=5)) as z:
                ff(re.search(zz, await z.text("utf-8", "ignore")).group(1), text)
        except:
            s.wfile.write(('<p style="color:green">' + text + '</p>').encode())
    async def f_(url, zz, text1, text2, a, b, f=1, headers=headers):
        try:
            async with aiohttp.request(method='GET'if f else'POST', url=url, headers=headers, timeout=aiohttp.ClientTimeout(total=5), data={'areaid': 101050115} if not f else{}) as z:
                z = re.findall(zz, await z.text())
            ff(z[a], text1)
            ff(z[b], text2)
        except:
            s.wfile.write(('<p style="color:green">' + text1 + '</p>').encode())
    async def f__(url, zz, text1, text2, text3, a, b, c, f=1):
        try:
            async with aiohttp.request(method='GET'if f else'POST', url=url, headers=headers, timeout=aiohttp.ClientTimeout(total=30), json={"cityId": 284767, "cityType": 0} if not f else{}) as z:
                z = re.findall(zz, await z.text())
            ff(z[a], text1)
            ff(z[b], text2)
            ff(z[c], text3)
        except:
            s.wfile.write(('<p style="color:green">' + text1 + '</p>').encode())
    async def f___(url, zz, text1, text2, text3, text4, a, b, c, d):
        try:
            async with aiohttp.request(method='GET', url=url, timeout=aiohttp.ClientTimeout(total=5)) as z:
                z = re.findall(zz, await z.text())
                ff(z[a], text1)
                ff(z[b], text2)
                ff(z[c], text3)
                ff(z[d], text4)
        except:
            s.wfile.write(('<p style="color:green">' + text1 + '</p>').encode())
    url1 = "https://d1.weather.com.cn/sk_2d/101050115.html"
    url2 = "https://d1.weather.com.cn/wap_40d/101050115.html"
    url3 = "https://m.tianqi.com/nangangqu"
    url4 = "http://www.nmc.cn/rest/weather?stationid=50953"
    # url5 = "https://co.moji.com/api/weather2/weather?city=284767"
    url6 = "https://tianqi.2345.com/nangang1d/71467.htm"
    url7 = "https://tianqi.2345.com/t/shikuang/71467.js"
    # url8 = "https://www.qweather.com/weather/nangang-101050115.html"
    url8 = "https://devapi.qweather.com/v7/weather/now?key=a91212c50f7041b9a9c68ea15874dbcc&location=101050115"
    url9 = "https://weathernew.pae.baidu.com/weathernew/pc?query=%E5%8D%97%E5%B2%97%E5%A4%A9%E6%B0%94&srcid=4982"
    url10 = "https://wis.qq.com/weather/common?source=pc&weather_type=observe%7Cforecast_1h&province=%E9%BB%91%E9%BE%99%E6%B1%9F%E7%9C%81&city=%E5%93%88%E5%B0%94%E6%BB%A8%E5%B8%82&county=%E5%8D%97%E5%B2%97%E5%8C%BA"
    url11 = "https://api.caiyunapp.com/v2/Y2FpeXVuX25vdGlmeQ==/126.631248%2C45.743664/forecast"
    url12 = "https://rss.weather.com.cn/api/v1/obs/1h?lat=45.743663&lng=126.631248&type=obs1h"
    url13 = "http://nanning.welife100.com/PIndex/getnnIndexdata?areaid=101050115"
    url14 = "http://wx.tianqi.cn/Weather/getindexdata"
    url15 = "http://api.yytianqi.com/observe?city=CH050101&key=4d6orwbdmh1bau55"
    # http://www.yytianqi.com/search/CH050101.html ：(.*?)℃
    url16 = "https://openweathermap.org/data/2.5/weather?id=2037013&appid=439d4b804bc8187953eb36d2a8c26a02"
    url17 = "https://www.tianqiapi.com/free/day?appid=56761788&appsecret=ti3hP8y9&city=%E5%8D%97%E5%B2%97"
    url18 = "https://restapi.amap.com/v3/weather/weatherInfo?key=bb2729228cb4b74134910bfb25bc4a3f&city=230103"
    url19 = "http://aider.meizu.com/app/weather/listWeather?cityIds=101050101"
    url20 = "http://weather.123.duba.net/static/weather_info/101050115.html"
    url21 = "https://weatherapi.market.xiaomi.com/wtr-v3/weather/all?longitude=126.59&latitude=45.666&appKey=a&isGlobal=false&locale=zh_cn&sign=a"
    url22 = "http://api.help.bj.cn/apis/weather/?id=101050115"
    url23 = "https://api.msn.cn/weatherfalcon/weather/overview?cuthour=true&days=1&lat=45.760101318359375&lon=126.66900634765625&locale=zh-cn"
    url24 = "https://xiaobai.klizi.cn/API/other/qq_weather.php?msg=%E5%93%88%E5%B0%94%E6%BB%A8"
    url25 = "https://xiaobai.klizi.cn/API/other/tianqi_c.php?msg=%E5%93%88%E5%B0%94%E6%BB%A8"
    # url26 = "https://tianqi.so.com/weather/101050115"
    url27 = "http://m.weathercn.com/current-weather.do?id=2580971"
    # url28 = "https://www.tianqi5.cn/heilongjiang/huayuantianqiyubao.html"
    # url29 = "https://m.weaoo.com/haerbin-nangangqu-95912.html"
    url29 = "https://m.weaoo.com/haerbin-181237.html"
    url30 = "https://www.69tianqi.com/sight-101050101-haerbin151-60921.html"
    # url31 = "https://www.yangshitianqi.com/haerbin.html"
    url32 = "https://www.tianqi24.com/nangangqu/"
    url33 = "https://v.api.aa1.cn/api/api-tianqi-4/?id=101050115"
    url34 = "https://cloud-rest.lenovomm.com/cloud-weather/weather/weatherInfo"
    url35 = "https://cdn.weather.hao.360.cn/sed_api_weather_info.php?code=101050115"
    url36 = "http://m.chinaso.com/v5/general/v1/public/weather?code=230100"
    url37 = "https://m.sogou.com/viwww?op=14&query=%E9%BB%91%E9%BE%99%E6%B1%9F%09%E5%93%88%E5%B0%94%E6%BB%A8%09%E5%8D%97%E5%B2%97"
    url38 = "https://m.sogou.com/tworeq?queryString=%E5%93%88%E5%B0%94%E6%BB%A8%E5%A4%A9%E6%B0%94&ie=utf8&reqClassids=70269806&queryFrom=wap&dataPlatformSource=weather_card"
    url39 = "https://h5ctywhr.api.moji.com/weatherDetail"
    url40 = "http://apis.juhe.cn/simpleWeather/query?city=%E5%8D%97%E5%B2%97&key=251518e073ef6c3c9504dd286c3f6a86"
    url41 = "https://yiketianqi.com/api?version=v1&city=%E5%8D%97%E5%B2%97&appid=85841439&appsecret=EKCDLT4I"
    url42 = "https://api.seniverse.com/v3/weather/now.json?key=SCYrvkytJze9qyzOh&location=haerbin"
    url43 = "https://www.mxnzp.com/api/weather/current/%E5%8D%97%E5%B2%97%E5%8C%BA?app_id=eklrnkhmiltpfsux&app_secret=eTgyT3hERzBGSzZsSmVCalRBNVdHQT09"
    url44 = "https://way.jd.com/he/freeweather?city=CN101050115&appkey=da39dce4f8aa52155677ed8cd23a6470"
    url45 = "http://weather.365rili.com/weather_get_cities.do?citycodes=[%22101050101%22]"
    url46 = "https://weather.cma.cn/api/now/50953"
    # url45 = "https://weather.mp.qq.com/?adcode=230103"
    # url40 = "http://www.lpv4.cn:10000/api/idcode/?id=230103"
    printf = [f(url1, 'p":"(.*?)"', '  南岗weather', headers_), f(url2, 'b":"(.*?)"', '  (小时)南岗weather', headers_), f(url3, 'w">(.*?)<', '  南岗tianqi'), f__(url4, '[ft]e.{4,9}":(.*?)[},]', '  哈尔滨nmc', '  (体感)哈尔滨nmc', '  (小时)哈尔滨nmc', 0, 1, 17), f(url6, '-t">(.*?)°', '  南岗2345'), f(url7, 'p":"(.*?)"', '  南岗2345'), f_(url9, r'e":"(-?\d{1,2})","[uw]', '  南岗baidu', '  (体感)南岗baidu', 0, 1), f_(url10, 'ee":"(.*?)"', '  南岗qq', '  (小时)南岗qq', -1, 0), f(url11, 're":.*?ue":(.{1,5})}', '  花园caiyunapp'), f(url12, ':"(.*?)"', '  哈工大weather'), f_(url13, 'l12?":"(.*?)"', '  南岗welife100', '  (体感)南岗welife100',  0, 1), f_(url14, 'l12?":"(.*?)"', '  南岗tianqi', '  (体感)南岗tianqi', 0, 1, 0), f(url15, 'w":"(.*?)"', '  哈尔滨yytianqi'), f_(url16, '[mk][pe]":(.*?),"', '  哈尔滨openweathermap', '  (体感)哈尔滨openweathermap', 0, 1), f(url17, 'm":"(.*?)"', '  api南岗tianqiapi'), f(url18, 're":"(.*?)"', '  api南岗amap'), f_(url19, 'emp":"(.*?)"', '  api哈尔滨meizu', '  (体感)api哈尔滨meizu', 1, 0), f(url20, 'p":"(.*?)"', '  api南岗duba'), f_(url21, '℃","value":"(.*?)"', '  api南岗xiaomi', '  (体感)api南岗xiaomi', 1, 0), f(url22, 'p":"(.*?)"', '  api南岗bj'), f___(url23, r'[ml][ps]":(.*?)\.', '  南岗msn', '  (体感)南岗msn', '  (小时)南岗msn', '  (小时体感)南岗msn', 1, 0, 3, 2), f(url24, '：气温：(.*?)℃', '  api哈尔滨klizi'), f_(url25, r'"[tf].*[et]": (.*\d),?', '  api哈尔滨klizi', '  (体感)api哈尔滨klizi', 0, 1), f__(url27, '>(.*?)℃<', '  花园weathercn', '  (体感)花园weathercn', '  (阴影体感)花园weathercn', 2, 3, 4), f(url29, 'p">\n *(.*?)\n', '  南岗weaoo'), f(url30, 'l2">(.*?)<', '  哈工大69tianqi'), f_(url32, '[w<]["b]>(.*?)[< ][i°]', '  南岗tianqi24', '  (体感)南岗tianqi24', 0, 1), f(url33, 'p":"(.*?)"', '  api南岗aa1'), f_(url34, 'b":"(.*?)℃', '  哈尔滨lenovomm', '  (小时)哈尔滨lenovomm', -1, 0), f(url35, 're":"(.*?)"', '  南岗360'), f(url36, 'r":"(.*?)"', '  哈尔滨chinaso'), f(url37, '1": "(.*?)"', '  南岗sogou'), f(url38, r're><!\[CDATA\[(.*?)]', '  (小时)哈尔滨sogou'), f__(url39, r'[lp]":(-?\d{1,2}),"t', '  南岗moji', '  (体感)南岗moji', '  (小时体感)moji', 1, 0, 2, 0), f_(url8, r'"(-?\d{1,2})"', '  南岗qweather', '  (体感)南岗qweather', 0, 1), f(url40, 're":"(.*?)"', '  api南岗juhe'), f(url41, r'm":"(.*?)\\u', '  api南岗yiketianqi'), f(url42, 're":"(.*?)"', '  api哈尔滨seniverse'), f(url43, 'p":"(.*?)℃', '  api南岗mxnzp'), f_(url44, r'[lp]":"(-?\d{1,2})","[hv]', '  api南岗jd', '  (体感)api南岗jd', 1, 0), f(url45, 're":"(.*?)℃', '  哈尔滨365rili'), f(url46, 're":(.*?),', '  南岗cma'), ]
    # printf=[f(url46, 're":(.*?),', '  南岗cma')]
    # f(url28, 'b>(.*?)<', '  南岗tianqi5'),
    # f(url5, 'ue":(.*?),', '  南岗moji'),
    # f_(url8, '<p>(.*?)°</p>', '  南岗qweather', '  (体感)南岗qweather', 0, 1),
    # , f__(url40, r'[e"][m,][p"][ef][re][ae][tl][ui][rn][eg]":"(-?\d{1,2})","[wh][iu][nm][di][_d][is][dpt]["ey][:e "]["d:]', '  api南岗lpv4', '  (体感)api南岗lpv4', '  (小时)api南岗lpv4', 0, 1, 2)
    # [:,\[]["{]["l][l1j][12b]":"(-?\d{1,2})","[lfj]
    # f(url31, '1">(.*?)℃', '  哈尔滨yangshitianqi'),
    # f_(url26, r'(-?\d{1,2})℃</p', '  南岗so', '  (体感)南岗so', 0, 1),
    # f_(url45, r'(-?\d{1,2})[<°][s ][p<]', '  南岗qq', '  (小时)南岗qq', 0, 1, headers=headers_qq)
    # asyncio.get_event_loop().run_until_complete(asyncio.wait([asyncio.ensure_future(i) for i in printf]))
    async def runWeatheraios():
        await asyncio.wait([asyncio.ensure_future(i) for i in printf])
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(runWeatheraios())