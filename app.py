from flask import Flask, render_template, request, jsonify
from Tool import ChartTool,Analysis

import os
app = Flask(__name__)



# 网站主页
@app.route('/')
def index():
    project_path = os.path.dirname(os.path.abspath(__file__))
    china_map = ChartTool.geo()
    chart1 = Analysis.province_rt2(project_path)
    chart2 = Analysis.province_rt3(project_path)
    chart3 = Analysis.province_p1(project_path)
    city = "上海"
    return render_template("index.html",
                           map=china_map.render_embed(),
                           chart1=chart1.render().render_embed(),
                           city=city,
                           chart2=chart2.render(city).render_embed(),
                           chart3=chart3.render(city).render_embed()
                           )



@app.route('/getChartByCity', methods=['POST'])
def getChartByCity():
    project_path = os.path.dirname(os.path.abspath(__file__))
    city = request.form["city"].split(" : ")[0]
    chart = Analysis.province_rt3(project_path)
    data = {}
    data["city"] = city + "xx节前后降水与温度"
    data["chart"] = chart.render(city).render_embed()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
