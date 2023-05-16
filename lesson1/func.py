def main():
    """
        1 .create variable x
        2 .pow it
    """
    x = int(input("What is x ?"))
    print(f'sqr of {x} is {sqr(x)}')

def sqr(x):
    return pow(x,2)

main()