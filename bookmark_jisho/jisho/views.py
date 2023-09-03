from django.shortcuts import render
from django.http import HttpResponse
from jisho_api.word import Word

# Create your views here.
def home(request):
    return HttpResponse('test')

def search(request, query):
    try:
        results = Word.request(query)
        context = { 'query': query, 'count': 0, 'words': [] }  # words is list of dicts
        for word in results:
            sense_list = []
            for sense in word.senses:
                sense_list.append({
                    'sense_def': sense.english_definitions,
                    'sense_pos': sense.parts_of_speech
                })
            word_dict = {
                'slug': word.slug,
                'jp_word': word.japanese[0].word,
                'jp_read': word.japanese[0].reading,
                'senses': sense_list
            }
            context['words'].append(word_dict)
            context['count'] += 1
        context['words'].reverse()
        return render(request, 'jisho/search.html', context)
    except:
        return render(request, 'jisho/search.html', {'query': query, 'count': 0, 'words': None})
