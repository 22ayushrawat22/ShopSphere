# ============================================================
# ShopSphere - Payment Data Generator
# ============================================================

import pandas as pd
import numpy as np
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

ORDERS_PATH = BASE_DIR / "data" / "raw" / "orders.csv"
ORDER_ITEMS_PATH = BASE_DIR / "data" / "raw" / "order_items.csv"
OUTPUT_PATH = BASE_DIR / "data" / "raw" / "payments.csv"


# ============================================================
# 2. RANDOM SEED
# ============================================================

np.random.seed(42)


# ============================================================
# 3. LOAD DATA
# ============================================================

def load_data():

    print("Loading orders...")
    orders = pd.read_csv(
        ORDERS_PATH,
        parse_dates=["order_date"]
    )

    print("Loading order items...")
    order_items = pd.read_csv(ORDER_ITEMS_PATH)

    return orders, order_items


# ============================================================
# 4. CALCULATE ORDER VALUE
# ============================================================

def calculate_order_totals(order_items):

    # Calculate original price before discount
    order_items["gross_amount"] = (
        order_items["quantity"]
        * order_items["unit_price"]
    )

    # Calculate discount amount
    order_items["discount_amount"] = (
        order_items["gross_amount"]
        * order_items["discount_pct"]
        / 100
    )

    # Calculate final amount after discount
    order_items["net_revenue"] = (
        order_items["gross_amount"]
        - order_items["discount_amount"]
    )

    # Add all item values belonging to the same order
    order_totals = (
        order_items
        .groupby("order_id", as_index=False)["net_revenue"]
        .sum()
        .rename(columns={"net_revenue": "order_amount"})
    )

    return order_totals


# ============================================================
# 5. GENERATE PAYMENT DATA
# ============================================================

def generate_payments(orders, order_totals):

    # Combine orders with their calculated value
    payments = orders.merge(
        order_totals,
        on="order_id",
        how="left"
    )

    # --------------------------------------------------------
    # Payment ID
    # --------------------------------------------------------

    payments["payment_id"] = [
        f"PAY{i:07d}"
        for i in range(1, len(payments) + 1)
    ]

    # --------------------------------------------------------
    # Payment Date
    # --------------------------------------------------------

    payment_delay = np.random.randint(
        0,
        4,
        size=len(payments)
    )

    payments["payment_date"] = (
        payments["order_date"]
        + pd.to_timedelta(payment_delay, unit="D")
    )

    # --------------------------------------------------------
    # Payment Method
    # --------------------------------------------------------

    payment_methods = [
        "UPI",
        "Credit Card",
        "Debit Card",
        "Net Banking",
        "Wallet",
        "Cash on Delivery"
    ]

    payment_probabilities = [
        0.38,
        0.22,
        0.16,
        0.10,
        0.06,
        0.08
    ]

    payments["payment_method"] = np.random.choice(
        payment_methods,
        size=len(payments),
        p=payment_probabilities
    )

    # --------------------------------------------------------
    # Payment Status
    # --------------------------------------------------------

    payments["payment_status"] = "Successful"

    # Cancelled orders
    cancelled_mask = (
        payments["order_status"]
        .str.lower()
        == "cancelled"
    )

    payments.loc[
        cancelled_mask,
        "payment_status"
    ] = np.random.choice(
        ["Refunded", "Failed"],
        size=cancelled_mask.sum(),
        p=[0.70, 0.30]
    )

    # Returned orders
    returned_mask = (
        payments["order_status"]
        .str.lower()
        == "returned"
    )

    payments.loc[
        returned_mask,
        "payment_status"
    ] = "Refunded"

    # Small percentage of normal payments fail
    successful_mask = (
        payments["payment_status"]
        == "Successful"
    )

    successful_indices = payments.index[successful_mask]

    if len(successful_indices) > 0:

        failed_count = max(
            1,
            int(len(successful_indices) * 0.03)
        )

        failed_indices = np.random.choice(
            successful_indices,
            size=failed_count,
            replace=False
        )

        payments.loc[
            failed_indices,
            "payment_status"
        ] = "Failed"

    # --------------------------------------------------------
    # Payment Amount
    # --------------------------------------------------------

    payments["payment_amount"] = payments["order_amount"]

    # Failed payments don't represent collected money
    payments.loc[
        payments["payment_status"] == "Failed",
        "payment_amount"
    ] = 0

    # --------------------------------------------------------
    # Select final columns
    # --------------------------------------------------------

    payments = payments[
        [
            "payment_id",
            "order_id",
            "payment_date",
            "payment_method",
            "payment_status",
            "payment_amount"
        ]
    ]

    return payments


# ============================================================
# 6. SAVE DATA
# ============================================================

def save_data(payments):

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    payments.to_csv(
        OUTPUT_PATH,
        index=False
    )

    print()
    print("Payments generated successfully!")
    print()
    print("Dataset shape:")
    print(payments.shape)

    print()
    print("Payment status:")
    print(payments["payment_status"].value_counts())

    print()
    print("Payment methods:")
    print(payments["payment_method"].value_counts())

    print()
    print("Total payment value:")
    print(
        round(
            payments["payment_amount"].sum(),
            2
        )
    )

    print()
    print("Sample:")
    print(payments.head())


# ============================================================
# 7. MAIN
# ============================================================

def main():

    orders, order_items = load_data()

    print()
    print("Calculating order totals...")

    order_totals = calculate_order_totals(
        order_items
    )

    print(
        f"Calculated totals for "
        f"{len(order_totals):,} orders."
    )

    print()
    print("Generating payments...")

    payments = generate_payments(
        orders,
        order_totals
    )

    save_data(payments)


# ============================================================
# 8. ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()