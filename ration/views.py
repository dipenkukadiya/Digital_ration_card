from django.shortcuts import render ,redirect
from django import template
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from .models import registerdb ,logindb , familydb ,rationdb ,pricedb , pricebpl ,feedbackdb, tokondb
import json 
from django.db.models.functions import Concat
from django.contrib import messages
from django.core.mail import send_mail
from datetime import date
import random
from twilio.rest import Client
from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests
#from.models import current_token

# Create your views here
take_t = 1000
tok = 0
list_t = [0,]
adcard = 0

head=[]
link=[]
rno=[]

def tokon_home(request):

    price = pricedb.objects.all().order_by("-id")[0]
    return render(request, 'user_ration.html', {'price':price})


def user_tokon(request):
    global take_t
    global rno
    global adcard
    if (adcard in rno):
        print(adcard+'\n')
        print(rno)
        return render(request, 'home.html', {"take_t" : 0, 'link':link, 'head':head})
    else:
        take_t = take_t + 1 
        #link, head = news_p()
        #k=tokondb.objects.filter(tokon_num=take_t)
        #if k is False:
        p=""
        list_t.append(take_t)
        adharno = request.POST.get('aadharnoo')


        for c in range(1, 8):
            
            product = request.POST.get('product' + str(c))
            weight = request.POST.get('weight' + str(c))
            price = request.POST.get('price' + str(c))
            serial = request.POST.get('serial' + str(c))

            bill = request.POST['bill']
            #datee = request.POST['datee']

            if serial == "":
                print('no ......... nmnmn..z')
                return render(request, 'home.html',{"take_t" : take_t})
            
            p=p+serial+'):'+product+ ','+weight+'kg'+','+price+'rs'+'\n'
            
            print(serial)
            print(product)
            print(price)      
            
            tokon_db = tokondb(product=product, weight=weight,
                                price=price, serial=serial, tokon_num=take_t, adharno=adharno)

            tokon_db.save()    
        p=p+'your total bill is :'+str(bill)+'\n'+'aadhaar no:'+str( adharno)+'\n'+'your token is:'+str(take_t)
        tw(p)
        return render(request, 'home.html', {"take_t" : take_t, 'link':link, 'head':head})


def take_tok(request):
    global take_t
    global tok
    global aadhaarcard
    global rationcardno
    global adcard  
    global rno
    print("#################################################################################")
    print(rno)

    if (adcard in rno):
        data = {"token" : "wait for next month"}  #tokondb me adharno ka , already hy dekha?
        return JsonResponse(data) 
    else:
        #rno.append(adcard)
        take_t = take_t + 1
        list_t.append(take_t)
        print(list_t)
        data = {
            "token" : take_t
        }
        return JsonResponse(data)


def update_tok(request):
    global tok
    global adcard
    print(tok)

    try:
        data = {
            'tok' : list_t[tok]
        }

        if tok == '' or None:
            return JsonResponse(data)
        else:
            return JsonResponse(data)
    except:
        data = {
            'tok': list_t[0]
        }
        return JsonResponse(data)


def index(request):
    return render(request,'test.html')  #login submit me jaa

def validee(aadha):
    #aadha = request.POST['aadharnoo']
    if (familydb.objects.filter(aadhaar=aadha).exists()==True):  
        r=familydb.objects.get(aadhaar=aadha)
        temp=r.uid
        r = registerdb.objects.get(id=temp)
        print(r.emailid)
        return True, r.emailid
    elif (registerdb.objects.filter(aadharcard=aadha).exists()==True):
        r = registerdb.objects.get(aadharcard=aadha)
        print(r.emailid)
        return True, r.emailid
    else:
        print("not existed......")
        return False, False
    #return render(request,'ration.html')  
    #send_mail(
    #'One time password',
   # 'write otp and veryfied your aadaharcard := 1234',
    #'trykuchbhi@gmail.com',
   # ['jesavaliya2511@gmail.com'],
    #'fail_silently=False')

def deal_home(request):
    links, head = news_p()
    price = pricedb.objects.all().order_by("-id")[0]
    bplprice = pricebpl.objects.all().order_by("-id")[0]
    return render(request, 'deal_home.html', {'price': price, 'bprice': bplprice, 'link': link, 'head': head})

def home(request):
    price = pricedb.objects.all().order_by("-id")[0]
    bplprice = pricebpl.objects.all().order_by("-id")[0] 
    return render(request ,'home.html',{'price' : price  , 'bprice':bplprice, 'link':link, 'head':head })


def feedback(request):
    return render(request ,'feedback.html')
#####################no erorr abhi bhi le raha tokon, dekha nhi? samne to kiya

def news_p():
    URL = "https://www.ndtv.com/"
    header = {
        'Host': 'www.ndtv.com',
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    response = requests.get(URL, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")

    a = soup.find('div', {"class": "featured_cont"}).find('ul').find_all('li')
    news = []
    links = []

    p = 0

    for i in a:
        try:
            p = p + 1
            if p>3:
                result = i.find('a', {"class": "item-title"})
                links.append(result['href'])
                news.append(result.get_text())
        except:
            pass
    print(news)
    return news, links


def register_submit(request):
    if 'rationbooktype' in request.POST :
        rationbooktype = request.POST['rationbooktype']
    else :
        rationbooktype= False
    
    if 'sel' in request.POST :
        sel = request.POST['sel']
    else :
        sel = 0

    if 'income' in request.POST :
        income = request.POST['income']
    else :
         income = False

    if 'gas' in request.POST :
        gas = request.POST['gas']
    else :
        gas= False
    if 'electricity' in request.POST :
        electricity = request.POST['electricity']
    else :
        electricity = False


    userselection = request.POST['userselection']   
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    emailid = request.POST["emailid"]
    dob = request.POST["dob"]
    contactno = request.POST["contactno"]
    state = request.POST["state"]
    district = request.POST["district"]
    taluka = request.POST["taluka"]
    city = request.POST["city"]
    pincode = request.POST["pincode"]
    address = request.POST["address"]
    aadharcard = request.POST["aadharcard"]
    passbook = request.POST["passbook"]
    residential = request.POST["residential"]
    cast = request.POST["cast"]
    bank = request.POST["bank"]
    password= request.POST["password"]

    try:
        shopno= request.POST["shopno"]
        shopaddress= request.POST["shopaddress"]
    except MultiValueDictKeyError:
        shopno = 0 
        shopaddress = False
    try:
        uid = registerdb.objects.all().order_by("-id")[0]
        uid=uid.id+1
    except:
        uid= 1


    for x in range(1, int(sel)+1):
        ds = json.loads(request.POST["family_"+ str(x)])
        aadhaar=ds["aadhaar"]
        f_name=ds["f_name"]
        age=ds["age"]
        gender=ds["gender"]
        relation=ds["relation"]
    
        
        family_db = familydb(aadhaar = aadhaar ,f_name = f_name , age= age, gender = gender , relation = relation, uid=uid)
        family_db.save()

    register_db = registerdb(userselection=userselection,firstname=firstname,lastname=lastname,
                            emailid = emailid , dob = dob,contactno= contactno,state= state,district=  district,
                            taluka=taluka,city=city,pincode=pincode, address=address,shopno=shopno,shopaddress=shopaddress, aadharcard = aadharcard,
                            rationbooktype=rationbooktype,sel=sel,passbook=passbook,income=income,residential=residential,
                            cast= cast,bank=bank,gas=gas,electricity=electricity,password=password)
    register_db.save()
    return render(request, 'test.html')    



def login_submit(request):
    global adcard  
    global rationcardno
    global licenseno
    global head, link
    global rno
    ##oyyy ye kya not defined esa kyu aa f
    head, link = news_p()
    rationcardno = request.POST["rationcardno"]
    emailidd = request.POST["emailidd"]
    licenseno= request.POST["licenseno"]
    print(licenseno)
    passwordd= request.POST["passwordd"]

    price = pricedb.objects.all().order_by("-id")[0]
    bplprice = pricebpl.objects.all().order_by("-id")[0] 

    if licenseno is '':
        username = request.POST["rationcardno"]
        password = request.POST["passwordd"]
        register = registerdb.objects.filter(id=rationcardno)
        tik=0

        #current_token = current_token.filter(token=) #home.html ope
        tok
        print(register)
        for k in register:
            print(k.id)
            if str(username) == str(k.id) and str(passwordd) == str(k.password) :
                if k.credential=='true':
                    #print(price.date)
                    #print("hehjhjelo")
                    adcard = k.aadharcard 
                    #rno.append(adcard)
                    
                    tdb=tokondb.objects.filter(adharno=k.aadharcard) 
                    if(tdb.exists()):
                        adcard = tdb
                        tik=tdb[0].tokon_num
                        b=True
                        print(tik)
                        return render(request, 'home.html', {'price' : price  , 'bprice':bplprice,'ch':b, 'take_t':tik, 'link':link, 'head':head})
            
                    return render(request, 'home.html', {'price' : price  , 'bprice':bplprice, 'take_t':tik, 'link':link, 'head':head})
                else:
                    messages.error(request,'wrong credential')
                    print("credential pending")
                    print(k.credential)
                    return render(request, 'test.html',{'cre': k.credential})
            else:
                return render(request, 'test.html',{'cre': "hello"})
                    
    if rationcardno == '':
        username = request.POST["licenseno"]
        password = request.POST["passwordd"]
        register = registerdb.objects.filter(id=licenseno)
        print("dealer")
        for k in register:
            print(k.id)
            if str(username) == str(k.id) and str(passwordd) == str(k.password):
                if k.credential=='true':
                    #print(price.date)
                    #print("hehjhjelo")
                    return render(request, 'deal_home.html ',{'price' : price , 'bprice':bplprice, 'link':link, 'head':head})
                else:
                    messages.error(request,'wrong credential')
                    print("credential pending")
                    print(k.credential)
                    return render(request, 'test.html',{'cre': k.credential})      
            else:
                messages.error(request,'wrong credential')
                print("credential pending")
                print(k.credential)
                return render(request, 'test.html',{'cre': "hello"})

    return render(request, 'test.html',{'cre': "both"})  


def profile(request):
    if licenseno == '':
        register = registerdb.objects.get(id=rationcardno)
    else:
        register = registerdb.objects.get(id=licenseno)
    fam = familydb.objects.filter(uid = rationcardno)
    return render(request , 'profile.html', {'fam' : fam ,'register' : register})


def ration_next(request):
    global tok
    se = request.POST.get("nam",)
    tok = tok+1
    price = pricedb.objects.all().order_by("-id")[0]
    print(list_t)
    try:
        print(list_t[tok])
        register = tokondb.objects.filter(tokon_num=list_t[tok])
        for r in register:
            print(r.product)
            print(r.weight)
            print(r.price)
            print(r.tokon_num)

        print(register[0].weight)
        return render(request, 'ration.html', {'register' : register, 'price':price})
    except:
        return render(request, 'ration.html', {'finish': "NO ANOTHER TOKEN...!"})


def ration_submit(request):
    global re
    print(licenseno)
    if licenseno != '':
        global aadhaarcard
        aadhaarcard = request.POST['aadharnoo']

        serial = request.POST['serial1']
        print(serial)

        today = date.today()
        da = today.strftime("%d/%m/%Y")
        '''
        if (registerdb.objects.filter(aadharcard=aadhaarcard).exists()==True):
            r=registerdb.objects.filter(aadharcard=aadhaarcard)
            temp=r.aadaharcard
            r = registerdb.objects.get(id=temp)
        '''

        # aadhaarcard= request.POST['aadharnoo']
        # aadharnoo = request.POST['aadharnoo']

        if (familydb.objects.filter(aadhaar=aadhaarcard).exists() == True):
            h = familydb.objects.get(aadhaar=aadhaarcard)
            dd = h.uid
            print(dd)
        else:
            h = registerdb.objects.get(aadharcard=aadhaarcard)
            dd = h.id
            print(dd)

        for c in range(1, 8):
            #aadhaarcard = request.POST['aadharnoo']
            if (familydb.objects.filter(aadhaar=aadhaarcard).exists() == True):
                h = familydb.objects.get(aadhaar=aadhaarcard)
                dd = h.uid
                print(dd)
            else:
                h = registerdb.objects.get(aadharcard=aadhaarcard)
                dd = h.id
                print(dd)

                # aadharnoo = request.POST['aadharnoo']
            #datee = request.POST.get('da', False);
            otp = '0000'#request.POST['otp']
            product = request.POST['product' + str(c)]
            weight = request.POST['weight' + str(c)]
            price = request.POST['price' + str(c)]
            serial = request.POST['serial' + str(c)]
            bill = request.POST['bill']
            #datee = request.POST['datee']

            if serial == "":
                print('no ......... nmnmn..z')
                return render(request, 'ration.html')

            print(serial)
            print(product)
            print(price)

            ration_db = rationdb(aadharnoo=aadhaarcard, datee=da, otp=otp, product=product, weight=weight,
                                 price=price, serial=serial, bill=bill, rationn=dd)
            ration_db.save()
        return render(request, 'ration.html')
    else:
        return render(request, 'home.html')


def ration(request):
    if licenseno!='':
        return render(request ,'ration.html')
    else:
        price = pricedb.objects.all().order_by("-id")[0]
        bplprice = pricebpl.objects.all().order_by("-id")[0] 
        return render(request, 'home.html',{'price' : price , 'bprice':bplprice, 'cre':"aa"})


def ration_record(request):
    print(rationcardno)
    if rationcardno!="" or '':
      
        hist = rationdb.objects.filter(rationn = rationcardno).order_by('datee')
       
        for i in hist:
            print(i.datee)  

        return render(request ,'ration_record.html',{'hist' : hist})  
    else:
        price = pricedb.objects.all().order_by("-id")[0]
        bplprice = pricebpl.objects.all().order_by("-id")[0] 
        return render(request, 'home.html',{'price' : price , 'bprice':bplprice, 'cre':"aaa"})

def feedback_sub(request):
    complain = request.POST["complain"]
    ee = request.POST["ee"]
    feedback_db =feedbackdb(complain=complain,ee=ee)
    feedback_db.save()
    return render(request,'feedback.html',{'cre':"g"})


def  tw(bd):
    account_sid = 'AC467df994d5cb27d3be8cd13a1812fc59'
    auth_token = 'dca5ba9f09deb291239768aa3dfc5ecd' 
    client = Client(account_sid,auth_token)
    messages = client.messages.create(
        body=bd,
        from_='+12058593606',
        to='+917016306728')
    print(messages.sid)
