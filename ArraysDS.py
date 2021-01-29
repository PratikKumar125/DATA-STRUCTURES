'''
#find duplicates in an array
arr = [1, 2, 3, 6, 3, 6, 1]
dup = []
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            dup.append(arr[i])
print(dup)


Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’.

Examples:  

Input  :  arr[] = {1, 5, 7, -1}, 
          sum = 6
Output :  2
Pairs with sum 6 are (1, 5) and (7, -1)
arr = [1, 5, 7, -1, 5]
s = 6
count = 0
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j] == s:
            count+=1
print(count)


#to find the missing number 
arr = [1, 2, 4, 6, 3, 7, 8]
n = len(arr)
total = ((n+1)*(n+2))//2
s = sum(arr)
missing = total-s
print(missing)

#move all negative elements to one side of the array
arr = [2, 5, 9, -3, 5, -2]
print(arr)
j=0
for i in range(0, len(arr)):
     if (arr[i] < 0) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp
            j = j + 1
print(arr)


#find the occurence of an integer in the array
arr = [1,3,5,1,1]
count = 0
for i in range(0, len(arr)):
    for j in range(0, len(arr)):
        if arr[i] == arr[j]:
            count+=1
        else:
            count = count
    print(arr[i],"occurs",count,"times")
    count = 0
   
#find union and intersection of two sorted arrays
arr1 = [1,2,3,4,5]
arr2 = [4,5,6,7,8]
union = []
inter = []
for i in range(0, len(arr1)):
    for j in range(0, len(arr2)):
        if arr1[i] == arr2[j]:
            inter.append(arr1[i])
        if arr1[i]!= arr2[j]:
            union.append(arr1[i])
            union.append(arr2[j])
            
print("intersection = ",inter)
print("union = ",set(union))


#find the leader
arr= [1,10,8,13,4]
for i in range(0,len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]<arr[j]:
            break
    if j == len(arr)-1:
        print(arr[i])


 

#to print the array in reverse order
arr = [1,2,3,4,5]
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end = " ")

#to find the max and min elemnt of the array
arr = [1,7,3,5]
maxnum = arr[0]
minnum = arr[0]
for elem in arr:
    if (elem)> maxnum:
        maxnum = elem
    elif (elem)< minnum:
        minnum = elem   
print(maxnum)
print(minnum)


#find the Kth max and Kth min element in an array
arr = [10, 5, 18, 20]
            #bubble sort
for i in range(len(arr)-1,0,-1):
    for j in range(i):
        if arr[j]>arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        else:
            pass
k = int(input("kth max and min"))
print("kth max", arr[-k])
print(arr[k-1])
'''
