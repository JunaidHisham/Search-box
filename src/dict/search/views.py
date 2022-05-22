# from django.shortcuts import render

# from search.models import Word, WordMeaning

# # Create your views here.


# def index(request):
#     # dictionary_words = {
#     #     "bird": "a warm-blooded egg-laying vertebrate animal distinguished by the possession of feathers, wings, a beak, and typically by being able to fly.",
#     #     "loyal": "giving or showing firm and constant support or allegiance to a person or institution.",
#     #     "happy": "feeling or showing pleasure or contentment.",
#     #     "apple": "the round fruit of a tree of the rose family, which typically has thin green or red skin and crisp flesh.",
#     #     "cartoon": "a simple drawing showing the features of its subjects in a humorously exaggerated way, especially a satirical one in a newspaper or magazine.",
#     # }
#     if request.method == "POST":
#         search_word = request.POST.get('search_word')
        
#         search_word = search_word.lower()

#         word_meaning = WordMeaning.objects.all()

#         if Word.objects.filter(word = search_word).exists():

#             if search_word in word_meaning.word :

#                 context = {
#                     "searchword": word_meaning.meaning,
#                     "word": search_word,
#                     "show": True,
#                 }
#                 return render(request, "index.html", context)
#             else:
#                 context = {
#                     "error": "!!! No Such Word Found !!!",
#                     "word": "",
#                     "show": True,
#                     "dict_words":'',
#                     "dict_key":'dict_key',
#                 }
#                 return render(request, "index.html", context)
#     else:
#         context = {
#             "searchword": "",
#             "word": "",
#             "show": False,

#         }

#     return render(request, "index.html", context)



# def create_word(request):
#     if request.method == "POST":
#         word = request.POST.get('word')
#         meaning = request.POST.get('word_meaning')
#         # priority = request.POST.get('')

#         if not Word.objects.filter(word=word).exists():
#             new_word = Word.objects.create(word=word)
#         else:
#             new_word = Word.objects.create(word=word)

#         WordMeaning.objects.create(
#             word= new_word,
#             meaning=meaning,
#             synonyms=synonyms
#         )
        

#         print(word)
#         print(synonyms)
#         print(meaning)


#     context = {}

#     return render(request, "addword.html", context)