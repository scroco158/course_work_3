from src import utils


def test_operations_loading():
    operations = utils.operations_loading()
    assert len(operations) == 101


def test_operation_sorting():
    operation = utils.operations_loading()
    operation = utils.operations_sort(operation)
    assert len(operation) == 5
