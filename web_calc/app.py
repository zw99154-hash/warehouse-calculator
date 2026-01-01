from flask import Flask, render_template, request, jsonify

# ① 创建 Flask 应用（你之前报错，就是少了这行）
app = Flask(__name__)


# ② 首页
@app.route('/')
def index():
    return render_template('index.html')


# ③ 计算接口（AJAX 调用）
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    # ===== 1. 取输入值（统一转 float）=====
    wl = float(data['warehouse_length'])
    ww = float(data['warehouse_width'])
    wh = float(data['warehouse_height'])

    gl = float(data['goods_length'])
    gw = float(data['goods_width'])
    gh = float(data['goods_height'])

    qty = float(data['goods_qty'])

    # ===== 2. 计算公式 =====
    usable_area = wl * ww
    usable_volume = wl * ww * wh

    projection_area = gl * gw
    space_volume = gl * gw * gh

    ground_ratio = (projection_area * qty) / usable_area*100
    stereo_ratio = (space_volume * qty) / usable_volume *100

    # ===== 3. 返回给前端 =====
    return jsonify({
        "usable_area": round(usable_area, 2),
        "usable_volume": round(usable_volume, 2),
        "projection_area": round(projection_area, 2),
        "space_volume": round(space_volume, 2),
        "ground_ratio": round(ground_ratio, 4),
        "stereo_ratio": round(stereo_ratio, 2)
    })


# ④ 启动程序
if __name__ == '__main__':
    app.run(debug=True)
