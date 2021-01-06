import colorio


def test_show():
    # cs = colorio.cs.CIELAB()
    # cs = colorio.cs.CIEHCL()
    # cs = colorio.cs.CIELCH()
    # cs = colorio.cs.OsaUcs()
    # cs = colorio.cs.IPT()
    cs = colorio.cs.CAM16UCS(0.69, 20, 4.074)
    colorio.data.luo_rigg.show(cs, 50)
    colorio.data.luo_rigg.savefig("out.png", cs, 50)


def test_residuals():
    cs = colorio.cs.CIELAB()
    ref = 18.379222659827946
    res = colorio.data.luo_rigg.residuals(cs, 0.5)
    print(res)
    assert abs(res - ref) < 1.0e-14 * ref


if __name__ == "__main__":
    test_show()
    # test_residuals()
