
############################################################# while

# 1 Initialize offset

offset=8

# Code the while loop

while offset != 0 :
 print("correcting...")
 offset = offset - 1
 print(offset)


# 2 Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset -1
    else :
      offset = offset+1
    print(offset)


############################################################# for

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for aa in areas:
    print(aa)



# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas) :
    print("room" + str(index) + ":" + str(area))



