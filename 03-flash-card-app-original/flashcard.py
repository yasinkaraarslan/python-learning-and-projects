import pyfiglet
from rich.console import Console
from rich.table import Table

fh = open('words.data', encoding='utf-8').readlines()

wrds = dict()

wrng = dict()

count = 0
wins = 0
wrongs = 0


print("You can get help by writing", "'help'")

for line in fh :
        words = line.strip().split(":")
        if len(words) != 2 :
            continue
        wrds[words[0]] = words[1]
        bigword = words[0].upper()
        bword = pyfiglet.figlet_format(bigword)
        print(bword)
        if len(words[1]) < 4 :
               print(">>> NO HINT IS GIVEN FOR THIS WORD")
        wrd = input("Translate into Turkish: ")
        wrd = wrd.lower().strip()
        if len(words[1]) > 5 :
            if wrd == "help" :
               print(words[1][0], "_" * (len(words[1]) - 2), words[1][-1])
               wrd = input("Enter the Correct Answer: ")
               wrd = wrd.lower().strip()
        else :
            if wrd == "help" :
               print("HEY HEY I CAUGHT YOU :)")
               wrng[words[0]] = words[1]
               continue
        if wrd == words[1] :
            count = count + 1
            wins = wins + 1
            print("Congrats!", "Your Win Streak", wins)
        else :
            wins = 0
            wrongs = wrongs + 1
            wrng[words[0]] = words[1]
            print("False")

execute = Console()
finaltable = Table(title = "THE CARD TEST RESULTS")
finaltable.add_column("Information")
finaltable.add_column("Statistics")
finaltable.add_row("Number of Correct Answer", str(count))
finaltable.add_row("Number of Wrong Answer", str(wrongs))
finaltable.add_row("Total Score", f"% {int(100 * (count / len(wrds)))}")
execute.print(finaltable)

if len(wrng) < 1 :
    print("You have answered all the words correctly, Congratulations!!!")
    quit()


print("You did not know", wrongs, "words")

ex = input("Click Enter for words you don't know")

print("You can get help by writing", "'help'")

if len(ex) < 1 :
    for e, t in wrng.items() :
        print(pyfiglet.figlet_format(e.upper()))
        if len(t) <= 4 :
                print(">>> NO HINT IS GIVEN FOR THIS WORD")
                nword = input("Translate into Turkish: ")
                nword = nword.strip().lower()
                if nword == "help" :
                    print("HEY HEY I CAUGHT YOU :)")
                    nword = input("Enter the Correct Answer: ")
                if nword == t :
                   print("Congrats!!!")
                else :
                    print("Work Harder!", "Correct Answer: ", t)      
        if len(t) > 5 :
            nword = input("Translate into Turkish: ")
            nword = nword.strip().lower()
            if nword == "help" :
                print(t[0], '_' * (int(len(t)) - 2), t[-1])
                nword = input("Enter the Correct Answer: ")
            if nword == t :
                print("Congrats!!!")
            else :
                print("Work Harder!", "Correct Answer: ", t)

print("CONGRATULATIONS!!! YOU HAVE COMPLETED THE TEST")
       

 
        
