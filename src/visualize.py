from db import Database
import matplotlib.pyplot as plt

import itertools
colors = itertools.cycle(["r", "b", "g"])

db = Database()
records = db.select()

recIter = len(records) - len(records)//20
records = records[recIter:]

recTrue = []
recFalse = []
recBeforeFalse = []

for x in records:
    if(x[3]==1):
        recTrue.append(x)
    elif(x[3]==0):
        recFalse.append(x)
    else:
        recBeforeFalse.append(x)


lengthT = [x[1] for x in recTrue]
lengthF = [x[1] for x in recFalse]
lengthBF = [x[1] for x in recBeforeFalse]

speedT = [x[2] for x in recTrue]
speedF = [x[2] for x in recFalse]
speedBF = [x[2] for x in recBeforeFalse]

plt.plot(lengthT,speedT,'bo')
plt.plot(lengthF,speedF,'ro')
plt.plot(lengthBF,speedBF,'mo')

plt.show()