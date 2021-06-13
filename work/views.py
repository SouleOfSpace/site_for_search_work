from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Post, Newswork
from .forms import PostForm, SearchForm, ResumeForm, AdvencedSearchForm

from utils import parser_dev_by, searcher
from taggit.models import Tag

from  django.contrib import messages

# Create your views here.

def post_list(request, tag_slug=None):
    '''pass'''
    posts = Post.objects.filter(status='active')
    news = Newswork.objects.filter(status='active')
    tags = Tag.objects.all()

    form = SearchForm()
    query = None
    messages.success(request, request.GET)

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            posts = posts.filter(title__icontains=query)

    paginator = Paginator(posts, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'work/post/list.html', {'page_obj': page_obj, 'tag': tag, 'tags': tags,
                                                   'form_search': form, 'query': query, 'news': news})

def post_list_by_search(request):
    '''pass'''
    form = AdvencedSearchForm()
    posts = None

    if request.method == 'POST':
        form = AdvencedSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data
            posts = Post.objects.filter(title__icontains=query['title'],
                                        specialization__icontains=query['specialization'],
                                        level__icontains=query['level'],
                                        experience__icontains=query['experience'],
                                        level_english__icontains=query['level_english'],
                                        salary__icontains=query['salary'],
                                        city__icontains=query['city'],
                                        mode_work__icontains=query['mode_work'],
                                        talework=query['talework']
                                        )
            if query['size_company'] != 'None':
                posts = posts.filter(size_company__in=range(int(query['size_company'].split(',')[0]),int(query['size_company'].split(',')[1])))

        form = AdvencedSearchForm()
        return render(request, 'work/post/search.html', {'form_adv': form, 'posts': posts, 'status': 'Not valid'})

    return render(request, 'work/post/search.html', {'form_adv': form, 'posts': posts})

def post_detail(request, year, month, day, post, post_id):
    '''pass'''
    post = get_object_or_404(Post, slug=post, status='active', publish__year=year,
                             publish__month=month, publish__day=day, id=post_id)
    return render(request, 'work/post/detail.html', {'post': post})

@login_required(login_url='http://127.0.0.1:8000/works/')
def create_post(request):
    '''pass'''
    status = 'creating'
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            cd = post_form.cleaned_data
            tags = searcher.Searcher().get_destroed_requests(cd['tags'])

            new_post = post_form.save(commit=False)
            new_post.agent = request.user
            new_post.save()
            status = 'ready'

            post = Post.objects.first()
            for tag in tags:
                post.tags.add(tag.strip())

            return render(request, 'work/post/create.html', {'post_form': post_form, 'status': status})
    else:
        post_form = PostForm()
    return render(request, 'work/post/create.html', {'post_form': post_form, 'status': status})

@login_required(login_url='http://127.0.0.1:8000/works/')
def create_auto_post(request):
    '''pass'''
    status = 'Вакансии не обновлены'
    parser = parser_dev_by.ParserDevBy()
    links = parser.get_links()
    inf_agent = 'Не добавлены новые пользователи'

    for link in links:
        try:
            info = parser.get_info_work(url=link)
            info['link'] = link

            if len(User.objects.filter(email=info['Агент']['email'])):

                user = User.objects.get(email=info['Агент']['email'])
                inf_agent = 'Найдены пользователи'
            else:
                user = User.objects.create_user(username=info['Агент']['username'],
                                                password='admin',
                                                email=info['Агент']['email'],
                                                first_name=info['Агент']['first_name'],
                                                last_name=info['Агент']['last_name']
                                                )
                inf_agent = 'Добавлены новые пользователи'

            post = Post(
                link = info['link'],
                title = info['Название'][8:],
                specialization= info['Специализация'],
                level= info['Уровень'],
                experience= info['Опыт'],
                level_english= info['Уровень английского'],
                salary= info['Зарплата'],
                city= info['Город'],
                mode_work= info['Режим работы'],
                size_team= info['Размер команды'],
                size_company= int(info['Размер компании']),
                talework= info['Возможна удалённая работа'],
                # agent= info['Агент'],
                agent= user,
                description= info['Описание'],
                status= 'active')
            post.save(True)

            for tag in info['Тэги']:
                post.tags.add(tag)
            status = 'Вакансии обновлены'
            # break #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        except:
            status = 'Обновление прервано'
            continue
    #
    #
    return render(request, 'work/post/test.html', {'status': status, 'agent': inf_agent})

#--------------------Work_News-----------------------------------------
def newswork_detail(request, news, news_id):
    newswork = get_object_or_404(Newswork, slug=news, status='active', id=news_id)
    return render(request, 'work/newswork/detail.html', {'newswork': newswork,})
#----------------------------------------------------------------------

#--------------------Resume Work---------------------------------------
def create_resume(request, post_id):
    '''pass'''
    status = 'creating'
    if request.method == "POST":
        resume_form = ResumeForm(request.POST)
        if resume_form.is_valid():
            resume_form = resume_form.save(commit=False)
            resume_form.post = get_object_or_404(Post, id=post_id, status='active')
            resume_form.save()
            status = 'ready'
    else:
        resume_form = ResumeForm()
    return render(request, 'work/resume/create.html', {'resume_form': resume_form, 'status': status})
