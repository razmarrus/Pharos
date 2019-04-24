from person_class import *
from main_page import *
from new_company import *
from find_a_job import *

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
        self.names = ['nickname','first name', 'last name', 'headline', 'country', 'industry', 'education', 'current_job',
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
                 'summary', 'jobs', 'publication' , 'contacts', 'certificates' ,'nickname']#, 'volunteering']
        main_page_button = Button(self.frame, text="Back", command=lambda: self.to_main_page(root),
                   width=20, height=1)
        main_page_button.pack(anchor=SW,pady=3)

        my_company = Button(self.frame, text="My Company", command=lambda: self.to_new_company(root),
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

        job_button = Button(self.frame, text="Find a job", command=lambda: self.to_job_search(root, person.skills),
                   width=20, height=1)
        job_button.pack(anchor=S,pady=3)


if __name__ == '__main__':
    root = Tk()
    root.title("GUI на Python")
    root.geometry("450x450")

    personal_profile(root, dict['nia'])