t = 0
ymax = 0
ymax_local = 0 # without this line, ymax_local will only defined in the first if, error will occur at line 10
while t < 5:
    y = -t * (t - 2)
    if y > ymax:
        ymax = y
        ymax_local = ymax # a local copy of ymax
    print(f"t={t}, y={y}, ymax={ymax}")
    if ymax_local > 0:
        print(f"ymax_local={ymax_local}")
    t = t + 1