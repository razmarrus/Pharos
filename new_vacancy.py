from companies import *
from classes import *
from main_page import *


def add_vacancy(root, company):
    AdditionVacancyScreen(root, company).pack(side="top", fill="both", expand=True)
    root.mainloop()


class AdditionVacancyScreen(Frame):
    def __init__(self, root, company):

        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.names = ['position', 'requirements', 'city','company', 'salary', 'skills']

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()
        self.entries(root, company)

    def populate(self):
        '''Put in some fake data'''
        for row in range(len(self.names)):
            Label(self.frame, text=self.names[row], width=12, borderwidth="1",
                  relief="solid").grid(row=row * 2, column=0)
            Label(self.frame, text='', background='#FFCCBC').grid(row=row * 2 + 1, column=0)


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def destroy_example(self, root):
        self.canvas.destroy()
        self.frame.destroy()

        self.vsb.destroy()
        self.destroy()
        main_page(root)

    def entries(self, root, owner_company):

        def six_entries(self, strVar, i):
            counter = 0
            for x in range(2):
                for y in range(1, 4, 1):
                    entr(self, strVar[counter], x+i, y)
                    counter = counter + 1

        def entr(self, strVar, i, j = 1):
            entry = Entry(self.frame, textvariable=strVar, width=22, bd=2)
            entry.grid(row=i, column=j)
            print(i)

        but2 = Button(self.frame, text="Back", command=lambda: self.destroy_example(root), width=18)  # self.quit)#
        but2.grid(row=0, column=3)
        #'company', 'position', 'salary', 'skills'
        company = StringVar()
        position = StringVar()
        salary = StringVar()
        city = StringVar()
        requirements = StringVar()

        strVars = [ position, requirements, city, company, salary]
        for i in range(len(strVars)):
            entr(self, strVars[i], i * 2)

        skill_0 = StringVar()
        skill_1 = StringVar()
        skill_2 = StringVar()
        skill_3 = StringVar()
        skill_4 = StringVar()
        skill_5 = StringVar()
        skill_array = [skill_0 ,skill_1 ,skill_2 ,skill_3 ,skill_4 ,skill_5 ]
        #for i in range(12, 14, 1):
        six_entries(self, skill_array, len(strVars)*2)


        def to_out_array(array, out_array):
            for i in range(len(array)):
                if array[i].get() is not None and array[i].get() is not '':
                    out_array.append(array[i].get())

        def Save():
            out_skills = []
            to_out_array(skill_array, out_skills)

            print("out skills",out_skills)

            p = Vacancy(position.get(), requirements.get(), city.get(), company.get(), salary.get(), out_skills)
            print(p)
            companies[str(owner_company.name)].vacancy.update({str(position.get()): p})

            #vacancy_dict.update({str(name.get()): p})
            #print(dict)

            #for key, value in dict.items():
             #   print(key, value)

        i = 26
        Label(self.frame, text='', background='#FFCCBC').grid(row=i, column=0)
        but1 = Button(self.frame, text="Save", command=Save, width=18)
        but1.grid(row=i+1, column=2)


if __name__ == '__main__':
    root = Tk()
    root.title("GUI на Python")
    root.geometry("600x520")
    add_vacancy(root, companies['Blizzard'])
