from django.shortcuts import render
from django.views import generic
from googletrans import Translator

def home_view(request):
    if request.method == 'POST':
        if request.POST['my_textarea'] == "" or request.POST['my_textarea'] is None:
            return render(request,'index.html')
        else:
            original_text =request.POST['my_textarea']
        print(original_text)
        translator = Translator()
        output = translator.translate(original_text, dest='en')
        print (str(output.text.lower()))
        if str(output.text.lower()) == original_text.lower():
            return render(request, 'index.html',{
                                                'output_text':'Sorry, no translation available',
                                                'original_text':original_text})

        return render(request, 'index.html',{
                                            'output_text':output.text,
                                            'original_text':original_text})
    else:
        return render(request,'index.html')
