#from classes import *
from main_page import *
from company_class import *


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


if __name__ == '__main__':
    root = Tk()
    root.title("GUI на Python")
    root.geometry("600x520")
    add_company(root)
