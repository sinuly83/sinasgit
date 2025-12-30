from math import e
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, how are you?!"})

@api_view(['GET', 'POST'])
def hello_world2(request):
    if request.method == 'GET':
        return Response({"message": "Hello, how are you?!"})
    elif request.method == 'POST':
        return Response({"message": "Hello, how are you {} ?!".format(request.data["name"])})
    
@api_view(['GET', 'POST'])
def calculator(request):
    if request.method != 'POST':
        return Response({"error":"Only POST method is allowed"}, status = status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        try:
            num1 = request.data["num1"]
            num2 = request.data["num2"]
            opr = request.data["opr"]
        except:
            return Response({"error":"send num1 , num2 and opr parameters"}, status = status.HTTP_400_BAD_REQUEST)
        else:
            if isinstance(num1,int) and isinstance(num2,int):
                if opr == "add":
                    return Response({"result":num1+num2},status=status.HTTP_200_OK)
                elif opr == "sub":
                    return Response({"result":num1-num2},status=status.HTTP_200_OK)
                elif opr == "mul":
                    return Response({"result":num1*num2},status=status.HTTP_200_OK)
                elif opr == "div":
                    if num2 != 0:
                        return Response({"result":num1/num2},status=status.HTTP_200_OK)
                    else:
                        return Response({"error":"Division by zero is not allowed"}, status = status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"error":"send a valid operator"}, status = status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error":"num1 and num2 should be integers"}, status = status.HTTP_400_BAD_REQUEST)
