from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Forfait, Credit, Client, TotalCredit, TotalGeneral, RetraitCredit
from django.db.models import Sum

@receiver(post_save, sender=Forfait)
def calcul_credit(sender, instance, created, **kwargs):
 if created:
  client = instance.client
  forfait = instance.forfait
  calcul = forfait * 0.05
   
  Credit.objects.create(client=client, forfait=instance, credit=calcul)

@receiver(post_save, sender=Credit)
def update_total_credit_save(sender, instance, created, **kwargs):
    client = instance.client
    total_credit, created = TotalCredit.objects.get_or_create(client=client)
    total_credit.update_total_credit()

@receiver(post_save, sender=TotalCredit)
def update_total_credit_general(sender, instance, **kwargs):
    client = instance.client
    total_credit, created = TotalGeneral.objects.get_or_create()
    total_credit.update_total_general()

@receiver(post_save, sender=RetraitCredit)
def update_total_accorded(sender, instance, **kwargs):
    quantite, created = TotalGeneral.objects.get_or_create()
    quantite.update_total_accord_credit()

@receiver(post_delete, sender=Credit)
def update_total_credit_delete(sender, instance, **kwargs):
  pass

@receiver(post_delete, sender=TotalCredit)
def prevent_deletion(sender, instance, **kwargs):
  pass