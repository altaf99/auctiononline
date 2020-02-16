from django.contrib import admin
from .models import User, Product, Auction, Chat, Watchlist, Bid

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(Chat)
admin.site.register(Watchlist)
admin.site.register(Bid)