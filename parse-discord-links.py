import json
import re
import sys

# Patterns for each music platform
YOUTUBE_REGEX = re.compile(r'https?://(?:www\.)?(?:youtube\.com|youtu\.be)/[^\s"\'<>]+')
SPOTIFY_REGEX = re.compile(r'https?://(?:open\.)?spotify\.com/[^\s"\'<>]+')
SOUNDCLOUD_REGEX = re.compile(r'https?://(?:www\.)?soundcloud\.com/[^\s"\'<>]+')

def extract_links_from_content(content):
    return {
        "youtube": YOUTUBE_REGEX.findall(content),
        "spotify": SPOTIFY_REGEX.findall(content),
        "soundcloud": SOUNDCLOUD_REGEX.findall(content),
    }

def parse_json_for_links(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    youtube_links = set()
    spotify_links = set()
    soundcloud_links = set()

    for entry in data:
        content = entry.get("content", "")
        links = extract_links_from_content(content)
        youtube_links.update(links["youtube"])
        spotify_links.update(links["spotify"])
        soundcloud_links.update(links["soundcloud"])

    print("🎥 YouTube Links:")
    print("\n".join(sorted(youtube_links)) or "None found")

    print("\n🎧 Spotify Links:")
    print("\n".join(sorted(spotify_links)) or "None found")

    print("\n🎵 SoundCloud Links:")
    print("\n".join(sorted(soundcloud_links)) or "None found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_music_links.py your_file.json")
    else:
        parse_json_for_links(sys.argv[1])
