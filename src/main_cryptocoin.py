from blgncoin import Blockchain
from uuid import uuid4
from flask import Flask, jsonify, request

# Mining a Blockchain
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

node_address = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block() # last block of the chain
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(sender = node_address, receiver = 'Myself', amount = 1)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions': block['transactions']}
    return jsonify(response), 200

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

@app.route('/add_transactions', methods = ['POST'])
def add_transations():
    data = request.get_json(cache=False) # Don't forget to add cache=False

    if not ('sender' in data and 'receiver' in data and 'amount' in data):
        return 'You should provide all the necessary data', 400
    
    index = blockchain.add_transaction(data['sender'], data['receiver'], data['amount'])

    response = {'message': f'This transaction will be added to Block {index}'}

    return jsonify(response), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)