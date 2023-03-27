def getBibliothequeCount():
    result = _rc.request("select count(*) from public.bc_bib_etageres")
    return result 