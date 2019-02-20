from django.contrib import admin
from reviews.models import ReviewsModel


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'text')


admin.site.register(ReviewsModel, ReviewsAdmin)
# Register your models here.
