class MusicViewSet(viewsets.ModelViewSet):
    # params_list = []
    # queryset = Comment.objects.all()
    # serializer_class = CommentSerializer
    # print(kwargs['pk'])

    def list(self, request, **kwargs):
        status_id = self.kwargs['pk']

        self.queryset = Comment.objects.filter(status_id=status_id)
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
