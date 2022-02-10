from urllib.parse import urlparse


def is_ulr_valid(protocol, host, port, path):
    if protocol and host and port and path:
        if (protocol == 'http' and port == 443) or (protocol == 'https' and port == 80):
            return False
        return True
    return False


def print_result(url):
    result = urlparse(url)
    protocol = result.scheme
    host = result.netloc.split(':')[0]
    port = result.port
    if not port:
        if protocol == 'http':
            port = 80
        elif protocol == 'https':
            port = 443
    path = result.path
    if not path:
        path = '/'

    query = result.query
    fragment = result.fragment

    if is_ulr_valid(protocol, host, port, path):
        result = [f'Protocol: {protocol}', f'Host: {host}', f'Port: {port}', f'Path: {path}']
        if query:
            result.append(f'Query: {query}')
        if fragment:
            result.append(f'Fragment: {fragment}')
        return "\n".join(result)
    else:
        return 'Invalid URL'


ulrs = [
    ('http://mysite.com:80/demo/index.aspx', 'Valid'),
    ('https://my-site.bg', 'Valid'),
    ('https://mysite.bg/demo/search?id=22o#go', 'Valid'),
    ('http://softuni.bg/', 'Valid'),
    ('https://softuni.bg:447/search?Query=pesho&Users=true#go', 'Valid'),

    ('https://mysite:80/demo/index.aspx', 'Not Valid!'),
    ('somesite.com:80/search?', 'Not Valid!'),
    ('https/mysite.bg?id=2', 'Not Valid!'),
    ('http://google:443/', 'Not Valid!')
]

for (t, m) in ulrs:
    print(print_result(t) + '\n')
