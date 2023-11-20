from django.shortcuts import render
from PyDictionary import PyDictionary


def index(request):
    return render(request, 'index.html')


def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    context = {
        'meaning': meaning['Noun'][0],
        'synonyms': synonyms if synonyms else ['None'],
    }
    return render(request, 'word.html', context)
