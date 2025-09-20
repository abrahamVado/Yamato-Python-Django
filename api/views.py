from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from .responses import error

@require_GET
def healthz(_):
    return JsonResponse({"ok": True})

@require_GET
def readyz(_):
    return JsonResponse({"ready": True})

def not_implemented(_):
    return error("NOT_IMPLEMENTED", "This endpoint is not implemented yet.", status=501)

@require_POST
def auth_register(request): return not_implemented(request)

@require_POST
def auth_login(request): return not_implemented(request)

@require_POST
def auth_refresh(request): return not_implemented(request)

@require_POST
def auth_logout(request): return not_implemented(request)

@require_GET
def auth_session(request): return not_implemented(request)

@require_GET
def auth_oauth_start(request, provider): return not_implemented(request)

@require_GET
def auth_oauth_callback(request, provider): return not_implemented(request)

@require_POST
def webauthn_begin(request): return not_implemented(request)

@require_POST
def webauthn_finish(request): return not_implemented(request)

@require_POST
def magic_link(request): return not_implemented(request)

@require_POST
def magic_link_consume(request): return not_implemented(request)

@require_GET
def jwks(request): return not_implemented(request)
