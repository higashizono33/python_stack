from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def survey(request):
    return render(request, "index.html")

def result_process(request):
    if request.method == "POST":
        request.session['name'] = request.POST["name"]
        request.session['loc'] = request.POST["loc"]
        request.session['lang'] = request.POST["lang"]
        request.session['sport'] = request.POST["sport"]
        request.session['sex'] = request.POST["sex"]
        request.session['comment'] = request.POST["comment"]
        return redirect('/result')
        # return render(request, "result.html", context)

def result(request):
    print('got here from redirect!')
    context = {
        "name": request.session['name'],
        "loc": request.session['loc'],
        "lang": request.session['lang'],
        "sport": request.session['sport'],
        "sex": request.session['sex'],
        "comment": request.session['comment'],
    }
    return render(request, 'result.html', context)