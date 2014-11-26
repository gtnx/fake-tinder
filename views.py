from django.shortcuts import render_to_response
from django.template import RequestContext

import os
import random

def home(request):
  directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static/tinder/profiles")
  filenames = ["tinder/profiles/%s" % fn for fn in os.listdir(directory) if fn.endswith(".jpg")]
  random.shuffle(filenames)
  image0 = filenames[0]
  image1 = filenames[1]
  images = filenames[2:]
  return render_to_response("tinder/home.html", locals(), RequestContext(request))
