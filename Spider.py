# coding: utf-8

import UrlManager, HtmlDownloader, HtmlParser, HtmlOutputer

class Spider(object):

	def __init__(self):
		self.urls = UrlManager()
		self.downloader = UrlDownloader()
		self.parser = HtmlParser()
		self.outputer = HtmlOutputer()

	def crawl(self, root_url):
		self.urls.add(root_url)
		cnt = 1
		while self.urls.has_new():
			try:
				new_url = self.urls.get_new()
				print "Crawling #%d: %s" %(cnt, new_url)
				html_cont = self.downloader.download(new_url)
				(new_urls, new_data) = self.parser.parse(new_url, html_cont)
				self.urls.add_all(new_urls)
				self.outputer.collect(new_data)

				if cnt >= 1000:
					break

				cnt = cnt + 1
			
			except:
				print "Crawl fails"

		self.outputer.output()


if __name__ == "__main__":
	root_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
	spider_obj = Spider()
	spider_obj.crawl(root_url)

