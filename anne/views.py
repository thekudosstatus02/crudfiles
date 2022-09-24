from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile,Subject,Unit,Topic
from django.contrib.auth.models import User
from .forms import ProfileForm,SubjectForm,UnitForm,TopicForm,LoginForm,SearchForm,SearchTopicForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# every function is mappped with a specific url 
# when user enter a url a function is called
# according the fun definition a new page will be directed with some information or the same page will be directed with some changes

# decorators used such that this page will be
# reached only user is ligged only otherwise it will direct to mentioned login page
@login_required(login_url='http://localhost:8000/user-login/')
def searchTopic(request):
    subject_id=request.GET['subject_id']
    subject=Subject.objects.get(id=subject_id)
    if request.method=='POST':
        form=SearchTopicForm(request.POST)
        name=form.data['topic_name']
        topics=[]
        for unit in subject.unit_set.all():
            for topic in unit.topic_set.all():
                if name.lower() in topic.topic_name.lower():
                   topics.append(topic)
        if topics==[]:
              return render(request,'anne/view_subject.html',{'subject':subject,'form':form,'msg':'topic not found...'})
        print(topics)
        return render(request,'anne/view_subject.html',{'subject':subject,'form':form,'topics':topics})

def searchTopicPublic(request):
    subject_id=request.GET['subject_id']
    subject=Subject.objects.get(id=subject_id)
    if request.method=='POST':
        form=SearchTopicForm(request.POST)
        name=form.data['topic_name']
        topics=[]
        for unit in subject.unit_set.all():
            for topic in unit.topic_set.all():
                if name.lower() in topic.topic_name.lower():
                   topics.append(topic)
        if topics==[]:
              return render(request,'anne/public_subject.html',{'subject':subject,'form':form,'msg':'topic not found...'})
        print(topics)
        return render(request,'anne/public_subject.html',{'subject':subject,'form':form,'topics':topics})

def publicSubject(request):
    subject_id=request.GET['subject_id']
    subject=Subject.objects.get(id=subject_id)
    form=SearchTopicForm()
    return render(request,'anne/public_subject.html',{'subject':subject,'form':form})

def publicProfile(request):
    user_id=request.GET['user_id']
    profile=Profile.objects.get(id=user_id)
    return render(request,'anne/public_profile.html',{'profile':profile})

# when we enter the name of teacher to be searched inside the form then the details filled will be passed inside the url
# using the request.POST method we will recieve all the details passed in url into the object named form 
def searchUser(request):
    if request.method=='POST': # this statement will run when we will search a user 
        form=SearchForm(request.POST)
        profile=Profile.objects.all() # all profiles inside the db
        users=[]
        print(users)
        for i in profile:
            if form.data['staff_name'].lower() in i.name.lower(): # if searched teacher exists or not
                users.append(i) # if teacher exists then just append in the list named users
                print(users)
        if len(users)==0: # if users list is empty then return the message no teacher/user found
            msg="!!! no user found !!!"
            return render(request,'anne/search.html',{'form':form,'msg':msg})
        print(users)
        return render(request,'anne/search.html',{'use_r':users,'form':form}) # return the list of searched users
    else: # this statement will run when no we just visit the page 
         print('ELSE inside searchUser')
         form=SearchForm()
         return render(request,'anne/search.html',{'form':form})

def signIn(request):
     if request.method=='POST': # when user filled the login form to validate himself/herself
        form=LoginForm(request.POST) # all the details filled inside the form are recieved in form object of LoginForm type
        if form.is_valid: # if form is valid 
            print(form,'is_valid')
            username=form.data['username']
            password=form.data['password']
            # authentication is being done to validate whether the user exists or not
            user=authenticate(username=username,password=password) 
            if user: # if user is authenticated 
                login(request,user) # session created for decorator
                try:
                   profile=Profile.objects.get(user=user) # loggedIn user profile is extracted from Profile_Lists 
                except:
                   profile=False
                # we are passing the profile details of user on private profile page    
                return render(request,'anne/view_profile.html',{'profile':profile})
            else: # if user is not authenticated
                form=LoginForm()
                msg="Either username or password is incorrect....TRY AGAIN !!!"
                res=render(request,'anne/user_login.html',{'form':form,'msg':msg})
                return res
     form=LoginForm() # when we just came to login form page
     res=render(request,'anne/user_login.html',{'form':form})
     return res

@login_required(login_url='http://localhost:8000/user-login/')
def addProfile(request):
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)

        if form.is_valid:
            profile=Profile()
            profile.name=form.data['name']
            profile.bio=form.data['bio']
            profile.dept=form.data['dept']
            profile.branch=form.data['branch']
            profile.guide=form.data['guide']
            return render(request,'anne/view_profile.html',{'profile':profile})
    else:
        form=ProfileForm()
    return render(request,'anne/add_profile.html',{'form':form})

@login_required(login_url='http://localhost:8000/user-login/')
def viewProfile(request):
    form=Profile.objects.all()
    return render(request,'anne/view_profile.html',{'form':form})

@login_required(login_url='http://localhost:8000/user-login/')
def updateProfile(request):
    if request.method=='POST':
        profile=Profile.objects.get(id=request.GET['profile_id'])
        form=ProfileForm(request.POST or None,request.FILES,instance=profile)
        form.save()
        return render(request,'anne/view_profile.html',{'profile':profile})

@login_required(login_url='http://localhost:8000/user-login/')
def editProfile(request):
    profile=Profile.objects.get(id=request.GET['profile_id'])
    profile_id=request.GET['profile_id']
    print(profile.id)
    fields={'id':profile.id,'dp':profile.dp,'name':profile.name,'bio':profile.bio,'education':profile.education,'branch':profile.branch,'dept':profile.dept,'guide':profile.guide,}
    form=ProfileForm(initial=fields)
    return render(request,'anne/edit_profile.html',{'form':form,'profile_id':profile_id})

@login_required(login_url='http://localhost:8000/user-login/')
def addSubjct(request):
    if request.method=='POST':
        form=SubjectForm(request.POST)
        if form.is_valid:
            subject=Subject()
            subject.subject_name=form.data['subject_name']
            subject.branch=form.data['branch']
            subject.year=form.data['year']
            profile=Profile.objects.get(id=request.GET['profile_id'])
            subject.profile=profile
            subject.save()
            return render(request,'anne/view_subject.html',{'subject':subject,'form':SearchTopicForm()})
    else:
        form=SubjectForm()
    return render(request,'anne/add_subject.html',{'form':form})

@login_required(login_url='http://localhost:8000/user-login/')
def updateSubject(request):
    if request.method=='POST':
        subject=Subject.objects.get(id=request.GET['subject_id'])
        form=SubjectForm(request.POST or None,instance=subject)
        if form.is_valid:
            form.save()
            return render(request,'anne/view_subject.html',{'subject':subject,'form':SearchTopicForm()})

@login_required(login_url='http://localhost:8000/user-login/')
def editSubject(request):
    subject=Subject.objects.get(id=request.GET['subject_id'])
    subject_id=request.GET['subject_id']
    fields={'subject_name':subject.subject_name,'branch':subject.branch,'year':subject.year}
    form=SubjectForm(initial=fields)
    return render(request,'anne/edit_subject.html',{'form':form,'subject_id':subject_id})

@login_required(login_url='http://localhost:8000/user-login/')
def addUnit(request):
    if request.method=='POST':
        form=UnitForm(request.POST)
        if form.is_valid:
            unit=Unit()
            unit.unit_name=form.data['unit_name']
            unit.unit_imp=form.data['unit_imp']
            subject=Subject.objects.get(id=request.GET['subject_id'])
            unit.unit_subject=subject
            unit.save()
            profile=unit.unit_subject.profile
            return render(request,'anne/view_subject.html',{'subject':subject,'form':SearchTopicForm()})
    else:
        form=UnitForm()
    return render(request,'anne/add_unit.html',{'form':form})

@login_required(login_url='http://localhost:8000/user-login/')
def updateUnit(request):
    if request.method=='POST':
        unit=Unit.objects.get(id=request.GET['unit_id'])
        form=UnitForm(request.POST or None,instance=unit)
        if form.is_valid:
            form.save()
            return render(request,'anne/view_subject.html',{'subject':unit.unit_subject,'form':SearchTopicForm()})

@login_required(login_url='http://localhost:8000/user-login/')
def editUnit(request):
    unit=Unit.objects.get(id=request.GET['unit_id'])
    unit_id=request.GET['unit_id']
    fields={'unit_name':unit.unit_name,'unit_imp':unit.unit_imp,}
    form=UnitForm(initial=fields)
    return render(request,'anne/edit_unit.html',{'form':form,'unit_id':unit_id})

@login_required(login_url='http://localhost:8000/user-login/')
def addTopic(request):
    if request.method=='POST':
        topic=Topic()
        topic.unit_topic=Unit.objects.get(id=request.GET['unit_id'])
        form=TopicForm(request.POST,request.FILES,instance=topic)
        if form.is_valid:
            form.save()
            subject=topic.unit_topic.unit_subject
            return render(request,'anne/view_subject.html',{'subject':subject,'form':SearchTopicForm()})
    else:
        form=TopicForm()
    return render(request,'anne/add_topic.html',{'form':form})

@login_required(login_url='http://localhost:8000/user-login/')
def updateTopic(request):
    if request.method=='POST':
        topic=Topic.objects.get(id=request.GET['topic_id'])
        form=TopicForm(request.POST or None,request.FILES,instance=topic)
        if form.is_valid:
            form.save()
            subject=topic.unit_topic.unit_subject
            form=SearchTopicForm()
            return render(request,'anne/view_subject.html',{'subject':subject,'form':form})

@login_required(login_url='http://localhost:8000/user-login/')
def editTopic(request):
    topic=Topic.objects.get(id=request.GET['topic_id'])
    topic_id=request.GET['topic_id']
    fields={'topic_name':topic.topic_name,'topic_weightage':topic.topic_weightage,'topic_link':topic.topic_link,'file':topic.file,}
    form=TopicForm(initial=fields)
    return render(request,'anne/edit_topic.html',{'form':form,'topic_id':topic_id})

@login_required(login_url='http://localhost:8000/user-login/')
def viewSubject(request):
    subject_id=request.GET['subject_id']
    subject=Subject.objects.get(id=subject_id)
    if request.method=='POST':
        form=SearchTopicForm(request.POST)
        name=form.data['topic_name']
        topics=[]
        for unit in subject.unit_set.all():
            for topic in unit.topic_set.all():
                if name.lower() in topic.topic_name.lower():
                   topics.append(topic)
        if topics==[]:
              return render(request,'anne/view_subject.html',{'subject':subject,'form':form,'msg':'topic not found...'})
        print(topics)
        return render(request,'anne/view_subject.html',{'subject':subject,'form':form,'topics':topics})
    else:
        form=SearchTopicForm()
        return render(request,'anne/view_subject.html',{'subject':subject,'form':form})


def About(request):
    return render(request,'anne/about.html')
