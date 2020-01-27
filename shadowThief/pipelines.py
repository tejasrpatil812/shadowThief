import sqlite3
from datetime import datetime
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ShadowthiefPipeline(object):

    def __init__(self):
        self.conn = sqlite3.connect('myMusics.db')
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS music""")
        self.curr.execute(""" 
            CREATE TABLE music(
                title text,
                author text,
                position int,
                source text,
                as_of datetime DEFAULT CURRENT_TIMESTAMP)  """)

    def store_db(self, item):
        self.curr.execute("""
        INSERT INTO music VALUES (?,?,?,?,?)""", (" ".join(item['title']), " ".join(item['author']), item['position'], item['source'], datetime.now()))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
