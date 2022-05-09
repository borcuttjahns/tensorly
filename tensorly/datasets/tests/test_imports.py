from ..data_imports import IL2data, load_covid19_serology


def test_IL2data():
    """ Test that data import dimensions match. """
    data = IL2data()

    tensor = data["tensor"]
    assert tensor.shape[0] == len(data["ticks"][0])
    assert tensor.shape[1] == len(data["ticks"][1])
    assert tensor.shape[2] == len(data["ticks"][2])
    assert tensor.shape[3] == len(data["ticks"][3])


def test_COVID19_data():
    """ Test that data import dimensions match. """
    data = load_covid19_serology()

    tensor = data["tensor"]
    assert tensor.shape[0] == len(data["ticks"][0])
    assert tensor.shape[1] == len(data["ticks"][1])
    assert tensor.shape[2] == len(data["ticks"][2])

