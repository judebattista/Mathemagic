# https://www.django-rest-framework.org/api-guide/viewsets/

from meetings.models import Meeting
from .serializers import MeetingSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import action

class MeetingViewSet(viewsets.ModelViewSet):
    serializer_class = MeetingSerializer
    
    queryset = Meeting.objects.all()

    @action(detail=False) # default method is get, and detail=False implies a set of things to return
    def meetings_by_user(self, request, pk=None):
        user = User.objects.get_by_natural_key(request.user.username)
        res = Meeting.objects.filter(people__username=user.username)
        page = self.paginate_queryset(res)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(res, many=True)
        return Response(serializer.data)
    
    # https://stackoverflow.com/questions/46404051/send-object-with-axios-get-request
    @action(detail=False)
    def meetings_by_group(self, request, pk=None):
        print(request.user.group.all())
        # groupName = request.data.get('group_name')

        # Groups a user is in can be done by:
        #   request.user.groups.all()
        #   Assume that there is some way to pass this through/get it...
        users = User.objects.filter(groups__name="EthicsBowl")
        res = Meeting.objects.filter(people__in=users)
        page = self.paginate_queryset(res)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(res, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def algorithm(self, request, pk=None):
        print(request.data)
        return Response(request.data)

    # Just want to return all the users and information on them,
    # This is definitely insecure, and should be changed
    @action(methods=['get'], detail=False)
    def all_users(self, request, pk=None):
        user_serializer = UserSerializer
        res = User.objects.all()
        page = self.paginate_queryset(res)
        if page is not None:
            serializer = user_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = user_serializer(res, many=True)
        return Response(serializer.data)




# The following lines of code are compressed by this simpler view set
# If you want more customization, don't use a viewset

# from rest_framework.generics import (
#     ListAPIView, 
#     RetrieveAPIView, 
#     CreateAPIView,
#     UpdateAPIView,
#     DestroyAPIView
# )
    
# class ArticleListView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetailView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleCreateView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleUpdateView(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDeleteView(DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer