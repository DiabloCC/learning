# -*- coding: utf-8 -*-
# codewars kata4_morse.py

MORSE_CODE = {".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F", "--.":"G",
"....":"H", "..":"I", ".---":"J", "-.-":"K", ".-..":"L", "--":"M", "-.":"N", "---":"O", 
".--.":"P", "--.-":"Q", ".-.":"R", "...":"S", "-":"T", "..-":"U", "...-":"V", ".--":"W", 
"-..-":"X", "-.--":"Y", "--..":"Z", ".----":"1", "..---":"2", "...--":"3", "....-":"4", 
".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", ".-.-.-":".", "--..--":",", 
"..--..":"?", ".----.":"'", "-.-.--":"!", "-..-.":"/", "-.--.":"(", "-.--.-":")", 
".-...":"&", "---...":":", "-.-.-.":";", "-...-":"=", ".-.-.":"+", "-....-":"-", 
"..--.-":"_", ".-..-.":'"', "...-..-":"$", ".--.-.":"@"}

def decodeBits(bits):
	# ToDo: Accept 0's and 1's, return dots, dashes and spaces
	b = bits[bits.find('1'):bits.rfind('1')+1]
	unit = i = b.find('0')
	if unit == -1:
		return '.'
	thissum = 1
	while i < len(b) - 1:
		if b[i+1] == b[i]:
			thissum += 1
		else:
			if thissum < unit:
				unit = thissum
			thissum = 1
		i += 1
	#if unit == len(b):
	#	return '.'
	print(unit)
	return b.replace('0000000' * unit, '   ').replace('000' * unit, ' ').replace('111' * unit, '-').replace('1' * unit, '.').replace('0' * unit, '')

def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return ''.join([MORSE_CODE.get(c,' ') for c in morseCode.strip().split(' ')]).replace('  ',' ').replace(' ES ',' & ')

def main():
	#bits = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
	# result = 'HEY JUDE'
	bits = '111111000000111111'
	print(decodeBits(bits))
	print(decodeMorse(decodeBits(bits)))

if __name__ == '__main__':
	main()