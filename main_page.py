from person_class import *
from company_class import *
from pymongo import MongoClient
from tkinter import messagebox


#from list_of_pers import *
#from add import *
#from personal_profile import *
#from new_company import *
#from company_list import *
#from company_profile import *
#from vacancy_profile import *


def main_page(root, nickname):
    buffer = Frame(root, background="#FFCCBC",  height=95, width =1500)
    buffer.pack()
    root.configure(background='#FFCCBC')
    #colors = ['#FFAB91','#BCAAA4','#EEEEEE']
    colors = ['#ECEFF1', '#CFD8DC', '#B0BEC5']

    def destroy_buttons():
        buffer.destroy()
        list_button.destroy()
        new_button.destroy()
        my_profile_button.destroy()
        quit_button.destroy()
        company_list_button.destroy()
        change_person_button.destroy()

    def but_callback_new():
        destroy_buttons()
        login_personal_profile(root)

    def but_callback_profile():
        destroy_buttons()
        personal_profile(root, dict[nickname], dict[nickname])

    def but_callback_list():
        destroy_buttons()
        start_search(root, dict[nickname])

    def but_callback_company_list():
        destroy_buttons()
        start_company_search(root, companies, dict[nickname])

    def but_callback_change_info():
        destroy_buttons()
        change_person(root, dict[nickname])

    my_profile_button = Button( text = 'see profile',
                         width=20,
                         height=3,
                         bg = colors[0],
                         command=but_callback_profile)

    my_profile_button.pack(pady=4)#padx=10, pady=10)

    list_button = Button( text = 'find person',
                         width=20,
                         height=3,
                         bg= colors[1],
                         command = but_callback_list)
    list_button.pack(pady=4)

    company_list_button = Button(text='find company',
                                      width=20,
                                      height=3,
                                      bg=colors[1],
                                      command=but_callback_company_list)
    company_list_button.pack(pady=4)

    change_person_button = Button(text='Change information',
                                  width=20,
                                  height=3,
                                  bg=colors[1],
                                  command=but_callback_change_info)
    change_person_button.pack(pady=4)

    quit_button = Button(text ='Quit',
           width=20, height=3,
           bg=colors[2],
           command = quit)
    quit_button.pack(pady=4)

    new_button = Button( text = 'To log screen',
                         width=20,
                         height=3,
                         bg=colors[2],
                         command = but_callback_new)
    new_button.pack(pady=4)

    root.mainloop()


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


'''  ===================================== Login Screen ===================================================  '''


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


'''  ===================================== PERSONAL PROFILE ===================================================  '''


def personal_profile(root, person, acc):
    Profile(root, person, acc).pack(side="top", fill="both", expand=True)
    root.mainloop()


class Profile(Frame):
    def __init__(self, root, person, acc):
        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.names = ['nickname','first name', 'last name', 'headline', 'country', 'industry', 'education', 'current_job',
                      'skills',
                      'summary', 'jobs', 'publication', 'contacts', 'certificates']

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)
        #self.person = person
        self.acc = acc
        self.personal(root, person)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def destroy_widgets(self, root):
        self.frame.destroy()
        self.canvas.destroy()
        self.vsb.destroy()
        self.destroy()

    def to_my_company(self, root):
        self.destroy_widgets(root)
        my_company(root, companies, self.acc)

    def to_new_company(self, root):
        self.destroy_widgets(root)
        add_company(root, self.acc)

    def to_main_page(self, root):
        self.destroy_widgets(root)
        main_page(root, self.acc.nickname)

    def to_job_search(self, root, skills):
        self.destroy_widgets(root)
        find_job(root, skills, self.acc)

    def new_label(self, nomination, txt):
        buffer = nomination + ":\t " + txt
        Label(self.frame, text = buffer, justify=LEFT, bg="#FFCCBC").pack(anchor=SW)
        #label.pack()

    def new_label_simple(self, txt):
        Label(self.frame ,text = txt,  bg="#FFCCBC").pack(anchor=SW)

    def call_multistring_label(self, name, perVar):
        if perVar is not None:
            self.multi_string_label(name, perVar)
        #label.pack()

    def multi_string_label(self, name, arr):
        self.new_label_simple("\n" + name + ":")
        for i in range(len(arr)):
            self.new_label_simple('\t\t'+arr[i])


    def personal(self, root, person):

        names = ['first name', 'last name', 'headline', 'country  ', 'industry  ', 'education', 'current_job', 'skills',
                 'summary', 'jobs', 'publication', 'contacts', 'certificates', 'nickname']#, 'volunteering']
        main_page_button = Button(self.frame, text="Back", command=lambda: self.to_main_page(root),
                   width=20, height=1)
        main_page_button.pack(anchor=SW,pady=3)
        if person.nickname == self.acc.nickname:
            my_company = Button(self.frame, text="My Company", command=lambda: self.to_my_company(root),
                       width=20, height=1)
            my_company.pack(anchor=SE,pady=3)
            new_company = Button(self.frame, text="New Company", command=lambda: self.to_new_company(root),
                       width=20, height=1)
            new_company.pack(anchor=SE,pady=3)
        self.new_label(names[13], person.nickname)
        self.new_label(names[0], person.name)
        self.new_label(names[1], person.last_name)
        if person.headline is not None:
            self.new_label(names[2], person.headline)

        self.new_label(names[3], person.country)
        self.new_label(names[4], person.industry)
        self.new_label(names[5], person.education)

        if person.current_job is not None:
            self.new_label(names[6], person.current_job)

        if person.skills is not None:
            self.multi_string_label(names[7], person.skills)

        if person.summary is not None:
            self.new_label(names[8], person.summary)

        personArr = [person.jobs, person.publication, person.contacts, person.certificates]
        for i in range(9, 13, 1):
            j = i - 9
            self.call_multistring_label(names[i], personArr[j])
        if person.nickname == self.acc.nickname:
            job_button = Button(self.frame, text="Find a job", command=lambda: self.to_job_search(root, person.skills),
                   width=20, height=1)
            job_button.pack(anchor=S,pady=3)


'''  ===================================== PERSON SEARCH ===================================================  '''


def start_search(root, acc):
    SearchScreen(root, acc).pack(side="top", fill="both", expand=True)
    root.mainloop()


class SearchScreen(Frame):
    def __init__(self, root, acc):

        Frame.__init__(self, root)
        self.acc = acc
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.names = ['first name*', 'last name*', 'headline', 'country*', 'industry*', 'education*', 'current_job',
                      'skills',
                      'summary', 'jobs', 'publication', 'contacts', 'certificates']

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.find(root)

    def destroy_widgets(self, root):
        self.canvas.destroy()
        self.frame.destroy()

        self.vsb.destroy()
        self.destroy()
        #main_page(root)

    def to_main_page(self, root):
        self.destroy_widgets(root)
        main_page(root, self.acc.nickname)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def find(self, root):
        Button(self.frame, width=15,text="Back" ,command=lambda: self.to_main_page(root)).grid(row=0, column=0)  # self.quit)#
        Label(self.frame, background='#FFCCBC').grid(row=1, column=0)
        Label(self.frame, text='Enter name').grid(row = 2, column=0 )
        target = StringVar()
        Entry(self.frame, textvariable=target, width=30, bd=2).grid(row = 2, column=1 )

        Button(self.frame, width=15, text="Find", command=lambda: self.find_by_name(target.get())).grid(row=2, column=2)
        Label(self.frame, background='#FFCCBC').grid(row=3, column=1)

        i = 4
        for key, value in dict.items():  # Rows
            print(key)
            Button(self.frame, text=key, width = 28,  command=lambda key = key: self.find_by_name(key)).grid(row=i, column=1)
            i= i+1

    def find_by_name(self, name):
        name = dict.get(name)
        if name is not None:
            self.destroy_widgets(root)
            personal_profile(root, name, self.acc)
        else:
            Error_label = Label(self.frame, text="No such person", background='#FFCCBC').grid(row=3, column=1)


'''  ===================================== PERSON ADDITION ===================================================  '''


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
        i = i+idif

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
        i = i + 1
        sert_0 = StringVar()
        sert_1 = StringVar()
        sert_2 = StringVar()
        sert_3 = StringVar()
        sert_4 = StringVar()
        sert_5 = StringVar()
        sert_array = [sert_0,sert_1,sert_2,sert_3,sert_4,sert_5]
        six_entries(self, sert_array, i)

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

            out_skills_1 = []
            to_out_array(skill_array, out_skills_1)
            out_skills_1.append('')
            out_skills_1.append('')
            out_skills_1.append('')
            out_skills_1.append('')
            out_skills_1.append('')
            out_skills_1.append('')
            out_skills = []
            out_skills.append(out_skills_1[0])
            out_skills.append(out_skills_1[1])
            out_skills.append(out_skills_1[2])
            out_skills.append(out_skills_1[3])
            out_skills.append(out_skills_1[4])
            out_skills.append(out_skills_1[5])
            to_out_array(sert_array, out_sert)
            out_sert.append('')
            out_sert.append('')
            out_sert.append('')
            out_sert.append('')
            out_sert.append('')
            out_sert.append('')
            to_out_array(publ_array, out_publications)
            out_publications.append('')
            out_publications.append('')
            out_publications.append('')
            out_publications.append('')
            out_publications.append('')
            out_publications.append('')
            #print("out skills",out_skills)
            Exists = False
            for key, value in dict.items():
                if key == nickname.get():
                    Exists = True
            if Exists:
                messagebox.showinfo("Error", "Nickname exists")
            else:
                p = Person(nickname.get(), password.get(), name.get(), last_name.get(), country.get(), industry.get(),
                           education.get(), skills=out_skills,
                           summary=summary.get(), headline=headline.get(),
                     contacts=contacts, current_job=current_job.get(), jobs=jobs, certificates=out_sert,
                            publication=out_publications)
                dict.update({str(nickname.get()): p})
                print(dict)
                client = MongoClient()
                db = client.ourdb
                collection = db.personcoll
                collection.insert_one({"nickname": p.nickname, "password": p.password, "first_name": p.name,
                                           "last_name": p.last_name, "country": p.country, "industry": p.industry,
                                           "education": p.education, "headline": p.headline,
                                           "summary": p.summary, "current_job": p.current_job, "skill_0": p.skills[0],
                                           "skill_1": p.skills[1], "skill_2": p.skills[2], "skill_3": p.skills[3],
                                           "skill_4": p.skills[4], "skill_5": p.skills[5], "job_0": p.jobs[0],
                                           "job_1": p.jobs[1], "publication_0": p.publication[0],
                                           "publication_1": p.publication[1], "publication_2": p.publication[2],
                                           "publication_3": p.publication[3], "publication_4": p.publication[4],
                                           "publication_5": p.publication[5], "contact_0": p.contacts[0],
                                           "contact_1": p.contacts[1], "certificate_0": p.certificates[0],
                                           "certificate_1": p.certificates[1], "certificate_2": p.certificates[2],
                                           "certificate_3": p.certificates[3], "certificate_4": p.certificates[4],
                                           "certificate_5": p.certificates[5]})

            for key, value in dict.items():
                    print(key, value)

        i = 26
        Label(self.frame, text='', background='#FFCCBC').grid(row=i, column=0)
        but1 = Button(self.frame, text="Save", command=Save, width=18)
        but1.grid(row=i+5, column=3)


''' ================================ PERSON INFORMATION CHANGE============================================== '''


def change_person(root, acc):
    ChangePersonScreen(root, acc).pack(side="top", fill="both", expand=True)
    root.mainloop()


class ChangePersonScreen(Frame):
    def __init__(self, root, acc):

        Frame.__init__(self, root)
        self.acc = acc
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.names = ['first name*', 'last name*', 'headline', 'country*', 'industry*',
                      'education*', 'current_job', 'skills', 'summary', 'jobs', 'publication', 'contacts',
                      'certificates']
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
        main_page(root, self.acc.nickname)

    def entries(self, root):

        def six_entries(self, strVar, i):
            counter = 0
            for x in range(2):
                for y in range(1, 4, 1):
                    entr(self, strVar[counter], x + i,y)
                    counter = counter + 1

        def entr(self, strVar, i, j=1):
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
        strVars = [name, last_name, headline, country, industry, education, current_job]
        for i in range(len(strVars)):
            entr(self, strVars[i], i * 2)
        name.set(self.acc.name)
        last_name.set(self.acc.last_name)
        headline.set(self.acc.headline)
        country.set(self.acc.country)
        industry.set(self.acc.industry)
        education.set(self.acc.education)
        current_job.set(self.acc.current_job)
        skill_0 = StringVar()
        skill_1 = StringVar()
        skill_2 = StringVar()
        skill_3 = StringVar()
        skill_4 = StringVar()
        skill_5 = StringVar()
        skill_array = [skill_0, skill_1, skill_2, skill_3, skill_4, skill_5]
        #for i in range(12, 14, 1):
        i=14
        six_entries(self, skill_array, i)
        i=i+idif
        lentemp = len(self.acc.skills)
        if lentemp > 0:
            skill_0.set(self.acc.skills[0])
            if lentemp > 1:
                skill_1.set(self.acc.skills[1])
                if lentemp > 2:
                    skill_2.set(self.acc.skills[2])
                    if lentemp > 3:
                        skill_3.set(self.acc.skills[3])
                        if lentemp > 4:
                            skill_4.set(self.acc.skills[4])
                            if lentemp > 5:
                               skill_5.set(self.acc.skills[5])
        summary = StringVar()
        entr(self, summary, i)
        summary.set(self.acc.summary)
        job_1 = StringVar()
        job_2 = StringVar()
        i=i+idif
        entr(self, job_1, i)
        i=i+1
        entr(self, job_2, i)
        lentemp = len(self.acc.jobs)
        if lentemp > 0:
            job_1.set(self.acc.jobs[0])
            if lentemp > 1:
                job_1.set(self.acc.jobs[1])
        publ_0 = StringVar()
        publ_1 = StringVar()
        publ_2 = StringVar()
        publ_3 = StringVar()
        publ_4 = StringVar()
        publ_5 = StringVar()
        publ_array = [publ_0, publ_1,publ_2,publ_3,publ_4,publ_5]
        i = i + 1
        six_entries(self, publ_array, i)
        lentemp = len(self.acc.publication)
        if lentemp > 0:
            publ_0.set(self.acc.publication[0])
            if lentemp > 1:
                publ_1.set(self.acc.publication[1])
                if lentemp > 2:
                    publ_2.set(self.acc.publication[2])
                    if lentemp > 3:
                        publ_3.set(self.acc.publication[3])
                        if lentemp > 4:
                            publ_4.set(self.acc.publication[4])
                            if lentemp > 5:
                                publ_5.set(self.acc.publication[5])
        contact_0 = StringVar()
        contact_1 = StringVar()
        i = i + idif
        entr(self, contact_0, i)
        i = i + 1
        entr(self, contact_1, i)
        i = i + 1
        lentemp = len(self.acc.contacts)
        if lentemp > 0:
            contact_0.set(self.acc.contacts[0])
            if lentemp > 1:
                contact_1.set(self.acc.contacts[1])
        sert_0 = StringVar()
        sert_1 = StringVar()
        sert_2 = StringVar()
        sert_3 = StringVar()
        sert_4 = StringVar()
        sert_5 = StringVar()
        sert_array = [sert_0,sert_1,sert_2,sert_3,sert_4,sert_5]
        six_entries(self, sert_array, i)
        lentemp = len(self.acc.certificates)
        if lentemp > 0:
            sert_0.set(self.acc.certificates[0])
            if lentemp > 1:
                sert_1.set(self.acc.certificates[1])
                if lentemp > 2:
                    sert_2.set(self.acc.certificates[2])
                    if lentemp > 3:
                        sert_3.set(self.acc.certificates[3])
                        if lentemp > 4:
                            sert_4.set(self.acc.certificates[4])
                            if lentemp > 5:
                                sert_5.set(self.acc.certificates[5])
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

            out_skills_1 = []
            to_out_array(skill_array, out_skills_1)
            out_skills_1.append('')
            out_skills_1.append('')
            out_skills_1.append('')
            out_skills_1.append('')
            out_skills_1.append('')
            out_skills_1.append('')
            out_skills = []
            out_skills.append(out_skills_1[0])
            out_skills.append(out_skills_1[1])
            out_skills.append(out_skills_1[2])
            out_skills.append(out_skills_1[3])
            out_skills.append(out_skills_1[4])
            out_skills.append(out_skills_1[5])
            to_out_array(sert_array, out_sert)
            out_sert.append('')
            out_sert.append('')
            out_sert.append('')
            out_sert.append('')
            out_sert.append('')
            out_sert.append('')
            to_out_array(publ_array, out_publications)
            out_publications.append('')
            out_publications.append('')
            out_publications.append('')
            out_publications.append('')
            out_publications.append('')
            out_publications.append('')
            newacc = Person(self.acc.nickname, self.acc.password, name.get(), last_name.get(),
                              country.get(), industry.get(), education.get(), skills=out_skills,
                          summary=summary.get(), headline=headline.get(),
                    contacts=contacts, current_job=current_job.get(), jobs=jobs, certificates=out_sert,
                            publication=out_publications)
            client = MongoClient()
            db = client.ourdb
            collection = db.personcoll
            collection.delete_one({"nickname": newacc.nickname})
            collection.insert_one({"nickname": newacc.nickname, "password": newacc.password, "first_name": newacc.name,
                                       "last_name": newacc.last_name, "country": newacc.country, "industry": newacc.industry,
                                       "education": newacc.education, "headline": newacc.headline,
                                       "summary": newacc.summary, "current_job": newacc.current_job, "skill_0": newacc.skills[0],
                                       "skill_1": newacc.skills[1], "skill_2": newacc.skills[2], "skill_3": newacc.skills[3],
                                       "skill_4": newacc.skills[4], "skill_5": newacc.skills[5], "job_0": newacc.jobs[0],
                                       "job_1": newacc.jobs[1], "publication_0": newacc.publication[0],
                                       "publication_1": newacc.publication[1], "publication_2": newacc.publication[2],
                                       "publication_3": newacc.publication[3], "publication_4": newacc.publication[4],
                                       "publication_5": newacc.publication[5], "contact_0": newacc.contacts[0],
                                       "contact_1": newacc.contacts[1], "certificate_0": newacc.certificates[0],
                                       "certificate_1": newacc.certificates[1], "certificate_2": newacc.certificates[2],
                                       "certificate_3": newacc.certificates[3], "certificate_4": newacc.certificates[4],
                                       "certificate_5": newacc.certificates[5]})
            dict.pop(self.acc.nickname)
            dict.update({newacc.nickname: newacc})
            print(dict)

            for key, value in dict.items():
                    print(key, value)

        i = 26
        Label(self.frame, text='', background='#FFCCBC').grid(row=i, column=0)
        but1 = Button(self.frame, text="Save", command=Save, width=18)
        but1.grid(row=i+5, column=3)


''' ==============================  COMPANY PROFILE  ======================================================  '''


def show_company_profile(root, company, acc):
    CompanyProfile(root, company,acc).pack(side="top", fill="both", expand=True)
    root.mainloop()


class CompanyProfile(Frame):
    def __init__(self, root, company, acc):

        Frame.__init__(self, root)
        self.acc = acc
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.names = ['name', 'founder', 'country', 'industry', 'company size', 'website']

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        #self.person = person
        self.personal(root, company)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def destroy_widgets(self, root):
        self.frame.destroy()
        self.canvas.destroy()
        self.vsb.destroy()
        self.destroy()
        #main_page(root)

    def to_main_page(self, root):
        self.destroy_widgets(root)
        main_page(root, self.acc.nickname)

    def to_show_vacancy_profile(self, root, name, company):
        self.destroy_widgets(root)
        show_vacancy_profile(root, name, company, self.acc)

    def to_new_vacancy(self, root, company):
        self.destroy_widgets(root)
        add_vacancy(root, company, self.acc)

    def new_label(self, nomination, txt):
        buffer = nomination + ":\t " + txt
        Label(self.frame, text = buffer, justify=LEFT, bg="#FFCCBC").pack(anchor=SW)

    def personal(self, root, company):

        b = Button(self.frame, text="Back", command=lambda: self.to_main_page(root),
                   width=20, height=1)
        b.pack(anchor=SW)
        if company.founder == self.acc.nickname:
            new_vacancy_button = Button(self.frame, text="New vacancy", command=lambda: self.to_new_vacancy(root, company),
                   width=20, height=1)
            new_vacancy_button.pack(anchor=SE,pady=3)

        names =  ['name', 'founder', 'country', 'industry', 'company_size', 'website']
        comp_vars = [company.name, company.founder, company.country, company.industry, company.company_size,
                    company.website]
        for i in range(len(comp_vars)):
            self.new_label(names[i], comp_vars[i])

        Label(self.frame, bg="#FFCCBC").pack(anchor=SW)
        Label(self.frame, text = 'vacancy:',bg="#FFCCBC").pack(anchor=SW)

        for key, value in company.vacancy.items():  # Rows
            #print(key)
            Button(self.frame, text=key, width=28, command=lambda: self.find_by_name(company, key)).pack(anchor=SW)
            if company.founder == self.acc.nickname:
                Button(self.frame, text='Delete', width=16, command=lambda: self.del_vacancy(root, company, key)).pack(anchor=NE)
            #Label(self.frame, bg="#FFCCBC").pack(anchor=SW)

        root.mainloop()

    def del_vacancy(self, root, company, name):
        company.vacancy.pop(name, None)
        client = MongoClient()
        db = client.ourdb
        collection = db.vacancies
        collection.delete_one({"position": name, "company": company.name})
        self.destroy_widgets(root)
        show_company_profile(root, company, self.acc)

    def find_by_name(self, company, name):
        print("going to", name)
        name = company.vacancy.get(name)
        print(name)
        if name is not None:
            self.to_show_vacancy_profile(root, name, company)
        else:
            Error_label = Label(self.frame, text="Can't find vacancy!", background='#FFCCBC').pack(anchor=SW)
            print("Can't find vacancy!")


'''  ===================================== COMPANY SEARCH ===================================================  '''


def start_company_search(root, company_list, acc):
    CompanySearchScreen(root, company_list, acc).pack(side="top", fill="both", expand=True)
    root.mainloop()


class CompanySearchScreen(Frame):
    def __init__(self, root, company_list, acc):

        Frame.__init__(self, root)
        self.acc = acc
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.names = ['first name*', 'last name*', 'headline', 'country*', 'industry*', 'education*', 'current_job',
                      'skills',
                      'summary', 'jobs', 'publication', 'contacts', 'certificates']

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.find(root, company_list)

    def destroy_widgets(self, root):
        self.canvas.destroy()
        self.frame.destroy()
        self.vsb.destroy()
        self.destroy()

    def to_main_page(self, root):
        self.destroy_widgets(root)
        main_page(root, self.acc.nickname)

    def go_to_show_company_profile(self, root, name):
        self.destroy_widgets(root)
        show_company_profile(root, name, self.acc)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def find(self, root, company_list):
        Button(self.frame, width=15,text="Back" ,command=lambda: self.to_main_page(root)).grid(row=0, column=0)  # self.quit)#
        Label(self.frame, background='#FFCCBC').grid(row=1, column=0)
        Label(self.frame, text='Enter name').grid(row = 2, column=0 )
        target = StringVar()
        Entry(self.frame, textvariable=target, width=30, bd=2).grid(row = 2, column=1 )

        Button(self.frame, width=15, text="Find", command=lambda: self.find_by_name(target.get(), company_list)).grid(row=2, column=2)
        Label(self.frame, background='#FFCCBC').grid(row=3, column=1)

        i = 4
        for key, value in company_list.items():  # Rows
            print(key)
            Button(self.frame, text=key, width = 28, command=lambda key=key: self.find_by_name(key, company_list)).grid(row=i, column=1)
            i= i+1

    def find_by_name(self, name, company_list):
        name = company_list.get(name)
        if name is not None:
            self.go_to_show_company_profile(root, name)
        else:
            Error_label = Label(self.frame, text="No such person", background='#FFCCBC').grid(row=3, column=1)


'''  ====================================== COMPANY ADDITION =============================================='''


def add_company(root, acc):
    AdditionCompanyScreen(root, acc).pack(side="top", fill="both", expand=True)
    root.mainloop()


class AdditionCompanyScreen(Frame):
    def __init__(self, root, acc):

        Frame.__init__(self, root)
        self.acc = acc
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.names = ['name', 'country', 'industry', 'company_size',  'website']

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


    def destroy_example(self, root):

        self.canvas.destroy()
        self.frame.destroy()

        self.vsb.destroy()
        self.destroy()
        main_page(root, self.acc.nickname)

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
            print(i)

        but2 = Button(self.frame, text="Back", command=lambda: self.destroy_example(root), width=18)  # self.quit)#
        but2.grid(row=0, column=3)
        idif = 2
        #'name', 'founder' ,'country','industry', 'company_size',  'company_size'
        name = StringVar()
#        founder = StringVar()
        country = StringVar()
        industry = StringVar()
        company_size = StringVar()
        website = StringVar()
        strVars = [name, country, industry, company_size,website]
        for i in range(len(strVars)):
            entr(self, strVars[i], i * 2)

        def Save():
            #name, founder, country, industry, company_size, website = None,
            p = Company(name.get(), self.acc.nickname, country.get(), industry.get(), company_size.get(), website.get())
            print(p)
            companies.update({str(name.get()): p})
            client = MongoClient()
            db = client.ourdb
            collection = db.companies
            collection.insert_one({"name": p.name, "founder": p.founder, "country": p.country, "industry":
                p.industry, "company_size": p.company_size, "website": p.website})
            #dict.update({str(name.get()): p})
            print(companies)


        i = len(strVars)*2
        Label(self.frame, text='', background='#FFCCBC').grid(row=i, column=0)
        but1 = Button(self.frame, text="Save", command=Save, width=18)
        but1.grid(row=i+1, column=2)


'''  ====================================== MY COMPANY ==================================================='''


def my_company(root, company_list, acc):
    ViewMyCompanies(root, company_list, acc).pack(side="top", fill="both", expand=True)
    root.mainloop()


class ViewMyCompanies(Frame):
    def __init__(self, root, company_list, acc):

        Frame.__init__(self, root)
        self.acc = acc
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.names = ['first name*', 'last name*', 'headline', 'country*', 'industry*', 'education*', 'current_job',
                      'skills',
                      'summary', 'jobs', 'publication', 'contacts', 'certificates']

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.find(root, company_list)

    def destroy_widgets(self, root):
        self.canvas.destroy()
        self.frame.destroy()
        self.vsb.destroy()
        self.destroy()

    def to_main_page(self, root):
        self.destroy_widgets(root)
        main_page(root, self.acc.nickname)

    def go_to_show_company_profile(self, root, name):
        self.destroy_widgets(root)
        show_company_profile(root, name, self.acc)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def find(self, root, company_list):
        Button(self.frame, width=15, text="Back", command=lambda: self.to_main_page(root)).grid(row=0,
                                                                                                column=0)  # self.quit)#
        Label(self.frame, background='#FFCCBC').grid(row=1, column=0)
#        Label(self.frame, text='Enter name').grid(row=2, column=0)
#        target = StringVar()
#        Entry(self.frame, textvariable=target, width=30, bd=2).grid(row=2, column=1)

#        Button(self.frame, width=15, text="Find", command=lambda: self.find_by_name(target.get(), company_list)).grid(
#            row=2, column=2)
#        Label(self.frame, background='#FFCCBC').grid(row=3, column=1)

        i = 4
        for key, value in company_list.items():  # Rows
            print(key)
            if value.founder == self.acc.nickname:
                Button(self.frame, text=key, width=28, command=lambda key=key: self.find_by_name(key, company_list)).grid(
                row=i, column=0)
                Label(self.frame, width=16, background='#FFCCBC').grid(row=i, column=1)
                Button(self.frame, text="Delete", width=16,
                       command=lambda key=key: self.delete_com(key, company_list)).grid(
                    row=i, column=3)
                i = i + 1

    def delete_com(self, name, company_list):
        company_list.pop(name, None)
        self.destroy_widgets(root)
        my_company(root, company_list, self.acc)

    def find_by_name(self, name, company_list):
        name = company_list.get(name)
        if name is not None:
            self.go_to_show_company_profile(root, name)
        else:
            Error_label = Label(self.frame, text="No such person", background='#FFCCBC').grid(row=3, column=1)


'''  ===================================== VACANCY VIEW ===================================================  '''


def show_vacancy_profile(root, vacancy, company, acc):
    VacancyProfile(root, vacancy, company, acc).pack(side="top", fill="both", expand=True)
    root.mainloop()


class VacancyProfile(Frame):

    def __init__(self, root, vacancy, company, acc):

        Frame.__init__(self, root)
        self.acc = acc
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.names = ['first name', 'last name', 'headline', 'country', 'industry', 'education', 'current_job',
                      'skills',
                      'summary', 'jobs', 'publication', 'contacts', 'certificates']

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.personal(root, vacancy, company)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def to_main_menu(self, root):
        self.destroy_widgets(root)
        main_page(root, self.acc.nickname)

    def to_company_page(self, root, company):
        self.destroy_widgets(root)
        show_company_profile(root, company, self.acc)

    def destroy_widgets(self, root):
        self.frame.destroy()
        self.canvas.destroy()
        self.vsb.destroy()
        self.destroy()
        #main_page(root)

    def new_label(self, nomination, txt):
        buffer = nomination + ":\t " + txt
        Label(self.frame, text = buffer, justify=LEFT, bg="#FFCCBC").pack(anchor=SW)
        #label.pack()

    def new_label_simple(self, txt):
        Label(self.frame ,text = txt,  bg="#FFCCBC").pack(anchor=SW)

    def call_multistring_label(self, name, perVar):
        if perVar is not None:
            self.multi_string_label(name, perVar)
        #label.pack()

    def multi_string_label(self, name, arr):
        self.new_label_simple("\n" + name + ":")
        for i in range(len(arr)):
            self.new_label_simple('\t\t'+arr[i])

    def personal(self, root, vacancy, company):

        to_main = Button(self.frame, text="To main menu", command=lambda: self.to_main_menu(root),
                   width=20, height=1)
        to_main.pack(anchor=SW,pady=3)

        b = Button(self.frame, text="Back", command=lambda: self.to_company_page(root, company),
                   width=20, height=1)
        b.pack(anchor=SW,pady=3)

        names = ['position', 'city', 'requirements',  'company', 'salary']
        vacancy_vars = [vacancy.position, vacancy.city, vacancy.requirements,  vacancy.company, vacancy.salary]
        for i in range(len(vacancy_vars)):
            self.new_label(names[i], vacancy_vars[i])

        if vacancy.skills is not None:
            self.multi_string_label('skills', vacancy.skills)

        root.mainloop()


'''  ===================================== VACANCY ADDITION ===================================================  '''


def add_vacancy(root, company, acc):
    AdditionVacancyScreen(root, company, acc).pack(side="top", fill="both", expand=True)
    root.mainloop()


class AdditionVacancyScreen(Frame):
    def __init__(self, root, company, acc):

        Frame.__init__(self, root)
        self.acc = acc
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.names = ['position', 'requirements', 'city', 'salary', 'skills']

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()
        self.company = company
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
        main_page(root, self.acc.nickname)

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
        #company = StringVar()
        position = StringVar()
        salary = StringVar()
        city = StringVar()
        requirements = StringVar()

        strVars = [position, requirements, city, salary]
        for i in range(len(strVars)):
            entr(self, strVars[i], i * 2)

        skill_0 = StringVar()
        skill_1 = StringVar()
        skill_2 = StringVar()
        skill_3 = StringVar()
        skill_4 = StringVar()
        skill_5 = StringVar()
        skill_array = [skill_0, skill_1, skill_2, skill_3, skill_4, skill_5]
        #for i in range(12, 14, 1):
        six_entries(self, skill_array, len(strVars)*2)

        def to_out_array(array, out_array):
            for i in range(len(array)):
                if array[i].get() is not None and array[i].get() is not '':
                    out_array.append(array[i].get())

        def Save():
            out_skills = []
            to_out_array(skill_array, out_skills)

            print("out skills", out_skills)
            out_skills.append('')
            out_skills.append('')
            out_skills.append('')
            out_skills.append('')
            out_skills.append('')
            out_skills.append('')
            p = Vacancy(position.get(), requirements.get(), city.get(), self.company.name, salary.get(), out_skills)
            print(p)
            companies[str(owner_company.name)].vacancy.update({str(position.get()): p})
            client = MongoClient()
            db = client.ourdb
            collection = db.vacancies

            collection.insert_one({"position": p.position, "requirements": p.requirements, "city": p.city,
                                           "company": p.company, "salary": p.salary, "skill_0": p.skills[0],
                                           "skill_1": p.skills[1], "skill_2": p.skills[2], "skill_3": p.skills[3],
                                           "skill_4": p.skills[4], "skill_5": p.skills[5]})

        i = 26
        Label(self.frame, text='', background='#FFCCBC').grid(row=i, column=0)
        but1 = Button(self.frame, text="Save", command=Save, width=18)
        but1.grid(row=i+1, column=2)


'''  ===================================== JOB SEARCH ===================================================  '''


def find_job(root, current_skills, acc):
    JobSearch(root, current_skills, acc).pack(side="top", fill="both", expand=True)
    root.mainloop()


class JobSearch(Frame):
    def __init__(self, root, current_skills, acc):

        Frame.__init__(self, root)
        self.acc = acc
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
        #main_page(root, self.acc.nickname)

    def to_main_menu(self, root):
        self.canvas.destroy()
        self.frame.destroy()

        self.vsb.destroy()
        self.destroy()
        main_page(root, self.acc.nickname)

    def to_show_vacancy_profile(self, root, name, company):
        self.destroy_widgets(root)
        show_vacancy_profile(root, name, company, self.acc)

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

        but2 = Button(self.frame, text="Back", command=lambda: self.to_main_menu(root), width=18)  # self.quit)#
        but2.grid(row=0, column=3)
        Label(self.frame, text='', background='#FFCCBC').grid(row=1, column=0)
        Label(self.frame, text='enter skills', background='#FFCCBC').grid(row=2, column=1)

        skill_0 = StringVar()
        skill_1 = StringVar()
        skill_2 = StringVar()
        skill_3 = StringVar()
        skill_4 = StringVar()
        skill_5 = StringVar()

        skill_array = [skill_0, skill_1, skill_2, skill_3, skill_4, skill_5]
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
                    Button(self.frame, text=matching_vacancy[i].position, width=18, command=lambda
                        vac=matching_vacancy[i], owner = comp_owners[i]:
                    self.to_show_vacancy_profile(root, vac, owner)).grid(row=row, column=1)
                    row = row + 1


        i = 10
        Label(self.frame, text='', background='#FFCCBC').grid(row=i, column=0)
        but1 = Button(self.frame, text="Find", command=find, width=18)
        but1.grid(row=i+1, column=2)


if __name__ == '__main__':
    client = MongoClient()
    db = client.ourdb
    collection = db.personcoll

    '''for key, value in dict.items():      #добавление аккаунта
        collection.insert_one({"nickname": value.nickname, "password": value.password, "first_name": value.name,
                               "last_name": value.last_name, "country": value.country, "industry": value.industry,
                               "education": value.education, "headline": value.headline,
                               "summary": value.summary, "current_job": value.current_job, "skill_0": value.skills[0],
                               "skill_1": value.skills[1], "skill_2": value.skills[2], "skill_3": value.skills[3],
                               "skill_4": value.skills[4], "skill_5": value.skills[5], "job_0": value.jobs[0],
                               "job_1": value.jobs[1], "publication_0": value.publication[0],
                               "publication_1": value.publication[1], "publication_2": value.publication[2],
                               "publication_3": value.publication[3], "publication_4": value.publication[4],
                               "publication_5": value.publication[5], "contact_0": value.contacts[0],
                               "contact_1": value.contacts[1], "certificate_0": value.certificates[0],
                               "certificate_1": value.certificates[1], "certificate_2": value.certificates[2],
                               "certificate_3": value.certificates[3], "certificate_4": value.certificates[4],
                               "certificate_5": value.certificates[5]})'''



    for men in collection.find():
        p = Person(men["nickname"], men["password"], men["first_name"], men["last_name"], men["country"],
                   men["industry"], men["education"], [men["skill_0"], men["skill_1"], men["skill_2"], men["skill_3"],
                   men["skill_4"], men["skill_5"]], men["summary"], men["headline"], [men["contact_0"], men["contact_1"]],
                   men["current_job"], [men["job_0"], men["job_1"]], [men["certificate_0"], men["certificate_1"],
                                                                      men["certificate_2"], men["certificate_3"],
                                                                      men["certificate_4"], men["certificate_5"]],
                   [men["publication_0"], men["publication_1"], men["publication_2"], men["publication_3"],
                    men["publication_4"], men["publication_5"]])
        dict.update({p.nickname: p})
    collection = db.vacancies

    '''    for key, value in companies.items():
        for key1, vac in value.vacancy.items(): #добавление вакансии
            collection.insert_one({"position": vac.position, "requirements": vac.requirements, "city": vac.city,
                                   "company": vac.company, "salary": vac.salary, "skill_0": vac.skills[0],
                                   "skill_1": vac.skills[1], "skill_2": vac.skills[2], "skill_3": vac.skills[3],
                                   "skill_4": vac.skills[4], "skill_5": vac.skills[5]})'''



    vacancies = []
    for vac in collection.find():
        v = Vacancy(vac["position"], vac["requirements"], vac["city"], vac["company"], vac["salary"], [vac["skill_0"],
                                                                                                       vac["skill_1"],
                                                                                                       vac["skill_2"],
                                                                                                       vac["skill_3"],
                                                                                                       vac["skill_4"],
                                                                                                       vac["skill_5"]])
        vacancies.append(v)
    collection = db.companies

    '''    for key, value in companies.items(): #добавление компании
        collection.insert_one({"name": value.name, "founder": value.founder, "country": value.country, "industry":
                               value.industry, "company_size": value.company_size, "website": value.website})'''



    for comp in collection.find():
        c = Company(comp["name"], comp["founder"], comp["country"], comp["industry"], comp["company_size"],
                    comp["website"])
        for vac in vacancies:
            if vac.company == c.name:
                c.add_vacancy(vac)
        companies.update({c.name: c})
    print(dict)
    root = Tk()
    root.title("Pharos")
    root.geometry("600x520")
    root.configure(background='#FFCCBC')
    login_screen(root)
    #main_page(root, 'nia')