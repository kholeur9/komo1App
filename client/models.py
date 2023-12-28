from django.db import models

# Create your models here.
class Client(models.Model):
 id = models.AutoField(primary_key=True)
 numero = models.CharField(max_length=9, unique=True)

 class Meta:
   ordering = ['id']
  
 def credit(self):
   credits = Credit.objects.filter(client=self)
   total = sum(credit.credit for credit in credits)
   return total

 def __str__(self):
  return f"{self.id} - {self.numero}"

class Forfait(models.Model):
 client = models.ForeignKey(Client, on_delete=models.CASCADE)
 forfait = models.IntegerField(default=0)
 date = models.DateTimeField(blank=False, null=False)

 def __str__(self):
  return f"{self.client.numero} - Montant du forfait:{self.forfait} - Date: {self.date}"

class Credit(models.Model):
 client = models.ForeignKey(Client, on_delete=models.CASCADE)
 forfait = models.ForeignKey(Forfait, on_delete=models.CASCADE)
 credit = models.IntegerField(default=0)
 date = models.DateTimeField(auto_now_add=True)

 def __str__(self):
  return f"{self.client.numero} - Montant du fofait: {self.forfait.forfait} - Crédit obtenu: {self.credit} - Date: {self.date}"

class TotalCredit(models.Model):
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  total_credit = models.IntegerField(default=0)

  class Meta:
    ordering = ['client']
  
  def __str__(self):
    return f"{self.client} - Total credit: {self.total_credit}"

  def update_total_credit(self):
    credits = Credit.objects.filter(client=self.client)
    total = sum(credit.credit for credit in credits)
    self.total_credit = total
    self.save()

  def get_total_credit(self):
    return self.client.credit()


class TotalGeneral(models.Model):
  total_general = models.IntegerField(default=0)
  total_accord_credit = models.IntegerField(default=0)
  
  def __str__(self):
    return f"Total general des crédits : {self.total_general}"

  def update_total_general(self):
    total_credits = TotalCredit.objects.all()
    total = sum(credit.total_credit for credit in total_credits)
    self.total_general = total
    self.save()

  def update_total_accord_credit(self):
    total_quantite = RetraitCredit.objects.all()
    total = sum(retrait.quantite for retrait in total_quantite)
    self.total_accord_credit = total
    self.save()


class RetraitCredit(models.Model):
  en_attente = 'En attente'
  approuvé = 'Approuvé'
  rejete = 'Rejeté'

  STATUS_CHOICES = (
    (en_attente, 'En attente'),
    (approuvé, 'Approuvé'),
    (rejete, 'Rejeté'),
  )
  
  total_credit = models.ForeignKey(TotalCredit, on_delete=models.SET_NULL, null=True)
  quantite = models.IntegerField(default=0)
  data_forfait = models.IntegerField(default=0)
  data_mo = models.CharField(max_length=1000, default='0 Mo', blank=True, null=True)
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=en_attente, blank=True, null=True)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.total_credit.client} - Quantité retiré: {self.quantite} - Forfait obtenu: {self.data_forfait} Mo - Date: {self.date}"