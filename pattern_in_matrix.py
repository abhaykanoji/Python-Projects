import numpy as np

row = int(input("enter row value: "))
# col = int(input("enter col value: "))
arr = np.random.randint(row, size=(row,row))
print(arr)
# arr=[[1,2,3,4,],
#     [1,2,3,4,],
#     [1,2,3,4,],
#     [1,2,3,4,],]
p = 0
for i in range(0,row-1):
  # print(i)
  for j in range(0,row-1):
    # print(j)
    if (j+2)>=row:
      break
    if(i+2)>=row:
      break
    print("-"*10)
    select_row = 1
    s = 0
    for k in range(i,i+3):
      select_col = 1
      for l in range(j,j+3):
        if select_row==2:
          if select_col==2:
            print("",arr[k][l],end="")
            s += arr[k][l]
          else:
            print(" ",end="")
        else:
          print(arr[k][l],end=" ")
          s += arr[k][l]
        select_col += 1
      print(" ")
      select_row += 1
    p += 1
    print("-"*10)
    print(f"total : {s}")
print("-"*10)
print(f"poss : {p}")
print("-"*10)
       