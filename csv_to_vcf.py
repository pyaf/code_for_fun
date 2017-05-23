import csv

with open('KY_responses.csv', 'rb') as f:
    data = csv.reader(f)
    with open('KY.vcf', 'w') as f:
        for row in data:
            f.write('BEGIN:VCARD\nVERSION:2.1\n')
            f.write('FN:' + 'KY ' + row[1].split('@')[0] +'\n')
            f.write('TEL;CELL:' + row[5] + '\n')
            f.write('END:VCARD\n')
