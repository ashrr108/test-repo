# Test generated by RoostGPT for test roost-test using AI Model vertex

def scanner(string):
    """
    scanner: This function builds the tokens by the content of the file.
    The tokens will be saved in list 'tokens'
    """
    global tokens
    token = ""
    state = 0  # init state

    for ch in string:

        if state == 0:

            if ch == "m":  # catch mov-command

                state = 1
                token += "m"

            elif ch == "e":  # catch register

                state = 4
                token += "e"

            elif (ch >= "1" and ch <= "9") or ch == "-":  # catch a number

                state = 6
                token += ch

            elif ch == "0":  # catch a number or hex-code

                state = 17
                token += ch

            elif ch == "a":  # catch add-command

                state = 7
                token += ch

            elif ch == "s":  # catch sub command

                state = 10
                token += ch

            elif ch == "i":  # capture int command

                state = 14
                token += ch

            elif ch == "p":  # capture push or pop command

                state = 19
                token += ch

            elif ch == "l":  # capture label

                state = 25
                token += ch

            elif ch == "j":  # capture jmp command

                state = 26
                token += ch

            elif ch == "c":  # catch cmp-command

                state = 29
                token += ch

            elif ch == ";":  # capture comment

                state = 33

            elif ch == '"':  # catch a string

                state = 34
                # without "

            elif ch.isupper():  # capture identifier

                state = 35
                token += ch

            elif ch == "d":  # capture db keyword

                state = 36
                token += ch

            elif ch == "$":  # catch variable with prefix $

                state = 38
                # not catching $

            elif ch == "_":  # catch label for subprogram

                state = 40
                # not catches the character _

            elif ch == "r":  # catch ret-command

                state = 44
                token += ch

            else:  # other characters like space-characters etc.

                state = 0
                token = ""

        elif state == 1:  # state 1

            if ch == "o":

                state = 2
                token += ch

            elif ch == "u":

                state = 47
                token += ch

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 2:  # state 2

            if ch == "v":

                state = 3
                token += "v"

            else:  # error case
                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 3:  # state 3

            if ch.isspace():

                state = 0
                tokens.append(Token(token, "command"))
                token = ""

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 4:  # state 4
            if ch >= "a" and ch <= "d":

                state = 5
                token += ch

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 5:  # state 5
            if ch == "x":
                state = 13
                token += ch

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 6:  # state 6

            if ch.isdigit():

                state = 6
                token += ch

            elif ch.isspace():

                state = 0
                tokens.append(Token(token, "value"))
                token = ""

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 7:  # state 7

            if ch == "d":

                state = 8
                token += ch

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 8:  # state 8

            if ch == "d":

                state = 9
                token += ch

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 9:  # state 9

            if ch.isspace():

                state = 0
                tokens.append(Token(token, "command"))
                token = ""

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 10:  # state 10

            if ch == "u":

                state = 11
                token += ch

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 11:  # state 11

            if ch == "b":

                state = 12
                token += ch

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 12:  # state 12

            if ch.isspace():

                state = 0
                tokens.append(Token(token, "command"))
                token = ""

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 13:  # state 13

            if ch == "," or ch.isspace():

                state = 0
                tokens.append(Token(token, "register"))
                token = ""

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 14:  # state 14

            if ch == "n":

                state = 15
                token += ch

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 15:  # state 15

            if ch == "t":

                state = 16
                token += ch

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 16:  # state 16

            if ch.isspace():

                state = 0
                tokens.append(Token(token, "command"))
                token = ""

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 17:  # state 17

            if ch == "x":

                state = 18
                token += ch

            elif ch.isspace():

                state = 0
                tokens.append(Token(token, "value"))
                token = ""

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 18:  # state 18

            if ch.isdigit() or (ch >= "a" and ch <= "f"):

                state = 18
                token += ch

            elif ch.isspace():

                state = 0
                tokens.append(Token(token, "value"))
                token = ""

            else:  # error case

                state = 0
                token = ""
                raise InvalidSyntax()

        elif state == 19:  # state 19

            if ch == "u":

                state = 20
                token += ch

            elif ch == "o":

                state = 23
                token += ch

            else