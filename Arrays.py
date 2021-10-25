def max_product(arr):
    length = len(arr)
    if(length<=2):
        print("No Pair Exists")
        return
    x=arr[0];y=arr[1]

    #traversing the array with every possible pair
    for i in range(0,length):

        for j in range(i+1,length):

            if(arr[i]*arr[j]>x*y):
                x=arr[i];y=arr[j]

    return x,y
            
    

num = [17,25,129,96,9602,5134]
print("Array values: ",num)
print("Maximun Product pair:",max_product(num))
