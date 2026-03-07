import feedparser

FEEDS = {
    'Brasil': 'https://g1.globo.com/rss/g1/',
    'Mundo': 'https://www.bbc.com/portuguese/index.xml'
}

def buscar_titulos():
    todos_os_titulos = []
    for local, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:10]: # Pegamos 10 de cada para ter mais amplitude
            todos_os_titulos.append(entry.title)
    return todos_os_titulos

if __name__ == "__main__":
    titulos = buscar_titulos()
    for t in titulos:
        print(f" {t}")
