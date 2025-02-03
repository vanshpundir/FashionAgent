
def get_search_agg_prompt():
    return """Search for products based on specified criteria. Parameters: name, color, price_range, size."""

def get_shipping_time_estimator_prompt():
    return """Estimate shipping time and feasibility. Parameters: user_location, delivery_date."""

def get_discount_promo_checker_prompt():
    return """Check and apply discount promo codes. Parameters: base_price, promo_code."""

def get_competitor_price_comparison_prompt():
    return """Compare prices from various competitors. Parameter: product_name."""

def get_return_policy_checker_prompt():
    return """Check return policy details for a specified site. Parameter: site_name."""