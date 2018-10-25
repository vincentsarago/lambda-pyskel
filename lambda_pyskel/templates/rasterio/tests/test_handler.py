from pyskel import handler


def test_handler_count():
    """Test the handler function"""
    assert handler.main(None, None) == "Maybe"
