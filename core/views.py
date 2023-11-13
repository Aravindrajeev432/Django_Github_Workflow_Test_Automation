from django.http import JsonResponse


def my_view(request):
    data = {"message": "Hello, world!"}
    return JsonResponse(
        data
    )