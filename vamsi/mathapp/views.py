from django.shortcuts import render

def mileage(request):
    km = int(request.POST.get('distance', 0))
    l = int(request.POST.get('liters', 0))

    mileage = km / l if request.method == 'POST' and l != 0 else 0

    print("kilometer=", km)
    print("liter=", l)
    print("mileage=", mileage)

    return render(request, 'mathapp/math.html', {'km': km, 'l': l, 'mileage': mileage})