
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /assignment3/
#####################################################################

from bottle import route, run, default_app, debug, request

musics = [
          { 'name': 'Smells Like Teen Spirit',
            'year': 1991,
            'album': 'Nevermind',
            'band': 'Nirvana',
            'genre': 'Grunge'},

          { 'name': 'Welcome to the Jungle',
            'year': 1987,
            'album': 'Appetite for Destruction',
            'band': "Guns N' Roses",
            'genre': 'Hard Rock'}
]

def htmlify(title, content, style):
    page = """<!DOCTYPE html>
              <html>
                  <head>
                      <title>""" + title + """</title>""" + style + """
                      <meta charset="utf-8" />
                  </head>
                  <body>
                      """ + content + """
                  </body>
              </html>"""
    return page

def CSS():
    css = """<style>

        table.music td,th{
            border: solid 2px black;
            padding: 15px;
            border-style: groove;}
            
        table.music tr{
            border-style: groove;}

        table.music{
            border-collapse: collapse;
            border-style: groove;}
            
        table.add td{
            padding: 0 15px 0 0;
            align = "center";}
            
        table.music{
            border-collapse: collapse;
        }

        table.music td, th{
            border: solid 2px black;
            padding: 15px;
            align = "center";}
            </style>"""

    return css

def a3_index():
    indexCont = ""
    indexCont += '<table class = "music">\n'

    indexCont += "<tr>\n"
    indexCont += "<th>Name</th><th>Year</th><th>Album</th><th>Band</th><th>Genre</th>\n"
    indexCont += "</tr>\n"

    for music in musics:
        indexCont += "<tr>\n"
        indexCont += "<td>" + music['name'] + "</td>\n"
        indexCont += "<td>" + str(music['year']) + "</td>\n"
        indexCont += "<td>" + music['album'] + "</td>\n"
        indexCont += "<td>" + music['band'] + "</td>\n"
        indexCont += "<td>" + music['genre'] + "</td>\n"
        indexCont += "</tr>\n"

    indexCont += "</table>\n"
    indexCont += """<table class = "button">
        <tr>
        <td><a href = "/add_page/"><input type="submit" value = "Add a music!"></a></td>
        <td><a href = "/assignment3/"><input type="submit" value = "List the musics"></a></td>
        </tr>
        </table>\n"""

    return htmlify("My lovely website", indexCont, CSS())

def add_page():
    addPageContent = """<form method = "post" action = "/add_submit/">
        <table class = "add">
        <tr><td>Name:</td><td><input type = "text" name = "name" value = ""></td></tr>
        <tr><td>Year:</td><td><input type = "number" name = "year" value = ""></td></tr>
        <tr><td>Album:</td><td><input type = "text" name = "album" value = ""></td></tr>
        <tr><td>Band:</td><td><input type = "text" name = "band" value = ""></td></tr>
        <tr><td>Genre:</td><td><input type = "text" name = "genre" value = ""></td></tr>
        <tr><td colspan ="2"><input type = "submit" value = "Add"></td></tr>
        <table>
        </form>
        """
    return htmlify("Add a music!", addPageContent, CSS())

route ('/add_page/', 'GET', add_page)

def add_submit():
    musicData = request.POST

    name = str(musicData['name'])
    year = int(musicData['year'])
    album = str(musicData['album'])
    band = str(musicData['band'])
    genre = str(musicData['genre'])

    global musics
    musics = musics + [{'name': name, 'year': year, 'album': album, 'band': band, 'genre': genre}]

    addSubmitContent = """
        <p>The music below has been added to the list</p>
        <table class = "music">
        <tr><th>Name:</th><td>""" + name + """</td></tr>
        <tr><th>Year:</th><td>""" + str(year) + """</td></tr>
        <tr><th>Album:</th><td>""" + album + """</td></tr>
        <tr><th>Band:</th><td>""" + band + """</td></tr>
        <tr><th>Genre</th><td>""" + genre + """</td></tr>
        <tr><td colspan = "2"><a href = "/assignment3/"><input type = "submit" value = "Return to the list"></a></td></tr>
        </table>
        """
    return htmlify("Music successfully added!", addSubmitContent, CSS())

route ('/add_submit/', 'POST', add_submit)

def website_index():
    return htmlify('My lovely homepage',
                   """
                   <!-- p><a href="/assignment1/">Click for my assignment 1.</a></p -->
                   <!-- p><a href="/assignment2/">Click for my assignment 2.</a></p -->
                   <p><a href="/assignment3/">Click for my assignment 3.</a></p>
                   """, '')

route('/assignment3/', 'GET', a3_index)
route('/', 'GET', website_index)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on PythonAnywhere
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on PythonAnywhere
application = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()
