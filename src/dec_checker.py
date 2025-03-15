def decimal_integer_checker(input_str): #kaila

    state = True # will turn false if any condition isn't met
    numUnderscore = 0 # counts how many underscores are in succession

    if input_str  == "0": # checks if it's only 0
        pass

    elif input_str[0] in ["1","2","3","4","5","6","7","8","9"] and len(input_str) > 0 : # no leading 0 or _ in first character, checks if string is blank
        for i in range(1, len(input_str)-1): # starts after the first character and stops before the second to last character
            if input_str[i] in ["0","1","2","3","4","5","6","7","8","9"]:
                numUnderscore = 0
            elif input_str[i] == "_":
                numUnderscore += 1
            
            if numUnderscore > 1: # if there is more than 1 underscore in between numbers
                state = False
                break
        

        if input_str[-1] == "_":
            state = False

    else:
        state = False

    return state