from django.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout , login, get_user_model
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from .models import Feedback
from django.views.decorators.csrf import csrf_exempt
 
@csrf_exempt

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables, RequestContext(request)
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 


 # this login required decorator is to not allow  any  
# view without authenticating
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )
      


@login_required
def post_feedback(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = FeedbackForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required 
            post = form.save(commit=False)
            username=form.cleaned_data['username'],
            phone_no=form.cleaned_data['phone_no'],
            neighbourhood=form.cleaned_data['neighbourhood'],
            rating=form.cleaned_data['rating'],
            comments =form.cleaned_data['comments']
            post.save()
            

            return HttpResponseRedirect('/post_list/')

        else:
            form = FeedbackForm()
            variables = RequestContext(request, {
    'form': form
    })
         
def post_list(request):
    posts = Post.objects.filter(username).order_by('username')
    return render(request, 'post_list.html', {'posts': posts})

