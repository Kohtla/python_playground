import requests
from main import timer

def make_request(url):
    return requests.get(url)

@timer
def make_requests(number):
    results = {}
    for n in range(number):
        resp = make_request('https://google.com')
        
        if results.get(resp.status_code, None) is None:
            results[resp.status_code] = 1
        else:
            results[resp.status_code] += 1         
    return results


def main():
    results = make_requests(10)
    print(results)

if __name__ == "__main__":
    main()
