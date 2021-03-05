from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, "index.html")
    if request.method == "POST":
        print("a POST request is being made to this route")
        return redirect("/")

def result(request):
    if request.method == "POST":
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]
        val_from_field_three = request.POST["three"]
        val_from_field_four = request.POST["four"]
        val_from_field_five = request.POST["five"]
        val_from_field_six = request.POST["six"]
        context = {
            "val_one": val_from_field_one,
            "val_two": val_from_field_two,
            "val_three": val_from_field_three,
            "val_four": val_from_field_four,
            "val_five": val_from_field_five,
            "val_six": val_from_field_six,
        }
        return render(request, "result.html", context)