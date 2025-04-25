def get_public_id_from_url(url):
    if url is None:
        return None

    import re
    match = re.search(r'/upload/.*/(.*)\.(\w+)$', url)
    if match:
        return match.group(1)
    return None
