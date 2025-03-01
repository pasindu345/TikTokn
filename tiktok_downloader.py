from flask import Flask, request, jsonify
  import requests
  from bs4 import BeautifulSoup

  app = Flask(__name__)

  def get_tiktok_video_url(video_url):
      try:
          response = requests.get(video_url)
          soup = BeautifulSoup(response.text, 'html.parser')
          
          # Extract video URL from meta tag
          meta_tag = soup.find("meta", property="og:video")
          if meta_tag:
              return meta_tag["content"]
          
          # Alternative method: Extract from script tag
          script_tag = soup.find("script", {"type": "application/ld+json"})
          if script_tag:
              import json
              data = json.loads(script_tag.string)
              if "video" in data and "contentUrl" in data["video"]:
                  return data["video"]["contentUrl"]
          
          return None
      except Exception as e:
          print(f"Error: {e}")
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
