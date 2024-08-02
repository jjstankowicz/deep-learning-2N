from dl2np.utils import get_path


def test_get_path():
    out = get_path()
    condition = isinstance(out, str)
    out_str = str(type(out))
    error_str = f"Expected type(out) == str. Received type(out) == {out_str}."
    assert condition, error_str
