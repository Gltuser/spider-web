import pymysql


def connection():
    """

    :return: 连接，游标
    """
    conn = pymysql.connect("localhost",
                            user='root',
                            password ='0102003',
                            db = 'spider')
    cursor = conn.cursor()
    return conn, cursor


def close_connection(conn,cursor):
    cursor.close()
    conn.close()


def query(sql, *par):
    """

    :param sql: sql查询语句
    :param par: 占位符参数
    :return: sql查询结果，tuple
    """
    conn, cursor = connection()
    cursor.execute(sql, par)
    res = cursor.fetchall()
    close_connection(conn, cursor)
    return res


def get_c1_data():
    """

    :return:最新的全国数据
    """
    sql = '''
    select * from domestic_live 
    where tem = (select tem from domestic_live order by tem desc limit 1)
    '''
    res = query(sql)
    return res[0]


def get_c2_data():
    """

    :return: (省份，确诊总数)
    """
    sql = '''
    select province,sum(confirm)
    from detail
    where update_time = (select update_time from detail
    order by update_time desc limit 1)
    group by province 
    '''
    res = query(sql)
    return res

def get_l1_data():
    """

    :return:
    """
    sql = '''
    select date,confirm,suspect,heal,dead,nowConfirm,nowSevere from history
    '''

    res = query(sql)
    return res


def get_l2_data():
    """

    :return:
    """
    sql = '''
        select date,confirm_add,suspect_add,heal_add,dead_add from history
        '''

    res = query(sql)
    return res


def get_r1_data():
    """

    :return:
    """
    sql = '''select * from
    (select city,confirm from detail 
    where province not in ('湖北','上海','北京','重庆','天津') 
    and update_time = (select update_time from detail order by update_time desc limit 1)
    union
    select province as city,sum(confirm) as confirm from detail
    where province in ('上海','北京','重庆','天津') 
    and update_time = (select update_time from detail order by update_time desc limit 1) group by province) as b
    order by confirm desc limit 10
    '''
    # sql2 = '''select * from
    # (select city,dead from detail
    # where province not in ('湖北','上海','北京','重庆','天津')
    # and update_time = (select update_time from detail order by update_time desc limit 1)
    # union
    # select province as city,sum(dead) as dead  from detail
    # where province in ('上海','北京','重庆','天津')
    # and update_time = (select update_time from detail order by update_time desc limit 1) group by province) as b
    # order by dead desc limit 10
    # '''

    # res1 = query(sql1)
    res = query(sql)

    return res


def get_r2_data():
    """

    :return:
    """
    sql = '''
    select content from topsearch order by dt desc limit 20
    '''
    res = query(sql)

    return res








