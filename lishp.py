import sys

def isIdentifier(word):
    return word.startswith("{") and word.endswith("}")

def transpile(line):
    words = line.split()
    if len(words) >= 1:
        command = words[0]
    else:
        command = ""


    if len(words) >= 1 and command == "say":
        toPrint = []
        for word in words[1:]:
            if isIdentifier(word):
                if word != words[len(words) - 1]:
                    word = word.replace("{","").replace("}","") + ", "
                else:
                    word = word.replace("{","").replace("}","")
            else:
                if word != words[len(words) - 1]:
                    word = "\"" + word + "\", "
                else:
                    word = "\"" + word + "\""
            toPrint.append(word)

        return "print(" + " ".join(toPrint) + ")\n"


    if len(words) >= 4 and command == "set" and words[2] == "to":
        variable = words[1]
        value = []

        for v in words[3:]:
            if isIdentifier(v):
                v = v.replace("{","").replace("}","")
            elif not v.isdigit():
                v = "\"" + v + "\""
            value.append(v)

        return str( variable + " = " + " ".join(value) + "\n" )


    if len(words) >= 1:
        secondLast = words[ len(words) - 2 ]
    else:
        secondLast = ""

    if len(words) >= 4 and \
      command == "add" or command == "take" and \
      secondLast == "to" or secondLast == "from":

        effect = words[ 1 : words.index(secondLast) ]
        formatted_effect = []

        value = words[ len(words) - 1 ]

        for e in effect:
            if isIdentifier(e):
                e = e.replace("{","").replace("}","")
            formatted_effect.append(e)

        if command == "add":
            return value + " += " + " ".join(formatted_effect) + "\n"
        elif command == "take":
            return value + " -= " + " ".join(formatted_effect) + "\n"

def openFile(name):
    try:
        source = open(name, 'r')
        output = open(name.replace(".lishp", "") + ".py", 'w')
    except FileNotFoundError:
        print("File " + name + " not found.")
        sys.exit(1)

    output.write("from __future__ import print_function\n\n")

    for line in source.readlines():
        output.write(str(transpile(line)))


def main():
    openFile(sys.argv[1])

if __name__ == '__main__':
    main()
