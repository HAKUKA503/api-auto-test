import requests

BASE_URL = "http://127.0.0.1:8000"

def test_get_hello():
    resp = requests.get(f"{BASE_URL}/hello")
    print("【Hello接口】状态码:", resp.status_code)
    print("响应:", resp.json())
    assert resp.status_code == 200
    assert resp.json()["code"] == 200

def test_get_user():
    resp = requests.get(f"{BASE_URL}/user", params={"name": "zhangsan"})
    print("\n【用户接口】响应:", resp.json())
    assert resp.json()["username"] == "zhangsan"

def test_login_success():
    resp = requests.post(
        f"{BASE_URL}/login",
        params={"username":"admin","password":"123456"}
    )
    print("\n【登录成功】响应:", resp.json())
    assert resp.json()["result"] == "success"

if __name__ == "__main__":
    test_get_hello()
    test_get_user()
    test_login_success()
    print("\n✅ 所有API测试通过")