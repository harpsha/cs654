from django.shortcuts import render
import MySQLdb

def foo(request):
    db = MySQLdb.connect(user='me', db='mydb', passwd='secret', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT line FROM Line')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render(request, 'url/to/template.html', {'lines': names})


# Note that the foo function still uses the foo shortcut from Django to render the data
# Using pure Python would be like below:

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html]

if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('', 8080, app)
        print('Serving on port 8080...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')