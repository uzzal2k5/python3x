from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework_bulk.generics import ListBulkCreateAPIView, ListBulkCreateUpdateAPIView

from apps.models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import *
from rest_framework import viewsets, status
# Create your views here.

class NewRequestAllApi(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = NewUrl.objects.all()
        serializer = NewRequestSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NewRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewRequestDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return NewUrl.objects.get(pk=pk)
        except NewUrl.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = NewRequestSerializer(snippet)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = NewRequestSerializer(snippet, data=request.data)
        print("hello api")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = NewRequestSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostCommentDelete(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self, request, pk, format=None):
        print(pk)
        print("Hello I am here")
        snippets = Post.objects.all()
        serializer = PostSerializer(snippets, many=True)
        # print(serializer.data)
        return Response("get")

    def post(self, request, pk, format=None):

        print(request.data)
        print(pk)
        instance = Post.objects.get(status_id=pk)
        instance.delete()

        cmnt = Comment.objects.get(status_id=pk)
        cmnt.delete()
        return Response("done")


class UpdateNewRequest(UpdateAPIView):
    queryset = NewUrl.objects.all()
    serializer_class = NewRequestSerializer

    def update(self, request, *args, **kwargs):
        id = kwargs['pk']
        data = request.DATA
        qs = NewUrl.objects.filter(id=id)
        serializer = self.serializer_class(qs, data=data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class PostApi(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Post.objects.all()
        serializer = PostSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data['status_id'])
        # previous post and its comments delete first and then enter new post and its comments
        try:
            Post.objects.filter(status_id=request.data['status_id']).delete()
            Comment.objects.filter(status_id=request.data['status_id']).delete()
        except:
            pass

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostMessageApi(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Post.objects.all()
        serializer = PostMessageSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data['status_id'])
        # previous post and its comments delete first and then enter new post and its comments
        try:
            Post.objects.filter(status_id=request.data['status_id']).delete()
            Comment.objects.filter(status_id=request.data['status_id']).delete()
        except:
            pass

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PostSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PostSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentApi(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Comment.objects.all()
        serializer = CommentSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CommentSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CommentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# COMMENT VIEW WITH SPECIFIC status_id
class CommentStatusid(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self, request, pk, format=None):
        print("pk",pk)
        post = Post.objects.filter(pk=pk)
        snippets = Comment.objects.filter(status_id=post.first().status_id)
        serializer = CommentSerializer(snippets, many=True)
        return Response(serializer.data)

# DATE RANGE REQUEST

class DateRangeNewUrlAllApi(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = DateRangeNewUrl.objects.all()
        serializer = DateRangeNewUrlSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DateRangeNewUrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DateRangeNewUrlDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return DateRangeNewUrl.objects.get(pk=pk)
        except DateRangeNewUrl.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DateRangeNewUrlSerializer(snippet)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DateRangeNewUrlSerializer(snippet, data=request.data)
        print("hello api")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DateRangeNewUrlSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateDateRangeNewUrl(UpdateAPIView):
    queryset = DateRangeNewUrl.objects.all()
    serializer_class = DateRangeNewUrlSerializer

    def update(self, request, *args, **kwargs):
        id = kwargs['pk']
        data = request.DATA
        qs = DateRangeNewUrl.objects.filter(id=id)
        serializer = self.serializer_class(qs, data=data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class DateRangePostApi(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = DateRangePost.objects.all()
        serializer = DateRangePostSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DateRangePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DateRangePostDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return DateRangePost.objects.get(pk=pk)
        except DateRangePost.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DateRangePostSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DateRangePostSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DateRangeCommentApi(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = DateRangeComment.objects.all()
        serializer = DateRangeCommentSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DateRangeCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DateRangeCommentDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return DateRangeComment.objects.get(pk=pk)
        except DateRangeComment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DateRangeCommentSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DateRangeCommentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MisClassifiedDataApi(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = MisClassifiedDataStore.objects.all()
        serializer = MisClassifiedDataSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("hello test api")
        print(request.data)
        serializer = MisClassifiedDataSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostLogApi(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = MisClassifiedDataStore.objects.all()
        serializer = PostLogSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("hello postlog api")
        print(request.data)
        serializer = PostLogSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MusicViewSet(viewsets.ModelViewSet):
    # params_list = []
    # queryset = Comment.objects.all()
    # serializer_class = CommentSerializer
    # print(kwargs['pk'])

    def list(self, request, **kwargs):
        status_id = self.kwargs['pk']
        print(status_id)
        print(self.kwargs['filter_list'])
        self.queryset = Comment.objects.filter(status_id=status_id)
        self.queryset =Co
        self.serializer_class = CommentSerializer
        try:
            music = query_musics_by_args(status_id=status_id, **request.query_params)
            serializer = CommentSerializer(music['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = music['draw']
            result['recordsTotal'] = music['total']
            result['recordsFiltered'] = music['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


    # def get(self, request, **kwargs):
    #     try:
    #         music = Comment.objects.all()[0:50]
    #         serializer = CommentSerializer(music, many=True)
    #
    #         return Response(serializer.data, status=status.HTTP_200_OK, template_name=None, content_type=None)
    #
    #     except Exception as e:
    #         return Response(e.message, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)

class DataList(ListAPIView):
    queryset = Comment.objects.all()[:100]
    serializer_class = CommentSerializer

# class LargeResultsSetPagination(PageNumberPagination):
#     page_size = 1000
#     page_size_query_param = 'page_size'
#     max_page_size = 10000
#
#
# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 100
#     page_size_query_param = 'page_size'
#     max_page_size = 1000


class CampaignMessage(ListAPIView):
    """
    List all snippets, or create a new snippet.
    """
    # queryset = CampaignAnalysis.objects.all()
    # serializer_class = CampaignSerializer
    # pagination_class = LargeResultsSetPagination

    # def get(self, request, format=None):
    #     snippets = CampaignAnalysis.objects.values('id', 'status_message')
    #     serializer = CampaignSerializer(snippets, many=True)
    #     return Response(serializer.data)

    serializer_class = CampaignSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        # username = self.kwargs['username']
        return CampaignAnalysis.objects.all().order_by('-id')[:150]