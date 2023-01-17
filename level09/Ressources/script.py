import sys

def main(str):
	new = ""
	j = 0
	for i in str:
		new += chr(ord(i) + j)
		j -= 1
	print(new)

main(sys.argv[1])