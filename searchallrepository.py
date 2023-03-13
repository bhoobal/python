import json
import requests

topic_filters = 'sdgkajshdfjhs'

def parsejson(respnse_obj):

    data = respnse_obj
    topic_exclude = 'cloud-'
    topics_names = ""
    for item in range(0, len(data['items'])):
        if topic_exclude not in data['items'][item]['topics']:
            for topics_counter in enumerate(data['items'][item]['topics']):
                if str(topics_counter[1]) != topic_exclude:
                    topics_names = topics_names + "\t" + str(topics_counter[1])
            print(data['items'][item]['name'] + "\t" + "Topics names: " + topics_names)
            topics_names = ""


if __name__ == '__main__':
    url = "https://api.github.com/search/repositories?per_page=100&page=1&q=org%3A+topic%3A"+topic_filters+"+sort%3Aname-asc"

    payload = {}

    headers = {
        'Authorization': 'Basic AHSJKAHSJKAHSJKAHSJAHSJAH'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    num_pages = response.json()
    parsejson(num_pages)

    page_count = divmod(num_pages['total_count'], 100)
    if len(page_count) == 2 and page_count[1] <= 100:
        no_of_pages = page_count[0] + 1

    for page in range(2, no_of_pages + 1):
        paginated_url = "https://api.github.com/search/repositories?per_page=100&page=" + str(
            page) + "&q=org%3A+topic%3A"+topic_filters+"+sort%3Aname-asc"
        response = requests.request("GET", paginated_url, headers=headers, data=payload)
        parsejson(response.json())
