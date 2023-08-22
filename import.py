import random
l=["Rock", "Scissor", " Paper"]
ucount=0
ccount=0
while True:
  uc=int(input('''
  Game Start...
  1 Yes
  2 No | Exit''')) 
  if uc ==1:
    for a in range(1, 6):
      userInput=int(input('''
    1 Rock 
    2 Scissor
    3 Paper
    '''))
      if userInput==1:
        uchoice="Rock" 
      elif userInput==2:
        uchoice="Scissor"
      elif userInput==3:
        uchoice="Paper"
      Cchoice=random.choice(l) 
      if Cchoice==uchoice:
        print("Computer Value", Cchoice) 
        print("User Value", uchoice)
        print("Game Draw") 
        ucount=ucount+1
        ccount=ccount+1
      elif ((uchoice =="Rock" and Cchoice=="Scissor") or (uchoice=="Scissor" and Cchoice=="Paper") or (uchoice=="Paper" and Cchoice=="Rock")):
        print("Computer Value:--", Cchoice)
        print("User Value:--",uchoice)
        print("You Win")
        ucount=ucount+1
      else:
        print("Computer Value:--", Cchoice) 
        print("User Value:--", uchoice)
        print("Comptuer Win")
        ccount=ccount+1
    if ucount==ccount:
      print("Final Game Draw...")
      print() 
      print("User Score", ucount)
      print() 
      print("Comptuer Score",ccount)
    elif ucount>ccount:
      print("Final You Win The Game ...")
      print() 
      print("User Score:--", ucount)
      print() 
      print("Comptuer Score:--",ccount)
    else:
      print()    
      print("Final Comptuer Win The Game...")
      print() 
      print("User Score:--", ucount)
      print() 
      print("Comptuer Score:--",ccount)
  else:
    break