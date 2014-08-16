import sys

variables = {}

def getVars(word):
    if word.startswith("{") and word.endswith("}"):
        return variables[word.replace("{", "").replace("}","")]
    else:
        return word


def transpile(line):
    words = line.split()
    if len(words) >= 1:
        command = words[0]
    else:
        command = ""

    if len(words) >= 1 and command == "say":
        toPrint = []
        for word in words[1:]:
            toPrint.append(getVars(word))
        return "print(\"" + " ".join(toPrint) +"\")"

    if len(words) >= 4 and command == "set" and words[2] == "to":
        toSet = []
        for word in words[3:]:
            toSet.append(getVars(word))
        if any(i.isdigit() for i in " ".join(toSet)):
            variables[words[1]] = str(eval(" ".join(toSet)))
        else:
            variables[words[1]] = str(" ".join(toSet))

    if len(words) >= 1:
        secondLast = words[len(words) - 2]
    else:
        secondLast = ""
    if len(words) >= 4 and \
      command == "add" or command == "take" and \
      secondLast == "to" or secondLast == "from":

        if variables[words[len(words) - 1]]:
            exprnWithoutVars = words[1:len(words) - 2]
            expression = []

            toChange = variables[words[len(words) - 1]]

            for elem in exprnWithoutVars:
                expression.append(getVars(elem))
            if command == "add" and secondLast == "to":
                variables[words[len(words) - 1]] = \
                  str(int(toChange) + eval(" ".join(expression)))
            elif command == "take" and secondLast == "from":
                variables[words[len(words) - 1]] = \
                  str(int(toChange) - eval(" ".join(expression)))


def openFile(name):
    try:
        source = open(name, 'r')
        output = open(name.replace(".lishp", "") + ".py", 'w')
    except FileNotFoundError:
        print("File " + name + " not found.")
        sys.exit(1)

    for line in source.readlines():
        tr = transpile(line)
        if tr:
            output.write(str(tr))


def main():
    openFile(sys.argv[1])

if __name__ == '__main__':
    main()
