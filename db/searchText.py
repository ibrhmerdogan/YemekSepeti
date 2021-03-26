#text search işlemi yapmaktadır ve aranan textin içerilip içermediğini döndürü 0/1

#text ="text serach işlemi yapmaktadır iişlemleriii ve aranan textin içerilip içermediğini döndürü 0/1"
#searchText = "era"

def _searchFunction(text,sarchText):
    if  text.count(sarchText) > 0 :
        return 1
    else:
        return 0

#print(_searchFunction(text,searchText))