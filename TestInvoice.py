import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalucateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalucateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalucateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

# this test case is to make sure the quantity of product is not zero
def test_ProductQntNotZero(invoice, products):
    invoice.ProductQntNotZero(products)
    assert invoice.ProductQntNotZero(products) == True

# this test case is to test the total quantity of products
def test_CanCalucateTotalQnt(invoice, products):
    invoice.totalQnt(products)
    assert invoice.totalQnt(products) == 15
