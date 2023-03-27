from typing import Self


def getBibliothequeCount():
    result = Self._rc.request("select count(*) from public.bc_bib_etageres")
    return result 