import csv
def calc(reader):
    li=[]
    for row in reader:
        if not len(row)==0:
            k = row[0]
            j = row[1]
            date = row[2]
            time = row[3]
            ZTD = row[4]
            exist = False
            for l in li:
                if l[0]==date and l[1]==time:
                    exist=True
                    l[2]=l[2]+float(ZTD)*(1/(float(j)+2))
                    l[3]=l[3]+1/(float(j)+2)
            if exist==False:
                li.append([date,time,float(ZTD)*(1/(float(j)+2)),1/(float(j)+2)])
    for l in li:
        l.append(l[2]/l[3])
        print(l)

    with open('KEPN.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        for l in li:
            writer.writerow(l)

calc(csv.reader(open('ztd/KEPN.csv')))

