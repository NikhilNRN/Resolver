#Coding Part - Assignment 3
#Written by Nikhil and Andrew
#CS 4365.004

#The code uses the resolution principle to prove that a clause is valid by contradiction.

#Import statements to use throughout the code.
import re
import sys

#Driver function. Main body of the code is made here.
def main():
#Reads the file and ignores the exception errors that come with them.
    clauseNum = 1
    clause = []
    with open(sys.argv[1], errors='ignore') as inputFile:
        for item, line in enumerate(inputFile):
            line = re.sub(r'\n', '', line)
            line = re.sub(r'[ \t]+$', '', line)
            x = []
            for word in line.split(" "):
                x.append(word)
            clause.append(x)
    prove = clause[-1]
    del clause[-1]
    for i in clause:
        print(clauseNum, ". ", ' '.join(i), " { }", sep='')
        clauseNum += 1
    for j in range(len(prove)):
        if '~' in prove[j]:
            prove[j] = re.sub(r'~', '', prove[j])
        else:
            prove[j] = '~' + prove[j]
    for k in prove:
        clause.append([k])
        print(clauseNum, ". ", ' '.join([k]), " { }", sep='')
        clauseNum += 1

#Checks the file and uses the resolve function to check and make sure the input passed matches the
#specified policy stated in the assignment.
    a = 1
    while a < clauseNum - 1:
        b = 0
        while b < a:
            result = resolve(clause[a], clause[b], clause)
            if result is False:
                print(clauseNum, ". ","Contradiction", ' {', a + 1, ", ", b + 1, '}', sep='')
                clauseNum += 1
                print("Valid")
                sys.exit(0)
            elif result is True:
                b += 1
                continue
            else:
                print(clauseNum, ". ",' '.join(result), ' {', a + 1, ", ", b + 1, '}', sep='')
                clauseNum += 1
                clause.append(result)
            b += 1
        a += 1
    print('Not Valid')

#Resolve function that checks and makes sure each clause is adhered to the policy.
def resolve(x, y, clauses):
    temp = x + y
    resolved = None
    hashmap = {}
    for item in temp:
        if item not in hashmap.keys():
            hashmap[item] = 0
    resolved = list(hashmap.keys())
    ors = list(hashmap.keys())
    for line1 in x:
        for line2 in y:
            if negateFunction(line1, line2):
                resolved.remove(line1)
                resolved.remove(line2)
                if len(resolved) is 0:
                    return False
                elif validate(resolved):
                    return True
                else:
                    for cl in clauses:
                        if differenceFunction(resolved, cl) == []:
                            return True
                    return resolved
    if resolved == ors:
        return True
#Negate function that negates the clause to be proved.
def negateFunction(line1, line2):
    if line1 == ('~' + line2) or line2 == ('~' + line1):
        return True
    else:
        return False
#Utility function that will be used in the Resolve function.
def validate(resolved):
    for r1 in resolved:
        for r2 in resolved:
            if negateFunction(r1, r2):
                return True
    return False
#Utility function that will be used in the Resolve function.
def differenceFunction(line1, line2):
    a = [i for i in line1 + line2 if i not in line1 or i not in line2]
    return a
#Print function that will print the specified parameter that will be passed in.
def printFunction(x):
    for item in x:
        print()
if __name__ == "__main__":
    main()
