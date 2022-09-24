from django import forms
from .models import Profile,Subject,Unit,Topic

# here we are creating the forms to recieve the details of an object of a class 
# on saving the object it will add the object as a tuple inside the table

class ProfileForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields={'name','dp','bio','dept','branch','education','guide',}
        # widgets are used to apply the customize designing over the form 
        widgets={ 
        'name':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. The Weeknd'}),
        'bio':forms.TextInput(attrs={'class':'form-control','placeholder':'keep learning!!!'}),
        'dept':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. BTech/ BBA/ BA'}),
        'education':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. pheD in Maths or teaching from last 7 years.'}),
        'branch':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. CSE/IT/CIVIL'}),
        'guide':forms.Textarea(attrs={'class':'form-control','placeholder':"""Slow down-Don't rush into things. Let your life unfold. Wait a bit to see where it takes you, and take time to weigh your options. Enjoy every bite of food, take time to look around you, let the other person finish their side of the conversation. Allow yourself time to think, to mull a bit."""}),
        }

class SubjectForm(forms.ModelForm):

    class Meta:
        model=Subject
        fields={'subject_name','branch','year',}
        widgets={
        'subject_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Subject Name'}),
        'branch':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. Btech-CSE'}),
        'year':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. 2nd year/3rd sem'}),
        }

class UnitForm(forms.ModelForm):

    class Meta:
        model=Unit
        fields={'unit_name','unit_imp'}
        widgets={
        'unit_name':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. Python language'}),
        'unit_imp':forms.Textarea(attrs={'class':'form-control','placeholder':'unit important topics : e.g. topic1 ,topic2, topic3, topic4, topic5, topic6, topic7 topic8, topic9, topic10 and so on...'}),
        }


class TopicForm(forms.ModelForm):

    class Meta:
        model=Topic
        fields={'topic_name','topic_weightage','topic_link','file',}
        widgets={
        'topic_name':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. Python Functions'}),
        'topic_weightage':forms.Textarea(attrs={'class':'form-control','placeholder':'topic importance and weightage : e.g. this topic is generally being asked in examinations of about 7-8 marks as a direct question define and explain PYTHON Functions or give an example of Python Function.'}),
        }

class LoginForm(forms.Form):
    username=forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password=forms.CharField(label='',max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))

class SearchForm(forms.Form):
    staff_name=forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'search teacher'}))

class SearchTopicForm(forms.Form):
    topic_name=forms.CharField(label='',max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'search topic'}))
