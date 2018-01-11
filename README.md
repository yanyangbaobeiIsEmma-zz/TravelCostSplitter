# TravelCostSplitter
a python class to split cost between friends

Example to use the code:

```python
from TravelSplitter import SmartSplitter
import heapq as hp

grandCanyon = SmartSplitter()

# add persons
grandCanyon.addPerson('Guodong')
grandCanyon.addPerson('Yu')
grandCanyon.addPerson('Xuelian')
grandCanyon.addPerson('Yanyang')
grandCanyon.addPerson('Can')

allPersons = {'Guodong', 'Yu', 'Xuelian', 'Yanyang', 'Can'}
girls = {'Xuelian', 'Yanyang', 'Can'}
boys = {'Guodong', 'Yu'}
ubers = {'Guodong', 'Xuelian', 'Yanyang'}

# add cost:
# from Guodong
grandCanyon.addItem('SedonaPizzaCompany', 63.75, 'Guodong', allPersons)
grandCanyon.addItem('AlamoRent', 184.46, 'Guodong', allPersons)
grandCanyon.addItem('BlackBartsSteakHouse', 253.70, 'Guodong', allPersons)
grandCanyon.addItem('CowboyClub', 19.67, 'Guodong', allPersons)
grandCanyon.addItem('GreatWallOfChinaCuisine', 85.00, 'Guodong', allPersons)
grandCanyon.addItem('MandarinGourmet', 70.00, 'Guodong', allPersons)
grandCanyon.addItem('SwaddeeThaiCuisine', 86.22, 'Guodong', allPersons)
grandCanyon.addItem('TravelInsurancePolicy', 36.00, 'Guodong', allPersons)
grandCanyon.addItem('GrandCanyon', 30.00, 'Guodong', allPersons)

# from Yu
grandCanyon.addItem('Gas', 23.04 + 32.88, 'Yu', allPersons)
grandCanyon.addItem('Parking', 7.00, 'Yu', allPersons)

# from Xuelian
grandCanyon.addItem('BoyHotel', 250.13, 'Xuelian', boys)
grandCanyon.addItem('GirlHotel', 282.14, 'Xuelian', girls)
grandCanyon.addItem('Antelope', 340, 'Xuelian', allPersons)
grandCanyon.addItem('SafeWay+Parking', 69.57, 'Xuelian', allPersons)
grandCanyon.addItem('Uber', 25.48 + 16.65, 'Xuelian', ubers)

finalPay = grandCanyon.Split()
finalPay
```
output:
```python
{('Can', 'Guodong'): 107.03066666666666,
 ('Can', 'Xuelian'): 247.27399999999983,
 ('Yanyang', 'Xuelian'): 368.348,
 ('Yu', 'Guodong'): 322.403}
```



