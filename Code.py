list1 = [121, 91, 213, 115] 

def bubble_sort(list1): animations = []
9

    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            animations.append([0,j,j+1])
            animations.append([1,j,j+1])
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                
                animations.append([2,j,list1[j+1]])
                list1[j] = list1[j+1]
                animations.append([2,j+1,temp])
                list1[j+1] = temp 
    return animations
  
print(bubble_sort(list1)) 

