def validate_repo_url(url):
    return "/" in url and len(url.split("/")) == 2
