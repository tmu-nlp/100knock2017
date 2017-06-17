with open('answer50.txt','r') as i_f,open('answer51.txt','w') as a_f:
    for line in i_f:
        ans = line.split()
        for i in range(len(ans)):
#            print(ans[i])
            a_f.write(ans[i] + '\n')
#        print('\n')
        a_f.write('\n')
