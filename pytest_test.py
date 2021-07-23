import pytest

from system.checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_price('test_item_1', 1)
    checkout.add_item_price('test_item_2', 2)
    return checkout


def test_can_calculate_total(checkout):
    checkout.add_item('test_item_1')
    assert checkout.calculate_total() == 1


def test_can_calculate_total_with_multiple_items(checkout):
    checkout.add_item('test_item_1')
    checkout.add_item('test_item_2')
    assert checkout.calculate_total() == 3


def test_can_add_discount_rule(checkout):
    checkout.add_discount('test_item_1', 3, 2)


def test_can_apply_discount_rule(checkout):
    checkout.add_discount('test_item_1', 3, 2)
    checkout.add_item('test_item_1')
    checkout.add_item('test_item_1')
    checkout.add_item('test_item_1')
    assert checkout.calculate_total() == 1


def test_bad_item_exception(checkout):
    with pytest.raises(Exception):
        checkout.add_item('test_bad_item')
