def args_kwargs(*args,**kwargs):
    print("--------------------------------")
    print("All args",args)
    print("All kwargs",kwargs)
    print("--------------------------------")

#Error
#args_kwargs(a=2,b=30,45,39)
args_kwargs(45,39,a=2,b=30,)