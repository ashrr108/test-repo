# Test generated by RoostGPT for test roost-test using AI Model vertex

def parser():
    """
    parser: parses the tokens of the list 'tokens'
    """

    global tokens
    global eax, ebx, ecx, edx

    assert len(tokens) > 0, "no tokens"

    pointer = 0  # pointer for tokens
    token = Token("", "")
    tmpToken = Token("", "")

    while pointer < len(tokens):

        token = tokens[pointer]

        if token.token == "mov":  # mov commando

            # it must follow a register
            if pointer + 1 < len(tokens):
                pointer += 1
                token = tokens[pointer]
            else:
                print("Error: Not found argument!")
                return

            # TODO use token.t for this stuff
            if token.t == "register":

                tmpToken = token

                # it must follow a value / string / register / variable
                if pointer + 1 < len(tokens):
                    pointer += 1
                    token = tokens[pointer]
                else:
                    print("Error: Not found argument!")
                    return

                # converts the token into float, if token contains only digits.
                # TODO response of float
                if token.t == "identifier":  # for variables

                    # check of exists of variable
                    if token.token in variables:
                        token.token = variables[token.token]
                    else:
                        print("Error: undefine variable! --> " + token.token)
                        return
                elif token.t == "string":
                    pass
                elif isinstance(token.token, float):
                    pass
                elif token.token.isdigit():
                    token.token = float(token.token)
                elif token.token[0] == "-" and token.token[1:].isdigit():
                    token.token = float(token.token[1:])
                    token.token *= -1
                elif token.t == "register":  # loads out of register
                    if token.token == "eax":
                        token.token = eax
                    elif token.token == "ebx":
                        token.token = ebx
                    elif token.token == "ecx":
                        token.token = ecx
                    elif token.token == "edx":
                        token.token = edx

                if tmpToken.token == "eax":
                    eax = token.token
                elif tmpToken.token == "ebx":
                    ebx = token.token
                elif tmpToken.token == "ecx":
                    ecx = token.token
                elif tmpToken.token == "edx":
                    edx = token.token

            else:

                print("Error: No found register!")
                return

        elif token.token == "add":  # add commando

            pointer += 1
            token = tokens[pointer]

            if token.t == "register":

                tmpToken = token

                if pointer + 1 < len(tokens):
                    pointer += 1
                    token = tokens[pointer]
                else:
                    print("Error: Not found number!")
                    return

                # converts the token into float, if token contains only digits.
                if token.t == "register":

                    # for the case that token is register
                    if token.token == "eax":
                        token.token = eax
                    elif token.token == "ebx":
                        token.token = ebx
                    elif token.token == "ecx":
                        token.token = ecx
                    elif token.token == "edx":
                        token.token = edx

                elif isinstance(token.token, float):
                    pass
                elif token.token.isdigit():
                    token.token = float(token.token)
                elif token.token[0] == "-" and token.token[1:].isdigit():
                    token.token = float(token.token[1:])
                    token.token *= -1
                else:
                    print("Error: ", token, " is not a number!")
                    return

                if tmpToken.token == "eax":
                    eax += token.token

                    # update zero flag
                    if eax == 0:
                        zeroFlag = True
                    else:
                        zeroFlag = False
                elif tmpToken.token == "ebx":
                    ebx += token.token

                    # update zero flag
                    if ebx == 0:
                        zeroFlag = True
                    else:
                        zeroFlag = False
                elif tmpToken.token == "ecx":
                    ecx += token.token

                    # update zero flag
                    if ecx == 0:
                        zeroFlag = True
                    else:
                        zeroFlag = False
                elif tmpToken.token == "edx":
                    edx += token.token

                    # update zero flag
                    if edx == 0:
                        zeroFlag = True
                    else:
                        zeroFlag = False

            else:

                print("Error: No found register!")
                return

        elif token.token == "sub":  # sub commando

            pointer += 1
            token = tokens[pointer]

            if token.t == "register":

                tmpToken = token

                if pointer + 1 < len(tokens):
                    pointer += 1
                    token = tokens[pointer]
                else:
                    print("Error: Not found number!")
                    return

                # converts the token into float, if token contains only digits.
                if token.t == "register":

                    # for the case that token is register
                    if token.token == "eax":
                        token.token = eax
                    elif token.token == "ebx":
                        token.token = ebx
                    elif token.token == "ecx":
                        token.token = ecx
                    elif token.token == "edx":
                        token.token = edx

                elif isinstance(token.token, float):
                    pass
                elif token.token.isdigit():
                    token.token = float(token.token)
                elif token.token[0] == "-" and token.token[1:].isdigit():
                    token.token = float(token.token[1:])
                    token.token *= -1
                else:
                    print("Error: ", token, " is not a number!")
                    return

                if tmpToken.token == "eax":
                    eax -= token.token

                    # updated zero flag
                    if eax == 0:
                        zeroFlag = True
                    else:
                        zeroFlag = False
                elif tmpToken.token == "ebx":
                    ebx -= token.token

                    # update zero flag
                    if ebx == 0:
                        zeroFlag = True
                    else:
                        zeroFlag = False
                elif tmpToken.token == "ecx":
                    ecx -= token.token

                    # update zero flag
                    if ecx == 0:
                        zeroFlag = True
                    else:
                        zeroFlag = False
                elif tmpToken.token == "edx":
                    edx -= token.token

                    # update zero flag
                    if edx == 0:
                        zeroFlag = True
                    else:
                        zeroFlag = False

            else:

                print("Error: No found register!")
                return

        elif token.token == "int":  # int commando

            tmpToken = token

            if pointer + 1 < len(tokens):
                pointer += 1
                token = tokens[pointer]
            else:
                print("Error: Not found argument!")
                return

            if token.token == "0x80":  # system interrupt 0x80

                if eax == 1:  # exit program

                    if ebx == 0:
                        print("END PROGRAM")