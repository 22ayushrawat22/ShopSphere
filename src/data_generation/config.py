from pathlib import Path


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
CLEANED_DATA_DIR = DATA_DIR / "cleaned"
PROCESSED_DATA_DIR = DATA_DIR / "processed"


# ============================================================
# DATASET SIZE
# ============================================================

N_CUSTOMERS = 20_000
N_PRODUCTS = 1_000
N_ORDERS = 100_000

AVG_ITEMS_PER_ORDER = 2

N_REVIEWS = 60_000
N_RETURNS = 15_000


# ============================================================
# DATE RANGE
# ============================================================

START_DATE = "2024-01-01"
END_DATE = "2025-12-31"


# ============================================================
# RANDOM SEED
# ============================================================

RANDOM_SEED = 42


# ============================================================
# CUSTOMER SETTINGS
# ============================================================

CUSTOMER_SEGMENT_DISTRIBUTION = {
    "one_time": 0.35,
    "occasional": 0.30,
    "regular": 0.25,
    "loyal": 0.10,
}


# ============================================================
# PRODUCT CATEGORIES
# ============================================================

PRODUCT_CATEGORIES = [
    "Electronics",
    "Fashion",
    "Home & Kitchen",
    "Beauty & Personal Care",
    "Sports & Fitness",
    "Books",
]


# ============================================================
# PAYMENT METHODS
# ============================================================

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Wallet",
    "COD",
]


# ============================================================
# ORDER STATUSES
# ============================================================

ORDER_STATUSES = [
    "Delivered",
    "Shipped",
    "Processing",
    "Cancelled",
    "Returned",
]


# ============================================================
# RETURN REASONS
# ============================================================

RETURN_REASONS = [
    "Damaged",
    "Wrong Product",
    "Size Issue",
    "Quality Issue",
    "Changed Mind",
    "Late Delivery",
    "Other",
]


# ============================================================
# INDIAN CITIES
# ============================================================

CITY_STATE_MAP = {
    "Delhi": "Delhi",
    "Mumbai": "Maharashtra",
    "Bengaluru": "Karnataka",
    "Hyderabad": "Telangana",
    "Chennai": "Tamil Nadu",
    "Kolkata": "West Bengal",
    "Pune": "Maharashtra",
    "Ahmedabad": "Gujarat",
    "Jaipur": "Rajasthan",
    "Lucknow": "Uttar Pradesh",
    "Chandigarh": "Chandigarh",
    "Surat": "Gujarat",
    "Indore": "Madhya Pradesh",
    "Bhopal": "Madhya Pradesh",
    "Nagpur": "Maharashtra",
    "Patna": "Bihar",
    "Noida": "Uttar Pradesh",
    "Gurugram": "Haryana",
    "Faridabad": "Haryana",
    "Kochi": "Kerala",
    "Coimbatore": "Tamil Nadu",
    "Visakhapatnam": "Andhra Pradesh",
    "Bhubaneswar": "Odisha",
    "Dehradun": "Uttarakhand",
    "Ranchi": "Jharkhand",
    "Kanpur": "Uttar Pradesh",
    "Varanasi": "Uttar Pradesh",
    "Agra": "Uttar Pradesh",
    "Nashik": "Maharashtra",
    "Ludhiana": "Punjab",
}
# ============================================================
# PRODUCT SUBCATEGORIES
# ============================================================

PRODUCT_SUBCATEGORIES = {
    "Electronics": [
        "Smartphones",
        "Laptops",
        "Headphones",
        "Smartwatches",
        "Tablets",
        "Cameras",
        "Accessories",
    ],

    "Fashion": [
        "T-Shirts",
        "Shirts",
        "Jeans",
        "Trousers",
        "Dresses",
        "Footwear",
        "Jackets",
    ],

    "Home & Kitchen": [
        "Cookware",
        "Furniture",
        "Kitchen Appliances",
        "Storage",
        "Home Decor",
        "Lighting",
    ],

    "Beauty & Personal Care": [
        "Skincare",
        "Haircare",
        "Makeup",
        "Fragrances",
        "Personal Care",
    ],

    "Sports & Fitness": [
        "Running",
        "Gym Equipment",
        "Yoga",
        "Outdoor Sports",
        "Sportswear",
    ],

    "Books": [
        "Fiction",
        "Non-Fiction",
        "Technology",
        "Business",
        "Self Help",
        "Academic",
    ],
}


# ============================================================
# PRODUCT BRANDS
# ============================================================

PRODUCT_BRANDS = {
    "Electronics": [
        "NovaTech",
        "PixelPro",
        "Voltix",
        "TechSphere",
        "Auralink",
        "ZenByte",
    ],

    "Fashion": [
        "UrbanThread",
        "StyleCraft",
        "StreetLine",
        "ModeWear",
        "TrendRoot",
        "ClassicFit",
    ],

    "Home & Kitchen": [
        "HomeNest",
        "KitchenPro",
        "CasaLiving",
        "UrbanHome",
        "ComfortCraft",
    ],

    "Beauty & Personal Care": [
        "GlowPure",
        "DermaCare",
        "AuraBeauty",
        "PureSkin",
        "BloomCare",
    ],

    "Sports & Fitness": [
        "FitCore",
        "ActivePro",
        "RunX",
        "SportEdge",
        "FlexFit",
    ],

    "Books": [
        "KnowledgeHouse",
        "PageTurner",
        "ReadMore",
        "InsightBooks",
        "LearnPress",
    ],
}