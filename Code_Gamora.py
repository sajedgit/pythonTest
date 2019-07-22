def check_dialogue(text):
    if text.isalnum():
        #print("alpha",text)
        
        capital_word=text.capitalize()
        if capital_word==text:
            
            if capital_word=="Quill":
                print("I am going to ask you this one time, where is Gamora?")
            elif capital_word=="Stark":
                print("I will do you one better, who is Gamora?")
            elif capital_word=="Drax":
                print("I will do you one better, why is Gamora?")
            else:
                print("What is Gamora?")
            
            return True
        else:
            print("Please enter the  capitalize word")
            return False
        
    else:
        print("Please enter the  alphabetic characters")
        return False
    
try:
    input_no=int(input('Please choose a number between 1 and 11\n'))
    counter=0
    input_character=""
    while input_no>counter:
        counter+=1
        if input_no>0 and input_no<11:
            input_character =input()
            dialogue=check_dialogue(str(input_character))
            if not dialogue:
                break

        else:
            print("Please choose a number between 1 and 11 ")
            break
            
except ValueError:
    print("This is not a whole number.")


        
