import random
count = 0

def linear_search(arr,x):  
    for i in range(len(arr)):
        if arr[i] == x:
            global count
            count = count + 1
            return i
    return -1

def avg(z):
    print(f'Average of the index is:  {z/count :.2f}')

def main():
    arr = random.sample(range(1,10000),1000)
    z = 0
    # x = int(input("Enter the number to search: "))
    x = random.sample(range(1,10000),100)
    for i in range(len(x)):
        y = linear_search(arr,x[i])
        if (y == -1):
            top = 0
        else:
            print("Element found at index: ",y)
            z = z + (y+1)
    avg(z)

if __name__ == "__main__":
    main()
    

    