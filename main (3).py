'''python program to rearrange an array such that a[i]==i, a[i] != i return -1'''

def Array(ar,n):
  for i in range(n):
    for j in range(n):
      if(ar[j]==i):
        ar[j],ar[i]= ar[i],ar[j]

  for i in range(n):
    if(ar[i] != i):
      ar[i] = -1

  print("Array after rearrangement:")
  for i in range(n):
    print(ar[i],end = " ")

ar = [-1,-1,6,1,9,3,2,-1,4,-1]
n = len(ar)

Array(ar,n)

