## PYTHON COURSE

# Hello Word

```py
print('Hello')
```

# Function

 -- Avalible in Py --

print() : show screen
input() : allow user type
...

# Return Values

-- variable
x = something is Number, String, Object,...

> Ex: name = input('Your name')

```py

    name = input('what is your name ? ')
    print('Your name is', name)

```

-> orther code

> print('sting' + variable)
> print('sting' , variable)

```py

    name = input('what is your name ? ')
    print('Your name is' + name)

```

# Comments

-> say code do

> systax : # comment -> one line

> ''' muli comment '''


> Ex : # Ask your for their name

```py
    # Ask user for their name
    name= input('What your name?')
```

# pseudocode

-> phac thao program step by step

```py
    # ask user name?

    code

    # say user name

    code
```


# string

print(*object, sep=" ", end= '\n', file=sys.stdout, flush= False)

> *object -> khong gioi han object
> sep=" " -> "separator" phan cach -> " " -> single blank
> end='\n' -> new line
>

ex: 
```py
name = input("what's your name?")

print("hello, ",)
print(name)

```
-> hello,
-> David

ex: 

```py
name = input("what's your name?")

print("hello, ", end="")
print(name)
```
-> hello, David

ex: 
```py
name = input("what's your name?")

print("hello, ", end="???")
print(name)
```

-> hello,???David

ex: 
```py
name = input("what's your name?")

print("hello, ", name, sep='???')

```
-> hello,???David

ex: 
```py
name = input("what's your name?")

print("hello, \\"Tuan"")

```
-> hello, Tuan

### F Format code

ex: 
```py
name = input("what's your name?")

print(f"hello, {name}")

```
-> f : format string : chuoi dac biet

-> hello, Tuan


## String (str)

### Remove whitespace from str

name = input('Whats your name?')

> name = name.strip()


### Capitial user's name

name = name.capitalize()


### Title user name
name = name.title()

> Nguyen Quoc Tuan

### Combine with strip method and title method ...

ex :

```py
name = input("what's your name?")

name = name.strip().title()

print(f"hello, {name}")

```

> Nguyen Quoc Tuan


### Split user's name into first name and last name

```py
name = input('whats your name ? ').strip().title()

fistName, lastName = name.split()

print(f'your firstName is {firstname} and lastName is {lastname}')

```

-> your firstName is {firstname} and lastName is {lastname}



## int 

> + - * / %

### interactive mode

- using command 

> cmd: py -> >>> command python

---- end interactive mode ---

Ex 
```py
x = input("what's x ?")
y = input("what's Y ?")

z= x + y

print (f'z is {z}')

```

-> return " z is 1012"

-> because x and y is string and + to combine 2 string 
> solution is convert string to number by int() method

Ex:

* way 1

```py
x = input("what's x ?")
y = input("what's Y ?")

z= int(x) + int(y)

print (f'z is {z}')

```
-> return " z is 10"


* way 2

```py
x = int(input("what's x ?"))
y = int(input("what's y ?"))


z= x + y

print (f'z is {z}')

```

-> return " z is 10"

## Float


```py
x = float(input("what's x ?"))
y = float(input("what's y ?"))

z= x + y

print (f'z is {z}')

```

-> x = 3.3 ; y=5.5 -> z= 7.7

### Round method

-> up number ex 4.6 = 5

> systax: round(number[, ndigits])



```py
x = float(input("what's x ?"))
y = float(input("what's y ?"))

z= round(x + y)

print (f'z is {z}')

```

-> x = 3.3 ; y=5.5 -> z= 7.7 => 8


Ex : 1000 -> 1,000

```py
x = float(input("what's x ?"))
y = float(input("what's y ?"))

z= round(x + y)

print (f'z is {z:,}')

```

-> x = 999 ; y=1 -> z= 1000 => 1,000



### round (lam tron 2 chu so)

ex: 

```py
x = float(input("what's x ?"))
y = float(input("what's y ?"))

z= x / y

print (z)

```

-> x = 5 ; y=3 -> z= 0,666666

ex: 

> syntax : round(number, [so lam tron ])

```py
x = float(input("what's x ?"))
y = float(input("what's y ?"))

z= round(x / y, 2)

print (z)

```

-> x = 3 ; y=2 -> z= 0,67


### round with format string ({variable:.2f})

>syntax print(f'{x:.2f}')

-> .2 : lam tron 2 chu so

ex: 

```py
x = float(input("what's x ?"))
y = float(input("what's y ?"))

z= x / y

print (f'z is {z:.2f}')

```

-> x = 3 ; y=2 -> z= 0,67


## Function

 >syntax : def 
 -> def is define (create)

 
