import csv

reader = csv.reader(open('wrong_legalNames_from_live_20160412.csv', 'r'), delimiter=';')
writer = csv.writer(open('wrong_legalNames_from_live_20160412_unique.csv', 'w'), delimiter=';')

data = set()
i = 1
for row in reader:
    print "Processing " + i
    i += 1
    key = (row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip(), row[4].strip())

    if key not in data:
        writer.writerow(row)
        data.add(key)
    else:
        print "duplicate found"
        print ','.join(map(str, key))
