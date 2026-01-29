import os

name = os.getenv("NAME")

if name:
    print("Hello", name)
else:
    print("Env Var Not Set")
