from WikiAPI.WikiLinks import WikiLinks


if __name__ == '__main__':
    w = WikiLinks('countries.json', 'result.txt')
    for country, link in w:
        print(country, link)
