def bullets_sort(x):
    swap=0
    steps = 0
    n = len(x)
    pass_no = 0
    for i in range(n-1, 0, -1):
        pass_no += 1
        swapped = False  
        for j in range(i):
            steps += 1
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                print(x)
                swapped = True
                swap += 1  
                
        if not swapped:  
            break
        
    print("Swap:", swap)
    print("Steps:", steps)
    print("Passes:", pass_no)

if __name__ == "__main__":
    bullets_sort([2,1, 12,19,18,8, 15, 7, 3, 4, 6, 5, 11, 10, 9, 14, 13, 17, 16, 20])
