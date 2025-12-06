# Printing 1st subsequence whose sum is k

def gen_subseq_sum(sequence, k, index = 0, current_subseq = None, current_sum = 0):
    if(current_subseq is None):
        current_subseq = []

    #base
    if(index == len(sequence)):
        #Condition satisfied True val for method 
        # & outer false will not execute 
        if(current_sum == k):
            print(current_subseq)
            return True
        #Condition Not satisfied val will be False
        return False

    #include
    if(gen_subseq_sum(sequence, k, index+1, current_subseq + [sequence[index]], current_sum + sequence[index]) == True):
        return True

    #exclude
    if(gen_subseq_sum(sequence, k, index+1, current_subseq, current_sum) == True):
        return True
    
    #If none of the above 2 function calls return True
    #then return false
    return False



n = int(input("Enter seq length: "))
print("Enter elements: ")
seq = []
for i in range(n):
    seq.append(int(input()))

target_sum = int(input("Enter k: "))
gen_subseq_sum(seq, target_sum)

#TC = O(2^n)
#SC = O(n)




