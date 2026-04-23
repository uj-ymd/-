from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # 首頁：提供兩個直接連結到圖片路由的連結
    link = "<h1>歡迎進入陳語婕的網站</h1>"
    link += "<h3>請選擇要查看的檔案：</h3>"
    link += "<ul>"
    link += "<li><a href='/show_104'>1. 查看 104 生涯興趣測驗結果 (104.jpg)</a></li>"
    link += "<li><a href='/show_uj'>2. 查看 個人履歷 (uj.jpg)</a></li>"
    link += "</ul>"
    return link

@app.route("/show_104")
def show_104():
    # 顯示 104.jpg 的路由
    return """
    <h2>104 生涯興趣測驗結果</h2>
    <img src='/static/104.jpg' width='600'>
    <br><br>
    <a href='/'>返回首頁</a>
    """

@app.route("/show_uj")
def show_uj():
    # 顯示 uj.jpg 的路由
    return """
    <h2>個人履歷</h2>
    <img src='/static/uj.jpg' width='600'>
    <br><br>
    <a href='/'>返回首頁</a>
    """
