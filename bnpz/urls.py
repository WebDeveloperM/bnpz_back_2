from django.urls import path
from bnpz.back.views import *

urlpatterns = [
    path("new/<str:lang>", NewApiView.as_view()),
    path("news/<str:id>/<str:lang>", NewByCategoryApiView.as_view()),
    path("new_category/", CategoryNewApiView.as_view()),
    path("new_detail/<int:id>/<str:lang>/", NewDetailApiView.as_view()),
    
    path("gender/<str:lang>", GenderApiView.as_view()),
    path("gender_detail/<int:id>/<str:lang>/", GenderDetailApiView.as_view()),
    
    path("video/", VideoApiView.as_view()),
    
    path("product/<str:lang>", ProductApiView.as_view()),
    
    path("faq/<str:lang>/", FAQApiView.as_view()),
    
    path("gallery/<str:lang>/", GalleryApiView.as_view()),
    path("gallery_detail/<int:id>", GalleryDetailApiView.as_view()),
    
    path("selection/<str:id>/<str:lang>/", SelectionApiView.as_view()),
    path("selection_archive/<str:id>/<str:lang>/", SelectionArchiveApiView.as_view()),
    path("selection_category/", SelectionCategoryApiView.as_view()),
    path("selection_detail/<int:id>/<str:lang>/", SelectionDetailApiView.as_view()),
    path("selection_product/<int:id>/<str:lang>/", SelectionProductApiView.as_view()),
    
    path("add-message/", MessageApiView.as_view()),
    path("check-message/", MessageCheckApiView.as_view()),
    path("check-phone/", MessageCheckPhoneApiView.as_view()),

    path("sites/<str:lang>", SiteApiView.as_view()),
    path("statistic/<str:lang>", StatisticApiView.as_view()),

    path("certificate/<str:lang>", CertificateApiView.as_view()),
    path("certificate/<int:id>/<str:lang>", CertificateDetailApiView.as_view()),

    path("local/", LocalApiView.as_view()),

    path("lider/<str:lang>", LiderApiView.as_view()),
    path("lider-detail/<int:id>/<str:lang>", LiderDetailApiView.as_view()),

    path("repeat-code/", RepeatCodeApiView.as_view()),
    path("null-code/", NullCodeApiView.as_view()),
    
    path("add-captcha/", AddCaptchaView.as_view()),
    path("check-captcha/", CheckCaptchaView.as_view()),
    
    path("politica/<str:lang>", PoliticaApiView.as_view()),
    path("story/<str:lang>", StoryApiView.as_view()),

]