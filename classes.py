import sys
from tkinter import *
sys.path.insert(0, 'W:/university/2_course/ISP_2')


class Person:
    def __init__(self, first_name, last_name, country, industry, education, skills = None, summary = None, headline = None,
                 contacts = None, current_job = None, jobs = None, certificates = None, publication = None):
        self.name = first_name
        self.last_name = last_name
        self.country = country
        self.education = education
        self.industry = industry
        if skills is not None:
            self.skills = skills
        else:
            self.skills = None

        if headline is not None:
            self.headline = headline
        else:
            self.headline = None

        if summary is not None:
            self.summary = summary
        else:
            self.summary = None

        if contacts is not None:
            self.contacts = contacts
        else:
            self.contacts = None

        if current_job is not None:
            self.current_job = current_job
        else:
            self.current_job = None

        if certificates is not None:
            self.certificates = certificates
        else:
            self.certificates = None

        if jobs is not None:
            self.jobs = jobs
        else:
            self.jobs = None

        if publication is not None:
            self.publication = publication
        else:
            self.publication = None


    '''
    Полные профильные поля
    Поля для контактной информации
    Поля компании
    Поля публикации
    Патентные поля
    Поля языка
    Поля навыков
    Поля сертификации
    Поля для курсов
    Поля образования
    Волонтерские поля

    '''


    def __str__(self):
        return 'Person: %s, %s, industry %s,headline %s,education %s,\nskills %s,current job %s, %s, %s, %s]' % (self.name, self.last_name,
                                                            self.industry, self.headline, self.education,
                                                            self.skills, self.current_job, self.jobs, self.contacts,
                                                            self.certificates)

class Company:
    def __init__(self, name, industry, company_size, company_type,  website = None):
        self.name = name
        self.industry = industry
        self.company_size = company_size
        self.company_type = company_type
        if website is not None:
            self.website = website

    def __str__(self):
        return 'Company: [%s, %s, %s, %s]' % (self.name, self.industry, self.company_type, self.company_size)

#jango = Person("Jango", "fett", "")

person = Person("Grievous", "Sheelal", "Kali", "warlord", "higest academy of handsome military leaders",
                skills = ["Multihand figthing", 'jedi killing', 'Spinning'], summary = 'Looking for jeji kilkilng job',
                headline='victory or death',  contacts = ['emperrorBestStudent@empire.com'], current_job = "Robo", jobs = ["Killer", 'Jedi Killer'],
                certificates = ['cat healer courses', 'master of making pancakes'],
                publication = ['ten ways to kill a jedi', 'why two is better then one'])
mol = Person("Mol", "Dart", "Irodonia", "Sith Lord", "School of anger and toxicity", summary = 'Looking for jeji kilkilng job', skills = None, headline = None,
                 contacts = None, current_job = None, jobs = None, certificates = None, publication = None)
dict = { "Grievous": person,
        "Mol" : mol}

'''
root = Tk()
root.title("GUI на Python")
root.geometry("450x450")
'''

