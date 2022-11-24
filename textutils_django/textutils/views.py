from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get("text", "default")
    print(djtext)

    removepunc = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    newlineremover = request.POST.get("newlineremover", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    charactercounter = request.POST.get("charactercounter", "off")

    if (removepunc == "on"):
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {
            "purpose": "Removed punctuations", "analyzed_text": analyzed,
        }
        djtext = analyzed

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {
            "purpose": "Change to Uppercase", "analyzed_text": analyzed,
        }
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {
            "purpose": "Removed new line", "analyzed_text": analyzed,
        }
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {
            "purpose": "Removed extra space", "analyzed_text": analyzed,
        }
        djtext = analyzed

    if (charactercounter == "on"):
        analyzed = 0
        for char in djtext:
            analyzed += 1
        params = {
            "purpose": "Character counter", "analyzed_text": analyzed,
        }

    if (removepunc != "on") and (fullcaps != "on") and (newlineremover != "on") and (extraspaceremover != "on") and (
            charactercounter != "on"):
        return HttpResponse("Sorry you didn't select any options!!!")

    return render(request, "analyze.html", params)


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")
