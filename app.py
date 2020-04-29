from flask import Flask, render_template, request, jsonify
from Tool import ChartTool, Analysis, Enumeration

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
    days = Enumeration.days
    return render_template("index.html",
                           days=days,
                           city=city,
                           map=china_map.render_embed(),
                           chart1=chart1.render().render_embed(),
                           chart2=chart2.render(city).render_embed(),
                           chart3=chart3.render(city).render_embed()
                           )



@app.route('/getChart2ByCity', methods=['POST'])
def getChartByCity():
    project_path = os.path.dirname(os.path.abspath(__file__))
    city = request.form["city"]
    chart = Analysis.province_rt3(project_path)
    chart3 = Analysis.province_p1(project_path)
    data = {}
    data["city"] = city + "中秋节前后降水与温度"
    data["chart"] = chart.render(city).render_embed()
    data["chart3"] = chart3.render(city).render_embed()
    return jsonify(data)


@app.route('/getChart3ByCity', methods=['POST'])
def getChart3ByCity():
    project_path = os.path.dirname(os.path.abspath(__file__))
    city = request.form["city"]
    day = request.form["day"]
    chart = Analysis.province_p1(project_path)
    data = {}
    data["chart"] = chart.render(city, day).render_embed()
    return jsonify(data)


@app.route('/getMapOne', methods=['POST'])
def getMapOne():
    project_path = os.path.dirname(os.path.abspath(__file__))
    chart = Analysis.province_hm1(project_path)
    data = {}
    data["chart"] = chart.render().render_embed()
    return jsonify(data)

@app.route('/getMapTwo', methods=['POST'])
def getMapTwo():
    project_path = os.path.dirname(os.path.abspath(__file__))
    chart = Analysis.province_hm2(project_path)
    data = {}
    data["chart"] = chart.render().render_embed()
    return jsonify(data)


@app.route('/getMap', methods=['POST'])
def getMap():
    china_map = ChartTool.geo()
    data = {}
    data["chart"] = china_map.render_embed()
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)
