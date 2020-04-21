import re

from flask import Flask, render_template
from Tool import ChartTool
app = Flask(__name__)



# 网站主页
@app.route('/')
def index():
    shanghai_map = ChartTool.geo()
    return render_template("index.html",
                           chart=shanghai_map.render_embed()
                           )





if __name__ == '__main__':
    app.run(debug=True)
