from collections import deque

######### STACK YAPISI ############

liste_1=[1,2,3,4,5]
print(liste_1)

liste_1.append(15)
print(liste_1)

print(liste_1.pop())
print(liste_1)

#########  QUEUE YAPISI  ################

liste_2=[11,22,33,44,55]
print(liste_2)

liste_2.append(15)
print(liste_2)

print(liste_2.pop(0))
print(liste_2)



liste_3=deque([111,222,333,444,555])
print(liste_3)

print(liste_3.popleft())
print(liste_3)
