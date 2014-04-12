from django.utils.translation import ugettext_lazy as _
#from ipres.forms import IpaddressForm
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse

class Student:
	def __init__(self,name,age):
		self.name =name 
		self.age = age





def ipaddress(request):
     import pdb
#     pdb.set_trace()
     s1 = Student('john',88)
     s2 = Student('pikk',99)
     l1 = [s1,s2]
     hello="hellooooooooooooooo"
     return render_to_response('index.html', locals())
    
