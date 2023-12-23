from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Goods)
admin.site.register(Feedback)
admin.site.register(Rating)
admin.site.register(Promo)
admin.site.register(Meditation)
admin.site.register(Basket)
admin.site.register(Order)