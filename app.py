import re

from flask import Flask, render_template, jsonify, request
from Tool import ChartTool

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    shanghai_map = ChartTool.geo()
    return render_template("index.html",
                           chart=shanghai_map.render_embed()
                           )

@app.route('/getChart')
def getChart():
    data = {}
    data["chart1"] = ChartTool.line_color_with_js_func().render_embed()
    data["chart2"] = ChartTool.pie_set_colors().render_embed()
    return jsonify(data)

@app.route('/getChartByPlace', methods=['POST'])
def getChartByPlace():
    data = {}
    place = request.form["place"]
    re_place = re.findall("( :.*)", place)
    place = place.replace("".join(re_place), "")
    if ChartTool.line_color_with_js_func(place):
        data["chart1"] = ChartTool.line_color_with_js_func(place).render_embed()
    else:
        data["chart1"] = "no_weather"
    data["chart2"] = ChartTool.pie_set_colors(place).render_embed()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
