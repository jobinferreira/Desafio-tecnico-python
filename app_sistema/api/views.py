# from django.shortcuts import render

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# from app_sistema.models import Equipamento
# from app_sistema.api.serializers import EquipamentoSerializer


# @api_view(['GET'])
# def get_equipamentos(request):

#     if request.method == 'GET':
#         equipamentos = Equipamento.objects.all()

#         serializer = EquipamentoSerializer(equipamentos, many=True)
#         return Response(serializer.data)
    
#     return Response(status=status.HTTP_400_BAD_REQUEST)
