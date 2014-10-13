import json
from unittest import TestCase
import re
from datetime import date
import MySQLdb

sample_json_line = '{"developer": "labsdig", "developer_link": "/store/apps/developer?id=labsdig", "title": "Bunkatsukun", "app_url": "https://play.google.com/store/apps/details?id=labsdig.jp.geocities.bunkatsukun", "date_published": "January 21, 2012", "Description": " The whole width is divided at equal intervals with the arbitrary numbers of division.  ", "price": "0", "downloads": "100 - 500", "content_rating": "Everyone", "category": "", "operating_system": "2.1 and up", "rating": "5", "reviewers": "1"}'

class SQLDataDump:
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "root", "appsdb")

    def get_db_version(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        return '%s' % data
        pass

    def convert_object_to_insert_statement(self,json_object):
        # try:
        data = json.loads(json_object)
        sql="""INSERT INTO `appsdb`.`apps_default`
            (`price`,
            `developer`,
            `reviewers`,
            `title`,
            `dev_website`,
            `email`,
            `content_rating`,
            `date_published`,
            `operating_system`,
            `downloads`,
            `category`,
            `developer_link`,
            `app_url`,
            `Description`,
            `rating`)
            VALUES (%f, %s, %d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""" % \
            (float(data["price"]),
             data["developer"],
             int(data["reviewers"]),
             data["title"],
             data.get("dev_website", "Null"),
             data.get("email", "Null"),
             data["content_rating"],
             date(data["date_published"]), #should be fixed to fix the excution error!
             data["operating_system"],
             data["downloads"],
             data["category"],
             data["developer_link"],
             data["app_url"],
             data["Description"],
             data["rating"])
        print(sql)
        self.db.cursor().execute(sql)
        self.db.commit()
        return True
        # except:
        #     return False
        pass




    def __del__(self):
         self.db.close()

class SQLConnectionTest(TestCase):
    def setUp(self):
        self.instance = SQLDataDump()
        pass

    def test_connection(self):
        self.assertEqual(self.instance.get_db_version(), "5.6.21-log")
        pass

    def test_insert(self):
        self.assertTrue(self.instance.convert_object_to_insert_statement(sample_json_line))
        pass







