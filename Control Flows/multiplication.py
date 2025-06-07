# initialize an outer loop to store the rows running from 1-10
for i in  range(1,11):
    #an inner loop storing the columns running from 1-1-0
    for j in range (1,10):
        #multiply the current value of i and j
        product = i * j
        print(f"{i} x {j} is {product}",end="\t")
    #after a complete interation(1-10) of the inner loop go to a new line   
    print()
