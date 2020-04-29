from pyecharts import options as opts
from pyecharts.charts import PictorialBar, Line, Bar, Pie, Geo
from pyecharts.globals import SymbolType, ChartType
import pandas as pd
from pyecharts.commons.utils import JsCode
import re




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
                axislabel_opts=opts.LabelOpts(formatter="{value}% 降水概率", color="white")
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
                axislabel_opts=opts.LabelOpts(formatter="{value}%\n降水概率", color="white", font_size=10)
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

    def render(self, ctiy):


        # 几大城市天气情况

        city = self.weather[self.weather['city'] == ctiy]

        time_shanghai = city['time'].values.tolist()
        wea_shanghai = city['wea'].values.tolist()
        wea_list_shanghai = list(map(self.check_weather, wea_shanghai))
        tem_shanghai = city['tem'].values.tolist()
        tem_list_shanghai = list(map(self.trans_tem, tem_shanghai))
        line = Line(init_opts=opts.InitOpts(width="100%", height="100%", bg_color="#12406d"))
        line.add_xaxis(time_shanghai)
        line.add_yaxis("降水概率", wea_list_shanghai, is_smooth=True,
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
                       itemstyle_opts=opts.ItemStyleOpts(color="#FF6347")
                       )

        line.add_yaxis("温度", tem_list_shanghai,
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
                       itemstyle_opts=opts.ItemStyleOpts(color="#00BFFF")
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


class province_p:

    def __init__(self, csv_path):

        self.passenger = pd.read_csv('{}/data/passenger_flow.csv'.format(csv_path)).set_index("城市")  # 读取省会信息


    def render(self, city):

        days = self.passenger.loc[city, "周四（12日）":].index
        days = [i[3:6] for i in days]

        NUM_LIST = self.passenger.loc[city, "周四（12日）":].values
        NUM_LIST = [float(NUM) for NUM in NUM_LIST]

        MAX_NUM_LIST = [round(1-NUM, 2) for NUM in NUM_LIST]

        bar = Bar(init_opts=opts.InitOpts(width="100%", height="92%", bg_color="#12406d"))

        bar.add_xaxis(days)

        bar.add_yaxis("景区客流", NUM_LIST, stack='stack1', itemstyle_opts=opts.ItemStyleOpts(color='#FF6347'),)
        bar.add_yaxis("景区容量", MAX_NUM_LIST, stack='stack1', itemstyle_opts=opts.ItemStyleOpts(color='orange'),)

        bar.set_series_opts(label_opts=opts.LabelOpts(is_show=True, color="white"))
        bar.set_global_opts(

            legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white")),
            xaxis_opts=opts.AxisOpts(name='日期', name_textstyle_opts=opts.TextStyleOpts(color="orange"),
                                     axislabel_opts=opts.LabelOpts(rotate=-30, color="white"),
                                     is_show=True),
            yaxis_opts=opts.AxisOpts(
                name='客流占比',
                name_textstyle_opts=opts.TextStyleOpts(color="orange"),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=0)
                ),
                axislabel_opts=opts.LabelOpts(color="white")
            )

        )



        return bar



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
            type_=ChartType.HEATMAP
        )
        geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        geo.set_global_opts(
            visualmap_opts=opts.VisualMapOpts(range_color=['#7FFFAA', '#006400']),
            title_opts=opts.TitleOpts(title="Geo-HeatMap"),
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
            visualmap_opts=opts.VisualMapOpts(max_=30),
            title_opts=opts.TitleOpts(title="Geo-HeatMap"),
        )
        return geo


