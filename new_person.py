#from classes import *
from main_page import *


def add_person(root):
    AdditionPersonScreen(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


class AdditionPersonScreen(Frame):
    def __init__(self, root):

        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.names = [ 'nickname*','password*','first name*', 'last name*', 'headline', 'country*', 'industry*', 'education*', 'current_job',
                      'skills',
                      'summary', 'jobs', 'publication', 'contacts', 'certificates']

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()
        self.entries(root)

    def populate(self):
        '''Put in some fake data'''
        for row in range(len(self.names)):
            Label(self.frame, text=self.names[row], width=12, borderwidth="1",
                  relief="solid").grid(row=row * 2, column=0)
            Label(self.frame, text='', background='#FFCCBC').grid(row=row * 2 + 1, column=0)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def destroy_widgets(self, root):
        self.canvas.destroy()
        self.frame.destroy()

        self.vsb.destroy()
        self.destroy()
        login_screen(root)
        #main_page(root)

    def entries(self, root):

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
        idif = 2
        nickname = StringVar()
        password = StringVar()
        name = StringVar()
        last_name = StringVar()
        headline = StringVar()
        country = StringVar()
        industry = StringVar()
        education = StringVar()
        current_job = StringVar()
        strVars = [nickname, password, name, last_name, headline, country, industry, education,current_job]
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
        i = 18
        six_entries(self, skill_array, i)
        i = i +idif

        summary = StringVar()
        entr(self, summary, i)

        job_1 = StringVar()
        job_2 = StringVar()
        i = i + idif
        entr(self, job_1, i)
        i = i + 1
        entr(self, job_2, i)

        publ_0 = StringVar()
        publ_1 = StringVar()
        publ_2 = StringVar()
        publ_3 = StringVar()
        publ_4 = StringVar()
        publ_5 = StringVar()
        publ_array = [publ_0, publ_1,publ_2,publ_3,publ_4,publ_5]
        i = i + 1
        six_entries(self, publ_array, i)

        contact_0 = StringVar()
        contact_1 = StringVar()
        i = i + idif
        entr(self, contact_0, i)
        i = i + 1
        entr(self, contact_1, i)

        sert_0 = StringVar()
        sert_1 = StringVar()
        sert_2 = StringVar()
        sert_3 = StringVar()
        sert_4 = StringVar()
        sert_5 = StringVar()
        sert_array = [sert_0,sert_1,sert_2,sert_3,sert_4,sert_5]
        six_entries(self, sert_array, 24)

        def to_out_array(array, out_array):
            for i in range(len(array)):
                if array[i].get() is not None and array[i].get() is not '':
                    out_array.append(array[i].get())

        def Save():
            #first_name, last_name, country, industry, education, skills = None, summary = None, headline = None,
            #     contacts = None, current_job = None, jobs = None, certificates = None, volunteering = None, publication = None)
            out_skills = []
            out_sert = []
            out_publications = []
            jobs = [job_1.get(), job_2.get()]
            contacts = [contact_0.get(), contact_1.get()]


            to_out_array(skill_array, out_skills)
            to_out_array(sert_array, out_sert)
            to_out_array(publ_array, out_publications)
            #print("out skills",out_skills)

            p = Person(nickname.get(), password.get(),name.get(), last_name.get(), country.get(), industry.get(), education.get(), skills = out_skills,
                       summary = summary.get(), headline =headline.get(),
                 contacts = contacts, current_job = current_job.get(), jobs = jobs, certificates = out_sert,
                        publication =out_publications)
            dict.update({str(nickname.get()): p})
            print(dict)

            for key, value in dict.items():
                print(key, value)

        i = 26
        Label(self.frame, text='', background='#FFCCBC').grid(row=i, column=0)
        but1 = Button(self.frame, text="Save", command=Save, width=18)
        but1.grid(row=i+1, column=2)


if __name__ == '__main__':
    root = Tk()
    root.title("GUI на Python")
    root.geometry("600x520")
    add_person(root)
