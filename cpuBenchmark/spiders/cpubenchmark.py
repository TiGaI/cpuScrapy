from scrapy import Spider
from cpuBenchmark.items import CpubenchmarkItem
from scrapy.http.request import Request
from scrapy_splash import SplashRequest
import re
import pandas as pd

class cpubenchmark(Spider):
	name = 'cpubenchmark'
	allowed_urls = ['https://browser.geekbench.com']
	start_urls = ['https://browser.geekbench.com/processor-benchmarks']
	
	def parse(self, response):
		data = CpubenchmarkItem()
		rows = response.xpath('//*[@id="pc"]/tbody/tr')

		for row in rows:
			text = row.xpath('td[1]/a/text()').extract()
			description = row.xpath('td[1]/div/text()').extract()
			textArray = text[0].split(" ")
			if textArray[0] == 'Intel':
				if textArray[1].lower() == 'core':
					data['brand'], data['model'] = text.split("-")
				else:
					data['brand'], data['model'] = " ".join(textArray[0:len(textArray)]), textArray[-1]
			else:
				data['brand'], data['model'] = " ".join(textArray[0:len(textArray)]), textArray[-1]
			tempWord = description[0].split('(')
			data['speed'] = tempWord[0][0:3]
			data['core'] = tempWord[1][0:-1]
			data['benchmark'] = row.xpath('td[2]/text()').extract_first()
			# data={'brand': "intel", "model": "i9", "speed": 2.0, "core": "6 core", "benchmark": 23232}
			yield data