from ucimlrepo import fetch_ucirepo

def get_mammo():
    # fetch dataset (https://archive.ics.uci.edu/dataset/161/mammographic+mass)
    mammographic_mass = fetch_ucirepo(id=161)

    return mammographic_mass.data
    