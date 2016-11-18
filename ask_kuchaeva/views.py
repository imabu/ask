from django.http import HttpResponse

def hello(request):
    get = "GET:<br>"
    for key in request.GET:
        get += str(key) + " = " + str(request.GET[key]) + "<br>"
    data = request.POST.get("data")
    html = """
    <html>
    <body>
       <form method="post" action="">
            <p>
               text: <input type="text" name="data" value="%(data)s">
            </p>
            <p>
                <input type="submit" value="Submit">
            </p>
        </form>
    </body>
    </html>""" % {
        'data': data
    }
    post = "POST:<br>"
    for key in request.POST:
        post += str(key) + " = " + str(request.POST[key]) + "<br>"
    output = html + "<br>" + get + "<br>" + post
    return HttpResponse(output)