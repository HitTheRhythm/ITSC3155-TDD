def test_ProductQntNotZero(invoice, products):
    invoice.ProductQntNotZero(products)
    assert invoice.ProductQntNotZero(products) == True


def test_CanCalucateTotalQnt(invoice, products):
    invoice.totalQnt(products)
    assert invoice.totalQnt(products) == 10