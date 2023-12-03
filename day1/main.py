import regex

if __name__ == "__main__":
    total = 0

    f = open("input", "r")
    lines = f.readlines()

    d = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    e = {element: str(index + 1) for index, element in enumerate(d)}

    f = regex.compile(r"((?:\d)|(?:%s))" % "|".join(d))

    for line in lines:
        if len(line) > 0:
            a = f.findall(line, overlapped=True)

            r1 = a[0]
            r2 = a[len(a) - 1]

            if len(r1) > 1:
                r1 = e[r1]

            if len(r2) > 1:
                r2 = e[r2]

            r = r1 + r2
            print(line.strip())
            print(a)
            print(r)
            i = int(r)
            total += i
            print("---")

    print(total)
