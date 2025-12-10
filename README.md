# Ex.04 Design a Website for Server Side Processing
## Date:10.12.2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
math.html

<html>
<head>
    <title>Mileage of Vehicle</title>
    <style>
        body 
        {
            background-color: rgb(31, 208, 208)
        }
        .id1 
        {
            text-align: center;
            color: rgb(30, 0, 255);
        }
        .box 
        {
            text-align: center;
            width: 40%;
            background-color: rgb(181, 113, 24);
            border: solid 6px rgb(31, 29, 31);
            padding: 25px;
            margin: 60px auto;
        }
        .result 
        {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1 class="id1"><u>The Mileage Calculator</u></h1>
    <div class="box">
        
        <form method="post">
            {% csrf_token %}
            <label>Distance Travelled (km)</label><br>
            <input type="number" name="distance"><br><br>

            <label>Liters Consumed (L)</label><br>
            <input type="number" name="liters"><br><br>

            <button type="submit">Calculate</button>
        </form>

        <div class="result">
            
                Mileage: {{ mileage }} km/L
            
        </div>
    </div>
    <footer style="text-align: center; color: rgb(139, 95, 0); font-size: xx-large;">
        
        E.Vamsi Krishna (25005454)
    </footer>
</body>
</html>

views.py

from django.shortcuts import render

def mileage(request):
    km = int(request.POST.get('distance', 0))
    l = int(request.POST.get('liters', 0))

    mileage = km / l if request.method == 'POST' and l != 0 else 0

    print("kilometer=", km)
    print("liter=", l)
    print("mileage=", mileage)

    return render(request, 'mathapp/math.html', {'km': km, 'l': l, 'mileage': mileage})

urls.py

"""
URL configuration for vamsi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('', views.mileage, name='mileage'),
]
```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2025-12-10 201621.png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2025-12-10 201718.png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
