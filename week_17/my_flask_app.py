from flask import Flask, render_template, request  # 👈 這裡補上了 request

app = Flask(__name__)

# 1. 首页：让它直接渲染 index.html 网页文件
@app.route('/')
def index():
    # 提醒：记得要在 app.py 的同级目录下建一个叫 templates 的文件夹，里面放 index.html
    return render_template('index.html')

# 2. 关于我们页面
@app.route('/about')
def about():
    return '这是关于我们的页面！'

# 3. 用户中文打招呼
@app.route('/user/<name>')
def show_chinese_profile(name): # 改名，避免冲突
    return f'你好，{name}！'

# 4. 纯 Hello 页面
@app.route('/hello')
def hello():
    return 'Hello.'

# 5. 用户英文打招呼
@app.route('/hello/<name>')
def show_english_profile(name): # 改名，避免冲突
    return f'Hello, {name}！'

# ================= 新增下面這個判斷邏輯 =================
@app.route('/submit', methods=['POST'])
def submit():
    # 抓取前端網頁中 name="user_input" 的輸入框內容
    user_text = request.form.get('user_input')

    # 判斷：有沒有輸入？或者是不是只打了空白鍵？
    if not user_text or user_text.strip() == "":
        return """
        <h1 style='color: red;'>❌ 錯誤：你沒有輸入任何東西！</h1>
        <a href='/'><button>返回首頁</button></a>
        """
    else:
        return f"""
        <h1 style='color: green;'>✅ 收到資料：你輸入了 {user_text}</h1>
        <a href='/'><button>返回首頁</button></a>
        """
# =======================================================

if __name__ == "__main__":
    # 加上 host='0.0.0.0'
    app.run(host='0.0.0.0', debug=True)