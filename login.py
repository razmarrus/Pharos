from main_page import *

def login_screen(root):

    def destroy_buttons():
        buffer.destroy()
        new_button.destroy()
        my_profile_button.destroy()
        quit_button.destroy()

    def but_callback_new():
        destroy_buttons()
        add_person(root)

    def but_callback_profile():
        destroy_buttons()
        login_personal_profile(root)

    buffer = Frame(root, background="#FFCCBC",  height=95, width =1500)
    buffer.pack()
        #self.root.configure(background='#FFCCBC')
    colors = ['#ECEFF1', '#CFD8DC', '#B0BEC5']
    my_profile_button = Button(text='Log in',
                                        width=20,
                                        height=3,
                                        bg=colors[0],
                                        command=but_callback_profile)

    my_profile_button.pack(pady=4)  # padx=10, pady=10)

    new_button = Button(text='New profile',
                            width=20,
                            height=3,
                            bg=colors[1],
                            command=but_callback_new)
    new_button.pack(pady=4)

    quit_button = Button(text='Quit',
                             width=20, height=3,
                             bg=colors[2],
                             command=quit)
    quit_button.pack(pady=4)

    root.mainloop()


def login_personal_profile(root):
    LoginPersonalProfile(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


class LoginPersonalProfile(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")

        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                             tags="self.frame")

        self.widgets()

    def destroy_entry_screen(self, root):
        self.frame.destroy()
        self.canvas.destroy()
        self.destroy()
        login_screen(root)

    def enter_profile(self, nickname, password):

        print("nickname", nickname.get(), 'password', password.get())
        Label(self.frame, text='', bg="#FFCCBC").grid(row=5, column=1)
        if dict[nickname.get()]:
            if dict[nickname.get()].password == password.get():
                self.frame.destroy()
                self.canvas.destroy()
                self.destroy()
                main_page(root, nickname.get())
        else:
            Label(self.frame, text='incorrect input', bg="#FFCCBC").grid(row=5, column=1)

    def widgets(self):
        Button(self.frame, text='Back', width=15, command=lambda  r=root: self.destroy_entry_screen(r)).grid(
            row=0, column=0)
        Label(self.frame, text='', bg="#FFCCBC", width=12).grid(row=1, column=0)
        Label(self.frame, text='nickname   ', bg="#FFCCBC").grid(row=2, column=1)
        nickname = StringVar()
        Entry(self.frame, textvariable=nickname, width=30, bd=2).grid(row=2, column=2)

        Label(self.frame, text='password ', bg="#FFCCBC").grid(row=3, column=1)
        password = StringVar()
        Entry(self.frame, textvariable=password, width=30, bd=2).grid(row=3, column=2)
        Button(self.frame, text='Enter', width=18, command=lambda  nickname=nickname,
                                                             password=password:
        self.enter_profile( nickname, password)).grid(row=4, column=1)


if __name__ == '__main__':
    root = Tk()
    root.title("Pharos")
    root.geometry("600x520")
    root.configure(background='#FFCCBC')
    login_screen(root)
