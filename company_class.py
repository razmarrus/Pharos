class Company:
    def __init__(self, name, founder, country, industry, company_size, website=None, vacancy=None):
        self.name = name
        self.founder = founder
        self.industry = industry
        self.company_size = company_size
        self.country = country

        if website is not None:
            self.website = website
        else:
            self.website = None

        if vacancy is not None:
            self.vacancy = vacancy
        else:
            self.vacancy = {}

    def __str__(self):
        return 'Company: [%s, founder %s, %s, %s, %s, \nvacancy %s, %s]' % (self.name, self.founder
                                                               ,self.industry, self.country,
                                                               self.company_size, self.vacancy, self.website)

    def add_vacancy(self, vacancy):
        self.vacancy.update({vacancy.position: vacancy})


class Vacancy:
    def __init__(self, position, requirements, city, company, salary, skills, candidates=None):
        self.position = position
        self.city = city
        #self.requirements = requirements
        self.salary = salary
        self.company = company
        self.skills = skills
        self.requirements = requirements
        if candidates is not None:
            self.candidates = candidates
        else:
            self.candidates = None

    def __str__(self):
        return 'Vacancy: [%s, %s, %s, %s, %s, %s, %s]' % (self.position, self.city, self.company, self.skills,
                                                          self.requirements, self.salary, self.candidates)

    def add_candidate(self, candidate):
        buffer = candidate.name + candidate.last_name
        self.candidates.update({buffer: candidate})

#position, requirements, city, company, salary, skills
OpenAI = Company("OpenAI", "Ilon Musk", "USA", "Artificial Intelligence", '500', 'openai.com' )

Senior_SE = Vacancy("Senior Software Engineer", "These roles do not require machine learning background, though you should be interested in the field.",
                    'San Francisco', 'OpenAI','40000$', ['production services', 'Unix shell', 'system working',
                                                         'machine learning', '', ''], candidates=None)

ML_Engi = Vacancy("Machine Learning Engineer", 'The Machine Learning Engineer role is responsible for building AI systems that can perform previously impossible tasks or achieve unprecedented levels of performance. '
                  , 'San Francisco', 'OpenAI','40000$', ['machine learning', 'programming skills', 'AI safety', '', '', ''])


#print(OpenAI)
OpenAI.add_vacancy(Senior_SE)
OpenAI.add_vacancy(ML_Engi)
#print("\n",OpenAI)
#print("\n",OpenAI.vacancy)

Blizzard = Company('Blizzard', 'nia', 'USA', 'Computer Games', '4700', 'blizzard.com')
#companies = {Blizzard.name: Blizzard,
#             OpenAI.name: OpenAI}
companies = {}
#print(companies['OpenAI'].vacancy['Senior Software Engineer'])
