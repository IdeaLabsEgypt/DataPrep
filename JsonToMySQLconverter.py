# -*- coding: utf-8 -*-

import json
from unittest import TestCase
import MySQLdb
from datetime import datetime

sample_json_line = '{"developer": "labsdig", "developer_link": "/store/apps/developer?id=labsdig", "title": "Bunkatsukun", "app_url": "https://play.google.com/store/apps/details?id=labsdig.jp.geocities.bunkatsukun", "date_published": "January 21, 2012", "Description": " The whole width is divided at equal intervals with the arbitrary numbers of division.  ", "price": "0", "downloads": "100 - 500", "content_rating": "Everyone", "category": "", "operating_system": "2.1 and up", "rating": "5", "reviewers": "1"}'
sample_json_arabic_line = '{"developer": "بالعربي الفصيح", "developer_link": "/store/apps/developer?id=labsdig", "title": "Bunkatsukun", "app_url": "https://play.google.com/store/apps/details?id=labsdig.jp.geocities.bunkatsukun", "date_published": "January 21, 2012", "Description": " The whole width is divided at equal intervals with the arbitrary numbers of division.  ", "price": "0", "downloads": "100 - 500", "content_rating": "Everyone", "category": "", "operating_system": "2.1 and up", "rating": "5", "reviewers": "1"}'


class SQLDataDump:
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "root", "appsdb", use_unicode=True, charset="utf8")
        self.brokensqls = 0
        self.rejectedsqls = 0

    def get_db_version(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        return '%s' % data
        pass

    def convert_object_to_insert_statement(self, json_object):
        try:
            data = json.loads(json_object)
        except:
            self.brokensqls = self.brokensqls + 1
            return ""

        publish_date = datetime.strptime(data["date_published"], '%B %d, %Y').date()
        price = float(data["price"].strip("EGP ").replace(',', ''))
        developer = data.get("developer", "NA").replace('"', '\\"').replace('\\\\"', '\\"')
        description = data.get("Description", "NA").replace('"', '\\"').replace('\\\\"', '\\"')
        title = data.get("title", "NA").replace('"', '\\"').replace('\\\\"', '\\"')
        # print json_object
        sql = 'INSERT INTO `appsdb`.`apps_default` ' \
              '(`price`, ' \
              '`developer`, ' \
              '`reviewers`, ' \
              '`title`, ' \
              '`dev_website`, ' \
              '`email`, ' \
              '`content_rating`, ' \
              '`date_published`, ' \
              '`operating_system`, ' \
              '`downloads`, ' \
              '`category`, ' \
              '`developer_link`, ' \
              '`app_url`, ' \
              '`Description`, ' \
              '`rating`) ' \
              'VALUES (%f, "%s", %d, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");' % \
              (price,
               developer,
               int(data.get("reviewers", "NULL")),
               title,
               data.get("dev_website", "Null"),
               data.get("email", "Null"),
               data.get("content_rating", "NA"),
               publish_date,
               data.get("operating_system", "NA"),
               data.get("downloads", "0"),
               data.get("category", "NA"),
               data.get("developer_link", "NA"),
               data.get("app_url", "NA"),
               description,
               data.get("rating", "NA"))
        return sql

    def insert_into_db(self, sql):
        try:
            self.db.cursor().execute(sql)
            self.db.commit()
            return True
        except:
            print sql
            return False
        pass

    def run(self):
        counter = 0
        with open('apps_all_utf8_cleaned') as f:
            for line in f:
                sql = self.convert_object_to_insert_statement(line)
                success = self.insert_into_db(sql)
                if success == False:
                    self.rejectedsqls += 1

                counter += 1
                if counter % 1000 == 0:
                    # return counter
                    print counter
                    print self.brokensqls
                    print self.rejectedsqls
                    print "--------------"
        return 1000


    def __del__(self):
        self.db.close()


class SQLConnectionTest(TestCase):
    def setUp(self):
        self.instance = SQLDataDump()
        pass

    def test_connection(self):
        self.assertEqual(self.instance.get_db_version(), "5.6.21-log")
        pass

    def test_parsing_json_to_statement(self):
        expected_sql = u'INSERT INTO `appsdb`.`apps_default` (`price`, `developer`, `reviewers`, `title`, `dev_website`, `email`, `content_rating`, `date_published`, `operating_system`, `downloads`, `category`, `developer_link`, `app_url`, `Description`, `rating`) VALUES (0.000000, "labsdig", 1, "Bunkatsukun", "Null", "Null", "Everyone", "2012-01-12", "2.1 and up", "100 - 500", "", "/store/apps/developer?id=labsdig", "https://play.google.com/store/apps/details?id=labsdig.jp.geocities.bunkatsukun", " The whole width is divided at equal intervals with the arbitrary numbers of division.  ", "5");'
        self.assertEqual(self.instance.convert_object_to_insert_statement(sample_json_line), expected_sql)
        pass

    def test_parsing_json_to_statement_non_english(self):
        expected_sql = u'INSERT INTO `appsdb`.`apps_default` (`price`, `developer`, `reviewers`, `title`, `dev_website`, `email`, `content_rating`, `date_published`, `operating_system`, `downloads`, `category`, `developer_link`, `app_url`, `Description`, `rating`) VALUES (0.000000, "بالعربي الفصيح", 1, "Bunkatsukun", "Null", "Null", "Everyone", "2012-01-12", "2.1 and up", "100 - 500", "", "/store/apps/developer?id=labsdig", "https://play.google.com/store/apps/details?id=labsdig.jp.geocities.bunkatsukun", " The whole width is divided at equal intervals with the arbitrary numbers of division.  ", "5");'
        self.assertEqual(self.instance.convert_object_to_insert_statement(sample_json_arabic_line), expected_sql)
        pass

    def test_insert_statemnt(self):
        sql = self.instance.convert_object_to_insert_statement(sample_json_line)
        self.assertTrue(self.instance.insert_into_db(sql))
        pass

    def test_insert_statement_non_english(self):
        sql = self.instance.convert_object_to_insert_statement(sample_json_arabic_line)
        self.assertTrue(self.instance.insert_into_db(sql))
        pass

    def test_run_1000(self):
        self.assertEqual(self.instance.run(), 1000)







