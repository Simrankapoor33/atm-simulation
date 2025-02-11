import pandas as pd

def load_user_data():
    """
    Load user data from a hardcoded list.

    :return: DataFrame containing user data.
    """
    data = {
        'account_number': [123456789, 987654321, 234567890, 345678901],
        'pin': [1234, 5678, 9012, 3456],
        'balance': [1000, 2000, 5000, 6000]
    }
    return pd.DataFrame(data)