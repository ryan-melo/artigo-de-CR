# Esse código serve para realizaer o scraping do site e salvar todas as informações em um arquivo txt

import requests
from bs4 import BeautifulSoup

class Musica:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def __repr__(self):
        return f"'{self.titulo}' by {self.artista}"

class Data:
    def __init__(self, data):
        self.data = data
        self.posicoes = {}

    def adicionar_musica(self, posicao, musica):
        self.posicoes[posicao] = musica

    def __repr__(self):
        return f"Data: {self.data}, Músicas: {self.posicoes}"

datas = ['2010-01-04', '2010-01-11', '2010-01-18', '2010-01-25', '2010-02-01', '2010-02-08', '2010-02-15', '2010-02-22', '2010-03-01', '2010-03-08', '2010-03-15', '2010-03-22', '2010-03-29', '2010-04-05', '2010-04-12', '2010-04-19', '2010-04-26', '2010-05-03', '2010-05-10', '2010-05-17', '2010-05-24', '2010-05-31', '2010-06-07', '2010-06-14', '2010-06-21', '2010-06-28', '2010-07-05', '2010-07-12', '2010-07-19', '2010-07-26', '2010-08-02', '2010-08-09', '2010-08-16', '2010-08-23', '2010-08-30', '2010-09-06', '2010-09-13', '2010-09-20', '2010-09-27', '2010-10-04', '2010-10-11', '2010-10-18', '2010-10-25', '2010-11-01', '2010-11-08', '2010-11-15', '2010-11-22', '2010-11-29', '2010-12-06', '2010-12-13', '2010-12-20', '2010-12-27']

dados = []

for y in datas:
    link = f"https://www.billboard.com/charts/hot-100/{y}/"
    
    requisicao = requests.get(link)
    site = BeautifulSoup(requisicao.text, "html.parser")

    musics = site.find_all('ul', class_='o-chart-results-list-row')

    data_obj = Data(data=y)

    for entry in musics[:5]:
        if entry:
            position_tag = entry.find('span', class_='c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet')
            position = position_tag.get_text(strip=True) if position_tag else 'Posição não encontrada'

            title_tag = entry.find('h3', class_='c-title')
            title = title_tag.get_text(strip=True) if title_tag else 'Título não encontrado'

            artist_classes = [
                'c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only',
                'c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet'
            ]

            artist_tag = None
            for cls in artist_classes:
                artist_tag = entry.find('span', class_=cls)
                if artist_tag:
                    break

            artist = artist_tag.get_text(strip=True) if artist_tag else 'Artista não encontrado'

            musica = Musica(titulo=title, artista=artist)

            data_obj.adicionar_musica(posicao=position, musica=musica)
        else:
            print('Entrada não encontrada')

    dados.append(data_obj)
            
for data in dados:
    print(data)


with open('ranking_musicas_2010.txt', 'w', encoding='utf-8') as file:
    for data in dados:
        file.write(f"Data: {data.data}\n")
        
        if data.posicoes:
            for posicao, musica in data.posicoes.items():
                file.write(f"  Posição {posicao}: {musica.titulo} by {musica.artista}\n")
        else:
            file.write("  Nenhuma música encontrada\n")
        
        file.write("\n")

print("Dados escritos no arquivo 'ranking_musicas_2010.txt'.")