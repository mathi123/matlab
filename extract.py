import glob
import os
import json
import csv
from scipy.io import loadmat


folder="samples/TB_4kHz/"

def try_extract(x, num):
    results=[]
    base=x['hgS_070000'][0,0][2][0, 0][num][0, 0]

    m=0
    maxIndex=0
    i=0
    for junk in base:
        try:
            if(len(junk[0]) > m):
                m=len(junk[0])
                maxIndex=i
        except:
            pass
        i = i+1

    for r in base[maxIndex][0]:
        arr=r[2][0]
        x=round(arr[0],10)
        y=round(arr[1],10)
        results.append([x,y])
    return results

with open('result.csv', mode='w', newline='') as result_file:
    result_writer = csv.writer(result_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    result_writer.writerow(['bestand', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5', 'x6', 'y6', 'x7', 'y7', 'x8', 'y8'])

    for filename in glob.glob('{folder}*.fig'.format(folder=folder)):
        try:
            x = loadmat(filename)
            results=[]

            for i in range(21):
                try:
                    results=try_extract(x,i)
                    break
                except:
                    pass

            row=[filename]
            for sortedResult in sorted(results, key=lambda k: k[0]):
                row.append(sortedResult[0])
                row.append(sortedResult[1])

            result_writer.writerow(row)

        except:
            result_writer.writerow([filename])
