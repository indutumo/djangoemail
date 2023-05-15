from django.shortcuts import render
from .models import Customer
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string, get_template 
from django.shortcuts import render, redirect
from .forms import CustomForm

def index(request):
    return render(request,'emailapp/index.html')
    
def sendto_allcustomers(request):
    customers = Customer.objects.all()
    for customers in customers:
        print(customers.name)
        email_address = customers.email_address
        
        #subject = 'New Products'
        message = 'We have new products, check out our website'
        #email = send_mail(subject, message,'zolatechnologies@gmail.com',[email_address])
    
        subject = 'New Products'
        context = {'name': customers.name,'message': message}
        message = get_template('emailapp/email.html').render(context)
        email = EmailMessage(subject, message,"Zola Technologies Limited", [email_address])
        email.content_subtype = "html" 
        email.send()
    
    return redirect('index')


def sendto_activecustomers(request):
    customers = Customer.objects.filter(status='active')
    for customers in customers:
        print(customers.name)
        email_address = customers.email_address
        
        #subject = 'New Products'
        message = 'We have new products, check out our website'
        #email = send_mail(subject, message,'zolatechnologies@gmail.com',[email_address])
    
        subject = 'New Products'
        context = {'name': customers.name,'message': message}
        message = get_template('emailapp/email.html').render(context)
        email = EmailMessage(subject, message,"Zola Technologies Limited", [email_address])
        email.content_subtype = "html" 
        email.send()
    
    return redirect('index')


def sendto_inactivecustomers(request):
    customers = Customer.objects.filter(status='inactive')
    for customers in customers:
        print(customers.name)
        email_address = customers.email_address
        
        #subject = 'New Products'
        message = 'We have new products, check out our website'
        #email = send_mail(subject, message,'zolatechnologies@gmail.com',[email_address])
    
        subject = 'New Products'
        context = {'name': customers.name,'message': message}
        message = get_template('emailapp/email.html').render(context)
        email = EmailMessage(subject, message,"Zola Technologies Limited", [email_address])
        email.content_subtype = "html" 
        email.send()
    
    return redirect('index')


def custom_message(request):
    #getting information from the form
    if request.method == "POST":
        form = CustomForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            status = form.cleaned_data['status']
            subject = form.cleaned_data['subject']
            print(message)
            
            #sending  email    
            if status == 'all':
                customers = Customer.objects.all()
            else:
                customers = Customer.objects.filter(status=status)
            print(customers)    
            for customers in customers:
                print(customers.name)
                email_address = customers.email_address
                context = {'name': customers.name,'message': message}
                email_template = get_template('emailapp/email.html').render(context)
                email = EmailMessage(subject, email_template,"Zola Technologies Limited", [email_address])
                email.content_subtype = "html" 
                email.send()
            return redirect('custom_message')
        else:
            print(form.errors)
    return render(request,'emailapp/message.html')
    
'''   
def custom_message(request):
    #getting information from the form
    if request.method == "POST":
        form = CustomForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.cleaned_data['message']
            status = form.cleaned_data['status']
            subject = form.cleaned_data['subject']
            #function to send email    
            if status == 'all':
                customers_emails = Customer.objects.values_list('email_address', flat=True)
            else:
                customers_emails = Customer.objects.filter(status=status).values_list('email_address', flat=True)
                
            customers_emails = list(customers_emails)
            context = {'name': 'Customer','message': message}
            message = get_template('emailapp/email.html').render(context)
            email = EmailMessage(subject, message,"Zola Technologies Limited", customers_emails)
            email.content_subtype = "html" 
            email.send()
            return redirect('custom_message')
        else:
            print(form.errors)
            
    return render(request,'emailapp/message.html')
'''