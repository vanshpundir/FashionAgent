from typing import Optional, List, Dict, Union

def search_aggregator(name: Optional[str] = None, color: Optional[str] = None, price_range: Optional[List[float]] = None, size: Optional[str] = None) -> List[Dict[str, Union[str, float]]]:
    """
    Search for products based on specified criteria.

    Args:
        name (Optional[str]): Name of the product.
        color (Optional[str]): Color of the product.
        price_range (Optional[List[float]]): Price range for the product as [min, max].
        size (Optional[str]): Size of the product.

    Returns:
        List[Dict[str, Union[str, float]]]: List of products matching the search criteria.
    """
    # Simulated product database
    all_products = [
        {"name": "florat skirt", "color": "Blue", "price": 35.99, "size": "S"},
        {"name": "Floral Skirt", "color": "Pink", "price": 42.50, "size": "S"},
        {"name": "White Sneakers", "color": "White", "price": 65.00, "size": "8"},
        {"name": "casual Denim Jacket", "color": "Blue", "price": 80.00, "size": "M"},
        {"name": "Cocktail Dress", "color": "Red", "price": 120.00, "size": "M"}
    ]

    # Filter products based on search criteria
    
    return all_products

def shipping_time_estimator(user_location: str, delivery_date: str) -> Dict[str, Union[int, bool]]:
    """
    Estimate shipping time and feasibility.

    Args:
        user_location (str): The location of the user.
        delivery_date (str): The desired delivery date.

    Returns:
        Dict[str, Union[int, bool]]: Estimated shipping time and feasibility.
    """
    # Simulated shipping estimation logic
    shipping_times = {
        "New York": 3,
        "Los Angeles": 5,
        "Chicago": 4
    }
    estimated_days = shipping_times.get(user_location, 7)
    return {
        "estimated_days": estimated_days,
        "feasibility": estimated_days <= 7
    }

def discount_promo_checker(base_price: float, promo_code: str) -> Dict[str, Union[float, bool]]:
    """
    Check and apply discount promo codes.

    Args:
        base_price (float): The original price of the product.
        promo_code (str): The promo code to be applied.

    Returns:
        Dict[str, Union[float, bool]]: Discounted price and validity of the promo code.
    """
    # Simulated promo code logic
    promo_discounts = {
        "SAVE10": 0.10,
        "SAVE20": 0.20
    }
    discount = promo_discounts.get(promo_code, 0)
    discounted_price = base_price * (1 - discount)
    return {
        "discounted_price": discounted_price,
        "valid": discount > 0
    }

def competitor_price_comparison(product_name: str) -> List[Dict[str, Union[str, float]]]:
    """
    Compare prices from various competitors.

    Args:
        product_name (str): The name of the product to compare.

    Returns:
        List[Dict[str, Union[str, float]]]: Price comparisons from different sites.
    """
    # Simulated competitor price comparison
    competitor_prices = {
        "Floral Skirt": [35.99, 37.50, 34.99],
        "White Sneakers": [65.00, 64.50, 66.00],
        "casual denim jacket": [61.00, 60.50, 66.00],
    }
    prices = competitor_prices.get(product_name, [])
    return [{"site": f"Site{i+1}", "price": price} for i, price in enumerate(prices)]

def return_policy_checker(site_name: str) -> Dict[str, Union[str, bool]]:
    """
    Check return policy details for a specified site.

    Args:
        site_name (str): The name of the e-commerce site.

    Returns:
        Dict[str, Union[str, bool]]: Return policy details.
    """
    # Simulated return policy details
    return_policies = {
        "SiteA": {
            "return_window": "30 days",
            "free_returns": True,
            "condition": "Unworn with tags"
        },
        "SiteB": {
            "return_window": "14 days",
            "free_returns": False,
            "condition": "Original packaging"
        },
        "SiteC": {
            "return_window": "45 days",
            "free_returns": True,
            "condition": "No questions asked"
        }
    }
    return return_policies.get(site_name, {"error": "Site not found"})
