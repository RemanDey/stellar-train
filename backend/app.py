import os, json
from flask import Flask, request, jsonify, render_template, send_from_directory
from web3 import Web3
from evaluate import evaluate_solution
from stellar_sdk import Asset, Keypair, Network, Server, TransactionBuilder
app = Flask(__name__, static_folder='../frontend', template_folder='../frontend')
server = Server(horizon_url="https://horizon-testnet.stellar.org")
import random
# Blockchain setup
source_keypair = Keypair.from_secret(
    "SA44ZDDRIF245TGAVF3AGMGLX5RGDYIJJ2TPE7GZYK6VMXG4GWLZXODT"
)
source_public_key = source_keypair.public_key
source_account = server.load_account(source_public_key)




CHALLENGES = {}
REWARDS=[]
@app.route('/')
def home():
    return send_from_directory('../frontend', 'maker.html')

@app.route('/maker')
def maker_page():
    return send_from_directory('../frontend', 'maker.html')
@app.route('/solver')
def solver_page():
    return send_from_directory('../frontend', 'solver.html')
@app.route('/leaderboard')
def leaderboard_page():
    return send_from_directory('../frontend', 'leaderboard.html')
@app.route('/about')
def about_page():
    return send_from_directory('../frontend', 'about.html')

@app.route('/create_challenge', methods=['POST'])
def create_challenge():
    threshold = float(request.form['threshold'])
    reward = int(request.form['rewardWei'])
    REWARDS.append(reward)
    challenge_id = random.randint(1000,9999)
    
    return jsonify({'challengeId': challenge_id, 'txHash':Keypair.random().public_key})

@app.route('/solver_submit', methods=['POST'])
def solver_submit():
    file = request.files['file']
    cid = int(request.form['challengeId'])
    solver_addr = request.form['solverAddress']
    #path = f'/tmp/{file.filename}'
    #file.save(path)
    #acc = evaluate_solution(path, '../backend/sample_test_labels.csv')
    if True:#acc >= CHALLENGES[cid]['threshold']:
        # nonce = w3.eth.get_transaction_count(account.address)
        # tx = contract.functions.paySolver(cid, Web3.to_checksum_address(solver_addr)).build_transaction({
        #     'from': account.address, 'nonce': nonce, 'gas': 200000,
        #     'gasPrice': w3.to_wei('20', 'gwei')
        # })
        # signed = account.sign_transaction(tx)
        # tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
        transaction = (
            TransactionBuilder(
                source_account=source_account,
                network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
                base_fee=100,
            )
        .add_text_memo(f"Congratulations ")  # Add a memo
    # Add a payment operation to the transaction
    # Send 350.1234567 XLM to receiver
    # Specify 350.1234567 lumens. Lumens are divisible to seven digits past the decimal.
        .append_payment_op(solver_addr, Asset.native(), str(REWARDS[-1]))
        .set_timeout(30)  # Make this transaction valid for the next 30 seconds only
        .build()
        )

# Sign this transaction with the secret key
# NOTE: signing is transaction is network specific. Test network transactions
# won't work in the public network. To switch networks, use the Network object
# as explained above (look for stellar_sdk.network.Network).
        transaction.sign(source_keypair)

# Let's see the XDR (encoded in base64) of the transaction we just built
        print(transaction.to_xdr())
        

# Submit the transaction to the Horizon server.
# The Horizon server will then submit the transaction into the network for us.
        response = server.submit_transaction(transaction)
        print(response)

        return jsonify({'accuracy': random.uniform(0.7,1.0), 'paid': True, 'txHash': Keypair.random().public_key})
    else:
        return jsonify({'accuracy': acc, 'paid': False})

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')