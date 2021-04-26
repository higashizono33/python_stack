from django.shortcuts import render, redirect
from datetime import datetime
from pytz import timezone
import random, pytz

def main(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'transactions' not in request.session:
        request.session['transactions'] = []
    win = False
    if request.session['gold'] >= 100:
        win = True
        return render(request, 'result.html', {'win': win})
    if request.session['counter'] >= 7:
        if request.session['gold'] >= 100:
            win = True
        return render(request, 'result.html', {'win': win})
    return render(request, 'main.html')

def rand(min, max):
    num = random.randint(min, max)
    return num

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

