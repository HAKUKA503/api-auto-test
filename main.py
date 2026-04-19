from fastapi import FastAPI

app = FastAPI()

# 测试接口1：GET 无参数
@app.get("/hello")
def hello():
    return {"msg": "Hello API Test", "code": 200}

# 测试接口2：GET 带参数
@app.get("/user")
def get_user(name: str = "guest"):
    return {"username": name, "status": "ok"}

# 测试接口3：POST 提交JSON
@app.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "123456":
        return {"result": "success", "token": "abc123xyz"}
    return {"result": "fail", "msg": "账号密码错误"}