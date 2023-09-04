from .models import Place
from rest_framework import viewsets, permissions
from .serializers import PlaceSerializer
from rest_framework.filters import SearchFilter

class PlaceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = PlaceSerializer
    filter_backends = [SearchFilter]  # Agregamos SearchFilter para filtrar en todos los campos

    def get_queryset(self):
        # Limita la consulta a 10 registros para la lista
        return Place.objects.all()[:10]

    def perform_create(self, serializer):
        # Valida y crea un nuevo objeto Place
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def perform_update(self, serializer):
        # Valida y actualiza un objeto Place existente
        serializer.is_valid(raise_exception=True)
        serializer.save()

    # Sobrescribe el método `list` para aplicar el filtrado a través de parámetros GET
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Obtiene los parámetros de consulta GET
        filter_params = {}
        for param in request.query_params:
            filter_params[param] = request.query_params.get(param)

        # Aplica los filtros a todos los campos usando el operador OR
        filtered_queryset = queryset
        for param, value in filter_params.items():
            filtered_queryset = filtered_queryset.filter(**{f"{param}__icontains": value})

        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)
