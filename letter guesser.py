def lockedin_syndrome():
    while True:
        response = input("Is the letter between 'a-m'? (yes/no): ")
        if response.lower() == "yes":
            r2 = input("Is the letter between 'a-f'? (yes/no): ")
            if r2.lower() == "yes":
                r3 = input("Is the letter between 'a-c'? (yes/no): ")
                if r3.lower() == "yes":
                    r4 = input("Is the letter 'a'? (yes/no): ")
                    if r4.lower() == "yes":
                        return "a"
                    elif r4.lower() == "no":
                        r5 = input("Is the letter 'c'? (yes/no): ")
                        if r5.lower() == "yes":
                            return "c"
                        
                        elif r5.lower() == "no":
                            return "b"
                elif r3.lower() == "no":
                    r6 = input("Is the letter between 'd-e'? (yes/no): ")
                    if r6.lower() == "yes":
                        r7 = input("Is the letter 'd'? (yes/no): ")
                        if r7.lower() == "yes":
                            return "d"
                        elif r7.lower() == "no":
                            return "e"
                    elif r6.lower()=="no":
                        return "f"        
            elif r2.lower()=="no":
                r8 = input("is the letter between 'g-j'?(yes/no)")
                if r8.lower() == "yes":
                    r9 = input("Is the letter between 'g-h'? (yes/no): ")
                    if r9.lower() == "yes":
                        r10 = input("Is the letter 'g'? (yes/no): ")
                        if r10.lower() == "yes":
                            return "g"
                        elif r10.lower() == "no":
                            return "h"
                    elif r9.lower()=="no":
                        r11 = input("is the letter 'i'?(yes/no)")
                        if r11.lower() == "yes":
                            return "i"
                        elif r11.lower() == "no":
                            return "j"
                        
                elif r8.lower() == "no":
                    r12 = input("is the letter between 'k-l'?(yes/no)")
                    if r12.lower() == "yes":
                        r13 = input("Is the letter 'k'? (yes/no): ")
                        if r13.lower() == "yes":
                            return "k"
                        elif r13.lower() == "no":
                                return "l"
                        elif r12.lower()=="no":
                            return "m"
            
        elif response.lower() == "no":
            r14 = input("Is the letter between 'n-s'? (yes/no): ")
            if r14.lower() == "yes":
                r15 = input("Is the letter between 'n-p'? (yes/no): ")
                if r15.lower() == "yes":
                    r16 = input("Is the letter between 'n-o'? (yes/no): ")
                    if r16.lower() == "yes":
                        r17 = input("Is the letter 'n'? (yes/no): ")
                        if r17.lower() == "yes":
                            return "n"
                        elif r17.lower() == "no":
                            return "o"
                        
                elif r15.lower() == "no":
                    r18 = input("Is the letter between 'q-r'? (yes/no): ")
                    if r18.lower() == "yes":
                        r19 = input("Is the letter 'q'? (yes/no): ")
                        if r19.lower() == "yes":
                            return "q"
                        elif r19.lower() == "no":
                            return "o"
                    elif r18.lower() == "no":
                            return "s"
                
            elif r14.lower() == "no":
                r20 = input("Is the letter between 't-w'? (yes/no): ")
                if r20.lower() == "yes":
                    r21 = input("Is the letter between 't-u'? (yes/no): ")
                    if r21.lower() == "yes":
                        r22 = input("Is the letter 't'? (yes/no): ")
                        if r22.lower() == "yes":
                            return "t"
                        elif r22.lower() == "no":
                            return "u"
                    elif r21.lower() == "no":
                        r23 = input("Is the letter 'v'? (yes/no): ")
                        if r23.lower() == "yes":
                            return "v"
                        elif r23.lower() == "no":
                            return "w"
            elif r20.lower()=="no":
                r24=input("Is the letter between 'x-y'? (yes/no): ")
                if r24.lower() == "yes":
                    r22 = input("Is the letter 'x'? (yes/no): ")
                    if r22.lower() == "yes":
                        return "x"
                    elif r22.lower() == "no":
                        return "y"
                elif r24.lower() == "no":
                    return "z"
                    
        else:
            print("Please answer with 'yes' or 'no'.")

guessed_letters = []

while True:
    locked = lockedin_syndrome()
    guessed_letters.append(locked)
    print(locked)
    
    another_guess = input("next letter? (yes/no): ")
    if another_guess.lower() != "yes":
        break

print("Guessed letters:", guessed_letters)
