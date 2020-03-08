import requests
import json
import re
import pymysql
import time


connection = pymysql.connect('localhost', 'root', '0102003', 'spider')
curser = connection.cursor()


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                              (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    r = requests.get(url, headers=headers)
    return r.text


def get_info(data_other, data_h5):

    hs_dic = {}
    for i in data_other['chinaDayList']:
        i['deadRate'] = float(i['deadRate'])
        i['healRate'] = float(i['healRate'])
        i['date'] = time.strftime('%Y-%m-%d', time.strptime('2020.'+i['date'], '%Y.%m.%d'))
        hs_dic[i.pop('date')] = i

    for i in data_other['chinaDayAddList']:
        data_add = {
            'confirm_add': i['confirm'],
            'suspect_add': i['suspect'],
            'dead_add': i['dead'],
            'heal_add': i['heal'],
            'date': time.strftime('%Y-%m-%d', time.strptime('2020.'+i['date'], '%Y.%m.%d'))
        }

        hs_dic[data_add.pop('date')].update(data_add)

    detail_dic_cn = []
    update_time = data_h5['lastUpdateTime']
    for i in data_h5['areaTree'][0]['children']:
        province = i.get('name')
        for j in i['children']:
            dic = {
                'update_time':update_time,
                'province': province,
                'city': j.get('name'),
                'confirm': j.get('total').get('confirm'),
                'confirm_add': j.get('today').get('confirm'),
                'suspect': j.get('total').get('suspect'),
                'dead': j.get('total').get('dead'),
                'deadrate': j.get('total').get('deadRate'),
                'heal': j.get('total').get('heal'),
                'healrate': j.get('total').get('healRate'),
            }
            detail_dic_cn.append(dic)

    domestic_live = {}
    domestic_live[data_h5.get('lastUpdateTime')] = data_h5.get('chinaTotal')

    return hs_dic, detail_dic_cn, domestic_live


def save_to_history(data):
    insert = 'insert into history values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    for k, v in data.items():
        try:
            if curser.execute(insert, [k, v.get('confirm'), v.get('confirm_add'),v.get('suspect'), v.get('suspect_add'),
                                       v.get('heal'), v.get('heal_add'),v.get('dead'), v.get('dead_add'),
                                       v.get('nowConfirm'), v.get('nowSevere'), v.get('deadRate'), v.get('healRate')]):
                connection.commit()
                print('存储成功', data)

        except Exception as e:
            print(e)


def update_domestic_live(data):
    insert = 'insert into domestic_live values(%s,%s,%s,%s,%s,%s,%s)'
    dic = data[list(data.keys())[0]]
    try:
        curser.execute(insert, (list(data.keys())[0], dic.get('confirm'), dic.get('heal'),
                                   dic.get('dead'), dic.get('nowConfirm'), dic.get('suspect'), dic.get('nowSevere')))
        connection.commit()
    except Exception as e:
        print(e)


def update_details(data):

    select = 'select %s = (select update_time from detail order by id desc limit 1)'

    try:
        curser.execute(select, data[0]['update_time'])
        if not curser.fetchone()[0]:
            print(f'{time.asctime()} 开始更新数据')
            for i in data:
                keys = ','.join(i.keys())
                insert = 'insert into detail({}) values{}'.format(keys, tuple(i.values()))
                curser.execute(insert)
            connection.commit()
            print(f'{time.asctime()}完成数据更新')
        else:
            print('已是最新数据')
    except Exception as e:
        print(e)


def update_history(data):
    insert = 'insert into history values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    query = 'select * from history where date = %s'
    try:
        print(f'{time.asctime()} 开始更新历史数据')
        for k, v in data.items():
            if not curser.execute(query, k):
                curser.execute(insert, [k, v.get('confirm'), v.get('confirm_add'),
                                        v.get('suspect'), v.get('suspect_add'),
                                        v.get('heal'), v.get('heal_add'),
                                        v.get('nowConfirm'), v.get('nowSevere'),
                                        v.get('dead'), v.get('dead_add'),
                                        v.get('deadRate'), v.get('healRate')])
        connection.commit()
        print(f'{time.asctime()}更新完毕')
    except Exception as e:
        print(e)


def main(u_h5, u_other):

    data_other = json.loads(json.loads(get_html(u_other)[42:-1])['data'])
    data_h5 = json.loads(json.loads(get_html(u_h5)[41:-1])['data'])
    data = get_info(data_other, data_h5)
    save_to_history(data[0])
    update_details(data[1])
    update_history(data[0])
    update_domestic_live(data[2])


if __name__ == '__main__':
    url_h5 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=' \
             'jQuery34106621544254756455_1583076180092&_=1583076180093'
    url_other = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=' \
                'jQuery341006733527615872781_1583110821646&_=1583110821647'
    main(url_h5, url_other)
    connection.close()
