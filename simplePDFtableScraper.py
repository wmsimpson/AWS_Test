import scraperwiki
import requests
import lxml
import io

url = 'http://www.ct.gov/hix/lib/hix/CT_DSG_-12132014_version_1.2_%28with_clarifications%29.pdf'

pdfdata = open(url, 'r')
xmldata = scraperwiki.pdftoxml(pdfdata)
root = lxml.etree.fromstring(xmldata)

print(lxml.etree.tostring(root, pretty_print=True))