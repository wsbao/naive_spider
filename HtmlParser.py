# URL parser using python BeautifulSoup4 (third party library)

from bs4 import BeautifulSoup

class HtmlParser(object):

	def _get_new_urls(self, url, soup):
		links = soup.find_all("a")
		for link in links:


	def _get_new_data(self, url, soup):
		pass

	def parse(self, url, html_cont):
		if url is None or html_cont is None:
			return

		soup = BeautifulSoup(html_cont, "html.parser", from_encoding = "utf-8")
		new_urls = self._get_new_urls(url, soup)
		new_data = self._get_new_data(url, soup)
		return (new_urls, new_data)
	
