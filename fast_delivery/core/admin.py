import random
import string
from django.contrib import admin, messages

from .models import *

def payout_to_courier(modeladmin, request, queryset):
    payout_items=[]
    transaction_querysets=[]

    # Step 1 - Get all the valid couriers in queryset
    for courier in queryset:
        if courier.paypal_email:
            courier_in_transactions=Transaction.objects.filter(job__courier=courier,status=Transaction.IN_STATUS)

        if courier_in_transactions:
            transaction_querysets.append(courier_in_transactions)
            balance=sum(i.amount for i in courier_in_transactions)
            payout_items.append({
                "recipient_type": "EMAIL",
                "amount": {
                    "value": '{:.2f}'.format(balance*0.8), # 80% of the balance
                    "currency": "USD"
                },
                "receiver": courier.paypal_email,
                "note": "Payment for courier Thank you",
                "sender_item_id": courier.id
            })
    # Step 2 - Send Payment batch + email in receivers
    # sender_batch_id = ''.join(random.choices(string.ascii_uppercase) for i in range(12))
    try:
        for t in transaction_querysets:
            t.update(status=Transaction.OUT_STATUS)
        messages.success(request,"payout created successfully")
    except Exception as e:
        messages.error(request,str(e))

    # Step 3 - Update the status of the transactions to 'OUT" if success



payout_to_courier.short_description = "Payout to courier"

class CourierAdmin(admin.ModelAdmin):
    list_display = ['user_full_name','paypal_email','balance']
    actions=[payout_to_courier]

    def user_full_name(self,obj):
        return obj.user.get_full_name()

    def balance(self,obj):
        return round(sum(t.amount for t in  Transaction.objects.filter(
            job__courier=obj,
            status=Transaction.IN_STATUS))*0.8,2)
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['stripe_payment_intent_id', 'courier_paypal_email', 'customer', 'courier', 'job', 'amount', 'status', 'created_at']
    list_filter = ['status',]

    def customer(self, obj):
        return obj.job.customer
    
    def courier(self, obj):
        return obj.job.courier
    
    def courier_paypal_email(self, obj):
        return obj.job.courier.paypal_email if obj.job.courier else None

# Register your models here.
admin.site.register(Customer)
admin.site.register(Courier, CourierAdmin)
admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Transaction, TransactionAdmin)