import random
from datetime import datetime

import pandas as pd
from faker import Faker

from config import (
    N_CUSTOMERS,
    RAW_DATA_DIR,
    RANDOM_SEED,
    CITY_STATE_MAP,
)


# ============================================================
# CONFIGURATION
# ============================================================

random.seed(RANDOM_SEED)

fake = Faker("en_IN")
fake.seed_instance(RANDOM_SEED)


# ============================================================
# CUSTOMER GENERATION
# ============================================================

def generate_customers():
    """Generate the ShopSphere customer master dataset."""

    customers = []

    cities = list(CITY_STATE_MAP.keys())

    for i in range(1, N_CUSTOMERS + 1):

        customer_id = f"C{i:05d}"

        gender = random.choice(
            ["Male", "Female"]
        )

        first_name = fake.first_name_male() if gender == "Male" else fake.first_name_female()

        last_name = fake.last_name()

        date_of_birth = fake.date_of_birth(
            minimum_age=18,
            maximum_age=65
        )

        city = random.choice(cities)

        state = CITY_STATE_MAP[city]

        pincode = fake.postcode()

        signup_date = fake.date_between(
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2025, 12, 31)
        )

        customer = {
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "date_of_birth": date_of_birth,
            "city": city,
            "state": state,
            "pincode": pincode,
            "signup_date": signup_date,
            "customer_type": "Customer",
        }

        customers.append(customer)

    df = pd.DataFrame(customers)

    return df


# ============================================================
# SAVE DATASET
# ============================================================

def main():

    print("Generating customers...")

    customers_df = generate_customers()

    output_path = RAW_DATA_DIR / "customers.csv"

    customers_df.to_csv(
        output_path,
        index=False
    )

    print(f"Generated {len(customers_df):,} customers.")

    print(f"Saved to: {output_path}")

    print("\nFirst 5 rows:")
    print(customers_df.head())

    print("\nDataset shape:")
    print(customers_df.shape)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()