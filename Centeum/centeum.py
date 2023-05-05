import time
import subprocess
import os
import socket
import uuid
import os
import hashlib
import json
import base64
import uuid
import random
import sys
import string
from datetime import datetime
from ecdsa import SigningKey



CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'
END = '\033[0m'

print("Loading Centeum console")
animation = "|/-\\|"
for i in range(20):
   time.sleep(0.1)
   sys.stdout.write("\r"+animation[i % len(animation)])
   sys.stdout.flush()
sys.stdout.write("\n")

amount = 0
transfercount = 0
blockchainis = True
difficulty = 0
domine = False
iswallet = False
walletclose = False


def get_genesis_block():
   def genesis():
      return Block(0, "0", 1465154705, "genesis block", 0, 0,
         "816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7")

def get_prev_block():
   return self._chain[-1]


class Block(object):
   def __init__(self, index, previous_hash, timestamp, data,difficulty_bits, nonce, hash):
      self.index = index
      self.previous_hash = previous_hash
      self.timestamp = timestamp
      self.data = data
      self.difficulty_bits = difficulty_bits
      self.nonce = nonce
      self.hash = hash

class Blockchain(object):
   def __init__(self):

      self._chain = [self.get_genesis_block()]
      self.difficulty_bits = 0

   @property
   def chain(self):
      return self.dict(self._chain)

   def dict(self, chain):
      return json.loads(json.dumps(chain, default=lambda o: o.__dict__))  
      
      def __init__(self):

         self._chain = [self.get_genesis_block()]
         self.difficulty_bits = 0



def mine(difficulty):
   global amount
   global walletid
   global walletclose
   if walletclose == True:
   	print("> wallet is closed")
   options = [0.8, 1, 1.7, 1.9, 2.6, 0.4, 2.9]
   option = random.choice(options)
   private_key = SigningKey.generate()
   signature = private_key.sign(b"Centeum")
   for ebid in range(1):
      alphabet = list(string.ascii_lowercase)
      alphabet2 = list(string.ascii_uppercase)
      num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
      phase1 = random.choice(alphabet)
      phase2 = random.choice(alphabet)
      phase3 = random.choice(alphabet2)
      phase4 = random.choice(alphabet2)
      phase5 = random.choice(num)
      phase6 = random.choice(num)
      phase = str(phase1 + phase2 + phase3 + phase4 + phase5 + phase6).encode()
      phase = hashlib.sha256(phase).hexdigest()
      phase = hashlib.sha256(signature).hexdigest()
      block = phase
      time.sleep(option)
      sys.stdout.write(f"> hash {CBLUE}{CSELECTED}{block}{END} / {CGREEN}+0.500{END}CEN\n")
      amount += 0.500



while True:
   cent = input(f"[centeum] >")
   if "new user/utils/wallet" == cent:
      alphabet = list(string.ascii_lowercase)
      alphabet2 = list(string.ascii_uppercase)
      num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
      phase1 = random.choice(alphabet)
      phase2 = random.choice(alphabet)
      phase3 = random.choice(alphabet2)
      phase4 = random.choice(alphabet2)
      phase5 = random.choice(num)
      phase6 = random.choice(num)
      phase = str(phase1 + phase2 + phase3 + phase4 + phase5 + phase6).encode()
      walletid = hashlib.sha256(phase).hexdigest()

      print(f"Wallet ID: {walletid}")

      iswallet = True
   if "set console=start" == cent:
      if iswallet == False:
         print("> no locations found to store Centeum coins")
         exit()
      domine = True
      continue
   if domine == True:
      mine(10)
   if "set console=off" == cent:
      domine = False

   if "wallet.showbalance" == cent:
      print(f"> balance / {CGREEN}{amount}{END}CEN")
   if "wallet.cancel" == cent:
      cancelwallet = input("Cancelling your wallet will delete your wallet, so your money will not be recoverable [Y/n] ").lower()
      if cancelwallet == "y":
         iswallet = False
         amount = 0
         print(f"> wallet cancelled")
         continue