from django.http import JsonResponse

def error(code: str, message: str, status: int = 500) -> JsonResponse:
    return JsonResponse({"error": {"code": code, "message": message}}, status=status)
