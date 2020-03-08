from flask import Flask
from flask import render_template
from flask import jsonify

import time
import utils
from jieba.analyse import extract_tags
import string


app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("main.html")


@app.route("/time")
def get_time():
    return time.strftime("%Y-%m-%d %X")


@app.route('/c1')
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({'confirm': data[1],
                    'heal': data[2],
                    'dead': data[3],
                    'nowConfirm': data[4],
                    'suspect': data[5],
                    'nowSevere': data[6]
                    })


@app.route('/c2')
def get_c2_data():
    data = utils.get_c2_data()
    r = []
    for i in data:
        r.append({"name": i[0], "value": int(i[1])})
    return jsonify({"data": r})


@app.route('/l1')
def get_l1_data():

    data = utils.get_l1_data()
    dt, confirm, suspect, heal, dead, now_confirm, now_severe = [], [], [], [], [], [], []

    for i in data[7:]:
        dt.append(i[0].strftime('%m-%d'))
        confirm.append(i[1])
        suspect.append(i[2])
        heal.append(i[3])
        dead.append(i[4])
        now_confirm.append(i[5])
        now_severe.append(i[6])

    return jsonify({'dt': dt,
                    'confirm': confirm,
                    'suspect': suspect,
                    'heal': heal,
                    'dead': dead,
                    'now_confirm': now_confirm,
                    'now_severe': now_severe,
                    })


@app.route('/l2')
def get_l2_data():
    data = utils.get_l2_data()
    dt, confirm_add, suspect_add, heal_add, dead_add = [], [], [], [], []
    for i in data[7:]:
        dt.append(i[0].strftime('%m-%d'))
        confirm_add.append(i[1])
        suspect_add.append(i[2])
        heal_add.append(i[3])
        dead_add.append(i[4])

    return jsonify({'dt': dt,
                    'confirm_add': confirm_add,
                    'suspect_add': suspect_add,
                    'heal_add': heal_add,
                    'dead_add': dead_add
                    })


@app.route('/r1')
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    for i in data:
        city.append(i[0])
        confirm.append(int(i[1]))

    return jsonify({'city': city,
                    'confirm': confirm
                    })


@app.route('/r2')
def get_r2_data():
    data = utils.get_r2_data()
    l = []
    for i in data:
        word = i[0].rstrip(string.digits)
        hot_index = i[0][len(word):]
        key_words = extract_tags(word)
        for j in key_words:
            if not j.isdigit():
                l.append({'name': j, 'value': hot_index})

    return jsonify({'data': l})


if __name__ == 'main':
    get_r2_data()

    app.run(debug=True)


