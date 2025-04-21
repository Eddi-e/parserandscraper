import requests
import parser

def getisbn(title,surname,firstname):
    try:
        blacklistedisbns = parser.parseFile("blacklistedisbn.csv")
    except:
        print("if you want add a file to blacklist isbns create blacklistedisbn.csv (be sure to add a title row)")
        blacklistedisbns = []
    r = requests.get('https://www.googleapis.com/books/v1/volumes?q=intitle:'+title+' inauthor:'+firstname+' '+surname+'&printType=books&orderBy=relevance')
    jsonbooks = r.json()
    for item in jsonbooks['items']:
        volume_info = item['volumeInfo']
        authors = []
        for author in volume_info['authors']:
            authors.append(author.lower().split(" "))
        book_title = volume_info['title'].lower()
        if firstname.lower().split()[0] in authors[0] and surname.lower().split()[0] in authors[0]:
            if title.lower() == book_title or book_title == title.lower():   
                if 'industryIdentifiers' in volume_info:
                    for identifier in volume_info['industryIdentifiers']:
                        if identifier['type'] in ('ISBN_10','ISBN_13'):
                            id = (identifier['identifier']) 
                            if [str(id)] not in blacklistedisbns:
                                return id
                            


if __name__ == '__main__':
    print(getisbn("To the Lighthouse","Woolf","Virginia"))
    #getisbn("Demons","Dostoevsky","Fyodor")


    #identifier = r.json()['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier']