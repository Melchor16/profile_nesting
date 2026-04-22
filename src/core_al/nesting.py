def nesting_parts(parts, profiles):
    profiles_dict = {p.name: p for p in profiles}
    grouped_parts = group_parts(parts)
    nested = {}
    for profile, parts_list in grouped_parts.items():
        profile_length = profiles_dict[profile].length

        parts_lengths = [p.length for p in parts_list]
        parts_lengths.sort(reverse = True)

        nest = nesting(profile_length, parts_lengths)
        nested[profile] = {
            "nestings": nest,
            "profile_length": profile_length,
        }
    
    return nested
        

def nesting(profile_length, parts_lengths):
    bars = []

    for part in parts_lengths:
        placed = False

        for bar in bars:
            if sum(bar) + part <= profile_length:
                bar.append(part)
                placed = True
                break
        if not placed:
            bars.append([part])
    return bars

def group_parts(parts):
    available_parts = {}
    sorted_parts = sorted(parts, key= lambda p: p.length, reverse=True)

    for comp_prof in sorted_parts:
        if comp_prof.profile not in available_parts:
            available_parts[comp_prof.profile] = []

        for _ in range(comp_prof.qty):
            available_parts[comp_prof.profile].append(comp_prof.clone())

    return available_parts



    

