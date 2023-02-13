import random 
import easygui

def funct1245():
        Times = easygui.integerbox("How many times do you want to play?", "Question About Playing the Game", lowerbound=0,upperbound=99999999999)
        print (Times)  
        WelcomeforEasy = easygui.ccbox("Welcome to The World's Easiest Math Quiz!", "Mathematics Quiz")
        print (WelcomeforEasy)
      
      
        print("")
        list1 = []
        list2 = []
      
        for x in range (0,Times):
          num = random.randint(1,10)
          list1.append(num)
          num = random.randint(1,10)
          list2.append(num)

        count=0
        for x in range (0,Times):
          if answer3 == False:
              str11="What is "
              str12=" * "
              str13=" Mathematics Quiz"
              str1=str11, str(list1[x]), str12, str(list2[x]),str13
              str2= '' .join(str1)
              str2=str2.replace("{","")
              MultiplicationQforEasy = easygui.integerbox(str2, lowerbound=0,upperbound=99000000)
              print(MultiplicationQforEasy)
              if MultiplicationQforEasy == list1[x]*list2[x]:
                count=count+1
                print("Correct")
              else:
                print("Incorrect")
          if answer3 == True:
              str121="What is "
              str122=" + "
              str2=str121, str(list1[x]), str122, str(list2[x])
              str3= '' .join(str2)
              str3=str3.replace("{","")
              AdditionQforEasy = easygui.integerbox(str3,"Mathematics Quiz", lowerbound=0,upperbound=99000000)
              print(AdditionQforEasy)
              if AdditionQforEasy == list1[x]+list2[x]:
                count=count+1
                print("Correct")
              else:
                print("Incorrect")
        summarycode1 = "You Got " + str(count) + " out of ",  str(Times) +  " correct."
        summarycode2 = count/Times*100
        summarycode3 = str("% is your score. Thank You For Playing!")
        summarycode4 = (str(summarycode2) + str(summarycode3))
        summarycode1= '' .join(summarycode1)
        summarycode1=summarycode1.replace("{","")
        summary=easygui.msgbox(summarycode1)
        print(summary)  
        summary2=easygui.msgbox(str(summarycode4))
        
        print(summary2)



















def funct1256():
        TimesforMedium = easygui.integerbox("How many times do you want to play?", "Question About Playing the Game", lowerbound=0,upperbound=99999999999)
        print (TimesforMedium)  
        WelcomeforMedium = easygui.ccbox("Welcome to The World's Mediumest Math Quiz!", "Mathematics Quiz")
        print (WelcomeforMedium)
      
      
        print("")
        list1 = []
        list2 = []
      
        for x in range (0,TimesforMedium):
          num = random.randint(1,25)
          list1.append(num)
          num = random.randint(1,25)
          list2.append(num)

        count=0
        for x in range (0,TimesforMedium):
          if answer3 == False:
              str11="What is "
              str12=" * "
              str1=str11, str(list1[x]), str12, str(list2[x])
              str2= '' .join(str1)
              str2=str2.replace("{","")
              MultiplicationQforMedium = easygui.integerbox(str2, "Mathematics Quiz", lowerbound=0,upperbound=99000000)
              print(MultiplicationQforMedium)
              if MultiplicationQforMedium == list1[x]*list2[x]:
                count=count+1
                print("Correct")
              else:
                print("Incorrect")
          if answer3 == True:
              str121="What is "
              str122=" + "
              str2=str121, str(list1[x]), str122, str(list2[x])
              str3= '' .join(str2)
              str3=str3.replace("{","")
              AdditionQforMedium = easygui.integerbox(str3,"Mathematics Quiz", lowerbound=0,upperbound=99000000)
              print(AdditionQforMedium)
              if AdditionQforMedium == list1[x]+list2[x]:
                count=count+1
                print("Correct")
              else:
                print("Incorrect")
        summarycode1 = "You Got " + str(count) + " out of ",  str(TimesforMedium) +  " correct."
        summarycode2 = count/TimesforMedium*100
        summarycode3 = str("% is your score. Thank You For Playing!")
        summarycode4 = (str(summarycode2) + str(summarycode3))
        summarycode1= '' .join(summarycode1)
        summarycode1=summarycode1.replace("{","")
        summary=easygui.msgbox(summarycode1)
        print(summary)  
        summary2=easygui.msgbox(str(summarycode4))
        
        print(summary2)
















def funct1267():
        TimesforHard = easygui.integerbox("How many times do you want to play?", "Question About Playing the Game", lowerbound=0,upperbound=99999999999)
        print (TimesforHard)  
        WelcomeforHard = easygui.ccbox("Welcome to The World's Hardest Math Quiz!", "Mathematics Quiz")
        print (WelcomeforHard)
      
      
        print("")
        list1 = []
        list2 = []
      
        for x in range (0,TimesforHard):
          num = random.randint(1,100)
          list1.append(num)
          num = random.randint(1,100)
          list2.append(num)

        count=0
        for x in range (0,TimesforHard):
          if answer3 == False:
              str11="What is "
              str12=" * "
              str1=str11, str(list1[x]), str12, str(list2[x])
              str2= '' .join(str1)
              str2=str2.replace("{","")
              MultiplicationQforHard = easygui.integerbox(str2, "Mathematics Quiz", lowerbound=0,upperbound=99999999999)
              print(MultiplicationQforHard)
              if MultiplicationQforHard == list1[x]*list2[x]:
                count=count+1
                print("Correct")
              else:
                print("Incorrect")
          if answer3 == True:
              str121="What is "
              str122=" + "
              str2=str121, str(list1[x]), str122, str(list2[x])
              str3= '' .join(str2)
              str3=str3.replace("{","")
              AdditionQforHard = easygui.integerbox(str3,"Mathematics Quiz", lowerbound=0,upperbound=99999999999)
              print(AdditionQforHard)
              if AdditionQforHard == list1[x]+list2[x]:
                count=count+1
                print("Correct")
              else:
                print("Incorrect")
        summarycode1 = "You Got " + str(count) + " out of ",  str(TimesforHard) +  " correct."
        summarycode2 = count/TimesforHard*100
        summarycode3 = str("% is your score. Thank You For Playing!")
        summarycode4 = (str(summarycode2) + str(summarycode3))
        summarycode1= '' .join(summarycode1)
        summarycode1=summarycode1.replace("{","")
        summary=easygui.msgbox(summarycode1)
        print(summary)  
        summary2=easygui.msgbox(str(summarycode4))
        
        print(summary2)














def funct1278():
        TimesforImpossible = easygui.integerbox("How many times do you want to play?", "Question About Playing the Game", lowerbound=0,upperbound=99999999999)
        print (TimesforImpossible)  
        WelcomeforImpossible = easygui.ccbox("Welcome to The World's Impossiblest Math Quiz!", "Mathematics Quiz")
        print (WelcomeforImpossible)
      
      
        print("")
        list1 = []
        list2 = []
      
        for x in range (0,TimesforImpossible):
          num = random.randint(1,1000)
          list1.append(num)
          num = random.randint(1,1000)
          list2.append(num)

        count=0
        for x in range (0,TimesforImpossible):
          if answer3 == False:
              str11="What is "
              str12=" * "
              str1=str11, str(list1[x]), str12, str(list2[x])
              str2= '' .join(str1)
              str2=str2.replace("{","")
              MultiplicationQforImpossible = easygui.integerbox(str2, "Mathematics Quiz", lowerbound=0,upperbound=99999999999)
              print(MultiplicationQforImpossible)
              if MultiplicationQforImpossible == list1[x]*list2[x]:
                count=count+1
                print("Correct")
              else:
                print("Incorrect")
          if answer3 == True:
              str121="What is "
              str122=" + "
              str2=str121, str(list1[x]), str122, str(list2[x])
              str3= '' .join(str2)
              str3=str3.replace("{","")
              AdditionQforImpossible = easygui.integerbox(str3,"Mathematics Quiz", lowerbound=0,upperbound=99999999999)
              print(AdditionQforImpossible)
              if AdditionQforImpossible == list1[x]+list2[x]:
                count=count+1
                print("Correct")
              else:
                print("Incorrect")
        summarycode1 = "You Got " + str(count) + " out of ",  str(TimesforImpossible) +  " correct."
        summarycode2 = count/TimesforImpossible*100
        summarycode3 = str("% is your score. Thank You For Playing!")
        summarycode4 = (str(summarycode2) + str(summarycode3))
        summarycode1= '' .join(summarycode1)
        summarycode1=summarycode1.replace("{","")
        summary=easygui.msgbox(summarycode1)
        print(summary)  
        summary2=easygui.msgbox(str(summarycode4))
        
        print(summary2)


        








 
##COMMAND CENTER
answer = 99

answer1 = easygui.ccbox("Do you really want to continue?", "Mathematics Quiz Question")
print (answer1)

if answer1 == True:
  answer2 = easygui.msgbox("Time to get started with some math practice!", "Mathematics Quiz Screen")

  print (answer2) 

  if answer2 == "OK":
    answer3 = easygui.ynbox("Do you want to do addition or multiplication?", "Mathematics Quiz",('Add','Multiply'))
    print (answer3)    

    choices = ["Easy","Medium","Hard","Impossible"]
    Level = easygui.choicebox("Choose the difficulty:", "Mathematical Operators", choices)
    print (Level)   

    if Level == "Easy":
      funct1245()
    elif Level == "Medium":
      funct1256()
    elif Level == "Hard":
      funct1267()  
    elif Level == "Impossible":
      funct1278()  
else: 
  Goodbye=easygui.msgbox("Have a nice day!")





















