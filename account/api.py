from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm


@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    print(form.errors)

    if form.is_valid():
        form.save()
        message = 'success'
        return JsonResponse({'message': message})
    else:
        message = 'error'
        print(message)
        # Return a JsonResponse with a 4xx status code
        return JsonResponse({'message': message, 'errors': form.errors}, status=400)
