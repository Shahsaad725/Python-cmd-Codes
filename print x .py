k = 1

height = int(input("enter the height of the X shape:"))

if height % 2 !=0:
    height += 1

max_ = height
mid = height / 2


for line in range(1,(height+1),1):
        for check in range(1,(height+1),1):
            if check == k:
                print("+", end=" ")
            elif check == max_ and k != max_:
                print("+",end=" ")
                print(" ")
                break
            else:
                print(" ", end="")

        if line < height / 2:
            max_ -= 1
            k = line+1
        else:
            max_ +=1
            k -= 1