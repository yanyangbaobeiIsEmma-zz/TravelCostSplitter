# TravelCostSplitter
a python class to split cost between friends

Example to use the code:

```python
grandCanyon = spliter()

# add persons
grandCanyon.addPerson('Guodong')
grandCanyon.addPerson('Yu')
grandCanyon.addPerson('Xuelian')
grandCanyon.addPerson('Yanyang')
grandCanyon.addPerson('Can')

# some cost share groups
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
```
output:
```python
Yanyang owe Yu 12.584
Yanyang owe Xuelian 190.004
Yanyang owe Guodong 165.76
Yanyang owe Can 0
Yu owe Xuelian 194.395
Yu owe Guodong 153.176
Can owe Yu 12.584
Guodong owe Xuelian 55.2623333333
Can owe Xuelian 175.960666667
Can owe Guodong 165.76

finalPay:
{('Can', 'Guodong'): 165.76,
 ('Can', 'Xuelian'): 175.96066666666667,
 ('Can', 'Yu'): 12.584000000000001,
 ('Guodong', 'Xuelian'): 55.26233333333333,
 ('Yanyang', 'Can'): 0,
 ('Yanyang', 'Guodong'): 165.76,
 ('Yanyang', 'Xuelian'): 190.004,
 ('Yanyang', 'Yu'): 12.584000000000001,
 ('Yu', 'Guodong'): 153.176,
 ('Yu', 'Xuelian'): 194.39499999999998}
```



