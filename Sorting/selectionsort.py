# selection sort

# select the begining index
# check other elements with the index so that lower values are found
# swap if found 


def selectionsort(ls):
    for i in range(len(ls)):
        min_index = i
        for j in range(i+1,len(ls)):
            if ls[j] < ls[min_index]:
                min_index = j
        (ls[i],ls[min_index]) = (ls[min_index],ls[i])


example_list = [13,1,45,87,23,56]
print(example_list)
selectionsort(example_list)
print(example_list)
        