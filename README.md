# 🌟 StellarTrain  
### _A Decentralized Micropayment System for Machine Learning Data Labeling & Competitions_  

---

## 🚀 Overview  
**StellarTrain** is a decentralized, trustless, and transparent platform for hosting machine learning challenges and managing **micropayments for data labeling**.  

It bridges **Problem Makers** (companies, DAOs, individuals) and **Problem Solvers** (data scientists, ML engineers) via blockchain-backed automation, ensuring **instant payments**, **zero trust**, and **verifiable fairness**.  

The MVP focuses on one key user loop:  
> **Maker creates a challenge → Solver submits a file → Backend grades → Smart contract releases payment.**

---

## 🧠 Core Concepts  

| Component | Description |
|------------|--------------|
| **Blockchain (Soroban/Stellar)** | Handles escrow, payments, and event logging. |
| **Backend (Flask + Web3.py)** | Manages authentication, challenge lifecycle, and evaluation. |
| **Frontend (React + Tailwind)** | User dashboard, wallet connection, and submission portal. |
| **Evaluation Engine** | Grades submissions using scikit-learn metrics. |
| **Decentralized Storage (IPFS)** | (Future) Ensures dataset integrity and versioning. |

---

## 🧩 System Architecture  

```text
User (Wallet) ─▶ Frontend (React, Tailwind)
        │
        ▼
 Backend (Flask, Celery, Redis, scikit-learn)
        │
        ▼
 Smart Contract (Soroban on Stellar Testnet)
        │
        ▼
 Payment Trigger & Verification (Web3.py)
```

---

## 🪙 Blockchain Components  

**Smart Contract:** `Challenge.sol`  

Functions:  
- `createChallenge(uint deadline)` → Maker creates a new challenge with a reward pool.  
- `releasePayment(uint challengeId, address solver)` → Admin wallet releases rewards post-evaluation.  

> _All payments and events are transparent and verifiable on-chain._

---

## 🧰 Tech Stack  

| Layer | Tools & Frameworks |
|--------|--------------------|
| **Blockchain** | Soroban, Web3.py, Stellar SDK |
| **Backend** | Flask, Celery (async jobs), Redis, SQLAlchemy, scikit-learn |
| **Frontend** | React, Tailwind CSS, Ethers.js |
| **Storage** | IPFS (future), PostgreSQL (MVP) |
| **Deployment** | Docker, AWS / Render / Railway (Backend), Vercel (Frontend) |

---

## ⚙️ MVP Features  

✅ Challenge Creation (on-chain escrow)  
✅ Wallet-based Sign-In (Freighter)  
✅ Secure Submission Upload  
✅ Real-time Evaluation (scikit-learn)  
✅ On-chain Payment Release  
✅ Score Dashboard + Tx Verification  

---

## 📅 25-Day Development Roadmap  

### **Phase 1: Foundations (Days 1–7)**  
- Project setup: `/contracts`, `/backend`, `/frontend`.  
- Implement and deploy `Challenge.sol` smart contract on Stellar testnet.  
- Test contract creation and reward locking.  

### **Phase 2: Backend & Evaluation (Days 8–14)**  
- Build Flask API and PostgreSQL schema.  
- Implement wallet-based login and authentication.  
- Create `/submit` endpoint for file upload and synchronous evaluation.  

### **Phase 3: Frontend & Web3 Integration (Days 15–21)**  
- Build React + Tailwind UI.  
- Implement wallet connect and signature-based login.  
- Create challenge dashboard and submission flow.  

### **Phase 4: Payment Automation & Deployment (Days 22–25)**  
- Integrate backend trigger to `releasePayment()` smart contract function.  
- Test end-to-end payment loop using testnet tokens.  
- Deploy MVP (backend + frontend).  

---

## 🧑‍💻 How It Works  

1. **Maker Flow**  
   - Connect wallet → Create challenge → Fund it on-chain.  

2. **Solver Flow**  
   - Connect wallet → Submit `.csv` file → Get evaluated automatically.  

3. **Backend Flow**  
   - Grades submission → If score ≥ threshold → Triggers smart contract.  

4. **Blockchain Flow**  
   - Smart contract verifies and sends payment → Transaction visible on explorer.  

---

## 🔒 Security & Fairness  

- **Sandboxed Evaluation** (Future via Docker) to prevent malicious code.  
- **SHA256 Submission Hashing** to detect duplicates.  
- **On-chain Reputation System** (Future) for makers and solvers.  
- **NFT Rewards** (Future) for leaderboard achievements.  

---

## 🧭 Future Research Directions  

| Area | Description |
|------|--------------|
| **zkML (Zero-Knowledge ML)** | Private model verification on-chain. |
| **Homomorphic Encryption** | Evaluation on encrypted data. |
| **Federated Challenges** | Data stays local; only gradients shared. |
| **Cross-Chain Interoperability** | Rewards in multiple blockchain ecosystems. |

---

## 🪄 Example User Flow  

**Maker:**  
```bash
1. Connect Freighter Wallet
2. Create a challenge with 2 test MATIC
3. Wait for submissions
```

**Solver:**  
```bash
1. Connect wallet and log in
2. View available challenges
3. Upload `solution.csv`
4. View accuracy score
5. Receive automatic on-chain payment
```

---

## 🧪 Local Development  

### Prerequisites   
- Python ≥ 3.10  
- Docker  
- MetaMask / Freighter Wallet (Testnet)  
- Stellar Testnet account with test tokens  

### Setup  

```bash
# Clone repo
git clone https://github.com/<yourusername>/StellarTrain.git
cd StellarTrain
cd backend
python app.py
```


**Frontend Setup**
```bash
cd frontend
npm install
npm start
```

**Contract Deployment**
```bash
cd contracts
npx hardhat compile
npx hardhat run scripts/deploy.js --network testnet
```

---

## 🔗 Environment Variables  

| Variable | Description |
|-----------|--------------|
| `ADMIN_PRIVATE_KEY` | Backend wallet key for contract execution |
| `RPC_URL` | Stellar testnet RPC endpoint |
| `CONTRACT_ADDRESS` | Deployed Challenge.sol address |
| `DB_URL` | PostgreSQL connection string |
| `SECRET_KEY` | Flask session key |

---

## 📤 Deployment  

- **Backend:** Render / Railway  
- **Frontend:** Vercel  
- **Smart Contract:** Stellar Testnet  
- **Database:** Railway PostgreSQL  

---

## 🧾 License  
MIT License © 2025 — **StellarTrain Team**

---

