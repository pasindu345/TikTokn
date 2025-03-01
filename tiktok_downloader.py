from fastapi import FastAPI, HTTPException
from TikTokApi import TikTokApi

app = FastAPI()

@app.get("/download/video/{video_id}")
async def download_video(video_id: str):
    try:
        api = TikTokApi()
        video = await api.video(id=video_id)
        return {"video_url": video.download_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not extract video URL: {str(e)}")

@app.get("/download/photo/{video_id}")
async def download_photo(video_id: str):
    try:
        api = TikTokApi()
        video = await api.video(id=video_id)
        # Assuming the API provides a method to get photo URL
        return {"photo_url": video.photo_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not extract photo URL: {str(e)}")

@app.get("/download/audio/{video_id}")
async def download_audio(video_id: str):
    try:
        api = TikTokApi()
        video = await api.video(id=video_id)
        return {"audio_url": video.music.download_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not extract audio URL: {str(e)}")
