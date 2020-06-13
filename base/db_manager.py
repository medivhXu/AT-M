# !/uer/bin/env python3
"""
@author: Medivh Xu
@file: db_manager.py
@time: 2020-02-27 12:22
"""

import pymysql
import contextlib
from loguru import logger
from config_loader import conf_load


@contextlib.contextmanager
def mysql(filename=None, **conf):
    """
    mysql连接方法
        examples:
                :type(env) == dict
                with mysql(**env) as cur:
                    cur.execute('select * from message.sms_log
                                where mobile=175001234567 group by send_time DESC limit 1;')
                    result = cur.fetchall()
                    return result
    :return: 游标
    """
    if filename:
        conf = conf_load(filename).read()
    else:
        if not conf:
            conf = conf_load('../__conf.yaml').read()['MYSQL']
    conn = pymysql.connect(**conf)
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cur
    except Exception as e:
        logger.error(e)
        conn.rollback()
    finally:
        conn.commit()
        cur.close()
        conn.close()
