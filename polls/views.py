from django.shortcuts import render
import requests

from . import forms


def index(request):
    return render(request, "polls/index.html")


def mo5(request):
    if request.method == "POST":
        form = forms.mo5Form(request.POST)
        if form.is_valid():
            print(form.cleaned_data["sentence"])

            value = form.cleaned_data["sentence"]
            headers = {'Agent-Token': 'ad845e37d2e07137fcea056f4cd5823d'}
            params = {"sentence": value}
            url = 'https://www.viky.ai/api/v1/agents/babybel/phonenumbers/interpret.json'

            response = requests.get(url, headers=headers, params=params).json()

            if len(response["interpretations"]) != 0:
                return render(request, "polls/mo5.html", {"value": value, "response": response, "interpretations": response["interpretations"][0]["solution"]})
            else:
                return render(request, "polls/mo5.html", {"value": value, "response": response, "interpretations": False})

        else:
            print("There was an invalid form")
            return render(request, "polls/mo5.html")
    else:
        return render(request, "polls/mo5.html")
