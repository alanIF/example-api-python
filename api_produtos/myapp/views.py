from rest_framework import generics
from .models import Produto
from .serializers import ProdutoSerializer

# Create your views here.
class ProdutoList(generics.ListCreateAPIView):

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer