import PyPDF2
import requests
import io

url = 'http://www.vhi.org/flyers/APCD%20Data%20Dictionary.pdf'
# 'http://www.ct.gov/hix/lib/hix/CT_DSG_-12132014_version_1.2_%28with_clarifications%29.pdf'

r = requests.get(url)
f = io.BytesIO(r.content)

pdfReader = PyPDF2.PdfFileReader(f)

num_pages = 10 # pdfReader.numPages
count = 7 # Initial page
text = ""

# The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText()

csv = open('AWStest2.csv', 'w')
csv.write(text)
csv.close()