from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)
    category = forms.ChoiceField(choices=[('general-questions', 'General Questions'), 
                                          ('sugestions-feedback', 'Sugestions & Feedback'),
                                          ('Propose a Project','Propose a Object'),
                                          ('colab-partner', 'Collaborations & partnerships')])
                                        