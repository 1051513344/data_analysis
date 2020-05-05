# import random
# import unicodecsv as ucsv
#
# province_list = [
#     '河南','北京','河北','辽宁','江西','上海','安徽','江苏','湖南','浙江',
#     '海南','广东','湖北','黑龙江','澳门','陕西','四川','内蒙古','重庆','云南',
#     '贵州','吉林','山西','山东','福建','青海','天津'
# ]
# data = []
#
# with open('../data/passenger_flow.csv', 'wb') as f:
#     # 实例化csv写数据对象
#     writer = ucsv.writer(f, encoding='utf-8')
#     data.append(("城市",
#                  "周四（12日）", "周五（13日）",
#                  "周六（14日）", "周日（15日）",
#                  "周一（16日）", "周二（17日）",
#                  "周三（18日）", "周四（19日）"))
#     for province in province_list:
#         random1 =str(round(random.random(), 2))
#         random2 =str(round(random.random(), 2))
#         random3 =str(round(random.random(), 2))
#         random4 =str(round(random.random(), 2))
#         random5 =str(round(random.random(), 2))
#         random6 =str(round(random.random(), 2))
#         random7 =str(round(random.random(), 2))
#         random8 =str(round(random.random(), 2))
#         data.append((province,random1, random2, random3, random4, random5, random6, random7, random8))
#
#     writer.writerows(data)


import random
import unicodecsv as ucsv

province_list = [
    '河南','北京','河北','辽宁','江西','上海','安徽','江苏','湖南','浙江',
    '海南','广东','湖北','黑龙江','澳门','陕西','四川','内蒙古','重庆','云南',
    '贵州','吉林','山西','山东','福建','青海','天津'
]
data = []

with open('../data/score.csv', 'wb') as f:
    # 实例化csv写数据对象
    writer = ucsv.writer(f, encoding='utf-8')
    data.append(("城市", "分数"))
    for province in province_list:
        random_score =str(random.randint(50, 100))
        data.append((province, random_score))

    writer.writerows(data)



# import random
# import unicodecsv as ucsv
#
# province_list = [
#     '河南','北京','河北','辽宁','江西','上海','安徽','江苏','湖南','浙江',
#     '海南','广东','湖北','黑龙江','澳门','陕西','四川','内蒙古','重庆','云南',
#     '贵州','吉林','山西','山东','福建','青海','天津'
# ]
# data = []
#
# with open('../data/all_passer.csv', 'wb') as f:
#     # 实例化csv写数据对象
#     writer = ucsv.writer(f, encoding='utf-8')
#     data.append(("城市",
#                  "周五（6日）", "周六（7日）",
#                  "周日（8日）", "周一（9日）",
#                  "周二（10日）", "周三（11日）",
#                  "周四（12日）", "周五（13日）"))
#     for province in province_list:
#         random1 =str(round(random.random(), 2))
#         random2 =str(round(random.random(), 2))
#         random3 =str(round(random.random(), 2))
#         random4 =str(round(random.random(), 2))
#         random5 =str(round(random.random(), 2))
#         random6 =str(round(random.random(), 2))
#         random7 =str(round(random.random(), 2))
#         random8 =str(round(random.random(), 2))
#
#         data.append((province,random1, random2, random3, random4, random5, random6, random7, random8))
#
#     writer.writerows(data)

# import pandas as pd
#
# temperature = pd.read_csv("../data/all_temperature.csv").set_index("城市")
# temps = temperature.loc["上海", "周五（6日）":]
# for i in temps:
#     print(type(i))

# import pandas as pd
# import numpy as np
#
# temp = pd.read_csv("../data/all_temperature.csv").set_index("城市").loc["上海", "周五（6日）":]
# wea = pd.read_csv("../data/all_weather.csv").set_index("城市").loc["上海", "周五（6日）":]
# passer = pd.read_csv("../data/all_passer.csv").set_index("城市").loc["上海", "周五（6日）":]
#
# days = ["周五（6日）","周六（7日）","周日（8日）","周一（9日）","周二（10日）","周三（11日）","周四（12日）","周五（13日）"]
# factors = ["天气", "温度", "客流"]
#
# # print(temp)
#
# # data = pd.concat([temp, wea, passer], axis=1)
#
# lists = []
#
#
# for i, j, k in zip(temp, wea, passer):
#     row = []
#     row.append(i)
#     row.append(j)
#     row.append(k)
#     lists.append(row)
#
# data = np.array(lists)
#
# data = pd.DataFrame(data, columns=factors, index=days)
#
#
# print(data)






