# URL parser using python BeautifulSoup4 (third party library)

from bs4 import BeautifulSoup
import re, urlparse

class HtmlParser(object):

	def _get_new_urls(self, url, soup):
		new_urls = set()
		links = soup.find_all("a", href = re.compile(r"/wiki/\w+"))
		for link in links:
			new_url = link["href"]
			new_full_url = urlparse.urljoin(url, new_url)
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self, url, soup):
		new_data = {}
		new_data["url"] = url
		title_node = soup.find("h1", class_ = "firstHeading")
		new_data["title"] = title_node.get_text()
		summary_node = soup.find("p")
		new_data["summary"] = summary_node.get_text()
		return new_data

	def parse(self, url, html_cont):
		if url is None or html_cont is None:
			return
		
		soup = BeautifulSoup(html_cont, "html.parser", from_encoding = "utf-8")
		new_urls = self._get_new_urls(url, soup)
		new_data = self._get_new_data(url, soup)
		return new_urls, new_data	

