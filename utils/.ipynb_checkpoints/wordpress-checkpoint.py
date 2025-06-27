import requests

def post_to_wordpress(title, content, tags, publish_date, access_token, site_url):
    endpoint = f"https://public-api.wordpress.com/rest/v1.1/sites/{site_url}/posts/new"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    data = {
        "title": title,
        "content": content,
        "tags": tags,
        "date": publish_date,
        "status": "future"
    }

    try:
        response = requests.post(endpoint, headers=headers, data=data)
        if response.status_code == 201:
            return {
                "success": True,
                "status": "terjadwal",
                "url": response.json().get("URL", "")
            }
        else:
            return {
                "success": False,
                "error": response.text
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
