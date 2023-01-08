from django.core.mail import send_mail
from django.db import models
class Dht(models.Model):
    temp = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)
    def str(self):
        return "temperature= "+str(self.temp)

    def save(self, *args, **kwargs):
           if self.temp < 2:
                  # envoie du msg sur telegram
                  import telepot
                  token = '5820721206:AAEWQ8AYfDXPwq5aHcmfeWlp4N9cBj5IJ5I'
                  rece_id = 5227097810
                  bot = telepot.Bot(token)
                  bot.sendMessage(rece_id, 'depassement temp')
                  print(bot.sendMessage(rece_id, 'temperature severe .'))
                  # envoie du mail
                  send_mail(
                         'température dépasse la normale,' + str(self.temp),
                         'anomalie dans la machine',
                         'wiame.filali@ump.ac.ma',
                         ['wiamefilali014@gmail.com'],
                         fail_silently=False)
           return super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
           if self.temp >8:
                  # envoie du msg sur telegram
                  import telepot
                  token = '5947483565:AAFbcXU8YkATY2SwBZShVNf3BjDdr1k89TU'
                  rece_id = 5852743163
                  bot = telepot.Bot(token)
                  bot.sendMessage(rece_id, 'depassement temp')
                  print(bot.sendMessage(rece_id, 'temperature critique .'))
                  # envoie du mail
                  send_mail(
                         'température dépasse la normale,' + str(self.temp),
                         'anomalie dans la machine',
                         'wiame.filali@ump.ac.ma',
                         ['wiamefilali014@gmail.com'],
                         fail_silently=False)
           return super().save(*args, **kwargs)
