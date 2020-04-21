from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Line, Pie
import requests
from lxml import etree
import json
import re
jingwei_dict ={'上海野生动物园': ['31.0544670000', '121.7213980000'],
               '上海科技馆': ['31.2182160000', '121.5416720000'],
               '上海自然博物馆（上海科技馆分馆）': ['31.2349920000', '121.4626500000'],
               '上海博物馆': ['31.2285140000', '121.4753050000'],
               '上海佘山国家森林公园·西佘山园': ['31.0941660000', '121.1960410000'],
               '上海佘山国家森林公园·东佘山园': ['31.0941660000', '121.1960410000'],
               '上海豫园': ['31.2267680000', '121.4922090000'],
               '上海城市规划展示馆': ['31.2312630000', '121.4754960000'],
               '上海动物园': ['31.1926830000', '121.3631920000'],
               '陈云故里练塘古镇景区': ['31.0076900000', '121.0453100000'],
               '上海世纪公园': ['31.2163170000', '121.5528640000'],
               '上海大观园': ['31.0741870000', '120.9086880000'],
               '朱家角古镇': ['31.1091400000', '121.0548740000'],
               '上海古猗园': ['31.2917920000', '121.3168960000'],
               '上海市青少年校外活动营地——东方绿舟': ['31.1016940000', '121.0135610000'],
               '锦江乐园': ['31.1395790000', '121.4088830000'],
               '金山城市沙滩景区': ['30.7099010000', '121.3513690000'],
               '上海海洋水族馆': ['31.2407840000', '121.5020870000'],
               '上海月湖雕塑公园': ['31.0984200000', '121.2068400000'],
               '上海都市菜园景区': ['30.8652100000', '121.5901900000'],
               '上海海湾国家森林公园': ['30.8607560000', '121.6905300000'],
               '上海滨海森林公园': ['30.9631400000', '121.9114900000'],
               '上海田子坊景区': ['31.2082300000', '121.4684800000'],
               '上海M50创意园': ['31.2480880000', '121.4492470000'],
               '上海鲁迅公园': ['31.2717400000', '121.4832300000'],
               '上海和平公园': ['31.2708000000', '121.5034300000']}

weather_dict ={'上海野生动物园': 'http://www.weather.com.cn/weather1d/10102130010A.shtml#input',
         '上海科技馆': 'http://www.weather.com.cn/weather1d/10102130009A.shtml#input',
         '上海自然博物馆（上海科技馆分馆）': 'http://www.weather.com.cn/weather1d/10102010009A.shtml#input',
         '上海博物馆': 'http://www.weather.com.cn/weather1d/10102010011A.shtml#input',
         '上海佘山国家森林公园·西佘山园': 'http://www.weather.com.cn/weather1d/10102090002A.shtml#input',
         '上海佘山国家森林公园·东佘山园': 'http://www.weather.com.cn/weather1d/10102090002A.shtml#input',
         '上海豫园': 'http://www.weather.com.cn/weather1d/10102010006A.shtml#input',
         '上海城市规划展示馆': 'http://www.weather.com.cn/weather1d/10102010005A.shtml#input',
         '上海动物园': 'http://www.weather.com.cn/weather1d/10102010016A.shtml#input',
         '陈云故里练塘古镇景区': 'http://www.weather.com.cn/weather1d/10102080001A.shtml#input',
         '上海世纪公园': 'http://www.weather.com.cn/weather1d/10102130008A.shtml#input',
         '上海大观园': 'http://www.weather.com.cn/weather1d/10102080003A.shtml#input',
         '朱家角古镇': 'http://www.weather.com.cn/weather1d/10102080005A.shtml#input',
         '上海古猗园': 'http://www.weather.com.cn/weather1d/10102050003A.shtml#input',
         '上海市青少年校外活动营地——东方绿舟': 'http://www.weather.com.cn/weather1d/10102080002A.shtml#input',
         '锦江乐园': 'http://www.weather.com.cn/weather1d/10102020002A.shtml#input',
         '金山城市沙滩景区': 'http://www.weather.com.cn/weather1d/10102070002A.shtml#input',
         '上海海洋水族馆': 'http://www.weather.com.cn/weather1d/10102130007A.shtml#input',
         '上海月湖雕塑公园': 'http://www.weather.com.cn/weather1d/10112020701A.shtml#input',
         '上海都市菜园景区': 'http://www.weather.com.cn/weather1d/10102100002A.shtml#input',
         '上海海湾国家森林公园': 'http://www.weather.com.cn/weather1d/10102010014A.shtml#input',
         '上海滨海森林公园': 'http://www.weather.com.cn/weather1d/10102130002A.shtml#input',
         '上海田子坊景区': 'http://www.weather.com.cn/weather1d/10102010013A.shtml#input',
         '上海M50创意园': 'http://www.weather.com.cn/weather1d/10102010012A.shtml#input',
         '上海鲁迅公园': 'http://www.weather.com.cn/weather1d/10102010002A.shtml#input',
         '上海和平公园': 'http://www.weather.com.cn/weather1d/10102010001A.shtml#input'
}


def passenger_spider(place, all=False):
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    req = requests.get("https://shanghaicity.openservice.kankanews.com/public/tour/filterinfo2", headers=header)
    source = req.text.replace("/", "\/").encode().decode("unicode_escape").replace("\/", "/")
    d = json.loads(source)
    data = {}
    if all:
        return d
    else:
        for i in d:
            if place == i["NAME"]:
                data["NAME"] = i["NAME"]
                data["NUM"] = int(i["NUM"])
                data["MAX_NUM"] = int(i["MAX_NUM"])
                break
        return data


def passenger_spider_no_weather():
    place_all = passenger_spider(None, True)
    place_no_weather = []
    for i in place_all:
        if i["NAME"] not in jingwei_dict.keys():
            place_no_weather.append(i)
    return place_no_weather

def weather_spider(url):
    data = {}
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    req = requests.get(url.replace("weather1d", "weather"), headers=header)
    req.encoding = "utf8"
    dom_tree = etree.HTML(req.text)
    # 星期日期
    days = dom_tree.xpath("//div[@class='c7d']//ul[@class='t clearfix']/li/h1/text()")
    # 天气
    weather = dom_tree.xpath("//div[@class='c7d']//ul[@class='t clearfix']/li/p[@class='wea']/text()")
    # 高低温度
    max_min_t_list = dom_tree.xpath("//div[@class='c7d']//ul[@class='t clearfix']/li/p[@class='tem']//text()")
    max_min_t = "".join(max_min_t_list).lstrip("\n").rstrip("\n").split("\n\n")
    # 风向
    wind = dom_tree.xpath("//div[@class='c7d']//ul[@class='t clearfix']/li/p[@class='win']/em/span[1]/@title")
    # 风级
    wind_power = dom_tree.xpath("//div[@class='c7d']//ul[@class='t clearfix']/li/p[@class='win']/i/text()")
    data["days"] = days
    data["weather"] = weather
    data["max_min_t"] = max_min_t
    data["wind"] = wind
    data["wind_power"] = wind_power
    return data





def line_color_with_js_func(place="上海野生动物园") -> Line:
    if place is None:
        weather_data = weather_spider(weather_dict.get("上海野生动物园"))
    else:
        if place in weather_dict.keys():
            place_weather_url = weather_dict.get(place)
            weather_data = weather_spider(place_weather_url)
        else:
            return None


    x_data = [x.replace("".join(re.findall("（.*", x)), "") for x in weather_data.get("days")]
    y_data = [maxt.rstrip("℃").split("/")[0] for maxt in weather_data.get("max_min_t")]
    y_data2 = [mint.rstrip("℃").split("/")[1] for mint in weather_data.get("max_min_t")]

    area_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#6495ED'}, {offset: 1, color: '#12406d'}], false)"
    )

    c = (
        Line(init_opts=opts.InitOpts(width="100%", height="100%"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, color="white"))
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            "日最高气温",
            y_axis=y_data,
            is_smooth=True,
            is_symbol_show=True,
            symbol="circle",
            symbol_size=6,
            linestyle_opts=opts.LineStyleOpts(color="#fff"),
            label_opts=opts.LabelOpts(is_show=True, position="top", color="white", font_size=16),
            itemstyle_opts=opts.ItemStyleOpts(
                color="red", border_color="#fff", border_width=3
            ),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            areastyle_opts=opts.AreaStyleOpts(color=JsCode(area_color_js), opacity=1),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",
                boundary_gap=False,
                axislabel_opts=opts.LabelOpts(margin=30, color="#ffffff63"),
                axisline_opts=opts.AxisLineOpts(is_show=False),
                axistick_opts=opts.AxisTickOpts(
                    is_show=True,
                    length=25,
                    linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                ),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                position="right",
                axislabel_opts=opts.LabelOpts(margin=20, color="#ffffff63"),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(width=2, color="#fff")
                ),
                axistick_opts=opts.AxisTickOpts(
                    is_show=True,
                    length=15,
                    linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                ),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
        # 第二
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="日最低气温",
            y_axis=y_data2,
            is_smooth=True,
            is_symbol_show=True,
            symbol="circle",
            symbol_size=6,
            linestyle_opts=opts.LineStyleOpts(color="#fff"),
            label_opts=opts.LabelOpts(is_show=True, position="top", color="white", font_size=16),
            itemstyle_opts=opts.ItemStyleOpts(
                color="#0ff", border_color="#fff", border_width=3
            ),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            areastyle_opts=opts.AreaStyleOpts(color=JsCode(area_color_js), opacity=1),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="category",
                boundary_gap=False,
                axislabel_opts=opts.LabelOpts(margin=30, color="#ffffff63"),
                axisline_opts=opts.AxisLineOpts(is_show=False),
                axistick_opts=opts.AxisTickOpts(
                    is_show=True,
                    length=25,
                    linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                ),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                position="right",
                axislabel_opts=opts.LabelOpts(margin=20, color="#ffffff63"),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(width=2, color="#fff")
                ),
                axistick_opts=opts.AxisTickOpts(
                    is_show=True,
                    length=15,
                    linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                ),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    return c



def geo():
    place_avaliable = passenger_spider(None, all=True)
    place_no_weather = passenger_spider_no_weather()
    city = 'china'
    g = Geo(init_opts=opts.InitOpts(width="100%", height="100%", bg_color="#12406d"))
    g.add_schema(maptype=city, itemstyle_opts=opts.ItemStyleOpts(color="#135dbe", border_color="#fff"), zoom=1.2)
    # 定义坐标对应的名称，添加到坐标库中 add_coordinate(name, lng, lat)
    for k, v in jingwei_dict.items():
        g.add_coordinate(k, float(v[1]), float(v[0]))
    for item in place_no_weather:
        g.add_coordinate(item["NAME"], float(item["LOCATION_X"]), float(item["LOCATION_Y"]))

    coordinates = []
    for k in jingwei_dict.keys():
        data_pairs = []
        data_pairs.append(k)
        for p in place_avaliable:
            if k == p["NAME"]:
                if not p.get("MAX_NUM"):
                    data_pairs.append(0.0)
                else:
                    data_pairs.append(round(int(p["NUM"])/int(p["MAX_NUM"]), 2))
                break
        if len(data_pairs) == 1:
            data_pairs.append(0.0)
        data_pairs = tuple(data_pairs)
        coordinates.append(data_pairs)

    for item in place_no_weather:
        data_pairs = []
        data_pairs.append(item["NAME"])
        if (not item["MAX_NUM"]) or (item["MAX_NUM"] == ""):
            data_pairs.append(0)
        else:
            data_pairs.append(round(int(item["NUM"]) / int(item["MAX_NUM"]), 2))
        data_pairs = tuple(data_pairs)
        coordinates.append(data_pairs)

    # 定义数据对，
    # data_pair = [
    #     ('湖南省长沙市雨花区跳马镇仙峰岭', 25),
    #     ('湖南省长沙市宁乡市横市镇藕塘', 5),
    #     ('湖南省长沙市长沙县黄花镇新塘铺长沙黄花国际机场', 20)
    # ]
    data_pair = coordinates
    # Geo 图类型，有 scatter, effectScatter, heatmap, lines 4 种，建议使用
    # from pyecharts.globals import GeoType
    # GeoType.GeoType.EFFECT_SCATTER，GeoType.HEATMAP，GeoType.LINES

    # 将数据添加到地图上
    g.add('', data_pair, type_=ChartType.EFFECT_SCATTER)
    # 设置样式
    g.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False, formatter="{b}:{c}")
    )
    # 自定义分段 color 可以用取色器取色
    pieces = [
        {'max': 0.1, 'label': '10%以下', 'color': '#98F5FF'},
        {'min': 0.1, 'max': 0.3, 'label': '10%-30%', 'color': '#0f0'},
        {'min': 0.3, 'max': 0.5, 'label': '30%-50%', 'color': 'orange'},
        {'min': 0.5, 'max': 0.7, 'label': '50%-70%', 'color': '#E2C568'},
        {'min': 0.7, 'max': 0.8, 'label': '70%-80%', 'color': '#FCF84D'},
        {'min': 0.8, 'max': 0.9, 'label': '80%-90%', 'color': '#3700A4'},
        {'min': 0.9, 'max': 1, 'label': '90%-100%', 'color': '#DD675E'},
        {'min': 1, 'label': '100%以上', 'color': '#f00'}  # 有下限无上限
    ]
    #  is_piecewise 是否自定义分段， 变为true 才能生效
    g.set_global_opts(
        visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=pieces, textstyle_opts=opts.TextStyleOpts(color="#fff"))
    )
    return g

def pie_set_colors(place="上海野生动物园") -> Pie:
    if place is "":
        place = "上海野生动物园"
    data = passenger_spider(place)
    c = (
        Pie(init_opts=opts.InitOpts(width="100%", height="100%"))
        .add("", [("景区客流", data["NUM"]), ("景区容量", data["MAX_NUM"] - data["NUM"])])
        .set_colors(["#FF6347", "orange"])
        .set_global_opts(title_opts=opts.TitleOpts(title=data["NAME"], title_textstyle_opts=opts.TextStyleOpts(color="white", font_size=15)), legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white")))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
    )
    return c