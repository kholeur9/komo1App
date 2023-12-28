from django.contrib import admin
from .models import Client, Forfait, Credit, TotalCredit, TotalGeneral, RetraitCredit

# Register your models here.
class ForfaitInline(admin.TabularInline):
 model = Forfait
 extra = 1
 
class CreditInline(admin.TabularInline):
 model = Credit
 extra = 1

class ClientAdmin(admin.ModelAdmin):
 inlines = [ForfaitInline, CreditInline]
 list_display = ('id', 'numero')

class RetraitCreditAdmin(admin.ModelAdmin):
  list_display = ('client_numero', 'quantite', 'data_forfait_short', 'date')

  def client_numero(self, obj):
    return obj.total_credit.client.numero
  client_numero.short_description = 'Client'

  def data_forfait_short(self, obj):
    return obj.data_forfait
  data_forfait_short.short_description = 'Data'

admin.site.register(Client, ClientAdmin)
admin.site.register(Forfait)
admin.site.register(Credit)
admin.site.register(TotalCredit)
admin.site.register(TotalGeneral)
admin.site.register(RetraitCredit, RetraitCreditAdmin)