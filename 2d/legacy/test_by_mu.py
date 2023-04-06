

x = 0
#x_seq = [x]
x_seq_list = [[x]]

N = 2

for i in range(N):
    sub_list = x_seq_list[-1]
#    print(sub_list)
    sub_list.append(1)
#    print(sub_list)
#    print(x_seq_list)

x_seq_list.append(sub_list)
#print(x_seq_list)

outlist = [[j for j in range(k)] for k in range(1,5)]
print(outlist)

#outlist[-1].append(1)
outlist[-1][-1] += 1
print(outlist)