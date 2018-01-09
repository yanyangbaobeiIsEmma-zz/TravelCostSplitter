# TravelCostSplitter
a python class to split cost between friends

Example to use the code:

```python
mySplit = spliter()
mySplit.addPerson('A')
mySplit.addPerson('B')
mySplit.addPerson('C')
mySplit.addPerson('D')
mySplit.addPerson('E')
mySplit.addItem("food", 20, 'C', {'A', 'B', 'C'})
mySplit.addItem("rent", 50, 'B', {'A', 'B', 'C', 'D', 'E'})
finalPayment = mySplit.Split()
# finalPayment is a dictionary of payments
```



