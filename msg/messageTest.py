#from django.db import models
from msg.models import Message

testmessage = Message.objects.all()
for x in testmessage:
    print x.username