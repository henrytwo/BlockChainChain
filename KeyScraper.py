import urllib.request
import urllib
import sha256frompubkey

keynames = {}

def get_key(user):
    global keynames

    new_keys = set()

    response = urllib.request.urlopen('https://keybase.pub/'+user+'/gatekeeper')
    if response.getcode() == 200:
        data = [x for x in str(response.read()).split("\\n") if "<td class=\"name-col\"><a href=\"https://keybase.pub/%s/" % user in x]
        files = []
        for file in data:
            if "class=\"file\"" in file:
                for word in file.split("\""):
                    if ".pub" in word:
                        files.append(word)
                        break
        for key in files:
            print("Checking file:", "https://"+user + ".keybase.pub/gatekeeper/"+key.split("/")[-1]+"?dl=1")
            data = urllib.request.urlopen("https://"+user + ".keybase.pub/gatekeeper/"+key.split("/")[-1]+"?dl=1")
            if response.getcode() == 200:
                k = str(data.read().decode('utf-8')).strip()
                new_keys.add(k)

                keynames[sha256frompubkey.sha256_fingerprint_from_pub_key(k)] = key.split("/")[-1]

    return new_keys


if __name__ == "__main__":
    get_key("henrytwo")
