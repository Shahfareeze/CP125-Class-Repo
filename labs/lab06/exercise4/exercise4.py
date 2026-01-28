def synchronize_databases(legacy_list, modern_set, blacklist):
    clean_legacy = set()
    for item in legacy_list:
        if item[1] not in blacklist:
            clean_legacy.add(item[0])

    lost_id = clean_legacy - modern_set
    ghost_id = modern_set - clean_legacy


    return (lost_id, ghost_id)

Legacy= [(101, "ali@mail.com"), (102, "sara@mail.com")]
Modern_IDs= {101, 105}
Blacklist = {"sara@mail.com"}
result = synchronize_databases(Legacy, Modern_IDs, Blacklist)
print (result)
