#!/usr/bin/env python
import os,sys,time
from pyfiglet import Figlet
from random import choice
cout = 0
me = '\x1b[1;31m';ku = '\x1b[1;32m';hi = '\x1b[1;33m';bi = '\x1b[1;34m';ab = '\x1b[1;35m';cy = '\x1b[1;36m';pu = '\x1b[1;37m';col = [me,ku,hi,bi,ab,cy,pu];gas = choice(col);f = Figlet(font='shadow').renderText('Decompile');menu = Figlet(font='graffiti').renderText('Menu Decompile');mars = Figlet(font='graffiti').renderText('Decompile')
tanya = f'{pu}[{me}?{pu}] '
salah = f'{pu}[{me}!{pu}] '
def memegh():
	global cout
	cout = 0
	print(f'{mars}')
	print(f'{pu}DECOMPILE BERLAPIS {cy}[ {bi}MARSHAL {cy}| {bi}MARSHAL,ZLIB {cy}| {bi}MARSHAL,ZLIB,BASE64 {cy}]')
	try:
#		file = raw_input('File : ')
		file = input(f'{tanya}File : ')
#		out = raw_input('Output : ')
		out = input(f'{tanya}Output : ')
#		cot = int(raw_inpur('Lapis : '))
		cot = int(input(f'{tanya}Jumlah : '))
		if cot < 500:
			inp = open(file).read().replace('exec','x = ')
			cok = open('ih.py','w')
			cok.write('from sys import *\nfrom decompyle3.main import decompile\n' + inp + '\ndecompile(3.8, x, stdout)')
			cok.close()
			os.system('python ih.py > '+out)
			while True:
				if cot >= cout:
					q = open(out).read().replace('exec','x = ')
					w = open('ah.py','w')
					e = out.replace('','')
					if 'marshal' in q:
						w.write('from sys import *\nfrom decompyle3.main import decompile\n' + q + '\ndecompile(3.8, x, stdout)')
						w.close()
					elif 'marshal' not in q:
						w.write(q+'\nprint(x)')
						w.close()
						break
						sys.exit()
					os.system('python ah.py > '+e)
					cout += 1
					continue
				break
			for memek in range(cot):
				print(f'{pu}Suksess {ku}'+str(memek+1))
		else:
			print(f'\a{salah}melebihi batas !!!')
	except ValueError:
		print(f'\a{salah}kontol')
	except KeyboardInterrupt:
		print(f'\a{salah}ctrl-C Detected')
	except EOFError:
		print(f'\a{salah}ctrl-D Detected')

def kintil():
	global cout
	cout = 0
	print(f'{gas}{f}')
	print(f'{pu}DECOMPILE {cy}[ {ku}BASE64 {cy}]')
	try:
		file = input(f'{tanya}File : ')
		out = input(f'{tanya}Output : ')
		jml = int(input(f'{tanya}Jumlah : '))
		if jml < 500:
			a = open(file).read().replace('exec','print')
			b = open('ih.py','w')
			b.write(f'# memek\n{a}')
			b.close()
			os.system(f'python2 ih.py > {out}')
			while True:
				if jml >= cout:
					c = open(out).read().replace('exec','print')
					d = open('ah.py','w')
					e = out.replace('','')
					if 'base64' in c:
						d.write(f'# Memegh\n{c}')
						d.close()
					elif 'base64' not in c:
						print(f'{salah}Bukan base64')
						break
						sys.exit()
					os.system(f'python2 ah.py > {e}')
					cout += 1
					continue
				break
			for kontol in range(jml):
				print(f'{pu}Suksess {ku}'+str(kontol+1))
		else:
			print(f'{salah}Melebihi batas !!!')
	except ValueError:
		print(f'{salah}Memegh')
	except KeboardInterrupt:
		print(f'{salah}ctrl-C Detected')
	except EOFError:
		print(f'{salah}ctrl-D Detected')

def jembod():
	global cout
	cout = 0
	print(f'{gas}{f}')
	print(f'{pu}DECOMPILE {cy}[ {ku}ZLIB {cy}]')
	try:
		file = input(f'{tanya}File : ')
		out = input(f'{tanya}Output : ')
		jml = int(input(f'{tanya}Jumlah : '))
		if jml < 500:
			a = open(file).read().replace('exec','print')
			b = open('ih.py','w')
			b.write(f'# memek\n{a}')
			b.close()
			os.system(f'python2 ih.py > {out}')
			while True:
				if jml >= cout:
					c = open(out).read().replace('exec','print')
					d = open('ah.py','w')
					e = out.replace('','')
					if 'zlib' in c:
						d.write(f'# Memegh\n{c}')
						d.close()
					elif 'zlib' not in c:
						print(f'{salah}Bukan zlib')
						break
						sys.exit()
					os.system(f'python2 ah.py > {e}')
					cout += 1
					continue
				break
			for kontol in range(jml):
				print(f'{pu}Suksess {ku}'+str(kontol+1))
		else:
			print(f'{salah}Melebihi batas !!!')
	except ValueError:
		print(f'{salah}Memegh')
	except KeboardInterrupt:
		print(f'{salah}ctrl-C Detected')
	except EOFError:
		print(f'{salah}ctrl-D Detected')
"""
# Tak pikir ada hex di py3 :v
def mymyc():
	global cout
	cout = 0
	print(f'{gas}{f}')
	print(f'{pu}DECOMPILE BERLAPIS {cy}[ {ku}HEX {cy}]')
	try:
		file = input(f'{tanya}File : ')
		out = input(f'{tanya}Output : ')
		jml = int(input(f'{tanya}Jumlah : '))
		if jml < 500:
			a = open(file).read().replace('exec','print')
			b = open('ih.py','w')
			b.write(f'# Bau Memegh\n{a}')
			b.close()
			os.system(f'python ih.py > {out}')
			while True:
				if jml >= cout:
					c = open(out).read().replace('exec','print')
					d = open('ah.py','w')
					e = out.replace('','')
					if 'hex' in c:
						d.write(f'# Bau Tytydh\n{c}')
						d.close()
					elif 'hex' not in c:
						print(f'{salah}Ini bukan hex')
						break
					os.system(f'python ah.py > {e}')
					cout += 1
					continue
				break
			for kontol in range(jml):
				print(f'[{kontol}] Suksess')
		else:
			print(f'{salah}Melebihi batas !!!')
	except ValueError:
		print(f'{salah}Memegh')
	except EOFError:
		print(f'{salah}ctrl-D Detected')
	except KeyboardInterrupt:
		print(f'{salah}ctrl-C Detected')"""
def main():
	os.system('clear')
	print(f'{gas}{menu}{ku}PYTHON')
	while True:
		print(f'{bi}='*20)
		print(f'{pu}[{me}1{pu}] Base64 [ {hi}berlapis{pu} ]\n{pu}[{me}2{pu}] Zlib [ {hi}berlapis{pu} ]\n{pu}[{me}3{pu}] Marshal [ {hi}berlapis{pu} ]\n{pu}[{me}4{pu}] Marshal,Zlib [ {hi}berlapis{pu} ]\n{pu}[{me}5{pu}] Marshal,Zlib,Base64 [ {hi}berlapis{pu} ]')
		print(f'{bi}='*20)
		pilih = input(f'{tanya}Pilih : ')
		if pilih in ['1','01']:
			kintil()
		elif pilih in ['2','02']:
			jembod()
#		elif pilih in ['3','03']:
#			mymyc()
		elif pilih in ['3','4','5','03','04','05']:
			memegh()
		else:
			print(f'{salah}Pilihan yang kamu pilih tidak tersedia')
if __name__ == '__main__':
	main()

