# -*- coding: utf-8 -*-
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Parte 1, criar uma blockchain

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        # cria um novo dicionario para o bloco
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        # adiciona o novo block a blockchain
        self.chain.append(block)
        return block
