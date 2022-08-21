import argparse

parser=argparse.ArgumentParser()
parser.add_argument("number1",help="first number")
parser.add_argument("number2",help="second number")
args=parser.parse_args()

print(args.number1)
print (args.nunber2)
