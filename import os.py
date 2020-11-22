import os
path = '.'
i = 0
n = 0
s=0  
for root, dirs, files in os.walk(path):
    for fl in files:
        if not fl.endswith('.pdf'):
            continue
        i += 1
   
        if not fl.endswith('.py'):
            continue
        n += 1
        if not fl.endswith('.mp3'):
            continue
        s += 1
if i>s and i>n:
    print(i)
if s>i and s>n:
    print(s)
if n>i and n>s:
    print(n)
    

def bypass(path, level=1):
   
    for i in os.listdir(path):
        if os.path.isdir(path +'\\'+i):
            
            
            print('Level=',level)
            
            bypass(path+'\\'+i,level+1)
                 
                
            print(level)
            
bypass(path)


