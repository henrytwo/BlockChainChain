import urllib.request
import urllib

def get_key(user):
    new_keys = set()

    response = urllib.request.urlopen('https://keybase.pub/'+user)
    if response.getcode() == 200:
        data = [x for x in str(response.read()).split("\\n") if "<td class=\"name-col\"><a href=\"https://keybase.pub/henrytwo/" in x]
        files = []
        for file in data:
            if "class=\"file\"" in file:
                for word in file.split("\""):
                    if ".pub" in word:
                        files.append(word)
                        break
        for key in files:
            print("Checking file:", "https://"+user + ".keybase.pub/"+key.split("/")[-1]+"?dl=1")
            data = urllib.request.urlopen("https://"+user + ".keybase.pub/"+key.split("/")[-1]+"?dl=1")
            if response.getcode() == 200:
                new_keys.add(str(data.read().decode('utf-8')))

    return new_keys


if __name__ == "__main__":
    get_key("henrytwo")
