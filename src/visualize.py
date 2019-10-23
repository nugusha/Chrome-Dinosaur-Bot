from db import Database
import matplotlib.pyplot as plt

import itertools
colors = itertools.cycle(["r", "b", "g"])

db = Database()
records = db.select()

recTrue = []
recFalse = []

for x in records:
    if(x[3]==1):
        recTrue.append(x)
    else:
        recFalse.append(x)


lengthT = [x[1] for x in recTrue]
lengthF = [x[1] for x in recFalse]
speedT = [x[2] for x in recTrue]
speedF = [x[2] for x in recFalse]

plt.plot(lengthT,speedT,'bo')
plt.plot(lengthF,speedF,'ro')

plt.show()