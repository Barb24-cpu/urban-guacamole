# testing kwargs
#
#List of kwargs
#The list of kwargs
# kwargs= dictionary
#list all the kwargs
def myKwargs(**kwargs):
    print("Kwargs is ", type(kwargs))
    print(kwargs)
    #print("b is", kwargs["b"])


#Senario a=23, b=30 =? {a:23, b:30}
#myKwargs(a=23, b=30, c=40)# {}
#kwargs-> {"a":23, "b":30}

#senario bno 3
#name="Samson" email="Samson@gmail.com"
#myKwargs({"name": "Samson",})
myKwargs(name="Samson", email="Sam@sam.com", dict={"a":"a"})

def area_rectangle(length, width):
    area = length * width
    print(f"For rectnagle with length {length} and Width {width} are is {area}")

#option 1 you call it directly with args.
area_rectangle(5, 2) #args
width = 4
length = 39
area_rectangle(width, length) #args
area_rectangle(width=width, length=length) #KWARGS
#option 3 you with kwargs:
area_rectangle(width=10, length=55)
#you have to match the parameter names with arguments
area_rectangle(width=10, length=55)
# area_rectangle(40)