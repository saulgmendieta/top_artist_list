import requests


def show_header():
    
    print("|------------------------|")
    print("|---- Music Top Data ----|")
    print("|------------------------|")


def show_options():
    
    genre = input("Choose the genre (1. Rock, 2. Pop, 3. Latin, 4. Disco, 5. Metal)")

    try:
        intgengre = int(genre)
        if intgengre>0 and intgengre<=5:
            return intgengre
        else:
            return 0
    except:
        return 0


def get_data(option):

    genre = ''
    
    if option == 0:
        print('Not valid choice given...')
    elif option == 1:
        genre='rock'
    elif option == 2:
        genre='pop'
    elif option == 3:
        genre='latin'
    elif option == 4:
        genre='disco'
    elif option == 5:
        genre='metal'
    else:
        print('Not valid choice given...')

    if genre != '':
        url = 'http://ws.audioscrobbler.com/2.0/?method=tag.gettopartists&'\
              f'tag={genre}&api_key=3a7505a1aa65c1e90e7d13d439349635&format=json'
        resp = requests.get(url)

        if resp.status_code in {400,404,500}:
            return None

        data = resp.json()

        topartists = data.get('topartists').get('artist')

        top_five_artists = []

        for i in range(0,5):
            top_five_artists.append(topartists[i].get('name'))

        return top_five_artists
        
    else:
        return None
        


def print_data(data):

    if data != None:
        print('The results are: ')

        c = 1
        for artist in data:
            print(f"{c}. {artist}")
            c+=1


def main():
    option = 0
    show_header()

    while option == 0:

        option = show_options()
        
        data = get_data(option)

        print_data(data)


if __name__ == "__main__":

    main()
