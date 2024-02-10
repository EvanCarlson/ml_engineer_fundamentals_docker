import pandas as pd


if __name__ == "__main__":
    print("Let's print an example Dataframe below:")
    df = pd.DataFrame(
        {
            "Make": ["Subaru", "Subaru", "Toyota"],
            "Model": ["Forester", "Outback", "Tacoma"]
        }
    )
    print(df.head())
