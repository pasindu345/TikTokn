from fastapi import FastAPI
from TikTokApi import TikTokApi

app = FastAPI()

@app.get("/download/video/{video_id}")
async def download_video(video_id: str):
    api = TikTokApi()
    video = await api.video(id=video_id)
    return {"video_url": video.download_url}

@app.get("/download/photo/{video_id}")
async def download_photo(video_id: str):
    api = TikTokApi()
    video = await api.video(id=video_id)
    # Assuming the API provides a method to get photo URL
    return {"photo_url": video.photo_url}

@app.get("/download/audio/{video_id}")
async def download_audio(video_id: str):
    api = TikTokApi()
    video = await api.video(id=video_id)
    return {"audio_url": video.music.download_url}
