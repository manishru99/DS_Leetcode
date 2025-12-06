#78. Subsets

#Recursion on subsequences

def solve(i, arr, f):
    if i == len(arr):
        print(f, end=" ")
        return
    # Picking
    f.append(arr[i])
    solve(i + 1, arr, f)
    # Popping out while backtracking
    f.pop()
    solve(i + 1, arr, f)

def main():
    arr = [1, 2, 3]
    f = []
    print("All possible subsequences are:")
    solve(0, arr, f)

if __name__ == "__main__":
    main()
