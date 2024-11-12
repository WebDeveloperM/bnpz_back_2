from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from bnpz.back.serializers import *
from bnpz.message import code, result
from bnpz.send_code import send_code, refresh_token, check_phone
from bnpz.models import SmsCode, LocalDocs
from datetime import date


class Home(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        return Response({"message" : "Okdaaa"})


# Create your views here.
class CategoryNewApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        category = CategoryNew.objects.all()
        serializer = CategoryNewSerializer(category, many=True)
        return Response(serializer.data)


class NewApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        lang = kwargs['lang']

        news = New.objects.filter(is_active=True, language__title=lang).order_by("-date")[:4]
        serializer = NewSerializer(news, many=True)

        # for Archive tender
        selections = Selection.objects.all()
        for selection in selections:
            if selection.term < date.today():
                selection.is_active = False
                selection.save()

        return Response(serializer.data)


class NewByCategoryApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        id = kwargs.get('id')
        lang = kwargs['lang']
        if not id:
            return Response({"error": "Id not found"}, status=status.HTTP_400_BAD_REQUEST)

        if id == "all":
            news = New.objects.filter(language__title=lang).order_by('-date')
            serializer = NewSerializer(news, many=True)
            return Response(serializer.data)
        try:
            news = New.objects.filter(category__id=id, language__title=lang).order_by('-date')
        except:
            return Response({"error": "Category not found"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = NewSerializer(news, many=True)
        return Response(serializer.data)
    

class GenderApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        lang = kwargs['lang']

        try:
            news = Gender.objects.filter(language__title=lang).order_by('-date')
        except:
            return Response({"error": "Category not found"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = GenderSerializer(news, many=True)
        return Response(serializer.data)


class GenderDetailApiView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        id = kwargs.get('id')
        lang = kwargs.get('lang')

        if not id:
            return Response({"error": "Id not found"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            new = Gender.objects.filter(number=id, language__title=lang).last()
            new.view += 1
            new.save()
        except:
            return Response({"error": "Id bo'yicha ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = GenderSerializer(new)
        return Response(serializer.data)
    

class NewDetailApiView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):

        id = kwargs.get('id')

        if not id:
            return Response({"error": "Id not found"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            print(id, kwargs['lang'])
            new = New.objects.filter(number=id, language__title=kwargs['lang']).last()
            print(new, "888888888888888888")
            new.view += 1
            new.save()
        except:
            return Response({"error": "Id bo'yicha ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NewSerializer(new)
        return Response(serializer.data)


class VideoApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)


class ProductApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        lang = kwargs['lang']
        products = Product.objects.filter(language__title=lang)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class FAQApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        faqs = FAQ.objects.filter(language__title=kwargs['lang'])
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)


class GalleryApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        print(kwargs['lang'], "1111111111111111111111111")
        galleries = Gallery.objects.filter(language__title=kwargs['lang'])
        serializer = GallerySerializer(galleries, many=True)
        return Response(serializer.data)


class GalleryDetailApiView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        print(request.data, args, kwargs)
        id = kwargs.get('id')
        if not id:
            return Response({"error": "Id not found"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            gallery = Gallery.objects.get(id=id)
        except:
            return Response({"error": "Id bo'yicha ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        gallery.view += 1
        gallery.save()
        serializer = GallerySerializer(gallery)
        return Response(serializer.data)


class SelectionCategoryApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        category = CategoryTender.objects.all()
        serializer = CategoryTenderSerializer(category, many=True)
        return Response(serializer.data)


class SelectionApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        id = kwargs.get('id')
        lang = kwargs['lang']
        if not id:
            return Response({"error": "Id not found"}, status=status.HTTP_400_BAD_REQUEST)
        if id == "all":
            selections = Selection.objects.filter(language__title=lang, is_active=True).order_by("-date_add")
            serializer = SelectionSerializer(selections, many=True)
            return Response(serializer.data)
        try:
            selections = Selection.objects.filter(category__id=id, language__title=lang, is_active=True).order_by("-date_add")
        except:
            return Response({"error": "Id bo'yicha ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SelectionSerializer(selections, many=True)
        return Response(serializer.data)


class SelectionArchiveApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        id = kwargs.get('id')
        lang = kwargs['lang']
        if not id:
            return Response({"error": "Id not found"}, status=status.HTTP_400_BAD_REQUEST)
        print(id, lang, "--------------------")
        if id == "all":
            selections = Selection.objects.filter(language__title=lang, is_active=False).order_by("-date_add")
            print(selections, "111111111111111")
            serializer = SelectionSerializer(selections, many=True)
            return Response(serializer.data)
        try:
            selections = Selection.objects.filter(category__id=id, language__title=lang, is_active=False).order_by("-date_add")
        except:
            return Response({"error": "Id bo'yicha ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SelectionSerializer(selections, many=True)
        return Response(serializer.data)


class SelectionDetailApiView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        number = kwargs.get('id')
        if not id:
            return Response({"error": "Id not found"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            selection = Selection.objects.filter(number=number, language__title=kwargs['lang']).last()
            selection.view += 1
            selection.save()
            print(selection)
        except:
            return Response({"error": "Id bo'yicha ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SelectionSerializer(selection)
        return Response(serializer.data)


class SelectionProductApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        id = kwargs.get('id')
        if not id:
            return Response({"error": "Id not found"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            selections = SelectionProduct.objects.filter(selection__number=id, is_active=True,
                                                         language__title=kwargs['lang'])
        except:
            return Response({"error": "Id bo'yicha ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SelectionProductSerializer(selections, many=True)
        return Response(serializer.data)


class MessageApiView(APIView):
    @staticmethod
    def post(request):
        serializers = AddMessageSerializer(data=request.data)
        refresh_token()
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)


class MessageCheckApiView(APIView):
    @staticmethod
    def post(request):
        phone = request.data.get('phone')
        email = request.data.get('email')
        if not email or not phone:
            return Response({"error": "Email or Phone not found"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            message = Message.objects.filter(phone=phone, email=email).last()
        except:
            raise ValidationError({"error": "Email or Phone not found"})

        if not message:
            return Response({"message": "Murojaat topilmadi yoki ma'lumotlaringizni tekshiring"},
                            status=status.HTTP_400_BAD_REQUEST)
        if message.is_active:
            serializer = CheckMessageSerializer(message)
            if message.phone:
                check_phone(f"998{message.phone[7:].replace(' ', '')}", code)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Murojaat ko`rib chiqilyapdi"}, status=status.HTTP_400_BAD_REQUEST)


class MessageCheckPhoneApiView(APIView):
    @staticmethod
    def post(request):
        id = request.data.get('id')
        code = request.data.get('code')
        message = Message.objects.filter(id=id).last()
        sms_code = SmsCode.objects.filter(phone=f"998{message.phone[7:].replace(' ', '')}").last()
        if not sms_code or sms_code.code != code:
            raise ValidationError({"message": 'Verification code incorrect. Try again.'}, status.HTTP_400_BAD_REQUEST)
        serializer = CheckMessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SiteApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        lang = kwargs.get("lang")
        sites = Site.objects.filter(language__title=lang)
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)


class StatisticApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        lang = kwargs.get('lang')
        sites = Statistic.objects.filter(language__title=lang)
        serializer = StatisticSerializer(sites, many=True)
        return Response(serializer.data)


class CertificateApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        certificates = Certificate.objects.filter(language__title=kwargs['lang'])
        serializer = CertificateSerializer(certificates, many=True)
        return Response(serializer.data)


class CertificateDetailApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        certificates = Certificate.objects.filter(language__title=kwargs['lang'], number=kwargs['id']).last()
        serializer = CertificateSerializer(certificates)
        return Response(serializer.data)


class LocalApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        documents = LocalDocs.objects.all()
        serializer = LocalDocsSerializer(documents, many=True)
        return Response(serializer.data)


class LiderApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        liders = Lider.objects.filter(language__title=kwargs['lang'])
        serializer = LiderSerializer(liders, many=True)
        return Response(serializer.data)


class LiderDetailApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        lider = Lider.objects.filter(number=kwargs['id'], language__title=kwargs['lang']).last()
        serializer = LiderSerializer(lider)
        return Response(serializer.data)


class RepeatCodeApiView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        id = request.data.get('id')
        message = Message.objects.filter(id=id).last()
        check_phone(f"998{message.phone[7:].replace(' ', '')}", code)
        serializer = CheckMessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NullCodeApiView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        id = request.data.get('id')
        message = Message.objects.filter(id=id).last()
        sms = SmsCode.objects.filter(phone=f"998{message.phone[7:].replace(' ', '')}").last()
        sms.code = None
        sms.save()
        return Response({"message": "Ok"})
        
        
class AddCaptchaView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        print(request.data)
        captcha = request.data.get('captcha')
        shifr = request.data.get('shifr')
        captcha = Captcha.objects.create(code=captcha, shifr=shifr)
        serializers = CaptchaSerializer(captcha)
        return Response(serializers.data)


class CheckCaptchaView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        print(request.data)
        captcha = request.data.get('captcha')
        shifr = request.data.get('shifr')
        captcha = Captcha.objects.filter(code=captcha, shifr=shifr).last()
        serializers = CaptchaSerializer(captcha)
        return Response(serializers.data)


class PoliticaApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        politica = Politica.objects.filter(language__title=kwargs['lang']).last()
        serializer = PoliticaSerializer(politica)
        return Response(serializer.data)
        
        
class StoryApiView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        story = Story.objects.filter(language__title=kwargs['lang']).last()
        serializer = StorySerializer(story)
        return Response(serializer.data)