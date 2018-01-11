
#### split money
## assumption 1: 1 item is only paid by one person
## assumption 2: the payer can be or not be the taker of the item: need checker!
## for 1 item: I have 1 payer, and multiple takers, 
## takers need to share the cost
## input: 
# per item: store in dict
# payer
# takers (including payer)
# cost

# output:
# payments from between persons
class NaiveSplitter(object):

    def __init__(self):
        self.persons = set()
        self.items = dict()

    def addPerson(self, person):
        self.persons.add(person)

    def addItem(self, item, cost, payer, takers):
        # let takers be a set
        if payer not in self.persons:
            return "Check this payer's name, it is not added yet!"
        for taker in takers:
            if taker not in self.persons:
                return "Check this taker's name " + str(taker) + ", it is not added yet!"
        if item in self.items:
            return str(item) + " is already in items! Double check!"
        self.items[item] = [payer, takers, cost]

    def Split(self):
        # first create a ledger & initialize
        # definition: person1 owe (need to pay) person2 # of money
        ledger = dict()
        finalPay = dict()
        for person1 in self.persons:
            for person2 in self.persons:
                if person1 != person2:
                    ledger[(person1, person2)] = 0
                                                   
        for item in self.items:
            payer, takers, cost = self.items[item]
            for taker in takers:
                if taker != payer:
                    ledger[(taker, payer)] += cost * 1.0/len(takers)
                    ledger[(payer, taker)] -= cost * 1.0/len(takers)
        personsList = list(self.persons)
        for i in range(len(personsList)):
            for j in range(i+1, len(personsList)):
                payment = ledger[(personsList[i], personsList[j])]
                if payment >= 0:
                    finalPay[(personsList[i], personsList[j])] = payment
                    print(str(personsList[i]) + " owe "  + str(personsList[j]) + " " +  str(payment))
                else:
                    finalPay[(personsList[j], personsList[i])] = - payment
                    print(str(personsList[j]) + " owe " + str(str(personsList[i])) + " " + str(-payment) )
        return finalPay



### A smart cost splitter will ouput minimum number of transactions
class SmartSpliter(object):
    def __init__(self):
        self.persons = set()
        self.items = dict()
        
    def addPerson(self, person):
        self.persons.add(person)
        
    def addItem(self, item, cost, payer, takers):
        # let takers be a set
        if payer not in self.persons:
            return "Check this payer's name, it is not added yet!"
        for taker in takers:
            if taker not in self.persons:
                return "Check this taker's name " + str(taker) + ", it is not added yet!"
        if item in self.items:
            return str(item) + " is already in items! Double check!"
        self.items[item] = [payer, takers, cost]
        
    def Split(self):
        ledger = dict() # key: person, value = [payment amount, need to pay amount]
        transaction = dict()
        for person in self.persons:
            ledger[person] = [0, 0]
        for item in self.items:
            payer, takers, cost = self.items[item]
            ledger[payer][0] += cost
            for taker in takers:
                ledger[taker][1] += cost * 1.0 / len(takers)
        #print (ledger)
        
        posHeap = []
        negHeap = []
        
        sumToReceive = 0
        for person in ledger:
            toReceive = ledger[person][0] - ledger[person][1]
            sumToReceive += toReceive
            if toReceive >= 0:
                hp.heappush(posHeap, (toReceive, person))
            else:
                hp.heappush(negHeap, (toReceive, person))
        #print(posHeap)
        #print(negHeap)
        
        # assert sum of posHeap + sum of negHeap = 0
        #print("sumToReceive = " + str(sumToReceive))
        assert(sumToReceive < 0.0001)
        
        while (len(posHeap) > 0 and len(negHeap) > 0) : 
            curPos = posHeap.pop() # the largest one
            curNeg = negHeap[0] # the smallest one 
            # curNeg need to pay curPos
            negHeap.remove(curNeg)
            
            diff = curPos[0] + curNeg[0]
            if diff >= 0:
                transaction[(curNeg[1], curPos[1])] = -curNeg[0]
                if diff > 0:
                    hp.heappush(posHeap, (diff, curPos[1]))
            else:
                transaction[(curNeg[1], curPos[1])] = curPos[0]
                hp.heappush(negHeap, (diff, curNeg[1]))
        return transaction      
