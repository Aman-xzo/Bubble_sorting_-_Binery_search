
# Function for bubble sort
def B_short(l:list):
    for i in range(len(l),0,-1):
        for ii in range(i-1):
            if l[ii] > l[ii+1]:
                temp = l[ii]
                l[ii] = l[ii+1]
                l[ii+1] = temp

# Function for binery search
def B_search(lst:list, Search:int):
    try:
        Search = int(Search)

    except Exception as e:
        return "Value must be int"

    first_index = 0 
    last_index = (len(lst)-1) 
    
    try:
        while True: # <-- first_index <= last_index
            middle_index = (first_index+last_index)//2 

            if Search == lst[first_index]:
                # print ("fc 1")
                return first_index+1
                
            elif Search == lst[middle_index]:
                # print ("fc 2")
                return middle_index+1
                
            elif Search == lst[last_index]:
                # print ("fc 3")
                return last_index+1
                
            elif Search > lst[last_index] or Search < lst[first_index]:
                # print ("fc 4")
                return "Not found"


            elif (Search < lst[middle_index]): 
                # print("Second condition")
                last_index = middle_index -1

            elif (Search > lst[middle_index]):
                # print("Third condition")
                first_index = middle_index +1

    except Exception as e:
        return e

# trying both B_short and B_search
if __name__ == "__main__":
    l = [3,4,6,79,9,65,2,85,12,54,36]
    B_short(l)
    print(l)
    result = B_search(l,54)
    print(result)