import io, re
import PyPDF2
import requests

url = 'http://www.ct.gov/hix/lib/hix/CT_DSG_-12132014_version_1.2_%28with_clarifications%29.pdf'

r = requests.get(url)
f = io.BytesIO(r.content)

reader = PyPDF2.PdfFileReader(f)
contents = reader.getPage(10).extractText() #.split('[A-Z][^A-Z]*|\n')

#data = re.sub( r"([A-Z])", r" \1", contents).split() #findall('[a-zA-Z][^A-Z]*', contents)

print(contents)

# csv = open('AWStest.csv', 'w')
# csv.write(contents)
# csv.close()
#
# with open(AWStest.csv) as fobj:
#     for line in fobj:
#         data = re.split()