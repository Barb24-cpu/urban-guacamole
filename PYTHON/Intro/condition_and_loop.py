age = 20

# if(<conditions>){
# 
# }
if age > 18: #end of for loop or if
    print("You can drink")
    print("Something Else")
    if age == 23:
        print("This is awsome")
    print("Another line")
#else if
elif age == 44:
    print("You are not that young")
else:
    print("Last else")


k = 0


while k < 30:
    k = k + 1
    print("K is ", k)


# range(start,stop,step)
for i in range(0, 5, 1):
    print("I is ", i)

ar = [23, "hello", 67, 45, 40] #5
#for(let i=0;i<ar.length;i++){0-99}
for i in range(0, len(ar)):
    single_item = ar[i]
    print(single_item)

#for(let singleItem of arr)
for single_item in ar:
    print("Single item", single_item)