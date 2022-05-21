def multiply_and_greeting(*args,**kwargs):
    multiply=1
    for num in args:
        multiply*=num
    print(multiply)
    print(f"Hello{kwargs}")