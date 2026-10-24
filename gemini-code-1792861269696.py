import os
import json
import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

@app.get("/")
async def get():
    return HTMLResponse("Voice Bot Server is Running Live!")

@app.websocket("/media-stream")
async def handle_media_stream(websocket: WebSocket):
    await websocket.accept()
    print("📲 Вхідне підключення дзвінка від Twilio")

    try:
        while True:
            message = await websocket.receive_text()
            data = json.loads(message)

            if data['event'] == 'start':
                print(f"📞 Дзвінок розпочато (Call SID: {data['start']['callSid']})")

            elif data['event'] == 'media':
                pass

            elif data['event'] == 'stop':
                print("🔇 Дзвінок завершено")
                break
    except Exception as e:
        print(f"Помилка з'єднання: {e}")
    finally:
        await websocket.close()