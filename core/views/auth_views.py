from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, logout
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
def token_login(request):
    try:
        company = request.POST.get("company","")
        username = request.POST.get("username","")
        password = request.POST.get("password","")

        user = authenticate(username=username, password=password)
        if user is not None:
            assert company.lower()==user.profile.company.name.lower(), "ERROR: INVALID COMPANY"
            token = Token.objects.get_or_create(user=user)[0].key
            data = {"token":token, "role":user.profile.role.name, "name":user.first_name, "company":user.profile.company.id}
            print(data)
            return Response(data)
        else:
            assert 1==2, "INVALID CREDENTAILS"
    
    except AssertionError as msg:
        print(msg)
        return Response({"error":str(msg)}, status=400)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def token_logout(request):
    try:
        request.user.auth_token.delete()
        logout(request)
        return Response('User Logged out successfully')
    
    except AssertionError as msg:
        print(msg)
        return Response({"error":str(msg)}, status=400)




