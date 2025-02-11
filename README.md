# ATM Simulation

This project simulates an ATM machine, allowing users to perform various banking operations such as checking account balances, withdrawing cash, depositing cash, changing PINs, and viewing transaction history.

## Features

- **Account Balance Inquiry**: Check the current balance of your account.
- **Cash Withdrawal**: Withdraw cash from your account.
- **Cash Deposit**: Deposit cash into your account.
- **PIN Change**: Change your account PIN for security.
- **Transaction History**: View a history of all transactions made.

## Project Structure

```
atm-simulation
├── src
│   ├── atm.py          # Main entry point for the ATM simulation
│   ├── account.py      # Account management functionalities
│   ├── transaction.py   # Transaction history management
│   └── utils
│       └── __init__.py # Utility functions
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd atm-simulation
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the ATM simulation, execute the following command:
```
python src/atm.py
```

Follow the on-screen instructions to interact with the ATM system.