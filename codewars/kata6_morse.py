# -*- coding: utf-8 -*-
# codewars kata6_morse.py

MORSE_CODE = {".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F", "--.":"G", "....":"H", 
"..":"I", ".---":"J", "-.-":"K", ".-..":"L", "--":"M", "-.":"N", "---":"O", ".--.":"P", "-.-":"Q", 
".-.":"R", "...":"S", "-":"T", "..-":"U", "...-":"V", ".--":"W", "-..-":"X", "-.--":"Y", "--..":"Z", 
"-----":"0", ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", 
"---..":"8", "----.":"9", ".-.-.-":".", "---...":":", "--..--":",", "-.-.-.":";", "..--..":"?", 
"-...-":"=", ".----.":"'", "-..-.":"/", "-.-.--":"!", "-....-":"-", "..--.-":"_", ".-..-.":'"', 
"-.--.":"(", "-.--.-":")", "...-..-":"$", ". ...":"&", ".--.-.":"@"}

def decodeMorse(morseCode):
	# s = [w.split(' ') for w in morseCode.strip().split('   ')]
	# r = '
	# for w in s:
			# r += ''.join([MORSE_CODE[c] for c in w]) + ' '
	# return r.strip().replace(' ES ', ' & ')
	return ' '.join(''.join(MORSE_CODE[c] for c in l.split(" ")) for l in  morseCode.strip().split('   ')).replace(' ES ', ' & ')
	#return  ''.join([MORSE_CODE.get(l,' ') for l in  morseCode.strip().split(' ')]).replace('  ',' ').replace(' ES ', ' & ')

def main():
	s='.... . -.--   .--- ..- -.. .   . ...   ....'
	print(decodeMorse(s))
	#decodeMorse(s)

if __name__ == '__main__':
	main()
