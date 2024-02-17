from requests import Response
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from .permissions import isStaffEditorPermissions
from api.authentication import TokenAuthentication



class ProductMixinView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.UpdateModelMixin,
                       generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


product_mixin_view = ProductMixinView.as_view()


class ProdutListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, isStaffEditorPermissions]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.DjangoModelPermissions]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# not using this

class ProductListAPIView(generics.ListAPIView):
    # not gona use this method
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# not using this


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # getting a detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data

            return Response(data)

        else:
            # getting a list view
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)

    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        else:
            return Response({'Invalid': "Not a good data"}, status=400)
