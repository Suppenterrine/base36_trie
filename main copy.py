import numpy as np


base_ids = []
base_const = 36

"""
	solarSystem: "Druzotune",
	planet: "Alpha Ganacci",
	land: DE,
	prefecture: "Chizaki",
	village: "Akashima",
	building: "Haus der Yukihira's",
"""

for base in range(0, 2):
    bnum = base

    base_ids.append(
        {
            # "id": np.base_repr(bnum, base_const),
            "id": bnum,
            str(base): []
        }
    )

    print(bnum,f"\t{base}\t{np.base_repr(bnum, base_const)}")


    for sec in range(0, 3):
        snum = int(f"{base}{sec}")

        base_ids[base][str(base)].append(
            {
                # "id": np.base_repr(snum, base_const),
                "id": f"{base}{sec}",
                str(sec): []
            }
        )

        print(snum,f"\t{base}{sec}\t{np.base_repr(snum, base_const)}")


        for third in range(0, 2):
            tnum = int(f"{base}{sec}{third}")

            base_ids[base][str(base)][sec][str(sec)].append(
                {
                    # "id": np.base_repr(tnum, base_const),
                    "id": f"{base}{sec}{third}",
                    str(third): third
                }
            )
            print(tnum,f"\t{base}{sec}{third}\t{np.base_repr(tnum, base_const)}")
    


print(base_ids)