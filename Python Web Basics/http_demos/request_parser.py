validated_paths = []

while True:
    command = input()
    if command == "END":
        break
    validated_paths.append(command)

http_request = input()


def get_requested_path(request):
    http_method, http_path = request.split('/')[:2]
    searched_path = '/' + http_path.split(' ')[0] + '/' + http_method.lower()
    return searched_path.strip()


def is_path_valid(valid_paths, requested_path):
    if requested_path in valid_paths:
        return True


searched_path = get_requested_path(http_request)

if is_path_valid(validated_paths, searched_path):
    status_code = 'OK'
    length = len(status_code)
    print(f"""HTTP/1.1 200 {status_code}
Content-Length: {length}
Content-Type: text/plain

{status_code}""")
else:
    status_code = 'Not Found'
    length = len(status_code)
    print(f"""HTTP/1.1 404 {status_code}
Content-Length: {length}
Content-Type: text/plain

{status_code}""")