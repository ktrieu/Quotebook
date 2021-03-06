from django.contrib import admin
from app.models import Quote, SubmittedQuote
from django.core.mail import send_mail
from django.template.loader import render_to_string

def approve_quote(modeladmin, request, queryset):
    for submitted_quote in queryset:
        new_quote = Quote()
        new_quote.quote = submitted_quote.quote
        new_quote.attribution = submitted_quote.attribution
        new_quote.save()
        #send a notification email
        if submitted_quote.submitter_email != '':
            send_approve_email(submitted_quote.submitter_email, new_quote.pk)
        submitted_quote.delete()

def send_approve_email(to_email, quote_id):
   html = render_to_string('app/approve_email.html', {'quote_url' : 'www.quotebook.me/' + str(quote_id)})
   email = send_mail('Your quote has been approved', 'Your quote has been approved. See it at www.quotebook.me/' + str(quote_id),
                    'no-reply@quotebook.me', [to_email], html_message=html)

class QuoteAdmin(admin.ModelAdmin):
    search_fields = ('quote', 'attribution', 'rating', 'num_ratings')

class SubmittedQuoteAdmin(admin.ModelAdmin):
    actions=[approve_quote]

admin.site.register(Quote, QuoteAdmin)
admin.site.register(SubmittedQuote, SubmittedQuoteAdmin)