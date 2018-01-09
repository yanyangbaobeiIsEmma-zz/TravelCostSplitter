
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
class splitter(object):
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