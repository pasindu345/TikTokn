from fastapi import FastAPI
from TikTokApi import TikTokApi

app = FastAPI()

@app.get("/download/{video_id}")
async def download_video(video_id: str):
    api = TikTokApi()
    video = await api.video(id=video_id)
    return {"video_url": video.download_url}
