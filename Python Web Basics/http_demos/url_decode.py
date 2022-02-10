from urllib.parse import unquote

urls_to_be_decoded = [
    'http://www.google.bg/search?q=C%23',
    'https://mysite.com/show?n%40m3= p3%24h0',
    'http://url-decoder.com/i%23de%25?id=23',
]

expected_result = ['http://www.google.bg/search?q=C#',
                   'https://mysite.com/show?n@m3= p3$h0',
                   'http://url-decoder.com/i#de%?id=23',
                   ]

result = [unquote(ulr) for ulr in urls_to_be_decoded]
assert result == expected_result
