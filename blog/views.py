import requests
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    list_bad = []
    response_bad=requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    for a in response_bad:
        if a['season'] not in list_bad:
            list_bad.append(a['season'])
    list_saul = []
    response_saul=requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    for a in response_saul:
        if a['season'] not in list_saul:
            list_saul.append(a['season'])

    return render(request,'home.html', {'list_bad':list_bad, 'list_saul':list_saul})

def breaking(request):
    list_bad = []
    response_bad=requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    for a in response_bad:
        if a['season'] not in list_bad:
            list_bad.append(a['season'])
    return render(request,'breaking.html',{'list_bad':list_bad})

def saul(request):
    list_saul = []
    response_saul=requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    for a in response_saul:
        if a['season'] not in list_saul:
            list_saul.append(a['season'])
    return render(request,'saul.html',{'list_saul':list_saul})

def season(request, pk):
    season = {}
    response=requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    for e in response:
        if int(e['season']) == int(pk) and e['title'] not in season:
            season[e['episode_id']] = e['title']
    return render(request,'season.html',{'season':season,'pk':pk})

def seasonbad(request, pk):
    seasonbad = {}
    response=requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    for e in response:
        if int(e['season']) == int(pk) and e['title'] not in seasonbad:
             seasonbad[e['episode_id']] = e['title']
    return render(request,'season.html',{'seasonbad':seasonbad,'pk':pk})

def episode(request, pk):
    episode_elements = {}
    pk = str(pk)
    URL ='https://tarea-1-breaking-bad.herokuapp.com/api/episodes/'+pk
    response3=requests.get(URL).json()
    print(type(response3))
    print(response3)
    for k in response3[0]:
        episode_elements[k] = response3[0][k]
        if k =="characters":
            characters = response3[0][k]
            
    return render(request,'episode.html',{'elements':episode_elements,'pk':pk,'characters':characters})

def character(request, pk):
    name = ""
    nickname = ""
    status = ""
    portrayed = ""
    ocupation = []

    char = {}
    quotes= []
    appearance =[]
    temp_saul = []
    nam = "+".join(pk.split(" "))

    URL ='https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+nam
    URL2 ='https://tarea-1-breaking-bad.herokuapp.com/api/quote?author='+nam
    response=requests.get(URL).json()
    response2=requests.get(URL2).json()


    for k in response[0]:
        if k == "appearance":
            appearance = response[0][k]
        if k == "better_call_saul_appearance":
            temp_saul = response[0][k]
        if k == "img":
            picture = response[0][k]
        if k =="name":
            name = response[0][k]
        if k =="nickname":
            nickname = response[0][k]
        if k =="occupation":
            occupation = response[0][k]
        if k =="status":
            status = response[0][k]
        if k == "portrayed":
            portrayed = response[0][k]

        char[k] = response[0][k]

    for k in response2:
        quotes.append(k['quote'])
      

    return render(request,'character.html',{'nickname':nickname,'name':name, 'occupation':occupation,'status': status, 'picture':picture,'portrayed':portrayed, 'appearance': appearance, 'temp_saul':temp_saul,'quotes':quotes})


def search(request):
    search_str =""
    search=[]

    if request.method == 'POST':
         search_input=request.POST['SearchInput']
         search_input = "+".join(search_input.split(" "))
    
    URL ='https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+search_input
    result=requests.get(URL).json()
    for i in result:
        for x in i:
            if x == "name":
                search.append(i['name'])   

    return render(request,'search.html',{'search': search})
