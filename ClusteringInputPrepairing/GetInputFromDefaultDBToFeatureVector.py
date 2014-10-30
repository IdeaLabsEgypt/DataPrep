# -*- coding: utf-8 -*-
import codecs

import json
from unittest import TestCase
import MySQLdb
from datetime import datetime

class PrepareFeatureVectorFromInputDB:
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "root", "appsdb", use_unicode=True, charset="utf8")

    def fetch_data(self):
        sql = "SELECT ID, reviewers, length(downloads), rating FROM appsdb.apps_default "
        cur = self.db.cursor()
        print "Executing query"
        success = cur.execute(sql)
        print success
        print "Starting loop"
        with codecs.open("resulting_features_with_IDs", 'w', encoding='utf8') as w:
            row = cur.fetchone()
            while row is not None:
                w.write(",".join([str(c) for c in row]))
                w.write("\n")
                row = cur.fetchone()

    def __del__(self):
        self.db.close()

if __name__ == "__main__":
    print "start"
    runner = PrepareFeatureVectorFromInputDB()
    runner.fetch_data()
