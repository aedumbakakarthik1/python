"""
1)int
---
decimal
binary
octal
hexadecimal

bin()
oct()
hex()

1,2,3,,2334,23,13,3456

2)float
-----
2.111
9.08
4.67
99999.52
1.2e4

3)complex number
------
a+bj it is allow but a+jb in not allowed
a=>real part
b=>imaginary part


4)bool
------
True  and
False



str:
----------

single quoted ==> string
double quoted ==> string
triple quoted ==> multi line String literal






"""
# print(True/False)
#ZeroDivisionError: division by zero

name="karthik "
print( name[0])
print( name[3])
print( name[-5])

#name[start:end]   returns substring from begin to end-1 index

print(name[0:7])

full_name = "aedumbaka karthik"
#full_name[start:end:step] 
print(full_name[0:15:2])

print(name*3)


"""
len()

this is use to get the length of thr string and


"""

print(len(name))
print(len("hello karthik"))



"""
python 's fundametal data types:
2. char ==> str type only
3. long ==> int type only


"""

"""
----------------------------------------------------------------
type Casting:
------- -----
we can covent one type to another type
it is alo know as type coersion
------
int()
float()
complex()
bool()
str()


"""
a=8097.456789
print(int(a))
b=786
print(float(b))
c=764
print(complex(c))
d=6997
print(bool(d))
e=0 
f=1
print(bool(e))
print(bool(f))
j=208765
print(str(j))
k=10+9j
print(int(k)) #TypeError: can't convert complex to int

