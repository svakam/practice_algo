from ucimlrepo import fetch_ucirepo

def get_mammo():
    # fetch dataset
    mammographic_mass = fetch_ucirepo(id=161)

    # data (as Pandas dataframes)
    return [mammographic_mass.data.features, mammographic_mass.data.targets]

