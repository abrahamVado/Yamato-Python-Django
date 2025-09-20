# Yamato Auth — Django + DRF Scaffold

**Decisions (locked):**
- IDs: **BIGINT**
- JWT: **HS256** (`JWT_SECRET`)
- Cookies: **cross-site** (`SameSite=None; Secure`), CORS required

This is a runnable skeleton that mounts all contract routes returning **501 Not Implemented**,
plus `/healthz` and `/readyz`. It wires **CORS (credentials)** and simple **security headers**.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# For plain http://localhost during dev, set COOKIE_SECURE=false in .env

python manage.py migrate   # creates default tables (SQLite by default; switch to Postgres in .env)
python manage.py runserver 0.0.0.0:8082

# test
curl -s http://localhost:8082/healthz
curl -i http://localhost:8082/auth/login  # -> 501 JSON envelope
```

## Routes mounted
- `POST  /auth/register`
- `POST  /auth/login`
- `POST  /auth/refresh`
- `POST  /auth/logout`
- `GET   /auth/session`
- `GET   /auth/oauth/{provider}`
- `GET   /auth/oauth/{provider}/callback`
- `POST  /auth/mfa/webauthn/begin`
- `POST  /auth/mfa/webauthn/finish`
- `POST  /auth/magic-link`
- `POST  /auth/magic-link/consume`
- `GET   /auth/oidc/.well-known/jwks.json`
- `GET   /healthz`
- `GET   /readyz`

## Next steps
- Switch DB to Postgres in `.env` and `settings.py` (example provided).
- Implement JWT + refresh rotation in `api/` (helpers to add).
- Add OAuth (allauth/social-auth) and WebAuthn (python-web-authn) when ready.
