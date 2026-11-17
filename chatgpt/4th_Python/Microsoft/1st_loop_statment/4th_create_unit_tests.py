""" def calculate_discount(price: float, discount_percent: float) -> float:
    "Calculate price after applying a discount."
    return price * (1 - discount_percent / 100)

# Test it
def test_calculate_discount():
    # No discount should return original price
    result = calculate_discount(100, 0)
    assert result == 100, "No discount should return original price"
    
    # 50% discount should return half price
    result = calculate_discount(100, 50)
    assert result == 50, "50% discount should return half price"
    
    print("All tests passed!")

# Run the test
test_calculate_discount() """

