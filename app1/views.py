from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, how are you?!"})

@api_view(['GET', 'POST'])
def hello_world2(request):
    if request.method == 'GET':
        return Response({"message": "Hello, how are you?!"})
    elif request.method == 'POST':
        return Response({"message": "Hello, how are you {} ?!".format(request.data["name"])})