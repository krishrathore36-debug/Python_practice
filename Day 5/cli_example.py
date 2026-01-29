import sys

# sys.argv[0] = file name
# sys.argv[1] = first argument

if len(sys.argv) > 1:
    print("Hello,", sys.argv[1])
else:
    print("No name provided")
