def url_to_id(url):
    if isinstance(url, str) and url:
        return url.split('/')[-1]
