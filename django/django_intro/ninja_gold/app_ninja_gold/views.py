from django.shortcuts import render, redirect
from datetime import datetime
from pytz import timezone
import random, pytz

# Create your views here.
def main(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'transactions' not in request.session:
        request.session['transactions'] = []
    if (request.session['gold'] >= 100):
        request.session.flush()
        return render(request, 'game_clear.html')

    return render(request, 'main.html')

def process_money(request, location):
    dateTimeObj = datetime.now(tz=pytz.utc)
    dateTimeObj = dateTimeObj.astimezone(timezone('US/Central'))
    timestampStr = dateTimeObj.strftime("%Y/%m/%d (%I:%M:%S %p)")
    
    if location == 'farm':
        money = rand(10,20)
        transaction = "Earned {} golds from the {} ({})".format(money, location, timestampStr)
    elif location == 'cave':
        money = rand(5,10)
        transaction = "Earned {} golds from the {} ({})".format(money, location, timestampStr)
    elif location == 'house':
        money = rand(2,5)
        transaction = "Earned {} golds from the {} ({})".format(money, location, timestampStr)
    else:
        money = rand(-50,50)
        if (money >= 0):
            transaction = "Earned {} golds from the {} ({})".format(money, location, timestampStr)
        else:
            transaction = "Lost {} golds from the {} ({})".format(money*-1, location, timestampStr)
    
    request.session['transactions'].append(transaction)
    request.session['counter'] += 1
    request.session['gold'] += money
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')

def rand(min, max):
    num = random.randint(min, max)
    return num

# def process_money_cave(request):
#     if 'cave' not in request.session:
#         request.session['cave'] = ""
#     dateTimeObj = datetime.now()
#     timestampStr = dateTimeObj.strftime("%Y/%m/%d (%H:%M:%S)")
#     money = rand(5,10)
#     request.session['cave'] += "Earned {} golds from the cave! ({}) / ".format(money, timestampStr)
#     request.session['counter'] += 1
#     request.session['gold'] += money
#     return redirect('/')

# def process_money_house(request):
#     if 'house' not in request.session:
#         request.session['house'] = ""
#     dateTimeObj = datetime.now()
#     timestampStr = dateTimeObj.strftime("%Y/%m/%d (%H:%M:%S)")
#     money = rand(2,5)
#     request.session['house'] += "Earned {} golds from the house! ({}) / ".format(money, timestampStr)
#     request.session['counter'] += 1
#     request.session['gold'] += money
#     return redirect('/')

# def process_money_casino(request):
#     if 'casino' not in request.session:
#         request.session['casino'] = ""
#     dateTimeObj = datetime.now()
#     timestampStr = dateTimeObj.strftime("%Y/%m/%d (%H:%M:%S)")
#     money = rand(-50,50)
#     if (money >= 0):
#         request.session['casino'] += "Earned {} golds from the casino! ({}) / ".format(money, timestampStr)
#     else:
#         request.session['casino'] += "Lost {} golds at the casino! ({}) / ".format(money, timestampStr)
#     request.session['counter'] += 1
#     request.session['gold'] += money
#     return redirect('/')

