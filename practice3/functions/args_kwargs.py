# 1
def total(*numbers):
    print(sum(numbers))
total(1, 2, 3)

# 2
def show_args(*args):
    for arg in args:
        print(arg)
show_args("Python", "Java", "C++")

# 3
def user_info(**data):
    for k, v in data.items():
        print(k, v)
user_info(name="Ali", age=22)

# 4

def example(*args, **kwargs):
    print(args)
    print(kwargs)
example(1, 2, name="Dana")
