print "hello";

import random
import sys
import time

if len(sys.argv) < 3:
    print 'must pass n and samples'
    sys.exit()

class HashTable:

    def __init__(self):
        self.tableLength = 105613
        self.HA = [None]*self.tableLength
        self.collissions = 0

    def ourHash(self, x):
        return  (x**2)%self.tableLength

    def collission(self, step, index, colType):
        if colType == 'par':
            return (index + step**2)%self.tableLength
        if colType == 'lin':
            return (index+1)%self.tableLength

    def insertItem(self, value, colType):
        index = self.ourHash(value)
        step = 1

        if self.HA[index] == value:
            return

        while(self.HA[index] and step < 100000):
            self.HA[index] = self.HA[index] + ','#+str(value)
            self.collissions += 1
            index = self.collission(step,index,colType)
            step+=1

        if(step == 1000):
            print 'collission, overwriting index '+str(index)

        self.HA[index] = str(value)

    def printTable(self):
        for i, v in enumerate(self.HA):
            print str(i) +': '+ str(v)

        print 'collissions ' + str(self.collissions)

    def histogram(self, other):
        i = 0
        while i<len(other):
            other[i] = int(other[i])+1 if self.HA[i] else other[i]
            i+=1
        return other


#exItems = [2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4]

def testItems(items,samples,colType):
    its = 0
    cols = []
    times = []
    randTimes = []
    histogram = [0]*100

    while its < samples:
        start = time.time()

        exItems = []
        i = 0

        randStart = time.time()
        while(i < items):
            exItems.append(random.randint(0,999999))
            i+=1
        randEnd = time.time()
        randTime = randEnd-randStart
        randTimes.append(randTime)

        ht = HashTable()

        for i in exItems:
            ht.insertItem(i,colType)

        #histogram = ht.histogram(histogram)

        cols.append(ht.collissions)

        its += 1

        #ht.printTable()

        end = time.time()
        times.append(end-start)
        #print 'iteration '+str(its)+' time: ' + str(end - start) + '   rand time: ' + str(randTime)

    #for i, v in enumerate(histogram):
    #    print str(i) +': '+ str(v)

    total = 0
    for i in cols:
        total += i
        #print i

    totalTime = 0
    for i in times:
        totalTime += i
        #print i

    totalRandTime = 0
    for i in randTimes:
        totalRandTime += i
        #print i

    print 'avg time: ' + str(totalTime/len(times)) + '   avg randTime: ' + str(totalRandTime/len(randTimes))
    return str(total/len(cols))

items = int(sys.argv[1])
samples = int(sys.argv[2])

par = testItems(items,samples,'par')
lin = testItems(items,samples,'lin')

print 'parabolic avg col: ' + par + '    n = ' + str(items) + ' samples: ' + str(samples)
print 'linear avg col:    ' + lin + '    n = ' + str(items) + ' samples: ' + str(samples)
