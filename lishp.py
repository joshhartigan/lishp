import sys

variables = {}

def makeString(word):
    if word.startswith("{") and word.endswith("}"):
        return variables[word.replace("{", "").replace("}","")]
    else:
        return word

def transpile(line):
    words = line.split()
    if len(words) >= 1 and words[0] == "say":
        toPrint = []
        for word in words[1:]:
            toPrint.append(makeString(word))
        return "print(\"" + " ".join(toPrint) +"\")"
    if len(words) >= 4 and words[0] == "set" and words[2] == "to":
        variables[words[1]] = str(eval(" ".join(words[3:])))


def openFile(name):
    try:
        source = open(name, 'r')
        output = open(name.replace(".lishp", "") + ".py", 'w')
    except FileNotFoundError:
        print("File " + name + " not found.")
        sys.exit(1)

    for line in source.readlines():
        print(variables)
        if transpile(line):
            output.write(transpile(line))
            output.write("\n")
        else:
            transpile(line)


def main():
    openFile(sys.argv[1])

if __name__ == '__main__':
    main()
