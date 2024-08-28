'''Draw the patten 'P' '''

num = 5
for i in range(num):
    if i == 0 or i == 2:
        for i in range(num-1):
            print('&' , end = ' ')
        print()
    elif i == 1:
        for a in range(num-1):
            if a == 0:
                print('&' , end = ' ')
            elif a == 3:
                print('&')
            else:
                print(' ',end = ' ')       
    else:
        print('&')
        
'''Output
->& & & & 
->&     &
->& & & & 
->&
->&'''