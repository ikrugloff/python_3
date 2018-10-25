from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# plain_text = cipher_suite.decrypt(cipher_text)


class MyDumbScreen(BoxLayout):  # Changed to a BoxLayout for simplicity

    def __init__(self, **kwargs):
        super(MyDumbScreen, self).__init__(**kwargs)
        self.orientation = "vertical"

        my_user_input = TextInput(multiline=True)
        self.add_widget(my_user_input)

        my_output = Label(text="initial value", text_size=(800, None))
        self.add_widget(my_output)

        def callback(instance, value):
            byte_value = b'value'
            enc_data = cipher_suite.encrypt(byte_value)
            if value:
                my_output.text = f'Your text is: \n{value}\n\nEncrypted text is: \n{enc_data}'
            else:
                my_output.text = f'Your text is: {value}\n\nEncrypted text is: '

        my_user_input.bind(text=callback)


class MyApp(App):

    def build(self):
        return MyDumbScreen()


if __name__ == '__main__':
    MyApp().run()
