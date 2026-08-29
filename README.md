# 🔐 Omarchy Zero-Trust Authentication Microservice

Enterprise OAuth2, JWT verification, and Role-Based Access Control (RBAC) microservice migrated from Azure DevOps to GitHub Enterprise.

---

## 📋 Migration & Governance Audit

* **Source Platform:** Azure DevOps (`source-ado-repos/omarchy-auth-service`)
* **Target Platform:** GitHub Enterprise (`FreeFades2Black/omarchy-auth-service`)
* **Pipeline Translation:** Converted legacy `azure-pipelines.yml` to native GitHub Actions `.github/workflows/ci.yml`.
* **Compliance Verdict:** `PASSED_100_PERCENT_PARITY`
* **Secret Scan:** `CLEAN` (0 exposed credentials in git history).

---

## 🚀 API Endpoints

* `GET /health` — Service health & uptime status.
* `POST /api/auth/token` — Issues signed JWT access tokens for authenticated clients.

---

## 🛠️ Local Development

```bash
# Run service locally
python3 -m uvicorn app:app --host 0.0.0.0 --port 8810
```
