#!/usr/bin/python

import sys

def isIdentifier(word):
    return word.startswith("{") and word.endswith("}")

def transpile(line, javascript = False):
    if line.isspace():
        return ""
    words = line.split()
    if len(words) >= 1:
        command = words[0]
    else:
        command = ""

    # 'say' - print command
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

        if javascript:
            return "console.log(" + " ".join(toPrint) + ");\n"
        return "print(" + " ".join(toPrint) + ")\n"

    # 'set x to y' - variable declaration
    if len(words) >= 4 and command == "set" and words[2] == "to":
        variable = words[1]
        value = ""

        for word in words[3:]:
            if isIdentifier(word):
                value += word.replace("{","").replace("}","")
            elif word.startswith("\"") and word.endswith("\""):
                value += word

            if word != words[ len(words) - 1 ]:
                value += " + "

        if javascript:
          return "var " + variable + " = " + value + ";\n"
        return variable + " = " + value + "\n"

    # mathematical operators
    if len(words) >= 1:
        secondLast = words[ len(words) - 2 ]
    else:
        secondLast = ""

    if len(words) >= 4 and \
      (command == "add" and secondLast == "to") or \
      (command == "take" and secondLast == "from") or \
      (command == "times" and secondLast == "by") or \
      (command == "divide" and secondLast == "by"):

        effect = words[ 1 : words.index(secondLast) ]
        formatted_effect = []

        value = words[ len(words) - 1 ]

        for e in effect:
            if isIdentifier(e):
                e = e.replace("{","").replace("}","")
            formatted_effect.append(e)

        if command == "add":
            if javascript:
                return value + " += " + " ".join(formatted_effect) + ";\n"
            return value + " += " + " ".join(formatted_effect) + "\n"
        elif command == "take":
            if javascript:
                return value + " -= " + " ".join(formatted_effect) + ";\n"
            return value + " -= " + " ".join(formatted_effect) + "\n"
        elif command == "times":
            if javascript:
                return value + " *= " + " ".join(formatted_effect) + ";\n"
            return value + " *= " + " ".join(formatted_effect) + "\n"
        elif command == "divide":
            if javascript:
                return value + " *= " + " ".join(formatted_effect) + ";\n"
            return value + " *= " + " ".join(formatted_effect) + "\n"


def openFile(name, javascript = False):
    try:
        source = open(name, 'r')
        if javascript:
            output = open(name.replace(".lishp", "") + ".js", 'w')
        else:
            output = open(name.replace(".lishp", "") + ".py", 'w')
    except FileNotFoundError:
        print("File " + name + " not found.")
        sys.exit(1)

    if not javascript:
        output.write("from __future__ import print_function\n\n")

    for line in source.readlines():
        if javascript:
            output.write(str(transpile(line, True)))
        else:
            output.write(str(transpile(line)))


def main():
    javascript = False
    if len(sys.argv) >= 3:
        if sys.argv[1] == "-js":
            openFile(sys.argv[2], True)
        else:
            print("Unknown option: ", sys.argv[1])
    else:
        openFile(sys.argv[1])

if __name__ == '__main__':
    main()
