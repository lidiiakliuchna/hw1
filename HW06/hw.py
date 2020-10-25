d = {}
with open("amh.tsv", encoding='utf-8') as file:
    vovel = file.readline()
    for line in file:
        key, *value = line.split()
        d[key] = value
    
    print("Enter text: ")
    st = str(input())
    result = list()
    len_st = len(st)
    for i in range(0,len_st):
        if st[i] in d:
            simb = d[st[i]]
            result = result + simb
 
    print(result)
