from classes import *
#from list_of_pers import *
#from add import *
#from personal_profile import *


def main_page(root):
    buffer = Frame(root, background="#FFCCBC",  height=95, width =1500)
    buffer.pack()
    root.configure(background='#FFCCBC')
    #colors = ['#FFAB91','#BCAAA4','#EEEEEE']
    colors = ['#ECEFF1','#CFD8DC','#B0BEC5']
    def butCallback_profile():
        buffer.destroy()
        list_button.destroy()
        new_button.destroy()
        my_profile_button.destroy()
        quit_button.destroy()
        personal_profile(root, dict['Grievous'])

    my_profile_button =  Button( text = 'see profile',
                         width=20,
                         height=3,
                         bg = colors[0],
                         command = butCallback_profile)
    my_profile_button.pack(pady=4)#padx=10, pady=10)

    def butCallback_list():
        #t_top.destroy()
        buffer.destroy()
        list_button.destroy()
        new_button.destroy()
        my_profile_button.destroy()
        quit_button.destroy()
        start_search(root)

    list_button = Button( text = 'find',
                         width=20,
                         height=3,
                         bg= colors[1],
                         command = butCallback_list)
    list_button.pack(pady=4)

    quit_button = Button(text ='Quit',
           width=20, height=3,
           bg=colors[2],
           command = quit)
    quit_button.pack(pady=4)

    def butCallback_new():
        buffer.destroy()
        list_button.destroy()
        new_button.destroy()
        my_profile_button.destroy()
        quit_button.destroy()
        add(root)


    new_button = Button( text = 'Add new',
                         width=20,
                         height=3,
                         command = butCallback_new)
    new_button.pack(pady=4)

    root.mainloop()

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

    def destroy_example(self, root):
        list = root.grid_slaves()
        for l in list:
            l.destroy()

        self.frame.destroy()
        self.canvas.destroy()
        self.vsb.destroy()
        self.destroy()
        main_page(root)

    def new_label(self, nomination, txt):
        buffer = nomination + ":\t " + txt
        Label(self.frame, text = buffer, justify=LEFT, bg="#FFCCBC").pack(anchor=SW)

    def new_label_simple(self, txt):
        Label(self.frame ,text = txt,  bg="#FFCCBC").pack(anchor=SW)

    def call_multistring_label(self, name, perVar):
        if perVar is not None:
            self.multi_string_label(name, perVar)

    def multi_string_label(self, name, arr):
        self.new_label_simple("\n" + name + ":")
        for i in range(len(arr)):
            self.new_label_simple('\t\t'+arr[i])

    def personal(self, root, person):

        names = ['first name', 'last name', 'headline', 'country  ', 'industry  ', 'education', 'current_job', 'skills',
                 'summary', 'jobs', 'publication' , 'contacts', 'certificates']#, 'volunteering']
        b = Button(self.frame, text="Back", command=lambda: self.destroy_example(root),
                   width=10, height=1)
        b.pack(anchor=SW,pady=3)

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


        root.mainloop()


def start_search(root):
    Search_screen(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


class Search_screen(Frame):
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

    def destroy_vigets(self, root):
        self.canvas.destroy()
        self.frame.destroy()

        self.vsb.destroy()
        self.destroy()
        #main_page(root)

    def to_main_page(self, root):
        self.canvas.destroy()
        self.frame.destroy()

        self.vsb.destroy()
        self.destroy()
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
            self.destroy_vigets(root)
            personal_profile(root, name)
        else:
            Error_label = Label(self.frame, text="No such person", background='#FFCCBC').grid(row=3, column=1)



def add(root):
    Addition_screen(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

class Addition_screen(Frame):
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


    def destroy_example(self, root):

        list = root.grid_slaves()
        #for l in list:
        #    l.destroy()
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

        def to_out_var(field, out_field):
            if field.get() is not None and field.get() is not '':
                out_field = field.get()


        def Save():
            #first_name, last_name, country, industry, education, skills = None, summary = None, headline = None,
            #     contacts = None, current_job = None, jobs = None, certificates = None, volunteering = None, publication = None)
            out_skills = []
            out_sert = []
            out_publications = []
            jobs = [job_1.get(), job_2.get()]
            out_jobs = []
            contacts = [contact_0.get(), contact_1.get()]
            out_contacts = []

            to_out_array(skill_array, out_skills)
            to_out_array(sert_array, out_sert)
            to_out_array(publ_array, out_publications)
            to_out_array(jobs, out_jobs)
            to_out_array(contacts, out_contacts)


            print("out skills",out_skills)


            p = Person(name.get(), last_name.get(), country.get(), industry.get(), education.get(), skills = out_skills,
                       summary = summary.get(), headline =headline.get(),
                 contacts = out_contacts, current_job = current_job.get(), jobs = jobs, certificates = out_sert,
                        publication =out_publications)
            dict.update({str(name.get()): p})
            print(dict)

            for key, value in dict.items():
                print(key, value)

        i = 26
        Label(self.frame, text='', background='#FFCCBC').grid(row=i, column=0)
        but1 = Button(self.frame, text="Save", command=Save, width=18)
        but1.grid(row=i+1, column=2)


#main_page(dict)
if __name__ == '__main__':
    root = Tk()
    root.title("GUI на Python")
    root.geometry("600x520")
    main_page(root)


