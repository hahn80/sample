from titan.sample import Flower, upper_name


def test_flower():
    flower = Flower("IRIS")
    assert flower.name == "IRIS"


def test_upper_name():
    name = "titan"
    uppered_name = upper_name(name)
    assert uppered_name == "TITAN"


if __name__ == "__main__":
    test_flower()
    test_upper_name()
