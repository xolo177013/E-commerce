# API Contract — E-Commerce Backend

This document is the single source of truth for the frontend developer. It describes every working backend endpoint: what to send, what comes back, and what errors look like. The frontend should be built against this document — no need to read Django code directly.

**Base URL (local dev via Docker):** `http://127.0.0.1:8000`

---

## Authentication Overview

This API uses JWT (JSON Web Tokens). After login, you receive two tokens:
- `access` — short-lived, send this with every request that requires login
- `refresh` — longer-lived, used only to get a new `access` token when it expires

**How to send the access token on protected requests:**
```
Authorization: Bearer <access_token>
```

---

## 1. Register a new user

**POST** `/api/register/`

**Request body:**
```json
{
    "username": "johndoe",
    "email": "john@example.com",
    "phone_number": "1234567890",
    "password": "somepassword123"
}
```

**Success response — `201 Created`:**
```json
{
    "id": 3,
    "username": "johndoe",
    "email": "john@example.com",
    "phone_number": "1234567890"
}
```
Note: password is never returned, for security.

**Possible error — `400 Bad Request`** (e.g. email already taken, password too short):
```json
{
    "email": ["custom user with this email already exists."]
}
```

---

## 2. Login (obtain tokens)

**POST** `/api/token/`

**Request body:**
```json
{
    "email": "john@example.com",
    "password": "somepassword123"
}
```

**Success response — `200 OK`:**
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Error — `401 Unauthorized`** (wrong email/password):
```json
{
    "detail": "No active account found with the given credentials"
}
```

---

## 3. Refresh access token

**POST** `/api/token/refresh/`

**Request body:**
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Success response — `200 OK`:**
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**When to use this:** the frontend should call this whenever an API request fails with `401` due to an expired access token — get a new one here instead of forcing the user to log in again.

---

## 4. Get current logged-in user info

**GET** `/api/me/`

**Headers required:**
```
Authorization: Bearer <access_token>
```

**Success response — `200 OK`:**
```json
{
    "id": 3,
    "username": "johndoe",
    "email": "john@example.com",
    "phone_number": "1234567890"
}
```

**Error — `401 Unauthorized`** (missing or invalid token):
```json
{
    "detail": "Authentication credentials were not provided."
}
```

---

## Frontend integration notes

- Store `access` and `refresh` tokens after login (e.g., in React state/context — not localStorage if avoidable, but that's a frontend architecture decision the frontend dev can make).
- Attach `access` token to every request that needs a logged-in user (anything except register/login).
- If a request returns `401`, try calling `/api/token/refresh/` once with the stored `refresh` token before giving up and redirecting to login.
- All request/response bodies are JSON — set `Content-Type: application/json` on every request.

---

## What's coming next (not built yet — don't build UI for these until this doc is updated)

- Product catalog endpoints (browse products, categories)
- Cart endpoints
- Order/checkout endpoints

This document will be updated as each new feature is completed and tested. Always check for the latest version before building against a new endpoint.