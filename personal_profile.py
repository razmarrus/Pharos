from classes import *
#from main_page import *


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



if __name__ == '__main__':
    root = Tk()
    root.title("GUI на Python")
    root.geometry("450x450")

    personal_profile(root, dict['Grievous'])