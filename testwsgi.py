from cgi import parse_qs, parse_qsl

html = """
<html>
<body>
<form method="post" action="">
Data: <input type="text" name="data"  >
<input type="submit">
<p>
POST: %(data)s
</p>
</form>
</body>
</html>
"""


def application(env, start_response):
    request_size = int(env.get('CONTENT_LENGHT', 0))
    post = env['wsgi.input'].read(request_size)
    post = parse_qs(post)
    data = post.get('data',[])

    get = parse_qsl(env['QUERY_STRING'])
    output = 'GET:\n'
    if env['QUERY_STRING'] != '':
        for val in get:
            output += '='.join(val)
            output += '\n'
    response =html%{'data': '!'.join(data)} + output
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [response]
