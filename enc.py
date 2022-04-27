#_* coding:utf-8 *_
# Start : 08-04-2021 15:03 WIB
# Done  : 08-04-2021 16:14 WIB

import sys as snif, os, marshal
from time import sleep as date

'''
!-- Note --!
         Kalo Mau Rikod Sertakan Sumber Peler
         Compile Marshal Only Python3 Not Support Python2
'''

exec(open("etc/.colors").read())

_black_ = lambda: print(f"""\n {red}╔═╗╦ ╦╔═╗╔═╗╔╦╗╔═╗╦╦  ╔═╗╦═╗\n {yellow}╠═╝╚╦╝║  ║ ║║║║╠═╝║║  ║╣ ╠╦╝\n {green}╩   ╩ ╚═╝╚═╝╩ ╩╩  ╩╩═╝╚═╝╩╚═  {purple}only python3\n {blue}=======================================\n {green}[{white}•{green}] {white}Creator   {red}: {yellow}Alvino_adijaya{green} & {black}kingtebe\n {green}[{white}•{green}] {white}Instagram {red}: {yellow}@mhff_xy\n {green}[{white}•{green}] {white}Github    {red}: {yellow}github.com/Al-Vino\n {green}[{white}•{green}] {white}Facebook  {red}: {yellow}legend.alvino\n {blue}=======================================\n""")

class Compile:

	def __init__(self):
		self._FaaL_ = "#----------------------------------------\n# Compile : Alvino\n# Facebook : legend.alvino\n# Github  : https://github.com/Al-Vino\n#----------------------------------------\nimport marshal\nexec(marshal.loads(%s))"
		self._Main_()

	def _Main_(self):
		__import__('os').system('clear')
		try:
			_black_()
			angka = 0
			file = input(f"  {red}➣ {white}Input File {yellow}: {green}")
			count = int(input(f"  {red}➣ {white}Jumlah {yellow}: {green}"))
			if ( count < 400 ):
				out = input(f"  {red}➣ {white}Output File {yellow}: {green}")
				ewe = open(file).read().encode('utf-8')
				xxx = compile(ewe, '<alvino>', 'exec')
				asu = repr(marshal.dumps(xxx))
				f = open(out, 'w')
				f.write(self._FaaL_ % asu)
				f.close()
				while ( count >= angka):
					meki = open(out).read().encode('utf-8')
					puki = compile(meki, '<alvino>', 'exec')
					peju = repr(marshal.dumps(puki))
					x = open(out, 'w')
					x.write(self._FaaL_ % peju)
					x.close()
					angka += 1
					date(1.2)
				exit(f"\n {green}[{white}•{green}] {white}Berhasil Tersimpan Di »» {green}{out} \n{white}")
		except ValueError:exit(f"\n {black}[ {white}Warning {red}! {white}Harus berupa angka babi {black}]\n")
		except FileNotFoundError:exit(f"\n {black}[ {white}Warning {red}! {white}File {yellow}{file} {white}Tidak Ditemukan {black}]\n")

if __name__=='__main__':
     Compile()
