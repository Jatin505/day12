import random
maxn=10
n=random.randint(1,maxn)
print("Welcome to guess the number game!")
print("Guess the number form 1 to %d"%maxn)
guess=None
while guess!=n:
    guess=int(input("your try:"))
    if guess>n:
        print("too high")
    if guess<n:
        print("too low")
print("congratulation you won")
