import PyPDF2
import requests
import io
import easytextract
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

url = 'http://www.ct.gov/hix/lib/hix/CT_DSG_-12132014_version_1.2_%28with_clarifications%29.pdf'

r = requests.get(url)
f = io.BytesIO(r.content)

# filename = 'CT_DSG_-12132014_version_1.2_(with_clarifications).pdf'
#open allows you to read the file
# pdfFileObj = open(filename, 'rb')
#The pdfReader variable is a readable object that will be parsed
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pdfReader = PyPDF2.PdfFileReader(f)

#discerning the number of pages will allow us to parse through all #the pages
num_pages = 26 # pdfReader.numPages
count = 9
text = ""
#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText()
# This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
if text != "":
   text = text
# If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
else:
   text = easytextract.process('CT_DSG_-12132014_version_1.2_(with_clarifications).pdf', method='tesseract', language='eng')
# Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.
# Now, we will clean our text variable, and return it as a list of keywords.

# print(text)

csv = open('AWStest2.csv', 'w')
csv.write(text)
csv.close()