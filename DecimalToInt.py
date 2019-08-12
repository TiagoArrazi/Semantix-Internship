from decimal import Decimal
from inspect import getmembers


a = Decimal(105000)
print(getmembers(a))
print(a.real)
print(type(a.real))
