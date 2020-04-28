from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType



def geo():
    province_distribution = {'河南': 45.23, '北京': 37.56, '河北': 21, '辽宁': 12, '江西': 6, '上海': 20, '安徽': 10, '江苏': 16,
                             '湖南': 9, '浙江': 13, '海南': 2, '广东': 22, '湖北': 8, '黑龙江': 11, '澳门': 1, '陕西': 11, '四川': 7,
                             '内蒙古': 3, '重庆': 3, '云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': 11, '福建': 4, '青海': 1,
                             '天津': 1
                             }

    data_pair = []
    for i, j in zip(province_distribution.keys(), province_distribution.values()):
        data_pair.append(tuple([i, j]))
    city = 'china'
    g = Geo(init_opts=opts.InitOpts(width="100%", height="92%", bg_color="#12406d"))
    g.add_schema(
        maptype=city,
        itemstyle_opts=opts.ItemStyleOpts(color="#135dbe", border_color="#fff"),
        zoom=1.2
    )
    g.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    g.set_global_opts(
        visualmap_opts=opts.VisualMapOpts(is_show=False)
    )
    g.add('', data_pair, type_=ChartType.EFFECT_SCATTER)

    return g




