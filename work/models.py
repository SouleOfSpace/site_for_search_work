from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    STATUS_CHOISE = (
        ('active', 'Active'),
        ('inactivate', 'Inactivate'),
    )

    # ссылка на работу
    link = models.URLField(unique=True)
    title = models.CharField(max_length=300)    #
    specialization =  models.CharField(max_length=40, blank=True)  # специализация
    level = models.CharField(max_length=40, blank=True)            # уровень работы
    experience = models.CharField(max_length=40, blank=True)       # опыт
    level_english = models.CharField(max_length=40, blank=True)    # уровень английского
    salary = models.CharField(max_length=40, blank=True)           # зарплата
    city = models.CharField(max_length=40, blank=True)              # город
    mode_work = models.CharField(max_length=40, blank=True)        # режим работы
    size_team = models.CharField(max_length=20, blank=True)        # размер команды
    size_company = models.IntegerField()     # размер компании
    talework = models.BooleanField(default=None)         # удаленная работа
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='work_post')  # агент
    tags = TaggableManager()             # теги работы
    description = models.TextField(blank=True)      # описание

    slug = models.SlugField(max_length=300, unique_for_date='publish')
    publish = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOISE, default='active')


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        '''pass'''
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    #pass
    def get_absolute_url(self):
        return reverse('work:post_detail', args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug,
                                                 self.id])

class Newswork(models.Model):
    '''pass'''
    STATUS_CHOISE = (
        ('active', 'Active'),
        ('inactivate', 'Inactivate'),
    )

    # post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='newsworks')
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_posts')  # агент
    title = models.CharField(max_length=100)
    body = models.TextField()
    tags = TaggableManager(blank=True)  # теги работы

    slug = models.SlugField(max_length=300, unique_for_date='publish')
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOISE, default='active')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        '''pass'''
        if not self.slug:
            self.slug = slugify(self.title)
        super(Newswork, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('work:news_detail', args=[self.slug,
                                                 self.id])

class Resume(models.Model):
    STATUS_CHOISE = (
        ('active', 'Active'),
        ('inactivate', 'Inactivate'),
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='work_post')
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=9)
    description = models.TextField(blank=True)
    publish = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=300, unique_for_date='publish')
    status = models.CharField(max_length=20, choices=STATUS_CHOISE, default='active')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return 'Resume  number {} by {}.'.format(self.id, self.email)

    def save(self, *args, **kwargs):
        '''pass'''
        if not self.slug:
            self.slug = slugify('{}-{}'.format(self.first_name, self.last_name))
            # self.slug = slugify('{}_{}'.format(self.first_name,self.last_name))
        super(Resume, self).save(*args, **kwargs)


