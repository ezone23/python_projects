# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:47:40 2020

@author: jiwon
"""

'''Quine McCluskey Method used
1. recieve input of minterm expression
2. convert inputs into binary number
3. determine the prime implicants
4. determine prime implicant chart
5. determine minimum solution using Petrick's method'''
# !!step 4 and step 5 not done!!

'''step 1. take in input'''
#recieve input of minterm expression devided with commas
minterm_expression = map(int,input("insert your minterm expression (divided with commas):").split(','))
minterms = list(minterm_expression)

'''step2. convert inputs into binary number'''
minterm_bin = []

#converting minterm into binary number
for minterm in minterms:
    if max(minterms)<8:       
        binary = format(minterm, "03b")  
        minterm_bin.append(str(binary))
        var_num = 3
    else:
        binary = format(minterm, "04b")  
        minterm_bin.append(str(binary))
        var_num = 4
               
#function to convert binary number into letter
def convert2letter(num):
    var0 = ['a','b','c','d']
    var1 = ['A','B','C','D']
    letter = ''
    for i in range(len(num)):
        if num[i]=='0':
            letter += var0[i]
        if num[i]=='1':
            letter += var1[i]
    return letter

#dividing minterms in groups
def group(num):
    count = 0
    for i in range(len(num)):
        if num[i]=='1':
            count +=1
    return count

'''step 3. determine prime implicants'''
#get each column for quine McCluskey method to determine prime implicants  
#Column 1
col1 = {0:[], 1:[], 2:[], 3:[], 4:[]}
for i in minterm_bin:
    for n in range(var_num+1):
        if group(i) == n:
            col1[n].append(i)

print(col1,'\n')

col1_val = list(col1.values())
col1_left = []
for x in col1_val:
    for y in x:
        col1_left.append(y)
#terms that are checked
col1_checked = []

#Column 2
col2 = {0:[], 1:[], 2:[], 3:[]}
for i in range(len(col1)):
    for n in range(len(col1[i])):
        count_left = 0
        for k in range(len(col1[i+1])):
            one_intersect = ''
            count = 0
            for l in range(var_num):
                if col1[i][n][l] == col1[i+1][k][l]:
                    one_intersect += col1[i][n][l]
                else:
                    one_intersect += '-'
                    count +=1
            if count<2:                
                col2[i].append(one_intersect)
                col1_checked.append(col1[i][n])
                col1_checked.append(col1[i+1][k])
            list(set(col2[i]))
col1_left = list(set(col1_left)-set(col1_checked))

col2_val = list(col2.values())
col2_left = []
for x in col2_val:
    for y in x:
        col2_left.append(y)
col2_checked = []

#Column 3
col3 = {0:[], 1:[], 2:[]}
for i in range(len(col2)):
    for n in range(len(col2[i])):
        for k in range(len(col2[i+1])):
            two_intersect = ''
            count = 0
            for l in range(var_num):
                if col2[i][n][l] == col2[i+1][k][l]:
                    two_intersect += col2[i][n][l]
                else:
                    two_intersect += '-'
                    count +=1
            if count<2:                
                col3[i].append(two_intersect)
                col2_checked.append(col2[i][n])
                col2_checked.append(col2[i+1][k])
            list(set(col3[i]))
col2_left = list(set(col2_left) - set(col2_checked))


for i in range(len(col3)):
    col3[i] = list(set(col3[i]))
    
col3_left = []
col3_val = col3.values()    
for x in col3_val:
    for y in x:
        col3_left.append(y)

#get prime implicants        
prime = []
#convert prime implicants into letter
#lowercase = 0, uppercase = 1   
for left1 in col1_left:
    prime.append(convert2letter(str(left1)))
for left2 in col2_left:
    prime.append(convert2letter(str(left2)))
for left3 in col3_left:
    prime.append(convert2letter(str(left3)))
print('prime implicants: ',prime)

f = ''
for i in prime:
    f += i
    f += ' + '

print('prime term is replaced as lower case')
print ('f=', f[:-3])

