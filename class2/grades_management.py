def add_child(data_dict, child):
    if child in data_dict:
        raise ValueError("Учень вже існує у словнику")
    data_dict[child] = {}
    return len(data_dict)

def calcucale_avg(data_dict, child, subject):
    if child not in data_dict:
        raise ValueError("Учня не знайдено у словнику")
    pup = data_dict[child]
    if subject not in pup:
        return -1
    grades = pup[subject]
    if not grades:
        return -1
    avg = sum(grades) / len(grades)
    if avg > 12:
        avg = 12
    return avg

