def price_after_discount(price: float, discount_percent: float) -> float:
    """Return price after applying a percentage discount."""
    if not discount_percent:
        return 0
    return price * (1 - discount_percent / 100)
