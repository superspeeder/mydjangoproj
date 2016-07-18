from django.shortcuts import render, redirect
from django.http import HttpResponse
import models

def index(request, indexn=0):
    contact = models.Contact.objects.get(pk=indexn)
    return HttpResponse('<h1>{fn} {ln}</h1><p><br><br>EMAIL: {e}<br>ADDRESS: {addr}<br>PHONE NUMBER: {pn} <br>BIRTHDAY: {bd}</p>'.format(fn=contact.fname, ln=contact.lname, e=contact.emailaddr, addr=contact.addr, bd=contact.birthday, pn=contact.phone_number))

def owner_contact(request):
    return index(request, 3)

def search(request, querytype, queryval):
    filtered_contacts = eval('models.Contact.objects.filter({qt}={qv})'.format(qt=querytype, qv=queryval))
    if len(filtered_contacts) == 1:
        return redirect('/book/index/{idx.pk}'.format(idx=filtered_contacts[0]))
    content = {'filtered_contacts' : filtered_contacts}
    return render(request, 'addressbook/search.html', content) 

def searchemail(request, queryval):
      filtered_contacts = eval('models.Contact.objects.filter(emailaddr={qv})'.format(qv=queryval))
      if len(filtered_contacts) == 1:
          return redirect('/book/index/{idx.pk}'.format(idx=filtered_contacts[0]))
      content = {'filtered_contacts' : filtered_contacts}
      return render(request, 'addressbook/search.html', content)

