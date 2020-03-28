#!/usr/bin/env python

from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from argparse import ArgumentParser, FileType

def decrypt_config(enc_file):
  # Hardcoded AES key
  key = (
    b'\x92\x9C\x9B\x2C\xF3\x15\x77\x11'
    b'\xE2\x2D\xB9\x78\xA2\xFF\x23\x37'
    b'\xC3\x1A\xE5\x8C\x8E\x65\xEE\x87'
    b'\x3D\x64\x01\x1A\x7E\x4C\xEF\x3E'
  )
  
  # Cipher mode is AES-ECB
  cipher = AES.new(
    key,
    AES.MODE_ECB
  )
  
  # Decode from base64
  ciphertext = b64decode(
    enc_file.read()
  )
  
  # Decrypt and remove padding
  plaintext = unpad(
    cipher.decrypt(
      ciphertext
    ),
    AES.block_size
  ).decode('utf-8')
  
  return plaintext

def get_args():
  parser = ArgumentParser()
  parser.add_argument(
    "file",
    type=FileType('r'),
  )
  args = parser.parse_args()
  return args


def main():
  args = get_args()
  
  plaintext = decrypt_config(
    args.file
  )
  
  print(
    plaintext
  )

if __name__ == '__main__':
  main()