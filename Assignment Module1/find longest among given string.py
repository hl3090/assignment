
l1 = ["pyhton","java","Android","Flutter"]

max = len(l1[0])

# print (max)
word = ""

for i in l1:
    if len(i)>max:
        word = i
        max = len(i)
        
print ("Max: ",max)
print ("Word: ",word)        
        