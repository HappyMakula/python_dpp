import csv
import math

f=0.0065
M=0.0289644
R=8.31432

def calc(reader,start):
    row1 = next(reader) 
    first =row1[1]
    for row in reader:
        date = row[0]
        time = row[1]
        id = row[2]
        typeP = row[3]
        lat = float(row[4])
        lon = row[5]
        x = row[6]
        y = row[7]
        h = float(row[8])
        hi = float(row[9])
        Ti = float(row[10])
        RH = float(row [11])
        pi = float(row [12])
        lat2=lat
        j=int(time[0])*10+int(time[1])-(int(first[0])*10+int(first[1]))
        if j<0:
            j=j+24
        if typeP == 'iterp':
            P=pi
        elif typeP == '2m':
            g=9.8063*(1-10**-7*((hi+h)/2)*(1-0.0026373*math.cos(2*lat2)+5.9*10**-6*(math.cos(2*lat2))**2))
            P=pi*((Ti-f*(h-hi))/Ti)**((g*M)/(R*f))
        else:
            P=0
        esat=6.112*math.exp((17.67*(Ti-273.15))/(Ti-273.15+243.5))
        e=RH/100*esat
        ZTD=0.0022777*(P+(1255/Ti+0.05)*e)
        with open('ztd/'+id+'.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([start,j,date, time, ZTD])

        #print (ZTD)
        #print (row)
calc(csv.reader(open('surface_20150912_06.csv')),0)
calc(csv.reader(open('surface_20150912_12.csv')),6)
calc(csv.reader(open('surface_20150912_18.csv')),12)
calc(csv.reader(open('surface_20150913_00.csv')),18)
calc(csv.reader(open('surface_20150913_06.csv')),24)
calc(csv.reader(open('surface_20150913_12.csv')),30)
calc(csv.reader(open('surface_20150913_18.csv')),36)