import io
import requests
import tabula

url = 'http://www.ct.gov/hix/lib/hix/CT_DSG_-12132014_version_1.2_%28with_clarifications%29.pdf'

r = requests.get(url)
f = io.BytesIO(r.content)

reader = tabula.read_pdf(r.content)

print(reader)
