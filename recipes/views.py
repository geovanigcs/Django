from django.shortcuts import render

# HTTP REQUEST
def home(request):
    return render(request, 'home.html')

# urlpatterns = [('admin/', admin.site.urls),
#     path('', home), #Home
#     path('sobre/', sobre), #/sobre/
#     path('contato/', contato) #/contato/
# ]