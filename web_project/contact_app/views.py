from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from contact_app.forms import Contact_forms

# Create views (controller)
def page_feedback(request):
    
    if request.method == 'POST':
        form_entry = Contact_forms(request.POST)
        print("Status: POST request received")

        if form_entry.is_valid():
            print("Status: form entry is valid")
            print('Feedback: ' + form_entry.cleaned_data['feedback'])
            print('Recommendation: ' + form_entry.cleaned_data['recommendation'])
            print('Email: ' + form_entry.cleaned_data['email'])

            # Show thank you page
            return HttpResponseRedirect('thanks')
    else:
        form_entry = Contact_forms()

    # Set Django template tag dictionary
    form_entry_tagdict = {'form_entry_key' : form_entry}
   
    return render(request, 'contact_app/page_feedback.html', context=form_entry_tagdict)

def page_tyfeedback(request):
    return render(request, 'contact_app/page_tyfeedback.html')