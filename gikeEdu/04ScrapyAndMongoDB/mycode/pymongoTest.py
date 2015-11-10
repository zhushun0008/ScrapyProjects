# _*_ coding:utf-8 _*_
import pymongo

conn = pymongo.MongoClient()
tdb = conn.jikeEdu
post_info = tdb['test']
zhushun_Chinese = {'name':u'朱顺', 'age':'5', 'skill': 'Python'}
zhushun_English = {'name':'zhushun', 'age':'5', 'skill': 'Python'}
wangqiuyi_Chinese = {'name':u'王秋怡', 'age':'5', 'skill': 'Python'}
post_info.insert(zhushun_Chinese)
post_info.insert(zhushun_English)
post_info.insert(wangqiuyi_Chinese)

