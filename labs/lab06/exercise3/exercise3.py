def audit_blocklists(list_a, list_b, list_c):

    universal = list_a & list_b & list_c
    redundant = (list_a & list_b | list_b & list_c | list_a & list_c)
    unique_a = list_a - (list_b | list_c)
    final_result = (universal, redundant, unique_a)
    return final_result



list_a = {"malware.exe", "virus.zip"}
list_b ={"virus.zip", "adware.dmg"}
list_c = {"virus.zip", "spyware.exe","malware.exe"}
result = audit_blocklists(list_a, list_b,list_c)
print (result)