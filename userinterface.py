import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Rectangle
from kivy.uix.filechooser import FileChooserListView
import os
from find_breed import predict, decode_breed



class ScreenThree(Screen):

    def __init__(self, **kwargs):
        super(ScreenThree, self).__init__(**kwargs)
        container = BoxLayout(orientation='vertical')

        filechooser = FileChooserListView()
        filechooser.bind(on_selection=lambda x: self.selected(filechooser.selection))

        open_btn = Button(text='Open and predict!',font_size='30sp', size_hint=(1, .2))
        open_btn.bind(on_release=lambda x: self.open(filechooser.selection))

        container.add_widget(filechooser)
        container.add_widget(open_btn)
        self.add_widget(container)



    def open(self, filename):

        image = filename[0]
        image = image.replace("\\", '/')

        TestApp.image_path =image

        breeds = predict(image)
        TestApp.breed_list = breeds

        screen2 = ScreenTwo(name='screen2')
        TestApp.my_screenmanager.add_widget(screen2)
        TestApp.flag=1

        print(breeds)
        self.changer()

    def changer(self,*args):
        self.manager.current = 'screen2'




class MyLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.26, 0.35, 0.51, 0.75)
            Rectangle(pos=self.pos, size=self.size)

class MyImage(Image):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.26, 0.35, 0.51, 0.75)
            Rectangle(pos=self.pos, size=self.size)




class ScreenOne(Screen):

    def __init__ (self,**kwargs):
        super (ScreenOne, self).__init__(**kwargs)

        generalBox=BoxLayout(orientation='vertical')

        my_box = BoxLayout()
        my_label = MyLabel(text='')
        my_box.add_widget(my_label)
        generalBox.add_widget(my_box)

        my_box1 = BoxLayout()
        logo=MyImage(source="resources/dog.png")
        my_label1 = MyLabel(text='Welcome to doggo \n breed classifier!', font_size='30sp')
        my_box1.add_widget(logo)
        my_box1.add_widget(my_label1)
        generalBox.add_widget(my_box1)

        my_box3 = BoxLayout()
        my_label3 = MyLabel(text='')
        my_box3.add_widget(my_label3)
        generalBox.add_widget(my_box3)

        my_box2=BoxLayout()
        my_button1 = Button(text="Select your doggo image!", font_size='30sp')
        my_button1.bind(on_press=self.changer)
        my_box2.add_widget(my_button1)
        generalBox.add_widget(my_box2)

        self.add_widget(generalBox)




    def changer(self,*args):
        TestApp.flag=1
        self.manager.current = 'screen3'

class ScreenTwo(Screen):

        def __init__(self, **kwargs):
            super(ScreenTwo, self).__init__(**kwargs)


            generalBox = BoxLayout(orientation='vertical')


            my_box = BoxLayout()
            userimage = MyImage(source=TestApp.image_path, size_hint=(1, 2.9), pos_hint={'top': 1})
            my_box.add_widget(userimage)
            generalBox.add_widget(my_box)


            for i in range(0, 3):
                TestApp.breed_names[i] = decode_breed(TestApp.breed_list[i])

            my_box1 = BoxLayout()
            image1 = MyImage(source=("resources/" + TestApp.breed_names[0] + ".jpg"), size_hint=(1, 1.2), pos_hint={'top': -1})
            image2 = MyImage(source=("resources/" + TestApp.breed_names[1] + ".jpg"), size_hint=(1, 1.2), pos_hint={'top': -1})
            image3 = MyImage(source=("resources/" + TestApp.breed_names[2] + ".jpg"), size_hint=(1, 1.2), pos_hint={'top': -1})
            my_box1.add_widget(image1)
            my_box1.add_widget(image2)
            my_box1.add_widget(image3)
            generalBox.add_widget(my_box1)

            my_box4 = BoxLayout()
            my_label4 = MyLabel(text='', size_hint=(1, 0.1))
            my_box4.add_widget(my_label4)
            generalBox.add_widget(my_box4)




            my_box3 = BoxLayout()
            breed1 = MyLabel(text=("Your dog is: " + str(TestApp.breed_names[0])),size_hint=(1, .4), pos_hint={'top': -0.20})
            breed2 = MyLabel(text=("Similar breed is: " + str(TestApp.breed_names[1])), size_hint=(1, .4), pos_hint={'top': -0.20})
            breed3 = MyLabel(text=("Similar breed is: " + str(TestApp.breed_names[2])), size_hint=(1, .4), pos_hint={'top': -0.20})
            my_box3.add_widget(breed1)
            my_box3.add_widget(breed2)
            my_box3.add_widget(breed3)
            generalBox.add_widget(my_box3)

            my_box2 = BoxLayout()
            my_button1 = Button(text="Try with another picture!", font_size='30sp', size_hint=(1, 0.4))
            my_button1.bind(on_press=self.changer)
            my_box2.add_widget(my_button1)
            generalBox.add_widget(my_box2)

            self.add_widget(generalBox)


        def changer(self,*args):
            TestApp.image_path = 'ok'
            self.manager.current = 'screen1'

class TestApp(App):
        image_path = 'ok'
        breed_list=["333"]
        my_screenmanager = ScreenManager()
        breed_names = ["tst", 'test', 'test']
        flag=0

        def build(self):

            screen1 = ScreenOne(name='screen1')
            screen3 = ScreenThree(name='screen3')
            self.my_screenmanager.add_widget(screen1)
            self.my_screenmanager.add_widget(screen3)
            return self.my_screenmanager

if __name__ == '__main__':
    TestApp().run()