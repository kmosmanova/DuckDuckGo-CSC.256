import requests


def get_ddg_presidents():
    '''
    Returns the list of presidents from
    duckduckgo api.
    '''
    URL = "https://api.duckduckgo.com"

    # request pages from duckduckgo api
    request = requests.get(URL, params={"q": "presidents of the united states",
                                        "format": "json"})

    # extract json data
    json_page = request.json()

    # contains names from queried results
    queried_names = []

    # look through each field in answers
    for field in json_page["RelatedTopics"]:

        # extract the name from the text of field
        cutoff = field["Text"].index(' -')
        name = field["Text"][:cutoff]

        # append to the list
        queried_names.append(name)

    return queried_names
