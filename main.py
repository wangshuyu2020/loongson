# from flask_script import Manager
from flask import render_template

from controller import create_app

# 创建APP对象
app = create_app('dev')


# # 创建脚本管理
# mgr = Manager(app)

# @app.route('/get_amb_tmp')
# def tmp():
#     return zzz.sxx()
# def abc():
#     result_dict = {1: 2, 3: 4, 5: 6}  # 结果dict
#     # for key, value in result_dict.items():
#     #     l_dict = {}
#     #     l_dict['name'] = key
#     #     l_dict['result'] = value
#     #     result_dict = dict(result_dict, **l_dict)
#     return result_dict

#
# @app.route("/")
# def index():
#     return render_template("index.html", abc={1: 2, 3: 4, 5: 6})

# @app.route("/abc")
# def api():
#     return abc()

if __name__ == '__main__':
    # mgr.run()
    app.run(threaded=True, host="127.0.0.1", port=7990)
