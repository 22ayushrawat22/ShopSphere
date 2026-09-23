import random
import pandas as pd

from config import (
    RAW_DATA_DIR,
    RANDOM_SEED,
)


# ============================================================
# CONFIGURATION
# ============================================================

random.seed(RANDOM_SEED)

# Average number of products in an order
MIN_ITEMS_PER_ORDER = 1
MAX_ITEMS_PER_ORDER = 5


# ============================================================
# HELPER FUNCTION
# ============================================================

def find_price_column(products):

    possible_columns = [
        "price",
        "unit_price",
        "selling_price",
        "sale_price"
    ]

    for column in possible_columns:
        if column in products.columns:
            return column

    raise ValueError(
        "Could not find a product price column. "
        f"Available columns: {list(products.columns)}"
    )


# ============================================================
# GENERATE ORDER ITEMS
# ============================================================

def generate_order_items():

    print("Loading orders...")
    
    orders_path = RAW_DATA_DIR / "orders.csv"
    products_path = RAW_DATA_DIR / "products.csv"

    orders = pd.read_csv(
        orders_path,
        parse_dates=["order_date"]
    )

    print(
        f"Loaded {len(orders):,} orders."
    )


    # --------------------------------------------------------
    # LOAD PRODUCTS
    # --------------------------------------------------------

    print("Loading products...")

    products = pd.read_csv(
        products_path
    )

    print(
        f"Loaded {len(products):,} products."
    )


    # --------------------------------------------------------
    # FIND IMPORTANT PRODUCT COLUMNS
    # --------------------------------------------------------

    price_column = find_price_column(products)

    product_ids = products["product_id"].tolist()


    # Create a dictionary:
    # product_id → price

    product_prices = dict(
        zip(
            products["product_id"],
            products[price_column]
        )
    )


    # --------------------------------------------------------
    # GENERATE ORDER ITEMS
    # --------------------------------------------------------

    order_items = []

    print("Generating order items...")


    for _, order in orders.iterrows():

        order_id = order["order_id"]

        # ----------------------------------------------------
        # NUMBER OF ITEMS IN THIS ORDER
        # ----------------------------------------------------

        number_of_items = random.randint(
            MIN_ITEMS_PER_ORDER,
            MAX_ITEMS_PER_ORDER
        )


        # ----------------------------------------------------
        # SELECT UNIQUE PRODUCTS
        # ----------------------------------------------------

        selected_products = random.sample(
            product_ids,
            number_of_items
        )


        # ----------------------------------------------------
        # CREATE EACH ORDER ITEM
        # ----------------------------------------------------

        for product_id in selected_products:

            quantity = random.choices(
                [1, 2, 3, 4],
                weights=[
                    0.65,
                    0.22,
                    0.10,
                    0.03
                ],
                k=1
            )[0]


            # ------------------------------------------------
            # PRODUCT PRICE
            # ------------------------------------------------

            unit_price = product_prices[
                product_id
            ]


            # ------------------------------------------------
            # DISCOUNT
            # ------------------------------------------------

            discount_pct = random.choices(
                [0, 5, 10, 15, 20, 25],
                weights=[
                    0.30,
                    0.20,
                    0.25,
                    0.12,
                    0.08,
                    0.05
                ],
                k=1
            )[0]


            # ------------------------------------------------
            # CREATE RECORD
            # ------------------------------------------------

            order_item = {
                "order_id": order_id,
                "product_id": product_id,
                "quantity": quantity,
                "unit_price": round(
                    float(unit_price),
                    2
                ),
                "discount_pct": discount_pct
            }

            order_items.append(
                order_item
            )


    # --------------------------------------------------------
    # DATAFRAME
    # --------------------------------------------------------

    order_items_df = pd.DataFrame(
        order_items
    )

    return order_items_df


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 60)
    print("ShopSphere Order Items Generator")
    print("=" * 60)

    order_items_df = generate_order_items()


    # --------------------------------------------------------
    # SAVE
    # --------------------------------------------------------

    output_path = (
        RAW_DATA_DIR /
        "order_items.csv"
    )

    order_items_df.to_csv(
        output_path,
        index=False
    )


    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    print()

    print(
        f"Generated "
        f"{len(order_items_df):,} order items."
    )

    print(
        f"Saved to: {output_path}"
    )

    print()

    print("First 10 order items:")

    print(
        order_items_df.head(10)
    )

    print()

    print("Dataset shape:")

    print(
        order_items_df.shape
    )

    print()

    print("Total quantity sold:")

    print(
        order_items_df["quantity"].sum()
    )

    print()

    print("Average discount:")

    print(
        f"{order_items_df['discount_pct'].mean():.2f}%"
    )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()