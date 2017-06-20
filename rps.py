from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.image import Image
import random

class rps_root(FloatLayout):
    result=ObjectProperty()
    Label(text='Rock Paper Scissors',pos_hint={'x':0,'y':.2})
    def choicerock(self,*args):
        choice=('Rock','r')
        self.oppchoice(choice)
    def choicepaper(self,*args):
        choice=('Paper','p')
        self.oppchoice(choice)
    def choicescissors(self,*args):
        choice=('Scissors','s')
        self.oppchoice(choice)
    def oppchoice(self,choice):
        n=('r','p','s')
        dich={'p':'Paper',
              's':'Scissors',
              'r':'Rock'
              }
        rnd=random.choice(n)
        if choice[1]==rnd:
            self.result.text='Tie'
        elif choice[1]=='p' and rnd=='r' or choice[1]=='r' and rnd=='s' or choice[1]=='s' and rnd=='p':
            self.result.text='Player wins! : %s beats %s' %(choice[0],dich[rnd])
        elif rnd=='p' and choice[1]=='r' or rnd=='r' and choice[1]=='s' or rnd=='s' and choice[1]=='p':
            self.result.text='Computer wins : %s beats %s' %(dich[rnd],choice[0])
class RpsApp(App):
    title='Rock Paper Scissors'

##if __name__=='__main__':
##    RpsApp().run()
