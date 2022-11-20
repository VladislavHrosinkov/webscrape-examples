import bs4, requests, webbrowser

# Отваряме страницата с филми
film_url = "https://www.kinomania.bg/bg_BG/programa.html"
film_re = requests.get(film_url)
film_re.raise_for_status()
parser = bs4.BeautifulSoup(film_re.text, "html.parser")

# Намираме садържанието
links = []
index = 0
selection = parser.find_all("tr")
for tr in selection:
    tr_parser = bs4.BeautifulSoup(str(tr), "html.parser")
    try:
        print(tr_parser.find("td").text)
    except:
        continue
    for link in tr_parser.find_all("a"):
        film_text = link.get_text(separator=" ")
        link_url = link.get("href")
        links.append(link_url)
        print(index, " ", film_text)
        index += 1

while True:
    try:
        n = int(input("Кой линк да отворим?\n"))
        webbrowser.open(links[n])
    except:
        print("Не е валиден линк.")