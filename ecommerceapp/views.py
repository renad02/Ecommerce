from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse,JsonResponse
from .models import storetype,items,itemsdetails,cart
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login ,authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,LoginUserForm
# Create your views here.

def index(request):
    
    template=loader.get_template('index.html')
    return HttpResponse(template.render({'request':request}))     # {'request':request} ارسلها لصفحة البيس عشان اقدر استخدم الركويست



def listitems(request):
     p=items.objects.filter(st_id=2)              # st_id=2 عشان فقط تجيب لي الملابس
     template=loader.get_template('listitems.html')
     return HttpResponse(template.render({'items':p,'request':request}))


def detials(request,id):               # صفحة تأخذ رقم المنتج عشان تعرض تفاصيل المنتج 
      
      template=loader.get_template('details.html')
      data=itemsdetails.objects.select_related('items').filter(id=id).first()             # يجيب الداتا من جدول ايتم ديتيلز , اذا شيلت فيرست يرجعها على شكل اوبجيكت ف راح اكتب فيرست عشان يرجع سجل واحد
      data.total=data.qty*data.items.price                                              # total = qty * price     العمليات الحسابيه تسويها في الباك ايند مو الفرونت 
      return HttpResponse(template.render({'data':data,'request':request}))


def care(request):
     c=items.objects.filter(st_id=4)                      # st_id=4 جدول العناية
     template=loader.get_template('care.html')
     return HttpResponse(template.render({'items':c,'request':request}))


def caredetials(request,id):                
      
      template=loader.get_template('care_items_details.html')
      data=itemsdetails.objects.select_related('items').filter(id=id).first()             
      data.total=data.qty*data.items.price                                              
      return HttpResponse(template.render({'data':data,'request':request}))



@login_required(login_url='/auth_login/')  
def checkout(request):
      template=loader.get_template('checkout.html')
      return HttpResponse(template.render({'request':request}))


@csrf_exempt
def add_to_cart(request):                   # اضافه للسله
     id=request.POST.get("id")
     p=cart(itmesid=id)                # cart is the name of table in models and itmesid is the variable
     p.save()
     row=cart.objects.all()
     count=0                         # عدد الشراء
     for item in row:
          count=count+1   
     request.session["cart"]=count             #  يعرض الرقم اللي فوق السله
     return JsonResponse({'count':count})       # ترجع قيمة الكاونت للفنكشن في الجافاسكربت


@csrf_exempt
def auth_login(request):
     form=LoginUserForm()
     if request.method=="POST":
          form=LoginUserForm(data=request.POST)
          if form.is_valid():
              username=form.cleaned_data['username']
              password=form.cleaned_data['password']
              print(username)

              user=authenticate(username=username,password=password)
              if user:
                   if user.is_active:
                        login(request,user)
                        return render(request,'checkout.html')
     context={'form':form}
     return render(request,'auth_login.html',context)

          
@csrf_exempt
def auth_register(request):
     template=loader.get_template('auth_register.html')
     form=CreateUserForm()
     if request.method=="POST":
          form=CreateUserForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('auth_login')
          context={'registerform':form}
          return HttpResponse(template.render(context=context))
     
     



    
    