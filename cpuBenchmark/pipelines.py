# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pathlib import Path
from scrapy.exporters import CsvItemExporter
import os
import csv

class CpubenchmarkPipeline(object):
	def __init__(self):
	   print("*"*50 + 10*"\n" + str(os.getcwd()) + 10*"\n" + 50*"*")
	   self.filename = 'CPUBenchmark.csv'
	
	# open the csv and begin to use CsvItemExporter object and start exporting
	def open_spider(self, spider):
	   self.csvfile = open(self.filename, mode='wb')
	   self.exporter = CsvItemExporter(self.csvfile)
	   self.exporter.start_exporting()
	
	# finish exporting then close csv
	def close_spider(self, spider):
		self.exporter.finish_exporting()
		self.csvfile.close()
		with open(self.filename, 'r') as f:
			reader = csv.reader(f)
			original_list = list(reader)
			cleaned_list = list(filter(None,original_list))

		with open(self.filename, 'w', newline='') as output_file:
			wr = csv.writer(output_file, dialect='excel')
			for data in cleaned_list:
				wr.writerow(data)
	# handles each item object that was yielded in the scraper
	def process_item(self, item, spider):
	   self.exporter.export_item(item)
	   return item
