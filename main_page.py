from person_class import *
from company_class import *

#from list_of_pers import *
#from add import *
#from personal_profile import *
#from new_company import *
#from company_list import *
#from company_profile import *
#from vacancy_profile import *


def main_page(root):
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

    def but_callback_new():
        destroy_buttons()
        add_person(root)

    def but_callback_profile():
        destroy_buttons()
        personal_profile(root, dict['Grievous'])

    def but_callback_list():
        destroy_buttons()
        start_search(root)

    def but_callback_company_list():
        destroy_buttons()
        start_company_search(root,companies)

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
                                      command= but_callback_company_list)
    company_list_button.pack(pady=4)

    quit_button = Button(text ='Quit',
           width=20, height=3,
           bg=colors[2],
           command = quit)
    quit_button.pack(pady=4)

    new_button = Button( text = 'Add new',
                         width=20,
                         height=3,
                         command = but_callback_new)
    new_button.pack(pady=4)

    root.mainloop()


'''  ===================================== PERSONAL PROFILE ===================================================  '''


def personal_profile(root, person):
    Profile(root, person).pack(side="top", fill="both", expand=True)
    root.mainloop()


class Profile(Frame):
    def __init__(self, root,person):

        Frame.__init__(self, root)
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
        #self.person = person
        self.personal(root, person)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def destroy_widgets(self, root):
        self.frame.destroy()
        self.canvas.destroy()
        self.vsb.destroy()
        self.destroy()

    def to_new_company(self, root):
        self.destroy_widgets(root)
        add_company(root)

    def to_main_page(self, root):
        self.destroy_widgets(root)
        main_page(root)

    def to_job_search(self, root, skills):
        self.destroy_widgets(root)
        find_job(root, skills)

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
                 'summary', 'jobs', 'publication' , 'contacts', 'certificates']#, 'volunteering']
        main_page_button = Button(self.frame, text="Back", command=lambda: self.to_main_page(root),
                   width=20, height=1)
        main_page_button.pack(anchor=SW,pady=3)

        my_company = Button(self.frame, text="My Company", command=lambda: self.to_new_company(root),
                   width=20, height=1)
        my_company.pack(anchor=SE,pady=3)

        new_company = Button(self.frame, text="New Company", command=lambda: self.to_new_company(root),
                   width=20, height=1)
        new_company.pack(anchor=SE,pady=3)

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

        job_button = Button(self.frame, text="Find a job", command=lambda: self.to_job_search(root, person.skills),
                   width=20, height=1)
        job_button.pack(anchor=S,pady=3)

        root.mainloop()


'''  ===================================== PERSON SEARCH ===================================================  '''


def start_search(root):
    SearchScreen(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


class SearchScreen(Frame):
    def __init__(self, root):

        Frame.__init__(self, root)
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
        main_page(root)

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
            Button(self.frame, text=key, width = 28,  command=lambda: self.find_by_name(key)).grid(row=i, column=1)
            i= i+1

    def find_by_name(self, name):
        name = dict.get(name)
        if name is not None:
            self.destroy_widgets(root)
            personal_profile(root, name)
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
        self.names = ['first name*', 'last name*', 'headline', 'country*', 'industry*', 'education*', 'current_job',
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
        main_page(root)

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
        name = StringVar()
        last_name = StringVar()
        headline = StringVar()
        country = StringVar()
        industry = StringVar()
        education = StringVar()
        current_job = StringVar()
        strVars = [name, last_name, headline, country, industry, education,current_job]
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
        six_entries(self, skill_array, 14)

        summary = StringVar()
        entr(self, summary, 16)

        job_1 = StringVar()
        job_2 = StringVar()
        entr(self, job_1, 18)
        entr(self, job_2, 19)

        publ_0 = StringVar()
        publ_1 = StringVar()
        publ_2 = StringVar()
        publ_3 = StringVar()
        publ_4 = StringVar()
        publ_5 = StringVar()
        publ_array = [publ_0, publ_1,publ_2,publ_3,publ_4,publ_5]
        six_entries(self, publ_array, 20)

        contact_0 = StringVar()
        contact_1 = StringVar()
        entr(self, contact_0, 22)
        entr(self, contact_1, 23)

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

            p = Person(name.get(), last_name.get(), country.get(), industry.get(), education.get(), skills = out_skills,
                       summary = summary.get(), headline =headline.get(),
                 contacts = contacts, current_job = current_job.get(), jobs = jobs, certificates = out_sert,
                        publication =out_publications)
            dict.update({str(name.get()+last_name.get()): p})
            print(dict)

            for key, value in dict.items():
                print(key, value)

        i = 26
        Label(self.frame, text='', background='#FFCCBC').grid(row=i, column=0)
        but1 = Button(self.frame, text="Save", command=Save, width=18)
        but1.grid(row=i+1, column=2)


''' ==============================  COMPANY PROFILE  =================================  '''


def show_company_profile(root, company):
    CompanyProfile(root, company).pack(side="top", fill="both", expand=True)
    root.mainloop()


class CompanyProfile(Frame):
    def __init__(self, root,company):

        Frame.__init__(self, root)
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
        main_page(root)

    def to_show_vacancy_profile(self, root, name, company):
        self.destroy_widgets(root)
        show_vacancy_profile(root, name, company)

    def to_new_vacancy(self, root, company):
        self.destroy_widgets(root)
        add_vacancy(root, company)

    def new_label(self, nomination, txt):
        buffer = nomination + ":\t " + txt
        Label(self.frame, text = buffer, justify=LEFT, bg="#FFCCBC").pack(anchor=SW)

    def personal(self, root, company):

        b = Button(self.frame, text="Back", command=lambda: self.to_main_page(root),
                   width=20, height=1)
        b.pack(anchor=SW)

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
            #Label(self.frame, bg="#FFCCBC").pack(anchor=SW)

        root.mainloop()

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


def start_company_search(root, company_list):
    CompanySearchScreen(root, company_list).pack(side="top", fill="both", expand=True)
    root.mainloop()


class CompanySearchScreen(Frame):
    def __init__(self, root, company_list):

        Frame.__init__(self, root)
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
        main_page(root)

    def go_to_show_company_profile(self, root, name):
        self.destroy_widgets(root)
        show_company_profile(root, name)

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
            Button(self.frame, text=key, width = 28, command=lambda: self.find_by_name(key, company_list)).grid(row=i, column=1)
            i= i+1

    def find_by_name(self, name, company_list):
        name = company_list.get(name)
        if name is not None:
            self.go_to_show_company_profile(root, name)
        else:
            Error_label = Label(self.frame, text="No such person", background='#FFCCBC').grid(row=3, column=1)


'''  ====================================== COMPANY ADDITION =============================================='''


def add_company(root):
    AdditionCompanyScreen(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


class AdditionCompanyScreen(Frame):
    def __init__(self, root):

        Frame.__init__(self, root)
        self.canvas = Canvas(root, borderwidth=0, background="#FFCCBC")
        self.frame = Frame(self.canvas, background="#FFCCBC")
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.names = ['name', 'founder' ,'country','industry', 'company_size',  'website']

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
        main_page(root)

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
        founder = StringVar()
        country = StringVar()
        industry = StringVar()
        company_size = StringVar()
        website = StringVar()
        strVars = [name, founder, country, industry, company_size,website]
        for i in range(len(strVars)):
            entr(self, strVars[i], i * 2)

        def Save():
            #name, founder, country, industry, company_size, website = None,
            p = Company(name.get(), founder.get(), country.get(), industry.get(), company_size.get(), website.get())
            print(p)
            companies.update({str(name.get()): p})
            #dict.update({str(name.get()): p})
            print(companies)


        i = len(strVars)*2
        Label(self.frame, text='', background='#FFCCBC').grid(row=i, column=0)
        but1 = Button(self.frame, text="Save", command=Save, width=18)
        but1.grid(row=i+1, column=2)


'''  ===================================== VACANCY VIEW ===================================================  '''


def show_vacancy_profile(root, vacancy, company):
    VacancyProfile(root, vacancy, company).pack(side="top", fill="both", expand=True)
    root.mainloop()


class VacancyProfile(Frame):

    def __init__(self, root, vacancy, company):

        Frame.__init__(self, root)
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
        main_page(root)

    def to_company_page(self, root, company):
        self.destroy_widgets(root)
        show_company_profile(root, company)

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

        i = 26
        Label(self.frame, text='', background='#FFCCBC').grid(row=i, column=0)
        but1 = Button(self.frame, text="Save", command=Save, width=18)
        but1.grid(row=i+1, column=2)



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

            row = 12
            Label(self.frame, text='', background='#FFCCBC').grid(row=row, column=0)
            row = row + 1
            if len(matching_vacancy) is 0:
                l = Label(self.frame, text='there are no vacancies', background='#FFCCBC').grid(row=row, column=2)
            else:
                print("found", matching_vacancy)
                for i in range(len(matching_vacancy)):
                    print(matching_vacancy[i])
                    Button(self.frame, text=matching_vacancy[i].position, width=18, command=lambda:
                    self.to_show_vacancy_profile(root, matching_vacancy[i], comp_owners[i] )).grid(row=row, column=1)
                    row = row + 1


        i = 10
        Label(self.frame, text='', background='#FFCCBC').grid(row=i, column=0)
        but1 = Button(self.frame, text="Find", command=find, width=18)
        but1.grid(row=i+1, column=2)


if __name__ == '__main__':
    root = Tk()
    root.title("GUI на Python")
    root.geometry("600x520")
    main_page(root)


