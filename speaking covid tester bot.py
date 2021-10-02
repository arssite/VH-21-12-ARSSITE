import pygame as pa
import pyttsx3
frnd= pyttsx3.init()
frnd.say("myself arssite covid test bot")
frnd.runAndWait()

a=input("enter your name")
b=input("enter your age")
c=int(input("how many sympmtoms you have from these reply in No.(0,1,2,3,4)  :fever \n   cough \n tiredness \nloss of taste or smell"))
if c==0:
          print("KUCH NHI HAI /n YOU ARE PERFECT")
          frnd.say("KUCH NHI HAI  YOU ARE PERFECT")
          frnd.runAndWait()
elif c==1:
              print("do wait for 24hrs then ")
elif c==2:
             g=int(input("any from these: sore throat \nheadache \n aches and pains \ndiarrhoea\n a rash on skin, \n or discolouration of fingers or toesred or irritated eye"))
              
             print(g)

             if g==1:
                             print("take precautions not corona")
             elif g==2:
                            print("book appointment")
             elif g==3:
                            print("book appointment")
             elif g==4:
                            print("book appointment")
             elif g==5:
                            print("book appointment")
             elif g==6:
                            print("book appointment")
             else:
                            print("take precaution not corona")
elif c==3:
             g=int(input("any from these: sore throat \nheadache \n aches and pains \ndiarrhoea\n a rash on skin, \n or discolouration of fingers or toesred or irritated eyes"))
             print(g)
             if g==1:
                             print("book appointment")
             elif g==2:
                            print("book appointment")
             elif g==3:
                            print("book appointment")
             elif g==4:
                            print("book appointment")
             elif g==5:
                            print("book appointment")
             elif g==6:
                            print("book appointment")
             else:
                            print("take precaution not corona")
else:
              print("REFRESH")




              pa.time.wai(6000)
