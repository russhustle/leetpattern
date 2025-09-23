import os

import pandas as pd

companies = [
    "Amazon",
    "Google",
    "Microsoft",
    "Meta",
    "Apple",
    "PayPay",
    "OpenAI",
    "Databricks",
    "ByteDance",
    "Bloomberg",
]
files = [
    "1.%20Thirty%20Days.csv",
    "2.%20Three%20Months.csv",
    "3.%20Six%20Months.csv",
    "4.%20More%20Than%20Six%20Months.csv",
    "5.%20All.csv",
]


def name_to_url(name: str, filename: str) -> str:
    url = "https://raw.githubusercontent.com/"
    url += "liquidslr/leetcode-company-wise-problems/refs/heads/main/"
    url += f"{name}/{filename}"
    return url


def url_to_problem_list(url: str) -> list[str]:
    company_wise_df = pd.read_csv(url)
    database = os.path.join(os.path.dirname(__file__), "questions.parquet")
    database = pd.read_parquet(database)
    merged_df = pd.merge(
        company_wise_df,
        database,
        left_on="Title",
        right_on="title",
        how="left",
    )
    merged_df.dropna(subset=["QID"], inplace=True)
    merged_df["QID"] = merged_df["QID"].astype(int)
    problem_list = merged_df["QID"].tolist()
    return problem_list


if __name__ == "__main__":
    for company in sorted(companies):
        url = name_to_url(company, files[2])
        problems = url_to_problem_list(url)
        print(f"    {company}: {problems[:30]}")
