"""
Please note this is a Work In Progress
"""


def colored_text(text, color):
    
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }

    if color not in colors:
        color = 'reset'

    print(f"{colors[color]}{text}{colors['reset']}")

def userchoicecolor(text):
    choose = input("Please select your color - avaliable options black, red, green, yellow, blue, magenta, cyan, white: ")
    colored_text(text, choose)
"""
Please use your knowledge and make a python code using the facade programing paradigm that makes 
virtual easter greeting cards. One class should handle different text colors, an other class should 
allow the user to select different ASCII images or create there own, an other class should allow the 
user to put a custom message or select a preset message. All of these classes should come to gether in a 
template class that allows the user to select a template for all of the options above or create there own. 

"""
class ASCII:
    def __init__ (self, userchoice, color):
        self.userchoice = userchoice
        self.color = color

    def ASCIImaker (self):
        print(self.userchoice)
        Ascii = ""
        if self.userchoice == "1":
            Ascii = """
                 
                      .--.
                    .'    ',
                  .'.*.*.*.*',
                 /            \
                 
                /              \
            
               Y                Y
               |.*.*.*.*.*.*.*.*|
               |.*.*.*.*.*.*.*.*|
               Y                Y
                \              /
                 \            /
             tms  `.*.*.*.*..'
                    `..__..'
            
            """
            return colored_text(Ascii, "yellow")
        if self.userchoice == "2":
            Ascii = """
             ,,..,,,,..,,,.., 
          .,%%%%%;;%%%;;%%%%;;%%,. 
       .;;%%%"""""''""''"""''";%%%;;, 
     .;%%%%'                    `;;%%%, 
   .%%%%;'                        `%%%;; 
  .%%%;;'      .sSSSSs.            `%%;;, 
  %%;;%'      .SSSSSSSS,%%%%,      `%;;%% 
 .;;%%% .::::.SSSSSSSSSS,%%%%%,oOOOo;;%%%, 
 %%%%;'.:xXXXXx!SSSSSSS!a@@@@@a!OOOOO%%%;; 
 %%;;% :XXXXXXXX!SSSSS!@@@@@@@@@!OOOO%%;;% 
 ;;%%% XXXXXXXXXX!SSS!@@@@@@@@@@@!OOO;;%%% 
a@@a@@a@@a@@a@@a@@a@@a@@a@@a@@a@.sSSSSSs.sSSs.sSSSSs. 
`;%%%;|;%%%;|;%%%;|;%%%;|;%%%;|,SSssssSS;SSSS;SSsssSS 
.%;|;%%%;|;%%%;|;%%%;|;%%%;|;%%,SSSSSSSS;SSSS;SSSSSSS 
`;%%%;|;%%%;|;%%%;|;%%%;|;%%%;|;`SSSSSS'^ssss^`SSSSS' 
.%;|;%%%;|;%%%;|;%%%;|;%%%;|;%%%;|;%,ssSSS'`SSSsss, 
`;%%%;|;%%%;|;%%%;|;%%%;|;%%%;|;%%%,SSSSSS' `SSSSSS 
 .;|;%%%;|;%%%;|;%%%;|;%%%;|;%%%;|,SSSSSS'  ,SSSSSS 
 `%%%;|;%%%;|;%%%;|;%%%;|;%%%;|;,SSS^SS'%  ,SSSSSS' 
  `|;%%%;|;%%%;|;%%%;|;%%%;|;%%,S';%%`S'  ,SSS^SSSmk 
    `;|;%%%;|;%%%;|;%%%;|;%%%;|;%%%;|;'   `S'  `S' 
            
            """
            return colored_text(Ascii,"green")
        else:
            print("please put your ascii image in the ascii.txt file and press enter when ready")
            print()
            
            with open('ascii.txt.txt') as f:
                Ascii = f.readlines()
            return userchoicecolor(Ascii)
        


class TextMaker:
    def __init__(self, userChoice, color):
        self.userchoice = userChoice
        self.color = color
    def text(self):
        TEXT = ""
        if self.userchoice == "1":
            TEXT = "Have Fun Hunting Eggs"
            TEXT = colored_text(TEXT, "magenta")
        elif self.userchoice == "2":
            TEXT = "Happy Easter!"
            TEXT = colored_text(TEXT, "blue")
        else:
            TEXT = input("Please put your message here: ")
            TEXT = userchoicecolor(TEXT)
        return TEXT

class Template:
    def __init__ (self, userInput):
        self.userInput = userInput
    def TemplateChoice(self):
        card = ""
        if self.userInput == "1":
            card = ASCII("1","will do").ASCIImaker()
            card2 =  TextMaker("1","will do").text()
        elif self.userInput == "2":
            card = ASCII("2","will do").ASCIImaker()
            card2 = TextMaker("2","will do").text()
        else:
            two = input("Please choose image 1 (egg) or image 2 (basket)")
            card2 = TextMaker("3","will do").text()
            
            if two == "1":
                card = ASCII("1","will do").ASCIImaker()
            elif two == "2":
                card = ASCII("2","will do").ASCIImaker()
            else:
                card = ASCII("1","will do").ASCIImaker()
              
            
        


#___________________________________
# general purpose menu system by Mirbalaj Rishi



def mainMenu(Option1, Option2, Option3):
    goodChoice = "no"
    while goodChoice == "no":
        userChoice = input(f"""
Please Input Your Choice
1.{Option1}
2.{Option2}
3.{Option3}

""").lower()
    
        print()
        if userChoice == "1" or userChoice == Option1.lower():
            goodChoice = "yes"
            return "1"
        elif userChoice == "2" or userChoice == Option2.lower():
            goodChoice = "yes"
            return "2"
        elif userChoice == "3" or userChoice == Option3.lower():
            goodChoice = "yes"
            return "3"
        else:
            goodChoice = "no"
            print("please choose one of the options below")



#-----------------------------------------------------


userInput = mainMenu("Egg Template", "Basket Template", "Custom") 
Template(userInput).TemplateChoice()





            
