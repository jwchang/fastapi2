from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
app.mount("/", StaticFiles(directory="public", html=True), name="static")

# Pydantic 모델을 사용하여 요청 본문을 검증합니다.
class CityWeatherRequest(BaseModel):
    city: str

# /get_city_weather 엔드포인트 추가
@app.post("/get_city_weather")
async def get_city_weather(request: CityWeatherRequest):
    city = request.city

    # 실제로는 외부 API를 호출하여 날씨 정보를 가져와야 합니다.
    # 여기서는 예제이므로 더미 데이터를 반환합니다.
    weather_data = {
        "Seoul": {"temperature": 20, "condition": "Sunny"},
        "New York": {"temperature": 15, "condition": "Cloudy"},
        "Paris": {"temperature": 18, "condition": "Rainy"}
    }

    if city in weather_data:
        return {"city": city, "weather": weather_data[city]}
    else:
        raise HTTPException(status_code=404, detail="City not found")

# FastAPI 애플리케이션을 실행합니다.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
