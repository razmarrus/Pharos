#from classes import *
from main_page import *
from vacancy_profile import *


def find_job(root, current_skills):
    JobSearch(root, current_skills).pack(side="top", fill="both", expand=True)
    root.mainloop()


class JobSearch(Frame):
    def __init__(self, root, current_skills):

        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.entries(root, current_skills)


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def destroy_widgets(self, root):
        self.canvas.destroy()
        self.frame.destroy()

        self.vsb.destroy()
        self.destroy()
        #main_page(root)

    def to_show_vacancy_profile(self, root, name, company):
        self.destroy_widgets(root)
        show_vacancy_profile(root, name, company)

    def entries(self, root, current_skills):

        def six_entries(self, strVar, i):
            counter = 0
            for x in range(2):
                for y in range(1, 4, 1):
                    entr(self, strVar[counter], x+i, y)
                    counter = counter + 1

        def entr(self, strVar, i, j = 1):
            entry = Entry(self.frame, textvariable=strVar, width=22, bd=2)
            entry.grid(row=i, column=j)
            #print(i)

        but2 = Button(self.frame, text="Back", command=lambda: self.destroy_widgets(root), width=18)  # self.quit)#
        but2.grid(row=0, column=3)
        Label(self.frame, text='', background='#FFCCBC').grid(row=1, column=0)
        Label(self.frame, text='enter skills', background='#FFCCBC').grid(row=2, column=1)

        skill_0 = StringVar()
        skill_1 = StringVar()
        skill_2 = StringVar()
        skill_3 = StringVar()
        skill_4 = StringVar()
        skill_5 = StringVar()

        skill_array = [skill_0 ,skill_1 ,skill_2 ,skill_3 ,skill_4 ,skill_5 ]
        if current_skills is not None:
            for i in range(len(current_skills)):
                skill_array[i].set(current_skills[i])
        #for i in range(12, 14, 1):
        six_entries(self, skill_array, 3)

        def to_out_array(array, out_array):
            for i in range(len(array)):
                if array[i].get() is not None and array[i].get() is not '':
                    out_array.append(array[i].get())

        def find():
            out_skills = []
            comp_owners = []
            matching_vacancy = []
            to_out_array(skill_array, out_skills)
            for key, value in companies.items():  # Rows
                if value.vacancy is not None:
                    #print(value.vacancy)
                    for vacancy_key, vacancy in value.vacancy.items():
                        for skill in vacancy.skills:
                            if skill in out_skills:
                                matching_vacancy.append(vacancy)
                                comp_owners.append(value)
                                break

            row = 12
            Label(self.frame, text='', background='#FFCCBC').grid(row=row, column=0)
            row = row + 1
            if len(matching_vacancy) is 0:
                l = Label(self.frame, text='there are no vacancies', background='#FFCCBC').grid(row=row, column=2)
            else:
                print("found", matching_vacancy)
                for i in range(len(matching_vacancy)):
                    print(matching_vacancy[i])
                    Button(self.frame, text=matching_vacancy[i].position, width=18, command=lambda vac=matching_vacancy[i], owner = comp_owners[i]:
                    self.to_show_vacancy_profile(root, vac, owner )).grid(row=row, column=1)
                    row = row + 1


        i = 10
        Label(self.frame, text='', background='#FFCCBC').grid(row=i, column=0)
        but1 = Button(self.frame, text="Find", command=find, width=18)
        but1.grid(row=i+1, column=2)


if __name__ == '__main__':
    root = Tk()
    root.title("GUI на Python")
    root.geometry("600x520")
    find_job(root, ['meow', 'woof', 'machine learning'])
