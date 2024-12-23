def loe_seis(failinimi):
    fail = open(failinimi, "r")
    return fail.read()

print(loe_seis("turniir.txt"))