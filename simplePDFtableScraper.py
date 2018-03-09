import io
import PyPDF2
import requests

url = 'http://www.ct.gov/hix/lib/hix/CT_DSG_-12132014_version_1.2_%28with_clarifications%29.pdf'

r = requests.get(url)
f = io.BytesIO(r.content)

reader = PyPDF2.PdfFileReader(f)
contents = reader.getPage(10).extractText().split('\n')

print(contents)