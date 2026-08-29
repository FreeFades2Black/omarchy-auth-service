from fastapi import FastAPI
app = FastAPI(title='Auth Service')
@app.get('/health')
def h(): return {'service': 'auth', 'status': 'ok'}
@app.post('/api/auth/token')
def token(): return {'access_token': 'jwt_mock_token_ok', 'expires_in': 3600}
