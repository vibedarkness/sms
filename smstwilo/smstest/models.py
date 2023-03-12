from django.db import models
import os
from twilio.rest import Client

# Create your models here.


class Score(models.Model):
    resultat=models.PositiveIntegerField()


    def __str__(self):
        return str(self.resultat)

        
    def save(self, *args, **kwargs):
        if self.resultat < 800:
            account_sid = "AC9f2ab4cd8bfc02faf81504153c0240af"
            auth_token = "c03f23145833dcf4d66797b82de385e7"
            client = Client(account_sid, auth_token)
            message = client.messages.create(
            body="bonjour oumar votre resultat est {self.resultat}",
            from_="+15747013851",
            to="+221786351787"
            )
            print(message.sid)
            
        return super().save(*args, **kwargs) # Call the real save() method

