import random

class Films:
    list_of_films = []
    def __init__(self, title, year, genre, number):
        self.title = title
        self.year = year
        self.genre = genre
        self.number = number
        self.list_of_films.append(self)
    def __str__(self):
        return f'"{self.title}" ({self.year})'
    def play(self, step = 1):
        self.number += step  

class Series(Films):
    list_of_series = []
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
        self.list_of_series.append(self)
    def __str__(self):
        return (f'"{self.title:}" S{self.season:02d}E{self.episode:02d}')
    def play(self, step = 1):
        self.number += step

film_1 = Films(title="Rambo 3", year="1989", genre="action", number=4)
film_2 = Films(title="Dune", year="2021", genre="asci-fi", number=5)
series_1 = Series(title="Cube", year="1999", genre="thriller", number=9, episode=2, season=1)
series_2 = Series(title="Alf", year="1989", genre="comedy", number=21, episode=4, season=2)
series_3 = Series(title="07 zgłoś się", year="1978", genre="criminal", number=19, episode=3, season=3)

list_of_all = [Films.list_of_films, Series.list_of_series]
list_simple = [film_1, film_2, series_1, series_2, series_3]


def get_movies():
    list_get_movies=[]
    for y in list_simple:
        if not isinstance(y, Series):
            list_get_movies.append(y.title)
    print(sorted(list_get_movies))

def get_series():
    list_get_series=[]
    for z in list_simple:
        if isinstance(z, Series):
            list_get_series.append(z.title)
    print(sorted(list_get_series))
def search():
  for i in list_simple:
    print(i.title)

def generate_views():
    f = random.choice(list_simple)
    n = random.randint(1,100)
    f.number = f.number + n
    print(f, f.number)

def generate_views_10():
   for i in range(10):
     generate_views()

def top_titles(x):
    d = {}
    for i in list_simple:
        da = {i.number: i.title}
        d.update(da)
    new_list = sorted(list(d.items()), reverse=True)
    print(new_list[:x])

get_movies()