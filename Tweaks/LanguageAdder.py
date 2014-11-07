# -*- coding: utf-8 -*-
from unittest import TestCase
import codecs
import MySQLdb
import langid

class LanguageAdder:
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "root", "appsdb", use_unicode=True, charset="utf8")
        pass

    def detect_language(self, doc):
        return langid.classify(doc)[0]

    def detect_language_tuple(self, doc):
        return langid.classify(doc)

    def run_test_file(self, inputfile, outputfile):
        readf = codecs.open(inputfile, "r", "utf-8")
        writef = codecs.open(outputfile, "w", "utf-8")
        for line in readf:
            writef.write(self.detect_language(line)+ "\n")
        writef.close()
        readf.close()
        return 1

    def get_rows_count(self, tablename):
        sql = "SELECT count(*) FROM %s limit 1000"%tablename
        cur = self.db.cursor()
        print "Executing query"
        success = cur.execute(sql)
        row = cur.fetchone()
        return long(row[0])


    def fetch_all_descriptions(self, tablename):
        desc_dict = {}
        sql = "SELECT ID, description FROM %s" % tablename
        cur = self.db.cursor()
        print "Executing query"
        cur.execute(sql)
        row = cur.fetchone()
        while row is not None:
            desc_dict[row[0]] = row[1]
            row = cur.fetchone()
        return desc_dict

    def fetch_description_by_id(self, tablename, id):
        sql = "SELECT description FROM %s WHERE ID = %d" % (tablename, id)
        cur = self.db.cursor()
        cur.execute(sql)
        return cur.fetchone()[0].strip()

    def unify_lang(self, lang_id):
        l = lang_id[0]
        if l == "fa":
            return "ar"
        return l

    def update_with_language(self, tablename):
        lang_set = set()
        max = self.get_rows_count(tablename)
        for id in range(1, max+1):
            desc = self.fetch_description_by_id(tablename, id)
            lang = self.unify_lang(langid.classify(desc))
            lang_set.add(lang)
            sql = 'UPDATE %s SET lang_id = "%s" WHERE ID = %d' %(tablename, lang, id)
            self.insert_into_db(sql,False)
            if id % 5000 == 0:
                print "%d -> %s" % (id, lang_set)
                self.commit_to_db()

        return max

    def insert_into_db(self, sql, autocommit):
        try:
            self.db.cursor().execute(sql)
            if autocommit:
                self.commit_to_db()
            return True
        except:
            print sql
            return False
        pass

    def commit_to_db(self):
        self.db.commit()

    def __del__(self):
        self.db.close()

if __name__ == "__main__":
    print "start"
    module = LanguageAdder()
    module.update_with_language("clustered_apps_kmeans_2")

class testAddLanguage(TestCase):
    def setUp(self):
        self.langadder = LanguageAdder()
        pass

    def test_detect_language(self):
        self.assertEqual(self.langadder.detect_language("This is a test"), "en")
        self.assertEqual(self.langadder.detect_language("je suis tres content"), "fr")
        self.assertEqual(self.langadder.detect_language("من سيربح المليون"), "ar")
        self.assertEqual(self.langadder.detect_language("がんばれ！ルルロロ　タッチ・ザ・ナンバーズ：公式コラボアプリ"), "ja")

    def test_file(self):
        # self.assertEqual(self.langadder.run_test_file("test_input","test_output"),1)
        self.assertEqual(self.langadder.run_test_file("test_input_description","test_output"),1)

    def test_rows_count(self):
        self.assertEqual(self.langadder.get_rows_count("clustered_apps_em_2"),1021380)

    def test_fetch_description_by_id(self):
        self.assertEqual(self.langadder.fetch_description_by_id("clustered_apps_em_2", 2), "Dr. ComputerNew game from SUD Inc.How to play :Compose equation to meet numbers in the top blackboard with the colored numbers and symbols.SUD Inc.")

    def test_fetch_all_descriptions(self):
        self.assertEqual(len(self.langadder.fetch_all_descriptions("clustered_apps_em_2")),1000)
        self.assertEqual(self.langadder.fetch_all_descriptions("clustered_apps_em_2")[2], " Dr. ComputerNew game from SUD Inc.How to play :Compose equation to meet numbers in the top blackboard with the colored numbers and symbols.SUD Inc.  ")

    def test_update_with_language(self):
        self.assertEqual(self.langadder.update_with_language("clustered_apps_em_2"), 1021380)