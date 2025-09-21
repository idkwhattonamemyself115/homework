import requests

# Make sure this matches the port your Flask server is running on
url = "http://127.0.0.1:5000/api/joke/3"  # get 3 jokes

try:
    response = requests.get(url)

    print("Status code:", response.status_code)
    print("Raw response:", repr(response.text))  # debug: see exactly what the server sent

    if response.status_code == 200 and response.text:
        data = response.json()
        print("\nHere are your jokes:")
        for joke in data:
            print(f"{joke['setup']} - {joke['punchline']}")
    else:
        print("Server returned an error or empty response:", response.status_code)

except Exception as e:
    print("Request failed:", e)