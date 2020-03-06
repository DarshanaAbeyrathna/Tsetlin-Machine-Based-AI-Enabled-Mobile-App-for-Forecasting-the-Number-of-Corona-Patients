from kivy.uix.dropdown import DropDown
import numpy
import kivy.app
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
import numpy as np

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        global features
        features = []
        self.s = None
        self.operators = [","]
        self.last_was_operator = None
        self.last_button = None
        self.dropper_text = None
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.dropdown = None
        
        self.testbox2 = TextInput(multiline=True, readonly=True, halign="center", font_size=14, size =(100, 100), size_hint =(2, 2))
        self.testbox2.text = "-------------------------------------------------------Predict next day Corona incidences------------------------------------------------------- \n Machine Learning algorithm: Regression Tsetlin Machine \n No. of Training Samples: "
        self.add_widget(self.testbox2)
        
        self.testbox3 = TextInput(multiline=True, readonly=True, halign="center", font_size=14, size =(100, 100), size_hint =(3, 3))
        self.testbox3.text = "Please select a country"
        self.add_widget(self.testbox3)
        
        self.solution = TextInput(multiline=True, readonly=True, halign="center", font_size=15, size =(100, 100), size_hint =(2, 2))
        self.add_widget(self.solution)   
        
        # ------------- Number Buttons ----------------------------------
            
        buttons1 = ["7", "8", "9"]
        h_layout = BoxLayout()
        for label in buttons1:
            button = Button(text=label, pos_hint={'center_x':0.5, 'center_y': 0.5})
            button.bind(on_press=self.on_button_press)
            h_layout.add_widget(button)
        self.add_widget(h_layout) 
        
        #-----------------------------------------------------------------
        buttons2 = ["4", "5", "6"]
        h_layout = BoxLayout()
        for label in buttons2:
            button = Button(text=label, pos_hint={'center_x':0.5, 'center_y': 0.5})
            button.bind(on_press=self.on_button_press)
            h_layout.add_widget(button)
        self.add_widget(h_layout)
        
        #----------------------------------------------------------------
        buttons3 = ["1", "2", "3"]
        h_layout = BoxLayout()
        for label in buttons3:
            button = Button(text=label,  pos_hint={'center_x':0.5, 'center_y': 0.5})
            button.bind(on_press=self.on_button_press)
            h_layout.add_widget(button)
        self.add_widget(h_layout)
     
        
        #----------------------------------------------------------------
        buttons4 = [".", "0", "C"]
        h_layout = BoxLayout()
        for label in buttons4:
            button = Button(text=label, width=20)
            button.bind(on_press=self.on_button_press)
            h_layout.add_widget(button)
        self.add_widget(h_layout)
        
        # ----------------- Next Feature and Predict Button ----------------------
        
        buttons5 = ["Next Feature", "Predict"]
        h_layout = BoxLayout()
        for label in buttons5:
            if label == "Next Feature":
                button = Button(text=label, width=10, background_color =(0.81, 0.07, 0.03, 1))
                button.bind(on_press=self.on_button_press)
            else:
                button = Button(text=label, width=10, background_color =(0, 1, 0, 1))
                button.bind(on_press=self.on_solution)
            h_layout.add_widget(button)
        self.add_widget(h_layout)
        
        #------------DropDown --------------------------------     
        
        self.dropdown = DropDown()
        for index in ["Overall", "China", "South Korea", "Italy", "USA"]:        
            btn = Button(text=index, size_hint_y=None, height=50)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)        
        
        self.mainbutton = Button(text='Country', pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.mainbutton.bind(on_press=self.dropper)
        self.add_widget(self.mainbutton)
        self.dropper_text = self.mainbutton.text
        
        
        self.testbox1 = Image(source='select.png')
        self.add_widget(self.testbox1)
        
        
        #-----------------------------------------------------------------
#        
    def dropper(self, instance):
        self.s = "pressed"
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.dropper_text = instance.text
        global TAs
        global Sup
        global Threds
        global labs
        Sup = np.zeros((7, 1), dtype=np.float32)
        labs = []

        self.remove_widget(self.testbox1)
    
        if self.dropper_text == "Overall": 
            TAs = numpy.load('TMextractsOverall.npy')
            Sup = numpy.load('RegSupOverall.npy')
            Threds = numpy.load('ThredsOverall.npy')
            labs = numpy.load('LabsOverall.npy')
            self.testbox3.text = "Overall"
            self.testbox1 = Image(source='overall.png')
            
        elif self.dropper_text == "China":
            TAs = numpy.load('TMextractsChina.npy')
            Sup = numpy.load('RegSupChina.npy')
            Threds = numpy.load('ThredsChina.npy')
            labs = numpy.load('LabsChina.npy')
            self.testbox3.text = "China"
            self.testbox1 = Image(source='china.gif')
            
        elif self.dropper_text == "South Korea":
            TAs = numpy.load('TMextractsSKorea.npy')
            Sup = numpy.load('RegSupSKorea.npy')
            Threds = numpy.load('ThredsSKorea.npy')
            labs = numpy.load('LabsSKorea.npy')
            self.testbox3.text = "South Korea"
            self.testbox1 = Image(source='SKorea.gif')
            
        elif self.dropper_text == "Italy":
            TAs = numpy.load('TMextractsItaly.npy')
            Sup = numpy.load('RegSupItaly.npy')
            Threds = numpy.load('ThredsItaly.npy')
            labs = numpy.load('LabsItaly.npy')
            self.testbox3.text = "Italy"
            self.testbox1 = Image(source='Italy.gif')
            
        elif self.dropper_text == "USA":
            TAs = numpy.load('TMextractsUSA.npy')
            Sup = numpy.load('RegSupUSA.npy')
            Threds = numpy.load('ThredsUSA.npy')
            labs = numpy.load('LabsUSA.npy')
            self.testbox3.text = "USA"
            self.testbox1 = Image(source='usa.gif')
        else:
            self.testbox3.text = "No country"
            self.testbox1 = Image(source='select.png')
                
        self.add_widget(self.testbox1)
        
        self.testbox2.text = "-------------------------------------------------------Predict next day Corona incidences------------------------------------------------------- \n - Machine Learning algorithm: Regression Tsetlin Machine \n - No. of Training Samples: %s (very low) \n - In order to obtain accorate predictions, train the algorithm with more samples and update the app" \
        % (int(Sup[3,0]))
        #(int(Sup[3,0]), Sup[4,0], Sup[5,0])
        
        ll = ''
        for i in labs:
            ll += (str(i) + ', ')
        
        self.testbox3.text = " %s is selected\n - Yesterday is 'd-1', Today is 'd', tomorrow is 'd+1'\n - Overall is 'O', China is 'C', South Korea is 'SK', Italy is 'I', and USA is 'U'\n - You are ready to predict %s(d+1). \n - No. of inputs needed: %s - [ %s ]. \n \
        Enter 'Next Feature' button after every feature. \n \
        After entering all features, press the 'Predict' button." \
        % (self.testbox3.text, self.testbox3.text, int(Sup[6,0]), ll)
        
        
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == "Next Feature":
            button_text = ","

        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if self.s == "pressed":
            features = []
            number = ''
            for i in text:
                if i != ',':
                    number = number+i
                else:
                    features.append(float(number))
                    number = '' 
            if i != ',':
                features.append(float(number))
                
            if len(features) == int(Sup[6,0]):
                
                inputs = []
                for row in range(len(Threds)):
                    for col in range(len(Threds[0])):
                        if Threds[row,col] == -1:
                            break
                        else:
                            if features[row] <= Threds[row,col]:
                                inputs.append(1)
                            else:
                                inputs.append(0)
                                                
                SUM = 0
                for pcluase in range(len(TAs)):
                    clauseoutput = 1
                    feature_index = 1
                    for x in range(len(inputs)):
                        if (TAs[pcluase,feature_index] == 1 and inputs[x] == 0) or (TAs[pcluase,feature_index+1] == 1 and inputs[x] == 1):
                            clauseoutput = 0
                            break
                        feature_index += 2
                    SUM += TAs[pcluase,0] * clauseoutput
                    
                output = ((SUM * (Sup[1,0]-Sup[2,0]))/ Sup[0,0]) + Sup[2,0]
                
                if text:        
                    inputfeatures = str(eval(self.solution.text)) 
                    solution = str(int(output))            
                    self.solution.text = "Input %s \n There will be %s Corona patients in %s on the selected day. \n \n Start again by pressing 'c'" % (inputfeatures, solution, self.dropper_text)
                
            else:
                output = "Wrong input size \n Start again by pressing 'c'"
            
                if text:          
                    solution = str(output)            
                    self.solution.text = solution
        else:
            output = "Select a country fitst. \n Start again by pressing 'C'"
            
            if text:          
                solution = str(output)            
                self.solution.text = solution

class FirstApp(kivy.app.App):
    def build(self):
       return MyGrid()
   
firstApp = FirstApp()
firstApp.run()