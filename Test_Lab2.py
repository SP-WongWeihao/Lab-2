import Lab2 as Lab2

def test_min_max():
    input_arr = [4, 5, 6, 8, 2]
    test_arr = (2, 8)
    result = Lab2.calc_min_max(input_arr)
    assert (result == test_arr)

def test_calc_average():
    input_arr = [5, 6, 7, 8, 24]
    test_result = 10
    result = Lab2.calc_average(input_arr)
    assert (result == test_result)

def test_calc_median():
    input_arr = [5, 3, 4, 8, 2]
    test_result = 4
    result = Lab2.calc_median_temperature(input_arr)
    assert (result == test_result)