#https://www.hackerrank.com/challenges/python-tuples/problem
n = raw_input()
input_line = raw_input()
input_list = input_line.split()
input_list = map(int, input_list)
input_list = [int(x) for x in input_list]
t = tuple(input_list)
print hash(t)
