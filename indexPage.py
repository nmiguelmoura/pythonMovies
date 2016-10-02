import os
import webbrowser
import re

#head of html
main_page_head = '''
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
                <title>Title</title>
                <meta name="viewport" content="width=device-width">
                <link rel="stylesheet" type="text/css" href="css/indexStyle.css">
        </head>
'''

#body of html(needs divs for all movies)
main_page_body = '''
        <body>
            <header>
                <h1>Movies list</h1>
            </header>
            <div class="wrapper">
                <div class="row">
                    {movies_placeholder}
                </div>
            </div>
            <div class="modal-window-trailer">
                <div class="video"></div>
                <img class="close-btn" src="assets/closeBtn.png" alt="close">
            </div>
            <footer>
                <p>Nuno Machado</p>
            </footer>
            <script type="text/javascript" src="src/main.min.js"></script>
        </body>
</html>
'''

#div to be created for each movie(needs title, poster and youtube_id from each movie)
movie_tile_content = '''
                    <div class="movie-tile sm-6-12 md-4-12 lg-4-12">
                        <div class="info">
                            <img src="https://image.tmdb.org/t/p/w600_and_h900_bestv2/{poster}" alt="{title}" data-youtube-id="{youtube_id}" data-overview="{overview}">
                            <h2 data-youtube-id="{youtube_id}" data-overview="{overview}">{title}</h2>
                        </div>
                    </div>
'''

#create movie tiles
def create_movie_tile(list_of_movies):
    #create variable content to store all movie tiles
    content = ''

    #loop through all movies in list
    for mov in list_of_movies:
        #use regular expressions to search for youtube id
        id = re.search(r'(?<=v=)[^&#]+', mov.trailer)
        id = id or re.search(r'(?<=be/)[^&#]+', mov.trailer)
        youtube_id = id.group(0) if id else None

        #add movie tile with each movie info to content
        content += movie_tile_content.format(
            title=mov.title,
            poster=mov.poster,
            youtube_id=youtube_id,
            overview=mov.overview
        )

    #get content
    return content


#generate and open page
def open_movies_page(list_of_movies):
    #open file and rewrite if already exists
    output_file = open('pyGeneratedIndex.html', 'w')

    #get all movies div and put them in body {movies_placeholder}
    rendered_content = main_page_body.format(movies_placeholder=create_movie_tile(list_of_movies))

    #write file with page_head and body plus movie divs
    output_file.write(main_page_head + rendered_content)

    output_file.close()

    #get url path
    url = os.path.abspath(output_file.name)

    #open file in browser
    webbrowser.open('file://' + url)
