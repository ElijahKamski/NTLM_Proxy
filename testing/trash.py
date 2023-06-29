import requests

def main():
    response = requests.get('http://google.com', proxies={"http": f"http://127.0.0.1:{5865}"})
    print(response)

if __name__=='__main__':
    main()