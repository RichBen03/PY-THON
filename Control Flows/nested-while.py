list1 = [1,2,3]
list2 = [4,5,6]

# for i in list1:
#     print(i, end=",")
#     for j in list2:
#         print(j,end=",")
#     print()
    
i=0 
while i < len(list1):
    j=0
    while j < len(list2):
        print(list1[i],list2[j], end="\t")
        j+=1
    print()
    i+=1