#! python3

'''
It would be nice if I could simply type a search term on the command line and have my computer automatically open a browser with all the top search results in new tabs. Let’s write a script to do this.
This is what your program does:

 - Gets search keywords from the command line arguments.

 - Retrieves the search results page.

 - Opens a browser tab for each result.
'''
# webbrowser to open tabs; requests to get info from webs;
# and sys to read arguments in the command line
import webbrowser, requests, sys, bs4

# Step 1: Get the Command Line Arguments and Request the Search Page
if len(sys.argv) == 1:
    print('No arguments passed')
else:
    toSearch = sys.argv[1:]
    req = requests.get('https://www.google.com/search?q=' + '+'.join(toSearch))
    try:
        # Step 2: Find All the Results
        req.raise_for_status()
        print('Status: {}'.format(req.status_code))
        soup = bs4.BeautifulSoup(req.text, 'html.parser')

        # Here I had a big problem. I never got any links from the HTML that
        # I was inspecting in Firefox. It seems that Google returns a different
        # HTML that the one that Firefox shows you. Therefore, there is no class
        # "r" (as shown in the browser) and ".r a" doesn't return anything.
        # 'Soup' shows another class, "kCrYT" that gets you the result.

        links = soup.select('.kCrYT > a')

        for link in range(5):

            # Now, every link comes with an initial "/url?q="
            # hence the '[7:]' to get rid of it.
            # There's also some added part after the '&' character,
            # so split() helps us remove that part.

            formatted_link = links[link].get('href')[7:].split('&')[0]
            webbrowser.open_new_tab(formatted_link)

    except Exception as exc:
        print('There was a problem: %s' % (exc))
