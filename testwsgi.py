from cgi import parse_qs, escape
html = """
<html>
<body>
<form method="post" action="">
<p>
<input type="text" name="data">
</p>
<p>
<input type="submit" value="Submit">
</p>
<p>
Data: %(data)s
</p>
</body>
</html>
"""
def application(env, start_response):
    try:
        request_body_size=int(env.get('CONTENT_LENTH',0))
    except (ValueError):
        request_body_size=0
    request_body=env['wsgi.input'].read(request_body_size)
    d=parse_qs(request_body)
    data=d.get('data','Empty')
    response_body= html%{'data':data}
    status='200 OK'
    response_headers=[('Content-Type','text/html'), ('Content-Lenght', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]
