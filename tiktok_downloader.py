from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_tiktok_video_url(video_url):
    # Extract the direct video URL from the TikTok page
    response = requests.get(video_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # TikTok stores the video URL in a meta tag
    meta_tag = soup.find("meta", property="og:video")
    if meta_tag:
        return meta_tag["content"]
    return None

@app.route('/download', methods=['GET'])
def download_tiktok():
    tiktok_url = request.args.get('url')
    if not tiktok_url:
        return jsonify({"error": "URL parameter is required"}), 400
    
    video_url = get_tiktok_video_url(tiktok_url)
    if not video_url:
        return jsonify({"error": "Could not extract video URL"}), 404
    
    return jsonify({"video_url": video_url})

if __name__ == '__main__':
    app.run(debug=True)
