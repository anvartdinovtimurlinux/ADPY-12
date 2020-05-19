import json
import wikipedia


class WikiLinks:
    def __init__(self, path_to_datafile, path_to_recordfile):
        with open(path_to_datafile, encoding='utf-8') as f:
            data_from_file = json.load(f)
        self.countries = [country['name']['official'] for country in data_from_file]
        self.path_to_recordfile = path_to_recordfile
        self.start = -1
        self.end = len(self.countries)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration

        country = self.countries[self.start]
        try:
            page = wikipedia.page(country)
        except wikipedia.WikipediaException:
            page = wikipedia.page('{} country'.format(country))
        with open(self.path_to_recordfile, 'a', encoding='utf-8') as f:
            f.write('{} - {}\n'.format(country, page.url))

        return country, page.url
