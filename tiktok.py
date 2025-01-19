import requests
from bs4 import BeautifulSoup
import re
import json

def get_user_info(identifier):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
    }
    url = f"https://www.tiktok.com/@{identifier}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        script_tag = soup.find("script", string=re.compile("webapp.user-detail"))
        if script_tag:
            script_content = script_tag.string
            
            match = re.search(r'webapp\.user-detail":({.*?}),\s*"webapp', script_content)
            if match:
                user_data_json = match.group(1)
                
                try:
                    user_data = json.loads(user_data_json)
                    
                    user_info = user_data.get("userInfo", {})
                    user = user_info.get("user", {})
                    stats = user_info.get("stats", {})

                    user_id = user.get("id", "No ID found")
                    unique_id = user.get("uniqueId", "No unique ID found")
                    nickname = user.get("nickname", "No nickname found")
                    followers = stats.get("followerCount", "No followers count found")
                    following = stats.get("followingCount", "No following count found")
                    likes = stats.get("heartCount", "No likes count found")
                    videos = stats.get("videoCount", "No videos count found")
                    signature = user.get("signature", "No biography found")
                    verified = user.get("verified", "No verified status found")
                    secUid = user.get("secUid", "No secUid found")
                    privateAccount = user.get("privateAccount", "No private account status found")
                    region = user.get("region", "No region found")
                    heart = stats.get("heart", "No heart count found")
                    friendCount = stats.get("friendCount", "No friend count found")
                    profile_pic = user.get("avatarLarger", "No profile picture found").replace('\\u002F', '/')

                    print("User Information:")
                    print(f"User ID: {user_id}")
                    print(f"Username: {unique_id}")
                    print(f"Nickname: {nickname}")
                    print(f"Region: {region}")
                    print(f"Followers: {followers}")
                    print(f"Following: {following}")
                    print(f"Likes: {likes}")
                    print(f"Videos: {videos}")
                    print(f"Biography: {signature}")
                    print(f"Verified: {verified}")
                    print(f"SecUid: {secUid}")
                    print(f"Private Account: {privateAccount}")
                    print(f"Heart: {heart}")
                    print(f"Friend Count: {friendCount}")
                    print(f"Profile Picture URL: {profile_pic}")

                except json.JSONDecodeError as e:
                    print(f"JSON decoding error: {e}")
            else:
                print("Could not extract user data from the script!")
        else:
            print("User data script not found in page!")
    else:
        print(f"Error: Unable to fetch page. Status code: {response.status_code}")

# get_user_info("khaby.lame")
get_user_info("youneszarou")
