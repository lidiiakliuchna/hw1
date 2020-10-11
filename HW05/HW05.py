with open("poem.txt", encoding="utf-8") as f:
    lines = f.readlines()
    average=0
    m = 0
for index, value in enumerate(lines):
        number_of_words = len(value.split())
        m += 1
        average += number_of_words 
k = average/m      
print(k) 
list_of_lists = []
for line in lines:
    line = line.split()
    list_of_lists.append(line)
 
sorted_lists = (sorted(list_of_lists, key=len))
diff = len(sorted_lists[-1])/len(sorted_lists[0])
print(diff)    
counter = 0   
percentage = 0 
with open("poem.txt", encoding="utf-8") as f:
    line_count = 0
    for line in f:
        line_count += 1
    for index, value in enumerate(lines):
        number_words = len(value.split()) 
        if number_words>5: 
            counter += 1
    percentage = (counter * 100)/line_count
print(percentage)