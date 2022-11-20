import bs4, requests, webbrowser

# Отваряме страницата с филми
film_url = "https://www.kinomania.bg/bg_BG/programa.html"
film_re = requests.get(film_url)
film_re.raise_for_status()
parser = bs4.BeautifulSoup(film_re.text, "html.parser")

# Намираме садържанието
links = []
for index, link in enumerate(parser.select("td > a")):
    film_text = link.get_text(separator=" ")
    link_url = link.get("href")
    links.append(link_url)
    print(index, " ", film_text)
    # if film_text != "Купи билет":
    #    print(film_text)

while True:
    try:
        n = int(input("Кой линк да отворим?\n"))
        webbrowser.open(links[n])
    except:
        print("Цяло число моля.")