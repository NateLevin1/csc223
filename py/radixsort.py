# see visualization: https://www.cs.usfca.edu/~galles/visualization/RadixSort.html

# radix sort (in place)
def radix_sort(list):
    # 1. Find the largest number in the array
    max_num = max(list)
    max_digits = len(str(max_num))

    # for each digit
    for i in range(0, max_digits):
        buckets = [[] for i in range(0, 10)]
        # create buckets - number with ith digit n is put into nth bucket
        for j in range(0, len(list)):
            num = list[j]
            digit = int(num / 10**i) % 10 # digit at pass-th place
            buckets[digit].append(num)
        
        # collect buckets & modify list in place
        index = 0
        for bucket in buckets:
            for num in bucket:
                list[index] = num
                index += 1

    return list

print(radix_sort([5,4,3,2,1]))
print("\n\n\n")

if __name__ == "__main__":
    list = []
    while True:
        user_input = input("\nEnter a number: ")
        num = 0
        try:
            num = int(user_input)
        except:
            print("No number provided, exiting.")
            break
        list.append(num)
        print("\nInput:")
        print(list)
        print("Output:")
        print(radix_sort(list))