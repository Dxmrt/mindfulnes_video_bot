from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = "credentials/client_secrets.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def authenticate_youtube():
    """Authenticate YouTube API."""
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=credentials)


def upload_video(video_file, title, description):
    """Uploads a video to YouTube."""
    youtube = authenticate_youtube()

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["mindfulness", "meditation"],
                "categoryId": "22"
            },
            "status": {"privacyStatus": "public"}
        },
        media_body=MediaFileUpload(video_file, chunksize=-1, resumable=True)
    )

    response = request.execute()
    print(f"Uploaded video with ID: {response['id']}")


if __name__ == "__main__":
    upload_video("generated_videos/mindfulness_video.mp4", "Daily Mindfulness", "A short mindfulness video.")
