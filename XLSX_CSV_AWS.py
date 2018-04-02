import xlrd
import csv

def csv_from_excel():
    wb = xlrd.open_workbook('VHI Data Mapping 20141009.xlsx')
    sh = wb.sheet_by_name('ENROLLMENT')
    your_csv_file = open('Enrollment_Test.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

# runs the csv_from_excel function:
csv_from_excel()