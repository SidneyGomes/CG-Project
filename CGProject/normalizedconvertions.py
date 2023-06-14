def ndcx(Xm, x, XM):

    print((x - Xm) / (XM - Xm))
    return (x - Xm) / (XM - Xm)


def ndcy(Ym, y, YM):
    print((y - Ym) / (YM - Ym))
    return (y - Ym) / (YM - Ym)


def dcx(ndh, ndcx):
    return round((ndcx * (ndh - 1)))


def dcy(ndv, ndcy):
    return round((ndcy * (ndv - 1)))
