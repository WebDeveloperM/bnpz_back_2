from django.contrib import admin
from django.contrib.auth.models import User, Group
from bnpz.models import *

# Register your models here.

# admin.site.unregister(User)
# admin.site.unregister(Group)

admin.site.register(Video)

    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('number', 'language', 'name', 'marka', 'document', 'world_standart', 'date')
    list_filter = ['name']
   

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('number', 'language', 'question', 'answer')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('language', 'title', 'date', 'view')
    list_filter = ['title']
    fields = ('language', 'title', 'img_1', 'img_2', 'img_3', 'img_4', 'img_5', 'img_6', 'img_7', 'img_8', 'img_9')


@admin.register(CategoryNew)
class CategoryNewAdmin(admin.ModelAdmin):
    list_display = ['title_uz']
    list_filter = ['title_uz']
    fields = ('title_uz', 'title_kr', 'title_ru', 'title_en')


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('number', 'category', 'language', 'title', 'date', 'is_active')
    list_filter = ['number', 'category']
    fields = ('number',
              'language', 'category', 'title', 'mainImage', 'description_1', 'description_2', 'img_1', 'description_3',
              'img_2', 'description_4', 'img_3',
              'description_5', 'img_4', 'img_5', 'is_active')
    

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('number', 'language', 'title', 'date', 'is_active')
    list_filter = ['number']
    fields = ('number',
              'language', 'title', 'mainImage', 'description_1', 'description_2', 'img_1', 'description_3',
              'img_2', 'description_4', 'img_3',
              'description_5', 'img_4', 'img_5', 'is_active')


@admin.register(CategoryTender)
class CategoryTenderAdmin(admin.ModelAdmin):
    list_display = ['title_uz']
    list_filter = ['title_uz']
    fields = ('title_uz', 'title_kr', 'title_ru', 'title_en')


@admin.register(Selection)
class SelectionAdmin(admin.ModelAdmin):
    list_display = ('number', 'category', 'language', 'service', 'is_active')
    list_filter = ['number', 'category']
    fields = ('number', 'category', 'language', 'service', 'condition', 'term', 'phone', 'is_active')


@admin.register(SelectionProduct)
class SelectionProductAdmin(admin.ModelAdmin):
    list_display = ('language', 'title', 'count', 'is_active')
    list_filter = ['selection']
    fields = ('selection', 'language', 'title', 'file', 'count', 'is_active')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'address', 'bthDate', 'phone', 'email', 'date', 'is_active')
    list_filter = ['is_active']


admin.site.register(Language)
admin.site.register(SmsCode)
admin.site.register(Eskiz)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('number', 'language', 'title', 'link')
    list_filter = ['language']


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('language', 'title', 'subtitle')
    list_filter = ['language']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['number', 'language', 'title', 'subtitle']
    list_filter = ['language']


@admin.register(LocalDocs)
class LocalDocsAdmin(admin.ModelAdmin):
    list_display = ['title', 'file']
    list_filter = ['title', 'file']


admin.site.register(Lider)
admin.site.register(Captcha)
admin.site.register(Politica)
admin.site.register(Story)
admin.site.register(Test)