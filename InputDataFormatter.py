# -*- coding: utf-8 -*-

# from __future__ import print_function
import codecs
import json
from unittest import TestCase
import re



# {"price": "0", "developer": "MMH Dev", "reviewers": "8270", "title": "English Arabic Dictionary",
# "dev_website": "https://www.google.com/url?q=http://www.iquest-es.com&sa=D&usg=AFQjCNG8o0hL6sk-VOmUJ_JJdBrlR94k_w",
#  "email": "mmh@iquest-es.com",
#  "content_rating": "Everyone",
#  "date_published": "September 8, 2014",
#  "operating_system": "2.3.3 and up",
#  "downloads": "500,000 - 1,000,000",
#  "category": "Education",
#  "developer_link": "/store/apps/developer?id=MMH+Dev",
#  "app_url": "https://play.google.com/store/apps/details?id=com.mmh.qdic",
#  "Description": " Q DictionaryFree offline Arabic-English and English-Arabic Dictionary, with simple, beautiful and easy
#  to use interface.First dictionary to support translation from other applications in a very simple way.Q Dictionary
#  Features:- English Arabic and Arabic English translation- Used offline- Cross apps translation to translated from
#  other apps like web browser, mail or sms without opining Q Dictionary and without interruptions- \u0650Automatic
#  detection of word root- 87k+ English words, 94k+ Arabic words including a lot of abbreviations- Automatic language
#  detection- Fast search with automatic suggestions- Speech-To-Text- English words Text-To-Speech- Word search history-
#  Favorite words list- Copy or share translation- Search for words on Google, Wikipedia or Wiktionary  ",
#  "rating": "4.188028812408447"}

# sample_non_english_input = '{"price": "0", "developer": "Mawuood Academy", "reviewers": "29262", "title": "\u062a\u0639\u0644\u0645 \u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629", "dev_website": "https://www.google.com/url?q=http://www.englishforarabs.com/&sa=D&usg=AFQjCNEHJyLmd7Sa2Y1g-gfjv3wIYKnhDw", "email": "youme9957@yahoo.com", "content_rating": "Everyone", "date_published": "July 9, 2014", "operating_system": "2.3 and up", "downloads": "1,000,000 - 5,000,000", "category": "Education", "developer_link": "/store/apps/developer?id=Mawuood+Academy", "app_url": "https://play.google.com/store/apps/details?id=mawuoodacademy.english.phrases", "Description": " \u062a\u0639\u0644\u0645 \u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629 \u0645\u0639 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0627\u0644\u0639\u0631\u0628\u064a \u0627\u0644\u0627\u0634\u0647\u0631 \u0639\u0644\u0649 \u0627\u0644\u0627\u0637\u0644\u0627\u0642 \u0648\u0627\u0644\u0630\u064a \u0644\u064a\u0633 \u0644\u0647 \u0645\u062b\u064a\u0644 \u0645\u0642\u0627\u0631\u0646\u0629 \u0645\u0639 \u0628\u0642\u064a\u0629 \u0627\u0644\u0628\u0631\u0627\u0645\u062c \u0627\u0644\u0627\u062e\u0631\u0649. \u0633\u0624\u0627\u0644 : \u0645\u0627\u0627\u0644\u0630\u064a \u064a\u0645\u064a\u0632 \u0628\u0631\u0646\u0627\u0645\u062c\u0646\u0627 \u0648\u064a\u062c\u0639\u0644\u0629 \u0627\u0644\u0627\u062e\u062a\u064a\u0627\u0631 \u0627\u0644\u0627\u0648\u0644 \u0644\u0643\u0644 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u064a\u0646 \u061f- \u0628\u0631\u0646\u0627\u0645\u062c\u0646\u0627 \u0634\u0645\u0648\u0644\u064a \u062d\u064a\u062b \u0633\u062a\u062c\u062f \u0641\u064a\u0647 \u0643\u0644 \u0645\u0627\u062a\u062d\u062a\u0627\u062c \u0627\u0644\u064a\u0647 \u0633\u0648\u0627\u0621 \u0643\u0646\u062a \u0628\u0645\u0633\u062a\u0648\u0649 \u0645\u0628\u062a\u062f\u0623 \u0627\u0648 \u0645\u062a\u0648\u0633\u0637 \u0627\u0648 \u062d\u062a\u0649 \u0645\u0633\u062a\u0648\u0649 \u0645\u062a\u0642\u062f\u0645 \u0648\u0643\u0630\u0644\u0643 \u0627\u0644\u0634\u0631\u062d \u0645\u0628\u0633\u0637 \u0648\u0628\u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0639\u0631\u0628\u064a\u0629 \u064a\u0646\u0627\u0633\u0628 \u0643\u0644 \u0627\u0644\u0645\u0633\u062a\u0648\u064a\u0627\u062a- \u0628\u0631\u0646\u0627\u0645\u062c\u0646\u0627 \u0627\u0644\u0648\u062d\u064a\u062f \u0627\u0644\u0630\u064a \u064a\u062f\u0639\u0645 \u062f\u0631\u0648\u0633\u0647 \u0628\u0627\u0644\u0646\u0637\u0642 \u0627\u0644\u0635\u062d\u064a\u062d \u0645\u0646 \u0642\u0628\u0644 \u0634\u062e\u0635 \u062d\u0642\u064a\u0642\u064a \u0639\u0644\u0649 \u0639\u0643\u0633 \u0627\u0644\u0628\u0631\u0627\u0645\u062c \u0627\u0644\u0627\u062e\u0631\u0649 \u0648\u0627\u0644\u062a\u064a \u062a\u0633\u062a\u062e\u062f\u0645 \u0627\u0644\u0646\u0637\u0642 \u0627\u0644\u0627\u0644\u064a \u0627\u0644\u062e\u0627\u0635 \u0628\u0627\u0644\u0647\u0627\u062a\u0641 \u0648\u0627\u0644\u0630\u064a \u064a\u0641\u062a\u0642\u062f \u0627\u0644\u0649 \u0627\u0644\u062f\u0642\u0629 \u062d\u064a\u062b \u0627\u0646\u0627\u063a\u0644\u0628 \u0645\u062e\u0627\u0631\u062c \u0627\u0644\u062d\u0631\u0648\u0641 \u0641\u064a \u0627\u0644\u0643\u0644\u0645\u0627\u062a \u063a\u064a\u0631 \u0648\u0627\u0636\u062d\u0629 \u0627\u0648 \u063a\u064a\u0631 \u0633\u0644\u064a\u0645\u0629 \u0648 \u0628\u0627\u0644\u062a\u0627\u0644\u064a \u064a\u0646\u0639\u0643\u0633 \u0633\u0644\u0628\u0627\u064b \u0639\u0644\u0649 \u0627\u0644\u0644\u0647\u062c\u0629 \u0627\u0644\u062a\u064a \u0633\u0648\u0641 \u062a\u0643\u062a\u0633\u0628\u0647\u0627 \u0627\u062b\u0646\u0627\u0621 \u0627\u0644\u062a\u0639\u0644\u0645 \u0648\u0627\u0646\u0627 \u0643\u0645\u062e\u062a\u0635 \u0628\u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629 \u0644\u0627 \u0627\u0646\u0635\u062d \u0628\u0647 \u0627\u0628\u062f\u0627\u064b\u0633\u0624\u0627\u0644 : \u0645\u0627 \u0641\u0627\u0626\u062f\u0629 \u0627\u0646 \u062a\u062a\u0639\u0644\u0645 \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629 \u0648\u0627\u0646\u062a \u0644\u0627 \u062a\u0633\u062a\u0637\u064a\u0639 \u0627\u0646 \u062a\u0641\u0647\u0645 \u0645\u0627\u064a\u0642\u0648\u0644\u0648\u0647 \u0644\u0643 \u0627\u0635\u062d\u0627\u0628 \u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0627\u0645 \u061f- \u0627\u0646 \u0645\u0627\u064a\u0645\u064a\u0632 \u0628\u0631\u0646\u0627\u0645\u062c\u0646\u0627 \u0647\u0648 \u0627\u0646\u0646\u0627 \u0646\u0642\u062f\u0645 \u0644\u0643\u0645 \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629 \u0627\u0644\u062d\u0642\u064a\u0642\u064a\u0629 \u0648\u0627\u0644\u062a\u064a \u0633\u0648\u0641 \u062a\u0633\u0645\u0639\u0647\u0627 \u0641\u064a \u0627\u0644\u0634\u0627\u0631\u0639 \u0627\u0648 \u0641\u064a \u0627\u0644\u0639\u0645\u0644 \u0627\u0648 \u0641\u064a \u0627\u0644\u0627\u0641\u0644\u0627\u0645 \u062d\u064a\u062b \u0627\u0639\u062a\u0645\u062f\u0646\u0627 \u0627\u0644\u0639\u0628\u0627\u0631\u0627\u062a \u0648\u0627\u0644\u0645\u0635\u0637\u0644\u062d\u0627\u062a \u0648\u0627\u0644\u062d\u0648\u0627\u0631\u0627\u062a \u0627\u0644\u062a\u064a \u064a\u0633\u062a\u062e\u062f\u0645\u0647\u0627 \u0627\u0644\u0646\u0627\u0633 \u0627\u0644\u0645\u062d\u0644\u064a\u0648\u0646\u0627\u062b\u0646\u0627\u0621 \u0645\u0645\u0627\u0631\u0633\u0629 \u0627\u0645\u0648\u0631 \u0627\u0644\u062d\u064a\u0627\u0629 \u0627\u0644\u064a\u0648\u0645\u064a\u0629 . \u0648\u0643\u0630\u0644\u0643 \u0648\u0641\u0631\u0646\u0627 \u0644\u0643\u0645 \u0645\u0627\u0627\u0646\u062a\u0645 \u0628\u062d\u0627\u062c\u0629 \u0627\u0644\u064a\u0647 \u0641\u0642\u0637 \u0628\u0639\u064a\u062f\u0627 \u0639\u0646 \u0627\u0644\u062a\u0639\u0642\u064a\u062f \u0648\u0627\u0644\u0627\u0633\u0631\u0641 \u0641\u064a \u0627\u062e\u062a\u064a\u0627\u0631 \u0627\u0644\u062f\u0631\u0648\u0633 \u0633\u0624\u0627\u0644 : \u0647\u0644 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0641\u0639\u0644\u0627\u064b \u0634\u0645\u0648\u0644\u064a \u0648\u0645\u062a\u062c\u062f\u062f \u0641\u064a \u0645\u062d\u062a\u0648\u0627\u0647 \u061f- \u0628\u0631\u0646\u0627\u0645\u062c\u0646\u0627 \u0641\u0639\u0644\u0627\u064b \u0634\u0645\u0648\u0644\u064a \u0648 \u0645\u062a\u062c\u062f\u062f \u0641\u064a \u0645\u062d\u062a\u0648\u0627\u0647 \u062d\u064a\u062b \u064a\u062a\u0645 \u0627\u0636\u0627\u0641\u0629 \u062f\u0631\u0648\u0633 \u0648\u0627\u0642\u0633\u0627\u0645 \u062c\u062f\u064a\u062f\u0629 \u0628\u0634\u0643\u0644 \u0634\u0628\u0647 \u064a\u0648\u0645\u064a \u0648\u062c\u0645\u064a\u0639 \u0627\u0644\u062f\u0631\u0648\u0633 \u0645\u062a\u0631\u062c\u0645\u0629 \u0644\u0644\u0639\u0631\u0628\u064a\u0629 \u0648\u0645\u062f\u0639\u0648\u0645\u0629 \u0628\u0627\u0644\u0635\u0648\u062a \u0641\u0627\u0644\u062d\u062f \u0627\u0644\u0627\u0646 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u064a\u0642\u062f\u0645\u0627\u0644\u0642\u0648\u0627\u0639\u062f \u0648\u0627\u0644\u0627\u0635\u0648\u0627\u062a \u0648\u0627\u0644\u0645\u0641\u0631\u062f\u0627\u062a \u0648\u0627\u0644\u0639\u0628\u0627\u0631\u0627\u062a \u0648\u0627\u0644\u0645\u0635\u0637\u0644\u062d\u0627\u062a \u0648\u0627\u0644\u0645\u0631\u0627\u062f\u0641\u0627\u062a \u0648\u0627\u0644\u0645\u062d\u0627\u062f\u062b\u0627\u062a \u0648\u0627\u0644\u0627\u062e\u062a\u0628\u0627\u0631\u0627\u062a \u0627\u0644\u0641\u0648\u0631\u064a\u0629 \u0648\u0627\u0644\u0627\u0641\u0639\u0627\u0644 \u0648\u0627\u0644\u0643\u062b\u064a\u0631 \u0627\u0644\u0643\u062b\u064a\u0631 \u0642\u0627\u062f\u0645 \u0628\u0623\u0630\u0646 \u0627\u0644\u0644\u0647 \u0639\u0632 \u0648\u062c\u0644\u0648\u0644\u0643\u064a \u062a\u0633\u062a\u0637\u064a\u0639 \u0627\u0646 \u062a\u062a\u062d\u062f\u062b \u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629 \u0628\u0634\u0643\u0644 \u0633\u0631\u064a\u0639 \u0648\u0628\u0648\u0642\u062a \u0642\u0635\u064a\u0631 \u0627\u0630\u0646 \u0639\u0644\u064a\u0643 \u0627\u0646 \u062a\u062a\u0639\u0644\u0645 \u0648\u062a\u062d\u0641\u0638 \u0627\u0644\u0639\u0628\u0627\u0631\u0627\u062a \u0627\u0644\u0627\u0633\u0627\u0633\u064a\u0629\u0644\u0647\u0630\u0647 \u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0639\u0627\u0644\u0645\u064a\u0629 \u0641\u0647\u0630\u0627 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0633\u0648\u0641 \u064a\u0633\u0627\u0639\u062f\u0643 \u0639\u0644\u0649 \u0627\u0646 \u062a\u062a\u062d\u062f\u062b \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629 \u0628\u0623\u0633\u0631\u0639 \u0648\u0642\u062a \u0645\u0645\u0643\u0646 !!\u062a\u0645 \u0627\u0639\u062f\u0627\u062f \u0647\u0630\u0627 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0628\u0634\u0643\u0644 \u062e\u0627\u0635 \u0644\u0643\u064a \u064a\u0633\u0627\u0639\u062f\u0643 \u0639\u0644\u0649 \u0628\u0646\u0627\u0621 \u0627\u0633\u0627\u0633 \u0635\u062d\u064a\u062d \u0648\u0642\u0648\u064a \u0641\u064a \u0647\u0630\u0647 \u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u062a\u064a \u0627\u0635\u0628\u062d\u062a \u0636\u0631\u0648\u0631\u0629 \u0645\u0644\u062d\u0629 \u0641\u064a \u0648\u0642\u062a\u0646\u0627 \u0627\u0644\u062d\u0627\u0636\u0631 .\u0647\u0630\u0627 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0647\u0648 \u0639\u0628\u0627\u0631\u0629 \u0639\u0646 \u0643\u0648\u0631\u0633 \u0643\u0627\u0645\u0644 \u0644\u062a\u0639\u0644\u064a\u0645 \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629 \u0644\u0644\u0645\u0628\u062a\u062f\u0626\u064a\u0646 \u062d\u064a\u062b \u0627\u0646\u0643 \u0633\u0648\u0641 \u062a\u062c\u062f \u0641\u064a\u0647 \u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0643\u062b\u0631 \u0645\u0646 \u0627\u0644\u0645\u062f\u0631\u0633\u0629 \u0627\u0648 \u062d\u062a\u0649 \u0627\u0644\u0645\u0639\u0647\u062f\u0645\u0644\u0627\u062d\u0638\u0629\u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u0645\u062f\u0639\u0648\u0645 \u0628\u0627\u0644\u0635\u0648\u062a !! \u0648\u0644\u0633\u0645\u0627\u0639 \u0646\u0637\u0642 \u0627\u0644\u0643\u0644\u0645\u0629 \u0627\u0636\u063a\u0637 \u0639\u0644\u0649 \u0627\u0644\u0643\u0644\u0645\u0629 \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629 \u0648\u0633\u0648\u0641 \u064a\u062a\u0645 \u0646\u0637\u0642 \u0627\u0644\u0643\u0644\u0645\u0629 \u0628\u0634\u0643\u0644 \u0645\u0628\u0627\u0634\u0631\u0645\u0645\u064a\u0632\u0627\u062a \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c\u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u064a\u062d\u062a\u0648\u064a \u0639\u0644\u0649 \u0639\u062f\u062f \u0647\u0627\u0626\u0644 \u0645\u0646 \u0627\u0644\u0639\u0628\u0627\u0631\u0627\u062a \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629 \u0648\u0627\u0644\u062a\u064a \u0647\u064a \u0627\u0644\u0627\u0647\u0645 \u0644\u0628\u0646\u0627\u0621 \u0627\u0633\u0627\u0633 \u0642\u0648\u064a \u0648\u0635\u062d\u064a\u062d \u0641\u064a \u0647\u0630\u0647 \u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0639\u0627\u0644\u0645\u064a\u0629 \u0648\u0627\u0644\u0627\u0643\u062b\u0631 \u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u0641\u064a \u0627\u0644\u062d\u064a\u0627\u0629 \u0627\u0644\u064a\u0648\u0645\u064a\u0629\u062c\u0648\u062f\u0629 \u0627\u0644\u0635\u0648\u062a \u0639\u0627\u0644\u064a\u0629 \u062c\u062f\u0627\u064b \u0645\u0639 \u0645\u0631\u0627\u0639\u0627\u0629 \u0633\u0631\u0639\u0629 \u0646\u0637\u0642 \u0627\u0644\u0639\u0628\u0627\u0631\u0629\u062c\u0645\u064a\u0639 \u0627\u0644\u0639\u0628\u0627\u0631\u0627\u062a \u062a\u0645 \u062a\u0633\u062c\u064a\u0644\u0647\u0627 \u0645\u0646 \u0642\u0628\u0644 \u0645\u062a\u062d\u062f\u062b \u0627\u0635\u0644\u064a \u0645\u062a\u062e\u0635\u0635\u062a\u0645 \u062a\u0631\u062c\u0645\u0629 \u062c\u0645\u064a\u0639 \u0647\u0630\u0647 \u0627\u0644\u0639\u0628\u0627\u0631\u0627\u062a \u0648\u0627\u0644\u0627\u0645\u062b\u0644\u0629 \u0627\u0644\u0645\u0648\u062c\u0648\u062f\u0629 \u0641\u064a \u062f\u0631\u0648\u0633 \u0627\u0644\u0642\u0648\u0627\u0639\u062f \u0627\u0644\u0649 \u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0639\u0631\u0628\u064a\u0629 \u0644\u0643\u064a \u062a\u0643\u0648\u0646 \u0627\u0644\u0641\u0627\u0626\u062f\u0629 \u0627\u0643\u0628\u0631 \u0628\u062d\u064a\u062b \u062a\u0641\u0647\u0645 \u0627\u0644\u0645\u0639\u0646\u0649 \u0648\u062a\u062d\u0641\u0638 \u0627\u0644\u0646\u0637\u0642 \u0627\u0644\u0635\u062d\u064a\u062d . \u0627\u063a\u0644\u0628 \u0627\u0644\u062f\u0631\u0648\u0633 \u0627\u0644\u0635\u0648\u062a\u064a\u0629 \u0645\u062f\u0639\u0648\u0645\u0629 \u0628\u0627\u0644\u0627\u0633\u0626\u0644\u0629 \u0648\u0627\u062c\u0648\u0628\u062a\u0647\u0627 \u0644\u0643\u064a \u062a\u062a\u0639\u0644\u0645 \u0643\u064a\u0641 \u062a\u0633\u0623\u0644 \u0648\u0643\u064a\u0641 \u062a\u062c\u064a\u0628\u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u064a\u062f\u0639\u0645 \u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0639\u0631\u0628\u064a\u0629 \u0628\u0634\u0643\u0644 \u0643\u0627\u0645\u0644\u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c \u064a\u062d\u062a\u0627\u062c \u0627\u0644\u0649 \u0627\u0644\u0627\u0646\u062a\u0631\u0646\u062a \u0644\u0643\u064a \u064a\u0639\u0645\u0644\u0627\u0642\u0633\u0627\u0645 \u0627\u0644\u0628\u0631\u0646\u0627\u0645\u062c1- \u0642\u0633\u0645 \u0627\u0644\u0642\u0648\u0627\u0639\u062f : \u062d\u064a\u062b \u0633\u062a\u062c\u062f \u0641\u064a\u0647 \u0634\u0631\u062d \u0645\u0641\u0635\u0644 \u0644\u062c\u0645\u064a\u0639 \u0627\u0644\u0645\u0648\u0627\u0636\u064a\u0639 \u0645\u062f\u0639\u0648\u0645 \u0628\u0627\u0644\u0627\u0645\u062b\u0644\u0629 \u0648\u0627\u0644\u0635\u0648\u062a2- \u0642\u0633\u0645 \u0627\u0644\u0627\u0635\u0648\u062a : \u0634\u0631\u062d \u0643\u0627\u0645\u0644 \u0644\u0644\u0627\u0635\u0648\u0627\u062a3- \u0642\u0633\u0645 \u0627\u0644\u0645\u0635\u0637\u0644\u062d\u0627\u062a : \u0627\u0634\u0647\u0631 \u0627\u0644\u0645\u0635\u0637\u0644\u062d\u0627\u062a \u0648\u0627\u0643\u062b\u0631\u0647\u0627 \u0627\u0633\u062a\u062e\u062f\u0627\u06454- \u0642\u0633\u0645 \u0627\u0644\u0645\u0641\u0631\u062f\u0627\u062a  : \u0643\u0644 \u0645\u0627\u062a\u062d\u062a\u0627\u062c \u0644\u0628\u0646\u0627\u0621 \u0645\u062e\u0632\u0648\u0646 \u0644\u063a\u0648\u064a \u0642\u0648\u064a \u0648\u0631\u0635\u064a\u0646 \u0648\u0645\u062f\u0639\u0648\u0645 \u0628\u0627\u0644\u0646\u0637\u0642 \u0627\u0644\u0635\u062d\u064a\u062d5- \u0642\u0633\u0645 \u0627\u0644\u0639\u0628\u0627\u0631\u0627\u062a : \u062a\u0645 \u0627\u0636\u0627\u0641\u0629 \u0627\u0644\u0639\u062f\u064a\u062f \u0645\u0646 \u0627\u0644\u0639\u0628\u0627\u0631\u0627\u062a \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629 \u062d\u064a\u062b \u062a\u0645\u062b\u0644 \u0645\u062e\u062a\u0644\u0641 \u062c\u0648\u0627\u0646\u0628 \u0627\u0644\u062d\u064a\u0627\u0629 \u0627\u0644\u064a\u0648\u0645\u064a\u06296- \u0642\u0633\u0645 \u0627\u0644\u0645\u062d\u0627\u062f\u062b\u0627\u062a : \u062a\u0645 \u0627\u0636\u0627\u0641\u0629 \u0627\u0644\u0639\u062f\u064a\u062f \u0645\u0646 \u0627\u0644\u0645\u062d\u0627\u062f\u062b\u0627\u062a \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u0629 \u0627\u0644\u0645\u062f\u0639\u0648\u0645\u0629 \u0628\u0627\u0644\u0627\u062e\u062a\u0628\u0627\u0631\u0627\u062a \u0648\u0627\u0644\u0643\u0644\u0645\u0627\u062a \u0627\u0644\u0645\u0641\u062a\u0627\u062d\u064a\u0629 7- \u0642\u0633\u0645 \u0627\u0644\u0645\u0631\u0627\u062f\u0641\u0627\u062a :\u062a\u0645 \u0627\u0636\u0627\u0641\u0629 \u0645\u0631\u0627\u062f\u0641\u0627\u062a \u0647\u064a \u0627\u0644\u0627\u0647\u0645 \u0641\u064a \u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0627\u0646\u062c\u0644\u064a\u0632\u064a\u06298- \u0642\u0633\u0645 \u0627\u0644\u0627\u0641\u0639\u0627\u0644 \u0627\u0644\u0634\u0627\u0630\u0629 : 134 \u0641\u0639\u0644 \u0647\u064a \u0627\u0644\u0627\u0647\u0645 \u0639\u0644\u0649 \u0627\u0644\u0627\u0637\u0644\u0627\u06429- \u0642\u0633\u0645 \u0627\u0644\u0641\u064a\u062f\u064a\u0648 : \u062f\u0631\u0648\u0633 \u0645\u0634\u0631\u0648\u062d\u0629 \u0628\u0627\u0644\u0635\u0648\u062a \u0648\u0627\u0644\u0635\u0648\u0631\u0629 \u0648\u0628\u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0639\u0631\u0628\u064a\u0629 \u0627\u0630\u0627 \u064a\u0645\u0643\u0646\u0643 \u0627\u0646 \u062a\u0642\u0631\u0621 \u0627\u0644\u062f\u0631\u0633 \u0627\u0648\u0644\u0627 \u0645\u0646 \u062f\u0631\u0648\u0633 \u0627\u0644\u0642\u0648\u0627\u0639\u062f \u0648\u0645\u0646 \u062b\u0645 \u062a\u0633\u0645\u0639 \u0627\u0644\u0644\u0641\u0638 \u0645\u0646 \u062e\u0644\u0627\u0644 \u0627\u0644\u062f\u0631\u0648\u0633 \u0627\u0644\u0645\u062f\u0639\u0648\u0645\u0629 \u0628\u0627\u0644\u0635\u0648\u062a \u0648\u062b\u0645 \u062a\u0634\u0627\u0647\u062f \u0627\u0644\u0641\u064a\u062f\u064a\u0648 \u0648\u0628\u0647\u0630\u0647 \u0627\u0644\u0637\u0631\u064a\u0642\u0629 \u0633\u0648\u0641 \u062a\u0631\u0633\u062e \u0627\u0644\u0645\u0639\u0644\u0648\u0645\u0629 \u0641\u064a \u0630\u0647\u0646\u0643 \u0627\u0644\u0649 \u0627\u0644\u0627\u0628\u062f  ", "rating": "4.4065680503845215"}'
# sample_low_maturity_input = '{"price": "0", "developer": "i-sync corporation", "reviewers": "5583", "title": "\u0623\u0644\u0642\u0631\u0622\u0646 \u0627\u0644\u0645\u0639\u0644\u0645 \u0644\u0644\u0623\u0637\u0641\u0627\u0644", "dev_website": "https://www.google.com/url?q=http://www.i-sync.mobi/&sa=D&usg=AFQjCNGoj2q-jdvI720VrdOU355RMwPl4g", "email": "i.sync.corporation@gmail.com", "content_rating": "Low Maturity", "date_published": "January 14, 2013", "operating_system": "2.2 and up", "downloads": "500,000 - 1,000,000", "category": "Education", "developer_link": "/store/apps/developer?id=i-sync+corporation", "app_url": "https://play.google.com/store/apps/details?id=com.isync.koraankids", "Description": " \u0623\u0644\u0642\u0631\u0622\u0646 \u0627\u0644\u0645\u0639\u0644\u0645 \u0644\u0644\u0623\u0637\u0641\u0627\u0644:\u0646\u0642\u062f\u0645 \u0644\u0644\u0623\u062d\u0628\u0627\u0621 \u0627\u0644\u0635\u063a\u0627\u0631 \u062a\u0637\u0628\u064a\u0642 \u062a\u0639\u0644\u064a\u0645 \u0627\u0644\u0642\u0631\u0622\u0646 \u0627\u0644\u0643\u0631\u064a\u0645 \u0644\u0644\u0623\u0637\u0641\u0627\u0644 . \u0627\u0646\u0647 \u0628\u0631\u0646\u0627\u0645\u062c \u0631\u0627\u0626\u0639 \u0644\u062a\u0639\u0644\u064a\u0645 \u0627\u0644\u0627\u0637\u0641\u0627\u0644  \u0633\u0648\u0631 \u0645\u0646 \u0627\u0644\u0642\u0631\u0622\u0646 \u0627\u0644\u0643\u0631\u064a\u0645 \u0628\u0637\u0631\u064a\u0642\u0629 \u0633\u0647\u0644\u0629 \u0648\u0645\u0645\u062a\u0639\u0629 \u0628\u0627\u0644\u0627\u0636\u0627\u0641\u0629 \u0627\u0644\u0649 \u0627\u0646\u0627\u0634\u064a\u062f \u0627\u0633\u0644\u0627\u0645\u064a\u0629 \u0644\u0644\u0627\u0637\u0641\u0627\u0644 \u0648\u0639\u062f\u0629 \u0627\u0644\u0639\u0627\u0628 \u0644\u062a\u0646\u0645\u064a\u0629 \u0648\u062a\u0646\u0634\u064a\u0637 \u0642\u062f\u0631\u0627\u062a\u0647\u0645 \u0627\u0644\u0630\u0647\u0646\u064a\u0629 \u0643\u0645\u0627 \u0646\u0642\u062f\u0645 \u0642\u0635\u0635\u0627 \u0645\u0635\u0648\u0631\u0629 \u0639\u0646 \u0627\u0644\u0627\u0646\u0628\u064a\u0627\u0621 \u0639\u0644\u064a\u0647\u0645 \u0627\u0644\u0633\u0644\u0627\u0645  .\u062e\u062a\u0627\u0645\u0627 \u0646\u0631\u062c\u0648 \u0645\u0646 \u0627\u0644\u0644\u0647 \u0623\u0646 \u064a\u062c\u0639\u0644 \u0639\u0645\u0644\u0646\u0627 \u0647\u0630\u0627 \u062e\u0627\u0644\u0635\u0627 \u0644\u0648\u062c\u0647\u0647 \u0627\u0644\u0643\u0631\u064a\u0645Quran For Kids:teaching quran for kids is now available as an application . a collection of surahs in a simple way plus some islamic songs for kids . finally we have some animated stories about prophets .  ", "rating": "4.427010536193848"}'
# sample_medium_maturity_input = '{"price": "0", "developer": "Speech-Tech Jewels Games", "reviewers": "6318", "title": "English listening", "dev_website": "https://www.google.com/url?q=http://www.zl09201989.com&sa=D&usg=AFQjCNEXgXHF95lsrFo7vB9g5CYRPOzbnQ", "email": "zl09201989@hotmail.com", "content_rating": "Medium Maturity", "date_published": "September 20, 2014", "operating_system": "2.3 and up", "downloads": "100,000 - 500,000", "category": "Education", "developer_link": "/store/apps/developer?id=Speech-Tech+Jewels+Games", "app_url": "https://play.google.com/store/apps/details?id=com.speechtech.app.listening", "Description": " English Listening is an application providing English News listening material. Mp3 audio includes corresponding English news, and audio corresponding text. Listening material is updated daily, so you can close and the fact that most content more interesting. Content Content and British English American English contains, I suggest you choose a fixed tone to listen to, which will help improve your listening and speaking skills. You can listen online listening content, but also the content of your favorite collections, you can also download your favorite content. Tags: English listening, listening comprehension  ", "rating": "4.093542098999023"}'
# sample_high_maturity_input = '{"price": "0", "developer": "\u0643\u062a\u0628 \u0627\u0633\u0644\u0627\u0645\u064a\u0629", "reviewers": "643", "title": "\u062a\u0639\u0644\u064a\u0645 \u0627\u0644\u0635\u0644\u0627\u0629 \u0644\u0644\u0627\u0637\u0641\u0627\u0644", "dev_website": "https://www.google.com/url?q=http://codendot.com&sa=D&usg=AFQjCNEm3ZFyZ-5aEURUMzGphrVawo_ICw", "email": "islamicbooks12@gmail.com", "content_rating": "High Maturity", "date_published": "October 18, 2013", "operating_system": "2.2 and up", "downloads": "100,000 - 500,000", "category": "Education", "developer_link": "/store/apps/developer?id=%D9%83%D8%AA%D8%A8+%D8%A7%D8%B3%D9%84%D8%A7%D9%85%D9%8A%D8%A9", "app_url": "https://play.google.com/store/apps/details?id=com.codendot.salatTutorialar", "Description": " \u0625\u0646 \u0633\u062a\u0648\u0646 \u0641\u064a \u0627\u0644\u0645\u0627\u0626\u0629 \u0645\u0646 \u0627\u0644\u0623\u0637\u0641\u0627\u0644 \u0627\u0644\u0645\u0633\u0644\u0645\u064a\u0646 \u0627\u0644\u0630\u064a\u0646 \u064a\u0639\u064a\u0634\u0648\u0646 \u0641\u064a \u0627\u0644\u0645\u062c\u062a\u0645\u0627\u0639\u0627\u062a \u0627\u0644\u063a\u0631\u0628\u064a\u0629 \u0644\u0627 \u064a\u0639\u0644\u0645\u0648\u0646 \u0643\u064a\u0641\u064a\u0629 \u0627\u0644\u0635\u0644\u0627\u0629. \u0645\u0647\u0645\u062a\u0646\u0627 \u0647\u064a \u0625\u0633\u062a\u062d\u062f\u062b \u062a\u0637\u0628\u064a\u0642\u0627\u062a \u0645\u0641\u064a\u062f\u0629 \u0644\u0644\u0637\u0641\u0644 \u0627\u0644\u0645\u0633\u0644\u0645 \u0627\u0644\u0630\u064a \u0647\u0648 \u0628\u062d\u0627\u062c\u0629 \u0644\u0645\u0639\u0631\u0641\u0629 \u0623\u0643\u062b\u0631 \u0639\u0646 \u062f\u064a\u0646 \u0627\u0644\u0625\u0633\u0644\u0627\u0645 \u0648\u062a\u0639\u0627\u0644\u064a\u0645\u0647 \u0648\u0643\u064a\u0641\u064a\u0629 \u0645\u0645\u0627\u0631\u0633\u0629 \u0627\u0644\u0641\u0631\u0627\u0626\u0636. \u0625\u0646 \u062a\u0637\u0628\u064a\u0642 \"\u062a\u0639\u0644\u064a\u0645 \u0627\u0644\u0635\u0644\u0627\u0629 \" \u0647\u062f\u0641\u0647\u0627 \u062a\u0639\u0644\u064a\u0645 \u0627\u0644\u0623\u0637\u0641\u0627\u0644 \u0643\u0644 \u0634\u064a\u0621 \u0639\u0646 \u0627\u0644\u0635\u0644\u0627\u0629 \u0625\u0630 \u064a\u0634\u0631\u062d \u0639\u0646 \u0645\u0648\u0627\u0642\u064a\u062a \u0627\u0644\u0635\u0644\u0627\u0629 \u0643\u0645\u0627 \u0643\u064a\u0641\u064a\u0629 \u0627\u0644\u0635\u0644\u0627\u0629. \u0645\u0646 \u062e\u0644\u0627 \u0647\u0630\u0627 \u0627\u0644\u062a\u0637\u0628\u064a\u0642 \u064a\u062a\u0639\u0644\u0645 \u0627\u0644\u0637\u0641\u0644 \u0645\u062c\u0645\u0648\u0639\u0629 \u0645\u0641\u0631\u062f\u0627\u062a \u0648\u0645\u0635\u0637\u0644\u062d\u0627\u062a \u0645\u062b\u0644: \u0631\u0643\u0648\u0639\u060c \u0633\u062c\u0648\u062f\u060c \u0648\u0636\u0648\u0621\u060c \u0635\u0644\u0627\u0629 \u0627\u0644\u0641\u062c\u0631\u060c \u0635\u0644\u0627\u0629 \u0627\u0644\u0638\u0647\u0631\u060c \u0635\u0644\u0627\u0629 \u0627\u0644\u0639\u0634\u064a. \u0623\u0637\u0644\u0642\u0646\u0627 \u0627\u0644\u0622\u0646 \u062a\u0637\u0628\u064a\u0642 \"\u062a\u0639\u0644\u064a\u0645 \u0627\u0644\u0635\u0644\u0627\u0629 \u0644\u0644\u0623\u0637\u0641\u0627\u0644\" \u0648\u0647\u0648 \u0623\u0648\u0644 \u062a\u0637\u0628\u064a\u0642 \u0645\u0646 \u0633\u0644\u0633\u0629 \u0646\u0633\u0639\u0649 \u0627\u0644\u0649 \u062a\u0637\u0648\u064a\u0631\u0647\u0627 \u0648\u0625\u062e\u0631\u0627\u062c\u0647\u0627 \u0644\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u064a\u0646 \u0648\u0647\u064a: \u2022\u062a\u0639\u0644\u0628\u0645 \u0627\u0644\u0635\u0644\u0627\u0629 \u0628\u0644\u063a\u0627\u062a \u0623\u062c\u0646\u0628\u064a\u0629 \u0645\u062b\u0644 \u0627\u0644\u0641\u0631\u0646\u0633\u064a\u0629\u060c \u0627\u0644\u0625\u0646\u0643\u0644\u064a\u0632\u064a\u0629\u060c \u0627\u0644\u0628\u0631\u062a\u063a\u0627\u0644\u064a\u0629 \u0648\u063a\u064a\u0631\u0647\u0627... \u2022\u062a\u0639\u0644\u064a\u0645 \u0627\u0644\u0648\u0636\u0648\u0621 \u2022\u062a\u0639\u0644\u064a\u0645 \u0627\u0644\u0635\u064a\u0627\u0645 \u2022\u062a\u0639\u0644\u064a\u0645 \u0641\u0631\u0627\u0626\u0636 \u0627\u0644\u062d\u062c \u0644\u0625\u0646\u062c\u0627\u0632 \u0647\u0630\u0647 \u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a \u0644\u064a\u0632\u0645\u0646\u0627 \u062f\u0639\u0645\u0627\u064b \u0645\u0627\u062f\u064a\u0627\u064b \u0644\u064a\u0635\u0627\u0631 \u0627\u0644\u0649 \u062a\u063a\u0637\u064a\u0629 \u0627\u0644\u0645\u0635\u0627\u0631\u064a\u0641 \u0627\u0644\u0645\u062a\u0631\u062a\u0628\u0629\u060c \u0648\u0645\u0646 \u0647\u0646\u0627 \u0644\u0645\u0633\u0647\u0627\u0645\u062a\u0643\u0645 \u062f\u0648\u0631\u0627\u064b \u0643\u0628\u064a\u0631\u0627\u064b \u0641\u064a \u062a\u062d\u0642\u064a\u0642 \u063a\u0627\u064a\u062a\u0646\u0627. \u0641\u0631\u064a\u0642 \u0627\u0644\u0639\u0645\u0644: \u0646\u062d\u0646 \u0645\u062c\u0645\u0648\u0639\u0629 \u0645\u0646 \u0645\u0637\u0648\u0631\u064a \u0627\u0644\u0628\u0631\u0627\u0645\u062c \u0625\u0633\u062a\u062d\u062f\u062b\u0646\u0627 \u062a\u0637\u0628\u064a\u0642 \u0645\u0641\u064a\u062f \u0644\u0644\u0637\u0641\u0644 \u0627\u0644\u0645\u0633\u0644\u0645 \u0627\u0644\u0630\u064a \u0647\u0648 \u0628\u062d\u0627\u062c\u0629 \u0644\u0645\u0639\u0631\u0641\u0629 \u0623\u0643\u062b\u0631 \u0639\u0646 \u062f\u064a\u0646 \u0627\u0644\u0625\u0633\u0644\u0627\u0645 \u0648\u062a\u0639\u0627\u0644\u064a\u0645\u0647 \u0648\u0643\u064a\u0641\u064a\u0629 \u0645\u0645\u0627\u0631\u0633\u0629 \u0627\u0644\u0641\u0631\u0627\u0626\u0636. \u0646\u062d\u0646 \u0642\u0633\u0645 \u0645\u0646 \u0634\u0631\u0643\u0629 \u0643\u0648\u062f \u0623\u0646\u062f \u062f\u0648\u062a www.codendot.com \u0647\u062f\u0641\u0646\u0627 \u062a\u062b\u0642\u064a\u0641 \u0645\u062c\u062a\u0645\u0639\u0646\u0627 \u0648\u062a\u0648\u0639\u064a\u062a\u0647 \u0648\u0646\u0639\u0645\u0644 \u062a\u062d\u062a \u0625\u0633\u0645 Islamic Books Sixty per cent of Muslim children living in Western communities who do not know how to pray. Our mission is developed useful applications for the Muslim child who is a need to learn more about the religion of Islam and its teachings and how to practice statutes.The application of the \"Prayer education\" aimed at teaching children all about prayer as explain about prayer times as how to pray.During this application the child learns a vocabulary of terms such as: bowing, prostration, and the light, the dawn prayer, noon prayer, Ashi prayer.We now apply \"prayer, education for children,\" which is the first application of a series seeking to develop and removing users, namely:\u2022 Talpm prayer in foreign languages \u200b\u200bsuch as French, English, Portuguese and other ...\u2022 Education ablution\u2022 Education fasting\u2022 Education ordinances pilgrimageTo accomplish these applications to Esmna support financially so they can be to cover the expenses incurred, hence Meshamtkm a major role in achieving our goal.Team:We are a group of software developers we have introduced a useful application for the Muslim child who is a need to learn more about the religion of Islam and its teachings and how to practice statutes.We are a division of On & Dot www.codendot.com our community education and awareness and working under the name of Islamic Books  ", "rating": "4.1493000984191895"}'
# sample_string_with_quote_error = '{"price": "0", "developer": "\"MMH Dev\"", "reviewers": "8270", "title": "English Arabic Dictionary", "dev_website": "https://www.google.com/url?q=http://www.iquest-es.com&sa=D&usg=AFQjCNG8o0hL6sk-VOmUJ_JJdBrlR94k_w", "email": "mmh@iquest-es.com", "content_rating": "Everyone", "date_published": "September 8, 2014", "operating_system": "2.3.3 and up", "downloads": "500,000 - 1,000,000", "category": "Education", "developer_link": "/store/apps/developer?id=MMH+Dev", "app_url": "https://play.google.com/store/apps/details?id=com.mmh.qdic", "Description": " Q DictionaryFree offline Arabic-English and English-Arabic Dictionary, with simple, beautiful and easy to use interface.First dictionary to support translation from other applications in a very simple way.Q Dictionary Features:- English Arabic and Arabic English translation- Used offline- Cross apps translation to translated from other apps like web browser, mail or sms without opining Q Dictionary and without interruptions- \u0650Automatic detection of word root- 87k+ English words, 94k+ Arabic words including a lot of abbreviations- Automatic language detection- Fast search with automatic suggestions- Speech-To-Text- English words Text-To-Speech- Word search history- Favorite words list- Copy or share translation- Search for words on Google, Wikipedia or Wiktionary  ", "rating": "4.188028812408447"}'
# sample_non_english_developer = sample_high_maturity_input
import MySQLdb
from datetime import datetime
from datetime import  date


class InputDataFormatter(object):
    def __init__(self, json_object):
        self.source_object = json_object
        self.developers = self.fetch_developer_data()
        self.android_versions_dict = self.load_file_into_dict('android_versions_enum')
        self.catogries_dict = self.load_file_into_dict('categories_enum')

    def string(self):
        return json.dumps(self.source_object)

    def price(self):
        price = float(self.source_object["price"].strip("EGP ").replace(',', ''))
        # return float(self.source_object["price"])
        return price

    def dev_name_length(self):
        return int(len(self.source_object["developer"]))

    def number_of_reviewers(self):
        return int(self.source_object.get("reviewers", ""))

    def is_english(self):
        pattern = unicode(u"[ابتثجحخدذرزسشصضطظعغفقكلمنهوي]")
        return re.search(pattern, self.source_object["title"]) is None

    def title_word_count(self):
        return len(self.source_object["title"].split())

    def title_legth(self):
        return len(self.source_object["title"])

    def content_rating(self):
        if self.source_object["content_rating"].lower() == "everyone":
            return 0
        elif self.source_object["content_rating"].lower() == "low maturity":
            return 1
        elif self.source_object["content_rating"].lower() == "medium maturity":
            return 2
        elif self.source_object["content_rating"].lower() == "high maturity":
            return 3

        return -1

    def fetch_developer_data(self):
        self.db = MySQLdb.connect("localhost", "root", "root", "appsdb", use_unicode=True, charset="utf8")
        sql = "SELECT distinct (lcase(developer)), count(*) as count FROM appsdb.apps_default Group by lcase(developer)"
        cur = self.db.cursor()
        cur.execute(sql)
        rows = dict(cur.fetchall())
        # with codecs.open("developers", 'w', encoding='utf8') as w:
        #     for k in rows.keys():
        #         w.write(k+"\n")
        return rows

    def number_of_apps_for_developer(self):
        return self.developers.get(self.source_object["developer"].lower(), "1")

    def date_published_difference(self):
        date_string = self.source_object["date_published"]
        publish_date = datetime.strptime(date_string, '%B %d, %Y').date()
        refernce_date = date(2000, 1, 1)
        difference = publish_date - refernce_date
        return difference.days

    def load_file_into_dict(self, filename):
        dict = {}
        # print (type(dict))
        counter = 0
        with open(filename) as f:
            for line in f:
                dict[line.rstrip()] = counter
                counter+=1
        return dict

    def android_version_enum(self):
        return self.android_versions_dict[self.source_object["operating_system"]]

    def number_of_downloads(self):
        return len(self.source_object.get("downloads", "0"))

    def category(self):
        return self.catogries_dict[self.source_object.get("category", "")]

    def description_legth(self):
        return len(self.source_object.get("Description", "").strip())

    def rating(self):
        return float(self.source_object.get("rating", "0"))


def run():
    counter=0
    broken_jsons=0
    obj = InputDataFormatter("")
    with codecs.open("features", 'w', encoding='utf8') as w:
        with codecs.open("apps_all_utf8_cleaned", 'r') as f:
            for line in f:
                try:
                    data = json.loads(line)
                except:
                    broken_jsons+=1
                    continue
                obj.source_object = data
                if obj.is_english() == False: continue
                price = obj.price()
                dev_name_len = obj.dev_name_length()
                reviewers = obj.number_of_reviewers()
                title_word_count = obj.title_word_count()
                title_length = obj.title_legth()
                content_rating = obj.content_rating()
                number_of_apps_for_developer = obj.number_of_apps_for_developer()
                age = obj.date_published_difference()
                version = obj.android_version_enum()
                downloads = obj.number_of_downloads()
                category = obj.category()
                description = obj.description_legth()
                rating = obj.rating()

                feature_vector="%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%(price, dev_name_len, reviewers, title_word_count,
                                                                                     title_length, content_rating, number_of_apps_for_developer,
                                                                                     age, version, downloads, category, description, rating)
                w.write(feature_vector)
                w.write("\n")
                if counter % 1000 == 0:
                    print counter
                counter += 1
    w.close()
    f.close()

if __name__ == "__main__":
    run()



class InputDataFormatterTest(TestCase):
    def setUp(self):
        data = []
        with open('sample_data.txt') as f:
            for line in f:
                data.append(json.loads(line))

        self.sample_input = data[0]
        self.sample_non_english_input = data[1]
        self.sample_low_maturity_input = data[2]
        self.sample_medium_maturity_input = data[3]
        self.sample_high_maturity_input = data[4]
        self.sample_string_with_quote_error = data[5]
        self.sample_non_english_developer = self.sample_high_maturity_input

        self.formatter = InputDataFormatter(self.sample_input)

    def test_single_backslash_quote(self):
        self.formatter = InputDataFormatter(self.sample_string_with_quote_error)
        self.assertEqual(self.formatter.dev_name_length(), 9)

    def test_parse_price(self):
        self.assertEqual(self.formatter.price(), 0.0)

    def test_dev_name_length(self):
        self.assertEqual(self.formatter.dev_name_length(), 7)

        self.formatter = InputDataFormatter(self.sample_non_english_developer)
        self.assertEqual(self.formatter.dev_name_length(), 11)

    def test_number_of_reviewers(self):
        self.assertEqual(self.formatter.number_of_reviewers(), 8270)

    def test_is_english(self):
        self.assertTrue(self.formatter.is_english())

        self.formatter = InputDataFormatter(self.sample_non_english_input)
        self.assertFalse(self.formatter.is_english())

    def test_title_lenght(self):
        self.assertEqual(self.formatter.title_legth(), 25)

    def test_title_word_count(self):
        self.assertEqual(self.formatter.title_word_count(), 3)

        self.formatter = InputDataFormatter(self.sample_non_english_input)
        self.assertEqual(self.formatter.title_word_count(), 3)

    def test_content_rating(self):
        self.assertEqual(self.formatter.content_rating(), 0)

        self.formatter = InputDataFormatter(self.sample_low_maturity_input)
        self.assertEqual(self.formatter.content_rating(), 1)

        self.formatter = InputDataFormatter(self.sample_medium_maturity_input)
        self.assertEqual(self.formatter.content_rating(), 2)

        self.formatter = InputDataFormatter(self.sample_high_maturity_input)
        self.assertEqual(self.formatter.content_rating(), 3)

    def test_fetch_developer_data(self):
        self.assertEqual(len(self.formatter.fetch_developer_data()), 266340)
        pass

    def test_number_of_apps_for_developer(self):
        self.formatter = InputDataFormatter(self.sample_input)
        self.assertEqual(self.formatter.number_of_apps_for_developer(), 2) #number of apps for "MMH Dev" is 2
        pass

    def test_date_published_difference(self):
        #self.assertEqual(self.formatter.date_published_difference(), 1000)
        self.assertEqual(self.formatter.date_published_difference(), 5364)
        pass

    def test_load_file_into_dict(self):
        self.assertEqual(len(self.formatter.load_file_into_dict('android_versions_enum')), 135)

    def test_android_version_enum(self):
        self.assertEqual(self.formatter.android_version_enum(), 1)

    def test_number_of_downloads(self):
        self.assertEqual(self.formatter.number_of_downloads(), 19)

    def test_categorey(self):
        self.assertEqual(self.formatter.category(), 40)

    def test_description_length(self):
         self.assertEqual(self.formatter.description_legth(), 773)

    def test_rating(self):
        self.assertEqual(self.formatter.rating(), 4.188028812408447)





