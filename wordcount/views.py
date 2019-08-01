
# Function for setting up the home page

# This allows us to return the string on homepage
from django.http import HttpResponse
from django.shortcuts import render
import operator

# Functions that handle the page you see online
def homepage(request):
    return render(request, 'home.html',)

# Explains what the website is about
def about(request):
    return render(request, 'about.html',)

# deals with counting of words your type into textbox
def count(request):
    fulltext = request.GET['fulltext']

# Counting the words on the string
    word_list = fulltext.split()
    # Counting the word that appears the most
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    sorted_words = sorted(word_dictionary.items(), key = operator.itemgetter(1),reverse=True)
    # Returns info to the html page
    return render(request, 'count.html',{'fulltext':fulltext, 'length':len(word_list),'sorted_words':sorted_words})
