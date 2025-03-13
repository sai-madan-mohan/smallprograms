import requests

def check_website_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"✅ {url} is Online! (Status Code: 200)"
        else:
            return f"⚠️ {url} is reachable but returned status code: {response.status_code}"
    except requests.ConnectionError:
        return f"❌ {url} is Offline! (Connection Error)"
    except requests.Timeout:
        return f"⏳ {url} took too long to respond! (Timeout)"
    except Exception as e:
        return f"❌ Error: {e}"

# User input
website = input("Enter website URL (include https://): ")
print(check_website_status(website))
