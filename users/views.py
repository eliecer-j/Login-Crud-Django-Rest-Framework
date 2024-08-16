from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from users.serializers import User_serializers
from users.models import User
from rest_framework.response import Response


class UsersList(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):

        user = request.data
        if not user:
            print({'res:''request vacio'})
            return Response(data=user, status=status.HTTP_400_BAD_REQUEST)
        serializer = User_serializers(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):

        self.permission_classes = [permissions.IsAuthenticated]
        self.check_permissions(request)
        users = User.objects.all()
        serializers = User_serializers(users, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)


# Create your views here.
