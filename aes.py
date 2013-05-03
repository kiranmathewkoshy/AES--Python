#!/usr/bin/env python

from Crypto.Cipher import AES
import base64
import os

def Encrypt_AES(key,plaintext):
	BLOCK_SIZE = 32
	PADDING = '{'
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
	cipher = AES.new(pad(key))
	encoded = EncodeAES(cipher, plaintext)
	return encoded

def Decrypt_AES(key,ciphertext):
	BLOCK_SIZE = 32
	PADDING = '{'
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	cipher = AES.new(pad(key))
	decoded = DecodeAES(cipher, ciphertext)
	return decoded

if __name__=='__main__':
	key='password'
	text='AES Encryption'
	print 'Original String= '+text
	print 'Key= '+key
	a=Encrypt_AES(key,text)
	print 'Cipher= '+a
	print 'Decrypted String= '+Decrypt_AES(key,a)	