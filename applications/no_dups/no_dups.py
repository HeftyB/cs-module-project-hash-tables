def no_dups(s):
    # Your code here
    split = s.split(" ")
    # print(split)
    set1 = set(list(split))
    # print("set")
    # print(set1)

    new_string = ""
    for i in split:
        if i in set1:
            if len(new_string) == 0:
                new_string = i
                set1.remove(i)
            else:
                new_string = new_string + " " + i
                set1.remove(i)

    return new_string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))