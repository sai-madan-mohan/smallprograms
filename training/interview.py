# # slicing function
# def reverse_string(s):
#     return s[::-1]
# print("reverse word is : ", reverse_string("SAIMADAN"))

# # "reversed function"
# s="MADAN"
# reverse_str=''.join(reversed(s))
# print("reversed word is" , reverse_str)

# checking is palindrome
def is_palindrome(s):
    return s == s[::-1]
s ="MADAMs"
if is_palindrome(s):
    print(f"{s} is palindrome")
else:
    print(f"{s} is not a palindrome")

# counting vowels
def count_vowels_consanants(s):
    vowels="AEIOUaeiou"
    v_count=0
    c_count=0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v_count+=1
            else:
                c_count+=1
    return v_count,c_count
s="MADAM"
v,c=count_vowels_consanants(s)
print(f"vowels count is {v} and consonants count is {c}")

# checking is prime
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n = 5
print(f"{n} is prime" if is_prime(n) else f"{n} is not prime")

# checking is fibonacci           
def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,a+b
fibonacci(9)

def factorial(n):
    result=1
    for i in range(2,n+1):
        result*=1
    return result
print(factorial(9))

def factorial_recursive(n):
    return 1 if n==0 else n*factorial_recursive(n-1)
print(factorial_recursive(5))


def even_odd(n):
    if n%2!=0:
        print("odd")
    else:
        print("even")
even_odd(9)