import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Application at {url} is UP. Status Code: 200")
        else:
            print(f"Application at {url} is DOWN. Status Code: {response.status_code}")
    except requests.ConnectionError:
        print(f"Connection error: Application at {url} is DOWN.")

if __name__ == "__main__":
    # Specify the URL of the application to be checked
    application_url = "http://www.memonotepad.com/"
    check_application_health(application_url)

