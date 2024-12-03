from rest_framework import serializers
from bnpz.models import *


class CategoryNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryNew
        fields = "__all__"


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = "__all__"


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class CategoryTenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTender
        fields = "__all__"


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class SelectionProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectionProduct
        fields = "__all__"


class AddMessageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    address = serializers.CharField()
    bthDate = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
    theme = serializers.CharField()
    text = serializers.CharField()

    def create(self, validated_data):
        return Message.objects.create(**validated_data)


class CheckMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = "__all__"


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class LocalDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalDocs
        fields = "__all__"


class LiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lider
        fields = "__all__"
        
        
        
class CaptchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Captcha
        fields = "__all__"


class PoliticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Politica
        fields = "__all__"


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"


class ConsLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsLink
        fields = "__all__"


class ConsPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsPhoto
        fields = "__all__"


class ConsVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsVideo
        fields = "__all__"