import pandas as pd


def find_customers(
    visits: pd.DataFrame, transactions: pd.DataFrame
) -> pd.DataFrame:
    visit_id = transactions["visit_id"].drop_duplicates()
    mask = ~visits["visit_id"].isin(visit_id)
    return (
        visits[mask]["customer_id"]
        .value_counts()
        .reset_index(name="count_no_trans")
    )


data = [[1, 23], [2, 9], [4, 30], [5, 54], [6, 96], [7, 54], [8, 54]]
visits = pd.DataFrame(data, columns=["visit_id", "customer_id"]).astype(
    {"visit_id": "Int64", "customer_id": "Int64"}
)
data = [[2, 5, 310], [3, 5, 300], [9, 5, 200], [12, 1, 910], [13, 2, 970]]
transactions = pd.DataFrame(
    data, columns=["transaction_id", "visit_id", "amount"]
).astype({"transaction_id": "Int64", "visit_id": "Int64", "amount": "Int64"})

print(find_customers(visits, transactions))
#    customer_id  count_no_trans
# 0           54               2
# 1           30               1
# 2           96               1
