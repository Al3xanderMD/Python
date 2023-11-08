def ascii_list(x=1, lst=[], flag=True):
    result = []
    for string in lst:
        temp = []
        for char in string:
            if (ord(char) % x == 0) == flag:
                temp.append(char)
        if temp:
            result.append(temp)
    return result

def main():
    lst = []
    while True:
        string = input("Enter a string: ")
        if string == "":
            break
        lst.append(string)
    x = int(input("Enter X number: "))
    flag = input("Enter 0 for even, 1 for odd: ")
    if flag == "0":
        flag = False
    elif flag == "1":
        flag = True
    else:
        print("Invalid input!")
        return
    result = ascii_list(x=x, lst=lst, flag=flag)
    
    print(result)

if __name__ == "__main__":
    main()
