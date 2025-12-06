#Printing subsequences whose sum is k

def gen_subseq_sum(sequence, k, index = 0, current_subseq = None, current_sum = 0):
    if(current_subseq is None):
        current_subseq = []

    #base
    if(index == len(sequence)):
        if(current_sum == k):
            print(current_subseq)
        return
    
    #include
    gen_subseq_sum(sequence, k, index+1, current_subseq + [sequence[index]], current_sum + sequence[index])

    #exclude
    gen_subseq_sum(sequence, k, index+1, current_subseq, current_sum)


n = int(input("Enter seq length"))
print("Enter elements:")
seq = []
for i in range(n):
    seq.append(int(input()))

target_sum = int(input("Enter k: "))
gen_subseq_sum(seq, target_sum)

# [sequence[index]] - curr elem being considered as a list to be included in the subseq list
# sequence[index] - get the curr elem to be added
#TC = O(2^n)
#SC = O(n)




