def word_count(s):
    # Your code here
    print(s)
    s = s.lower()
    print(s)
    dict = {}
    for c in s:
        if (c == "\"") or (c == "\'") or (c == "\"") or (c == ":") or (c == ";") or (c == ",") or (c == ".") or (c == "-") or (c == "+") or (c == "/") or (c == "\\") or (c == "|") or (c == "[") or (c == "]") or (c == "{") or (c == "}") or (c == "(") or (c == ")") or (c == "*") or (c == "^") or (c == "&") or (c == " "):
            print(c)
            list(s).remove(c)

    if len(s) == 0:
        return dict

    x = s.split(" ")
    for i in x:
        print(i)
        if i not in dict:
            dict[i] = 0
        dict[i] += 1
    #if len(x) == 0:
    #    return []
    print(dict)
    return dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
