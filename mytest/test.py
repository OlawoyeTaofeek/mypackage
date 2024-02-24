from mypackages import mymodule


def test_top_n():
    """
    make sure that top_n works correctly
    """
    
    assert mymodule.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4], "incorrect top_n"
    assert mymodule.top_n([10, 1, 12, 9, 3], 2) == [12, 10], "incorrect top_n"
    assert mymodule.top_n([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], "incorrect top_n"