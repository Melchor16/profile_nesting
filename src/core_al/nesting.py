
def nesting_parts(parts, profiles):
    profiles_dict = {p.name: p for p in profiles}
    available_parts = group_parts(parts)
    
    return available_parts

def group_parts(parts):
    available_parts = {}
    sorted_parts = sorted(parts, key= lambda p: p.length, reverse=True)

    for comp_prof in sorted_parts:
        if comp_prof.profile not in available_parts:
            available_parts[comp_prof.profile] = []

        for _ in range(comp_prof.qty):
            available_parts[comp_prof.profile].append(comp_prof.clone())

    return available_parts



    

