def find_max(arr):
    max_val = float('-inf')
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def main():
    # Example usage
    array = [3, 7, 2, 9, 4, 1, 8, 5, 6]
    maximum = find_max(array)
    print("Maximum value in the array:", maximum)

if __name__ == "__main__":
    main()
