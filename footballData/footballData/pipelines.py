# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import errno
import os
import collections
from scrapy import signals
from scrapy.exporters import XmlItemExporter

class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('items.json', 'wb')
    def process_item(self, item, spider): 
        line = json.dumps(dict(item)) + "\n" 
        self.file.write(line)
        return item

class XmlExportPipeline(object):

    def __init__(self):
        self.files = {}
        self.exporter = {}

    @classmethod
    def from_crawler(cls, crawler):
        '''Receives data from the crawler, creates the pipeline'''
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        '''Open XML file for writing'''
        outfile = open('%s.xml' % spider.name, 'w+b')
        self.files[spider] = outfile
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        '''Close the spider'''
        self.exporter.finish_exporting()
        outfile = self.files.pop(spider)
        outfile.close()

    def process_item(self, item, spider):
        '''Actually processes the xml file content'''
        if spider.name is 'match':
            filename = 'matches/' \
            + item['country'] \
            + '/' + item['league'] \
            + '/' + item['season'] \
            + '/' + str(item['stage']) \
            +'/%s.xml' % item['matchId']
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            file = open(filename, 'w+b')
            self.files[item['matchId']] = file
            self.exporter = XmlItemExporter(file)
            self.exporter.fields_to_export = [
                'country',
                'league',
                'season',
                'stage',
                'matchId', 
                'date',
                'homeTeamId',
                'awayTeamId',
                'homeTeamFullName', 
                'awayTeamFullName',
                'homeTeamAcronym',
                'awayTeamAcronym',
                'homeTeamGoal',
                'awayTeamGoal',
                'homePlayers',
                'awayPlayers',
                'homePlayersId',
                'awayPlayersId',
                'homePlayersX',
                'awayPlayersX',
                'homePlayersY',
                'awayPlayersY',
                'goal',
                'shoton',
                'shotoff',
                'foulcommit',
                'card',
                'cross',
                'corner',
                'possession']
            
            self.exporter.export_item(item)
            return item
        elif spider.name is 'player':
            filename = 'players/' \
            + item['name']+'_'+item['matchId']+'_'+item['fifaId']+'.xml'
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            file = open(filename, 'w+b')
            self.files[item['name']] = file
            self.exporter = XmlItemExporter(file)
            self.exporter.fields_to_export = [
                'name',
                'matchId',
                'fifaId',
                'birthday',
                'height',
                'weight',
                'stats']
            self.exporter.export_item(item)
            return item
