def main():
    
    list1 = [1, 2,2, 4,234, 3]
    
    list2 = [1, 3, 5, 2, 4, 4, 5, 23, 234 ]
    
    #set1 , set2 = set(list1), set(list2)
    
   # commonlist =list1.intersection(list2)
    
    #print(commonlist)
    
    commonlist = []
    
    for num in list1:
        if num in list2 and num  not in commonlist:
            commonlist.append(num)
            
    print(commonlist)       
    
    
if __name__ == "__main__":
       main() 