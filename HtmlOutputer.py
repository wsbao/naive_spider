# coding: utf-8

import Configure

class HtmlOutputer(object):

	def __init__(self):
		self.data_set = []

	def collect(self, data):
		if data is None:
			return
		self.data_set.append(data)
	
	def output(self):
		fout = open(Configure.html_ofile, "w")
		
		fout.write("<html>")
		fout.write("<body>")
		fout.write("<table>")
		
		for data in self.data_set:
			fout.write("<tr><td></td></tr>")
			print "Recording: %s" %data["url"]
			try:
				fout.write("<tr><td><a href='%s'>%s</a></td></tr>" \
					%(data["url"].encode(Configure.coding_set), data["title"].encode(Configure.coding_set)))
				fout.write("<tr><td>%s</td></tr>"%data["summary"].encode(Configure.coding_set))
			except:
				print "Record fails"
			fout.write("<tr><td></td></tr>")
		
		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")
		
		fout.close()

