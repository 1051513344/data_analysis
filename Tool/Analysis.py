from pyecharts import options as opts
from pyecharts.charts import PictorialBar, Line, Bar, Pie, Geo
from pyecharts.globals import SymbolType, ChartType
import pandas as pd
from pyecharts.commons.utils import JsCode
import re
from Tool.Predict import predict_passer



class province_rt:

    def __init__(self, csv_path):
        self.provincial = pd.read_csv('{}/data/provincial_capital.csv'.format(csv_path))  # 读取省会信息
        self.china_city_code = pd.read_csv('{}/data/china-city-list.csv'.format(csv_path))  # 读取城市 id 信息
        self.weather = pd.read_csv("{}/data/weather_data.csv".format(csv_path))  # 读取天气信息

    def trans_tem(self, tem):
        # 获取温度信息
        rege = r'-?(\d+)℃/-?(\d+)℃'
        tmp_tem = re.match(rege, tem)
        mid_tem = (int(tmp_tem.group(1)) + int(tmp_tem.group(2))) / 2
        return mid_tem

    # 转换降水信息
    def check_weather(self, wea):
        # 转换天气变量，数值越多，说明降水概率越大
        weather_dict = {
            "snow": 100,
            "rain": 80,
            "cloud": 50,
            "overcast": 60,
            "sun": 20
        }
        if wea[-1:] == '晴':
            wea = weather_dict['sun']
        elif wea[-1:] == '云':
            wea = weather_dict['cloud']
        elif wea[-1:] == '雨':
            wea = weather_dict['rain']
        elif wea[-1:] == '阴':
            wea = weather_dict['overcast']
        return wea

    def render(self):

        # 提取省会城市 id
        provincial_data = pd.DataFrame()
        for i in self.provincial['city'].values.tolist():
            for j in self.china_city_code['City_CN'].values.tolist():
                if j == i:
                    provincial_data = pd.concat([self.china_city_code[self.china_city_code['City_CN'] == j], provincial_data])

        # 按照城市分组
        wea_group = self.weather.groupby('city').apply(lambda x: x[:])
        # 提取当天天气信息
        weather_info = wea_group[wea_group['time'] == '周五（13日）']
        # 城市信息
        weather_info_ctiy = weather_info['city'].values.tolist()
        weather_info_ctiy = list(weather_info_ctiy)


        # 获取降水和温度信息
        weather_data = map(self.check_weather, weather_info['wea'].values.tolist())
        weather_data = list(weather_data)
        tem_data = map(self.trans_tem, weather_info['tem'].values.tolist())
        tem_data = list(tem_data)

        # 降水和温度柱状图
        pictorialbar = PictorialBar(init_opts=opts.InitOpts(width="100%", height="100%", bg_color="#12406d"))
        pictorialbar.add_xaxis(weather_info_ctiy)
        pictorialbar.add_yaxis(
            "降水量", weather_data,
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=18,
            symbol_repeat="fixed",
            symbol_offset=[0, 0],
            is_symbol_clip=True,
            itemstyle_opts=opts.ItemStyleOpts(color='#00BFFF'),
            symbol=SymbolType.ROUND_RECT
        )

        pictorialbar.add_yaxis(
            "温度", tem_data,
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=18,
            symbol_repeat="fixed",
            symbol_offset=[0, 0],
            is_symbol_clip=True,
            symbol=SymbolType.ARROW
        )

        pictorialbar.set_global_opts(

            legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white")),
            # title_opts=opts.TitleOpts(title="中秋节省会城市降雨和温度情况", title_textstyle_opts=opts.TextStyleOpts
            xaxis_opts=opts.AxisOpts(name="省份", name_textstyle_opts=opts.TextStyleOpts(color="white"),  axislabel_opts=opts.LabelOpts(rotate=-30, color="white"), is_show=True),
            yaxis_opts=opts.AxisOpts(
                name="温度/降水",
                name_textstyle_opts=opts.TextStyleOpts(color="white"),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=0)
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}% 降水量", color="white")
            ),
            datazoom_opts=opts.DataZoomOpts(),

        )


        # pictorialbar.render()
        return pictorialbar


class province_rt2:

    def __init__(self, csv_path):
        self.provincial = pd.read_csv('{}/data/provincial_capital.csv'.format(csv_path))  # 读取省会信息
        self.china_city_code = pd.read_csv('{}/data/china-city-list.csv'.format(csv_path))  # 读取城市 id 信息
        self.weather = pd.read_csv("{}/data/weather_data.csv".format(csv_path))  # 读取天气信息

    def trans_tem(self, tem):
        # 获取温度信息
        rege = r'-?(\d+)℃/-?(\d+)℃'
        tmp_tem = re.match(rege, tem)
        mid_tem = (int(tmp_tem.group(1)) + int(tmp_tem.group(2))) / 2
        return mid_tem

    # 转换降水信息
    def check_weather(self, wea):
        # 转换天气变量，数值越多，说明降水概率越大
        weather_dict = {
            "snow": 100,
            "rain": 80,
            "cloud": 50,
            "overcast": 60,
            "sun": 20
        }
        if wea[-1:] == '晴':
            wea = weather_dict['sun']
        elif wea[-1:] == '云':
            wea = weather_dict['cloud']
        elif wea[-1:] == '雨':
            wea = weather_dict['rain']
        elif wea[-1:] == '阴':
            wea = weather_dict['overcast']
        return wea

    def render(self):

        # 提取省会城市 id
        provincial_data = pd.DataFrame()
        for i in self.provincial['city'].values.tolist():
            for j in self.china_city_code['City_CN'].values.tolist():
                if j == i:
                    provincial_data = pd.concat([self.china_city_code[self.china_city_code['City_CN'] == j], provincial_data])

        # 按照城市分组
        wea_group = self.weather.groupby('city').apply(lambda x: x[:])
        # 提取当天天气信息
        weather_info = wea_group[wea_group['time'] == '周五（13日）']
        # 城市信息
        weather_info_ctiy = weather_info['city'].values.tolist()
        weather_info_ctiy = list(weather_info_ctiy)


        # 获取降水和温度信息
        weather_data = map(self.check_weather, weather_info['wea'].values.tolist())
        weather_data = list(weather_data)
        tem_data = map(self.trans_tem, weather_info['tem'].values.tolist())
        tem_data = list(tem_data)

        # 在双轴图中查看
        bar = Bar(init_opts=opts.InitOpts(width="100%", height="100%", bg_color="#12406d"))
        bar.add_xaxis(weather_info_ctiy)
        bar.add_yaxis("", weather_data)
        bar.extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} °C", color="white"), interval=5
            )
        )
        bar.set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30, color="white"), is_show=True),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=0)
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}%\n降水量", color="white", font_size=10)
            ),
            datazoom_opts=opts.DataZoomOpts()
        )
        bar.set_series_opts(itemstyle_opts={
            "normal": {
                "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(0, 244, 255, 1)'
                        }, {
                            offset: 1,
                            color: 'rgba(0, 77, 167, 1)'
                        }], false)"""),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": 'rgb(0, 160, 221)',
            }, "color": "white"
        })
        line = Line()
        line.add_xaxis(weather_info_ctiy).add_yaxis("", tem_data, yaxis_index=1)
        line.set_series_opts(label_opts=opts.LabelOpts(is_show=True, color="orange"))

        bar.overlap(line)

        return bar



class province_rt3:

    def __init__(self, csv_path):

        self.temperature = pd.read_csv("{}/data/all_temperature.csv".format(csv_path)).set_index("城市")  # 读取温度信息
        self.weather = pd.read_csv("{}/data/all_weather.csv".format(csv_path)).set_index("城市")  # 读取天气信息



    def render(self, city):

        days = ["周五（6日）","周六（7日）","周日（8日）","周一（9日）","周二（10日）","周三（11日）","周四（12日）","周五（13日）"]
        temps = self.temperature.loc[city, "周五（6日）":]
        wea = self.weather.loc[city, "周五（6日）":]


        line = Line(init_opts=opts.InitOpts(width="100%", height="100%", bg_color="#12406d"))
        line.add_xaxis(days)
        line.add_yaxis("降水量", wea, is_smooth=True,
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
                       itemstyle_opts=opts.ItemStyleOpts(color="#00BFFF")
                       )

        line.add_yaxis("温度", temps,
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
                       itemstyle_opts=opts.ItemStyleOpts(color="#FF6347")
                       )
        line.set_global_opts(
            legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white")),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30, color="white"), is_show=True),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=0)
                ),
                axislabel_opts=opts.LabelOpts(color="white", font_size=10)
            ),
        )
        line.set_series_opts(label_opts=opts.LabelOpts(is_show=True, color="orange"))


        return line


class province_passer:

    def __init__(self, csv_path):

        self.temp = pd.read_csv("{}/data/all_temperature.csv".format(csv_path)).set_index("城市")
        self.wea = pd.read_csv("{}/data/all_weather.csv".format(csv_path)).set_index("城市")
        self.passer = pd.read_csv("{}/data/all_passer.csv".format(csv_path)).set_index("城市")

    def render(self, city):

        self.temp = self.temp.loc[city, "周五（6日）":]
        self.wea = self.wea.loc[city, "周五（6日）":]
        self.passer = self.passer.loc[city, "周五（6日）":]

        pie = Pie(init_opts=opts.InitOpts(width="100%", height="100%"))
        pie.add("", [("景区客流", predict_passer(self.temp, self.wea, self.passer)), ("景区容量", 1 - predict_passer(self.temp, self.wea, self.passer))])
        pie.set_colors(["#FF6347", "orange"])
        pie.set_global_opts(legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white")))
        pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))

        return pie

class province_hm1:

    def __init__(self, csv_path):
        self.provincial = pd.read_csv('{}/data/provincial_capital.csv'.format(csv_path))  # 读取省会信息
        self.weather = pd.read_csv("{}/data/weather_data.csv".format(csv_path))  # 读取天气信息

    def trans_tem(self, tem):
        # 获取温度信息
        rege = r'-?(\d+)℃/-?(\d+)℃'
        tmp_tem = re.match(rege, tem)
        mid_tem = (int(tmp_tem.group(1)) + int(tmp_tem.group(2))) / 2
        return mid_tem

    # 转换降水信息
    def check_weather(self, wea):
        # 转换天气变量，数值越多，说明降水概率越大
        weather_dict = {
            "snow": 100,
            "rain": 80,
            "cloud": 50,
            "overcast": 60,
            "sun": 20
        }
        if wea[-1:] == '晴':
            wea = weather_dict['sun']
        elif wea[-1:] == '云':
            wea = weather_dict['cloud']
        elif wea[-1:] == '雨':
            wea = weather_dict['rain']
        elif wea[-1:] == '阴':
            wea = weather_dict['overcast']
        return wea

    def render(self):

        # 降水分布图
        provincial_list = self.provincial['provincial'].values.tolist()

        # 按照城市分组
        wea_group = self.weather.groupby('city').apply(lambda x: x[:])
        # 提取当天天气信息
        weather_info = wea_group[wea_group['time'] == '周五（13日）']

        # 获取降水和温度信息
        weather_data = map(self.check_weather, weather_info['wea'].values.tolist())
        weather_data_list = list(weather_data)


        geo = Geo(init_opts=opts.InitOpts(width="100%", height="92%", bg_color="#12406d"))
        geo.add_schema(maptype='china')
        geo.add(
            "降水分布图",
            [list(z) for z in zip(provincial_list, weather_data_list)],
            type_=ChartType.HEATMAP,
            color="#006400"
        )
        geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        geo.set_global_opts(
            legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white")),
            visualmap_opts=opts.VisualMapOpts(range_color=['#7FFFAA', '#006400']),
            title_opts=opts.TitleOpts(title="降水分布图",
                                      title_textstyle_opts=opts.TextStyleOpts(color="white")),
        )

        return geo


class province_hm2:

    def __init__(self, csv_path):
        self.provincial = pd.read_csv('{}/data/provincial_capital.csv'.format(csv_path))  # 读取省会信息
        self.weather = pd.read_csv("{}/data/weather_data.csv".format(csv_path))  # 读取天气信息

    def trans_tem(self, tem):
        # 获取温度信息
        rege = r'-?(\d+)℃/-?(\d+)℃'
        tmp_tem = re.match(rege, tem)
        mid_tem = (int(tmp_tem.group(1)) + int(tmp_tem.group(2))) / 2
        return mid_tem

    # 转换降水信息
    def check_weather(self, wea):
        # 转换天气变量，数值越多，说明降水概率越大
        weather_dict = {
            "snow": 100,
            "rain": 80,
            "cloud": 50,
            "overcast": 60,
            "sun": 20
        }
        if wea[-1:] == '晴':
            wea = weather_dict['sun']
        elif wea[-1:] == '云':
            wea = weather_dict['cloud']
        elif wea[-1:] == '雨':
            wea = weather_dict['rain']
        elif wea[-1:] == '阴':
            wea = weather_dict['overcast']
        return wea

    def render(self):

        # 降水分布图
        provincial_list = self.provincial['provincial'].values.tolist()

        # 按照城市分组
        wea_group = self.weather.groupby('city').apply(lambda x: x[:])
        # 提取当天天气信息
        weather_info = wea_group[wea_group['time'] == '周五（13日）']

        # 获取降水和温度信息
        tem_data = map(self.trans_tem, weather_info['tem'].values.tolist())
        tem_data = list(tem_data)

        geo = Geo(init_opts=opts.InitOpts(width="100%", height="92%", bg_color="#12406d"))
        geo.add_schema(maptype='china')
        geo.add(
            "温度分布图",
            [list(z) for z in zip(provincial_list, tem_data)],
            type_=ChartType.HEATMAP
        )
        geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        geo.set_global_opts(
            legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white")),
            visualmap_opts=opts.VisualMapOpts(max_=30),
            title_opts=opts.TitleOpts(title="温度分布图",
                                      title_textstyle_opts=opts.TextStyleOpts(color="white")
                                      ),
        )
        return geo


class province_scroe:

    def __init__(self, csv_path):
        self.score = pd.read_csv('{}/data/score.csv'.format(csv_path)).set_index("城市")  # 读取分数信息

    def get_score(self, city):
        return int(self.score["分数"][city])




