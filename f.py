import requests
import webbrowser
    

def main():
    url = input("Enter the URL: ")
    url=str(url)
    url1="https://"+url
    try:
        response = requests.get(url1)
        webbrowser.open(url1)
    except requests.RequestException as e:
        print("Error:", e)
    except webbrowser.Error as e:
        print("Error opening URL:", e)

if __name__ == "__main__":
    main()
