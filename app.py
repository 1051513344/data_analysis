from flask import Flask, render_template
from Tool import ChartTool,Analysis

import os
app = Flask(__name__)



# 网站主页
@app.route('/')
def index():
    project_path = os.path.dirname(os.path.abspath(__file__))
    china_map = ChartTool.geo()
    chart1 = Analysis.province_rt2(project_path)

    return render_template("index.html",
                           map=china_map.render_embed(),
                           chart1=chart1.render().render_embed()
                           )


if __name__ == '__main__':
    app.run(debug=True)
