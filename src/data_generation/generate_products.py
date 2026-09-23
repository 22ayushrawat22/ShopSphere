import random
from datetime import date

import pandas as pd
from faker import Faker

from config import (
    N_PRODUCTS,
    RAW_DATA_DIR,
    RANDOM_SEED,
    PRODUCT_CATEGORIES,
    PRODUCT_SUBCATEGORIES,
    PRODUCT_BRANDS,
)


# ============================================================
# CONFIGURATION
# ============================================================

random.seed(RANDOM_SEED)

fake = Faker("en_IN")
fake.seed_instance(RANDOM_SEED)


# ============================================================
# PRICE RANGES
# ============================================================

PRICE_RANGES = {
    "Electronics": (300, 80000),
    "Fashion": (300, 8000),
    "Home & Kitchen": (200, 25000),
    "Beauty & Personal Care": (150, 6000),
    "Sports & Fitness": (250, 20000),
    "Books": (100, 2500),
}


# ============================================================
# PRODUCT NAME COMPONENTS
# ============================================================

PRODUCT_ADJECTIVES = [
    "Premium",
    "Classic",
    "Advanced",
    "Smart",
    "Ultra",
    "Essential",
    "Pro",
    "Elite",
    "Everyday",
    "Modern",
]


# ============================================================
# GENERATE PRODUCTS
# ============================================================

def generate_products():

    products = []

    for i in range(1, N_PRODUCTS + 1):

        # ----------------------------------------------------
        # PRODUCT ID
        # ----------------------------------------------------

        product_id = f"P{i:05d}"


        # ----------------------------------------------------
        # CATEGORY
        # ----------------------------------------------------

        category = random.choice(PRODUCT_CATEGORIES)


        # ----------------------------------------------------
        # SUBCATEGORY
        # ----------------------------------------------------

        subcategory = random.choice(
            PRODUCT_SUBCATEGORIES[category]
        )


        # ----------------------------------------------------
        # BRAND
        # ----------------------------------------------------

        brand = random.choice(
            PRODUCT_BRANDS[category]
        )


        # ----------------------------------------------------
        # PRODUCT NAME
        # ----------------------------------------------------

        adjective = random.choice(PRODUCT_ADJECTIVES)

        product_name = (
            f"{brand} {adjective} {subcategory}"
        )


        # ----------------------------------------------------
        # PRICE
        # ----------------------------------------------------

        min_price, max_price = PRICE_RANGES[category]

        selling_price = random.randint(
            min_price,
            max_price
        )

        selling_price = round(
            selling_price / 10
        ) * 10


        # ----------------------------------------------------
        # COST PRICE
        # ----------------------------------------------------

        margin_rate = random.uniform(
            0.20,
            0.55
        )

        cost_price = selling_price * (
            1 - margin_rate
        )

        cost_price = round(
            cost_price / 10
        ) * 10


        # ----------------------------------------------------
        # STOCK
        # ----------------------------------------------------

        stock_quantity = random.randint(
            0,
            500
        )


        # ----------------------------------------------------
        # PRODUCT RATING
        # ----------------------------------------------------

        rating = round(
            random.triangular(
                2.5,
                5.0,
                4.2
            ),
            1
        )


        # ----------------------------------------------------
        # LAUNCH DATE
        # ----------------------------------------------------

        launch_date = fake.date_between(
    start_date=date(2023, 1, 1),
    end_date=date(2025, 6, 30)
)

        # ----------------------------------------------------
        # CREATE RECORD
        # ----------------------------------------------------

        product = {
            "product_id": product_id,
            "product_name": product_name,
            "category": category,
            "subcategory": subcategory,
            "brand": brand,
            "selling_price": selling_price,
            "cost_price": cost_price,
            "stock_quantity": stock_quantity,
            "rating": rating,
            "launch_date": launch_date,
        }

        products.append(product)


    # --------------------------------------------------------
    # CONVERT TO DATAFRAME
    # --------------------------------------------------------

    df = pd.DataFrame(products)

    return df


# ============================================================
# SAVE DATASET
# ============================================================

def main():

    print("Generating products...")

    products_df = generate_products()

    output_path = RAW_DATA_DIR / "products.csv"

    products_df.to_csv(
        output_path,
        index=False
    )

    print(
        f"Generated {len(products_df):,} products."
    )

    print(
        f"Saved to: {output_path}"
    )

    print("\nFirst 5 products:")

    print(
        products_df.head()
    )

    print("\nDataset shape:")

    print(
        products_df.shape
    )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()