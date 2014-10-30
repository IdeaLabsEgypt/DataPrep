# -*- coding: utf-8 -*-
import codecs

import json
from unittest import TestCase
import MySQLdb
from datetime import datetime

class PrepareFeatureVectorFromInputDB:
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "root", "appsdb", use_unicode=True, charset="utf8")

    def add_clusters(self, tablename, clusterfilename):
        id =1
        with codecs.open(clusterfilename) as f:
            for line in f:
                sql = "UPDATE %s SET cluster_id = %d WHERE ID = %d" % (tablename, int(line), id)
                id +=1
                self.insert_into_db(sql)
                # print success
                if id % 1000 == 0:
                    print id
                    self.db.commit()


    def insert_into_db(self, sql):
        try:
            self.db.cursor().execute(sql)
            return True
        except:
            print sql
            return False
        pass

    def __del__(self):
        self.db.close()

if __name__ == "__main__":
    print "start"
    runner = PrepareFeatureVectorFromInputDB()
    runner.add_clusters("appsdb.clustered_apps_kmeans", "clusters_kmeans_7clusters")
