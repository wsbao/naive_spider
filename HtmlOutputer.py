# coding: utf-8

class HtmlOutputer(object):

	def __init__(self):
		self.data_set = []

	def collect(self, data):
		if data is None:
			return
		self.data_set.append(data)
	
	def output(self):
		fout = open("Crawled.html", "w")
		
		fout.write("<html>")
		fout.write("<body>")
		fout.write("<table>")
		
		for data in self.data_set:
			fout.write("<tr><td></td></tr>")
			fout.write("<tr><td><a href='%s'>%s</a></td></tr>"%(data["url"], data["title"].encode("utf-8")))
			fout.write("<tr><td>%s</td></tr>"%data["summary"].encode("utf-8"))
			fout.write("<tr><td></td></tr>")
		
		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")
		
		fout.close()
