from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .serializers import PassSerializer
from .models import Pass
from django_filters import rest_framework as df_filters


class PassFilter(df_filters.FilterSet):
    class Meta:
        model = Pass
        fields = ['user__email']


class Passviewset(viewsets.ModelViewSet):
    queryset = Pass.objects.all()
    serializer_class = PassSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']
    filter_backends = [df_filters.DjangoFilterBackend]
    filterset_class = PassFilter

    def update(self, request, *args, **kwargs):
        passes = self.get_object()
        serializer = self.get_serializer(passes, data=request.data, partial=True)
        if serializer.is_valid():
            if passes.status != "New":
                raise ValidationError("Редактирование записи возможно только имея статус 'New' ")
            serializer.save()
            return Response({
                'state': 1,
                'message': 'Запись успешно обновлена'
            })

        else:
            return Response({
                'state': 0,
                'message': serializer.errors
            })
