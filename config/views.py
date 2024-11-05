
from rest_framework.response import Response
from rest_framework.views import APIView

class Home(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        return Response({"message" : "Okdaaa"})
