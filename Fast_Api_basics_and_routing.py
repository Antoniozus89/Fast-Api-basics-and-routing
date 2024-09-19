from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/main     ')
async def Get_main_page() ->dict:
    return {'message': 'Главная страница'}


@app.get("/user/admin")
async def Get_admin_page():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def Get_user_number(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def Gtt_user_info(username: str = Query(...), age: int = Query(...)):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


