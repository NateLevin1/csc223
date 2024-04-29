with open("aliceinwonderland.txt", "r") as f:
    arr = f.readlines()
    chars = {}
    for line in arr:
        for char in line:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1

    alphabet = chars.keys()
    sorted_alphabet = sorted(alphabet, key=lambda x: chars[x])

    print("#define ALPHABET_SIZE "+str(len(sorted_alphabet)))
    print("const char alphabet[ALPHABET_SIZE] = ", end="")
    print("\"", end="")
    for char in sorted_alphabet:
        if char == "\n":
            print("\\n", end="")
        elif char == "\"":
            print("\\\"", end="")
        else:
            print(char, end="")
    print("\";")

    print("const int freq[ALPHABET_SIZE] = ", end="")
    print("{", end="")
    for char in sorted_alphabet:
        print(chars[char], end=", ")
    print("};")

    
    