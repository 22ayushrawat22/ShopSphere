import random
from datetime import timedelta

import pandas as pd

from config import (
    N_ORDERS,
    RAW_DATA_DIR,
    RANDOM_SEED,
    ORDER_STATUSES,
)


# ============================================================
# CONFIGURATION
# ============================================================

random.seed(RANDOM_SEED)


# ============================================================
# ORDER GENERATION
# ============================================================

def generate_orders():

    print("Loading customer data...")

    customers_path = RAW_DATA_DIR / "customers.csv"

    customers = pd.read_csv(
        customers_path,
        parse_dates=["signup_date"]
    )

    print(
        f"Loaded {len(customers):,} customers."
    )


    # --------------------------------------------------------
    # PREPARE CUSTOMER DATA
    # --------------------------------------------------------

    customer_ids = customers["customer_id"].tolist()


    # --------------------------------------------------------
    # GENERATE ORDERS
    # --------------------------------------------------------

    orders = []

    print("Generating orders...")

    for i in range(1, N_ORDERS + 1):

        # ----------------------------------------------------
        # ORDER ID
        # ----------------------------------------------------

        order_id = f"O{i:06d}"


        # ----------------------------------------------------
        # SELECT CUSTOMER
        # ----------------------------------------------------

        customer_index = random.randrange(
            len(customers)
        )

        customer = customers.iloc[
            customer_index
        ]

        customer_id = customer["customer_id"]


        # ----------------------------------------------------
        # ORDER DATE
        # ----------------------------------------------------

        signup_date = customer["signup_date"]

        end_date = pd.Timestamp(
            "2025-12-31"
        )

        available_days = (
            end_date - signup_date
        ).days


        if available_days > 0:

            random_days = random.randint(
                0,
                available_days
            )

            order_date = (
                signup_date
                + timedelta(days=random_days)
            )

        else:

            order_date = signup_date


        # ----------------------------------------------------
        # ORDER STATUS
        # ----------------------------------------------------

        status = random.choices(
            ORDER_STATUSES,
            weights=[
                0.72,  # Delivered
                0.10,  # Shipped
                0.08,  # Processing
                0.05,  # Cancelled
                0.05,  # Returned
            ],
            k=1
        )[0]


        # ----------------------------------------------------
        # SALES CHANNEL
        # ----------------------------------------------------

        sales_channel = random.choices(
            [
                "Website",
                "Mobile App",
                "Marketplace"
            ],
            weights=[
                0.45,
                0.40,
                0.15
            ],
            k=1
        )[0]


        # ----------------------------------------------------
        # CREATE ORDER
        # ----------------------------------------------------

        order = {
            "order_id": order_id,
            "customer_id": customer_id,
            "order_date": order_date,
            "order_status": status,
            "sales_channel": sales_channel,
        }

        orders.append(order)


    # --------------------------------------------------------
    # CONVERT TO DATAFRAME
    # --------------------------------------------------------

    orders_df = pd.DataFrame(orders)

    return orders_df


# ============================================================
# SAVE DATASET
# ============================================================

def main():

    print("=" * 60)
    print("ShopSphere Order Generator")
    print("=" * 60)

    orders_df = generate_orders()

    output_path = RAW_DATA_DIR / "orders.csv"

    orders_df.to_csv(
        output_path,
        index=False
    )

    print()
    print(
        f"Generated {len(orders_df):,} orders."
    )

    print(
        f"Saved to: {output_path}"
    )

    print()
    print("First 5 orders:")
    print(
        orders_df.head()
    )

    print()
    print("Dataset shape:")
    print(
        orders_df.shape
    )

    print()
    print("Order status distribution:")
    print(
        orders_df["order_status"].value_counts()
    )

    print()
    print("Sales channel distribution:")
    print(
        orders_df["sales_channel"].value_counts()
    )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()