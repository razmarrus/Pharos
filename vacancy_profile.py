from classes import *
from companies import *
from main_page import *
from company_profile import *

def show_vacancy_profile(root, vacancy, company):
    VacancyProfile(root, vacancy, company).pack(side="top", fill="both", expand=True)
    root.mainloop()


class VacancyProfile(Frame):

    def __init__(self, root,vacancy, company):

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

if __name__ == '__main__':
    root = Tk()
    root.title("GUI на Python")
    root.geometry("450x450")

    show_vacancy_profile(root, companies['OpenAI'].vacancy['Senior Software Engineer'], companies['OpenAI'])