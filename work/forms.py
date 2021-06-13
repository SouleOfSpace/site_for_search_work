from .models import Post, Newswork, Resume
from django import forms

class PostForm(forms.ModelForm):
    '''pass'''
    tags = forms.CharField(max_length=400)
    class Meta:
        model = Post
        fields = ('link', 'title', 'specialization', 'level', 'experience', 'level_english',
                  'salary', 'city', 'mode_work', 'size_team', 'size_company',
                  'talework', 'description', 'status')

class SearchForm(forms.Form):
    '''pass'''
    query = forms.CharField(max_length=20)

class AdvencedSearchForm(forms.Form):
    '''pass'''
    choices_special = (('', 'Не важно'),
                       ('.NET / C #', '.NET / C #'),
                       ('Android', 'Android'),
                       ('Architect', 'Architect'),
                       ('Business Analysis', 'Business Analysis'),
                       ('C-level', 'C-level'),
                       ('C/C++', 'C/C++'),
                       ('DBA', 'DBA'),
                       ('Data Science', 'Data Science'),
                       ('DevOps/Sysadmin', 'DevOps/Sysadmin'),
                       ('Front-end/JS', 'Front-end/JS'),
                       ('Gamedev', 'Gamedev'),
                       ('Golang', 'Golang'),
                       ('Java', 'Java'),
                       ('Marketing/PR', 'Marketing/PR'),
                       ('Node.js', 'Node.js'),
                       ('Other', 'Other'),
                       ('PHP', 'PHP'),
                       ('Product Manager', 'Product Manager'),
                       ('Python', 'Python'),
                       ('QA Automation', 'QA Automation'),
                       ('QA Manual', 'QA Manual'),
                       ('Recruiting/HR', 'Recruiting/HR'),
                       ('Ruby/Rails', 'Ruby/Rails'),
                       ('Sales', 'Sales'),
                       ('Salesforce', 'Salesforce'),
                       ('Scala', 'Scala'),
                       ('Support', 'Support'),
                       ('Team/Tech Lead', 'Team/Tech Lead'),
                       ('Technical Writer', 'Technical Writer'),
                       ('UX/Design', 'UX/Design'),
                       ('iOS', 'iOS'))
    choices_level =(('', 'Не важно'),
                   ('Intern', 'Intern'),
                   ('Junior', 'Junior'),
                   ('Middle', 'Middle'),
                   ('Senior', 'Senior',),
                   ('Team Lead', 'Team lead'))
    choices_experience = (('', 'Не важно'),
                        ('Без опыта', 'Без опыта'),
                        ('год', 'С опытом'))
    choices_level_english = (('', 'Любой'),
                           ('Не важно', 'Без уровня'),
                           ('Beginner', 'Beginner'),
                           ('Elementary', 'Elementary'),
                           ('Pre-Intermediate', 'Pre-Intermediate'),
                           ('Intermediate', 'Intermediate'),
                           ('Upper-Intermediate', 'Upper-Intermediate'),
                           ('Advanced', 'Advanced'),
                           ('Proficiency', 'Proficiency'))
    choices_city = (('', 'Не важно'),
                     ('Минск', 'Минск'),
                     ('Могилев', 'Могилев'),
                     ('Витебск', 'Витебск'),
                     ('Гомель', 'Гомель'),
                     ('Гродно', 'Гродно'),
                     ('Брест', 'Брест'),
                     ('Солигорск', 'Солигорск'),
                     ('Барановичи', 'Барановичи'),
                     ('Бобруйск', 'Бобруйск'),
                     ('Полоцк', 'Полоцк'),
                     ('Орша', 'Орша'),
                     ('Слуцк', 'Слуцк'),
                     ('Молодечно', 'Молодечно'),
                     ('Борисов', 'Борисов'),
                     ('Клецк', 'Клецк'))
    choices_mode_work = (('', 'Не важно'),
                       ('Полный день', 'Полный рабочий день'),
                       ('Неполный день', 'Неполный рабочий день'))
    choices_salary = (('', 'Не важно'),
                      ('$', 'Указана'))
    choices_size_company = (('None', 'Не важно'),
                            ('0,40', '0 - 40'),
                            ('40,100', '40 - 100'),
                            ('100,700', '100 - 700'),
                            ('700,1400', '700 - 1400'),
                            ('1400,2100', '1400 - 2100'),
                            ('2100,2800', '2100 - 2800'))

    title = forms.CharField(max_length=20,required=False)  #
    specialization = forms.ChoiceField(choices=choices_special, required=False)  # специализация
    level = forms.ChoiceField(choices=choices_level, required=False)  # уровень работы
    experience = forms.ChoiceField(choices=choices_experience, required=False)  # опыт
    level_english = forms.ChoiceField(choices=choices_level_english, required=False)  # уровень английского
    salary = forms.ChoiceField(choices=choices_salary, required=False)  # зарплата
    city = forms.ChoiceField(choices=choices_city, required=False) # город
    mode_work = forms.ChoiceField(choices=choices_mode_work, required=False)  # режим работы
    size_company = forms.ChoiceField(choices=choices_size_company, required=False) # размер компании

    talework = forms.BooleanField(required=False)  # удаленная работа

class ResumeForm(forms.ModelForm):
    '''pass'''
    class Meta:
        model = Resume
        fields = ('first_name', 'last_name', 'email', 'phone', 'description')
