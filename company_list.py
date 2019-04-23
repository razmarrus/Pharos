#from classes import *
from main_page import *
from company_profile import *
from company_class import *
#from personal_profile import *


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


if __name__ == "__main__":
    root=Tk()
    root.geometry("450x450")
    CompanySearchScreen(root, companies).pack(side="top", fill="both", expand=True)
    root.mainloop()
