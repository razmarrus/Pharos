import sys
import json
import pickle
import pymongo
from tkinter import *
sys.path.insert(0, 'W:/university/2_course/ISP_2')


class Person:
    def __init__(self, nickname, password, first_name, last_name, country, industry, education, skills=None,
                 summary=None, headline=None, contacts=None, current_job=None, jobs=None, certificates=None,
                 publication=None):
        self.name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.password = password
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

person = Person("nia","kawai","Grievous", "Sheelal", "Kali", "warlord", "higest academy of handsome military leaders",
                skills = ["Multihand fighting", 'jedi killing', 'Spinning', "", "", ""], summary = 'Looking for jedi killing job',
                headline='hello there, general Kenobi',  contacts = ['emperrorBestStudent@empire.com', ""],
                current_job = "general of droid army", jobs = ["Killer", 'Jedi Killer'],
                certificates = ['cat healer courses', 'master of making pancakes', "", "", "", ""],
                publication = ['ten ways to kill a jedi', 'why four is better then one', "", "", "", ""])
mol = Person('desy','sempai',"Mol", "Dart", "Irodonia", "Sith Lord", "School of anger and toxicity",
             summary = 'Looking for jeji kilkilng job', skills=["", "", "", "", "", ""], headline='',
                 contacts=['', ''], current_job='', jobs=['', ''], certificates = ["", "", "", "", "", ""],
             publication=["", "", "", "", "", ""])
#dict = {person.nickname: person, mol.nickname: mol}
dict = {}
#with open('dict.p', 'wb') as fp:
#    pickle.dump(dict, fp, protocol=pickle.HIGHEST_PROTOCOL)

#with open('dict.p', 'rb') as fp:
#    dict = pickle.load(fp)

#print(dict)
#for key, value in dict.items():  # Rows
#    print(value)


#with open('dict.json', 'w') as person_dict:
#    json.dump(dict, person_dict)

#with open('dict.json') as person_dict:
#    dict = json.load(person_dict)
'''
root = Tk()
root.title("GUI на Python")
root.geometry("450x450")
'''

