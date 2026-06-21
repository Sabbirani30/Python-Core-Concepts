from linecache import updatecache
from typing import List

FirstTuple= ("Anik","Sabbir","Likhon","34","Anik","Likhon")
print(FirstTuple)
print(type(FirstTuple))
print(FirstTuple)
print(type(FirstTuple))


_2ndTuple=("Anik","Sabbir","Likhon")
print(FirstTuple)
print(type(FirstTuple))
print(_2ndTuple)
print(type(_2ndTuple))

_3rdTuple=("Anik","Southeast","CSE","294")
print(_3rdTuple)
print(type(_3rdTuple))
print(_3rdTuple)

#Access Items:
_4thTuple=("Anik","Southeast","CSE","294")
_4thTuple[2]
print(_4thTuple[2])
print(type(_4thTuple))

#Update:
FifthTuple=("Anik","Southeast","CSE",294,290)
Cd= list(FifthTuple)
Cd[2]="ML"
FifthTuple=tuple(Cd)
print("Update Item:",FifthTuple)