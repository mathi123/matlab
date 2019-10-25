import glob
import os
import json
import csv
from scipy.io import loadmat


folder="samples/"

with open('result.csv', mode='w', newline='') as result_file:
    result_writer = csv.writer(result_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    result_writer.writerow(['bestand', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5', 'x6', 'y6', 'x7', 'y7', 'x8', 'y8'])

    for filename in glob.glob('{folder}*ABR_11Hz_100dB.fig'.format(folder=folder)):
        try:
            x = loadmat(filename)

            results=[]
            base=x['hgS_070000'][0,0][2][0, 0][20][0, 0]

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

            row=[filename]
            for sortedResult in sorted(results, key=lambda k: k[0]):
                row.append(sortedResult[0])
                row.append(sortedResult[1])
            result_writer.writerow(row)

        except:
            result_writer.writerow([filename])
