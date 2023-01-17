# Write a Program that takes two lists and returns True if they have at least common member.

def findCommon(list1,list2):
    res= False
    for x in list1:
        for y in list2:
            if x==y:
                res=True
                return res

print(findCommon([1,2,3,4,4,1],[1,5,6,7,8,9,0]))
print(findCommon([2,3,4,5,67],[8,9,0,12,13]))

print("This program is done by 'Farooq Hussain")