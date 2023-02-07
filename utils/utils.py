def map_categories_to_index(categories: list[str],
                            categories_indexes: dict[str,int]) -> list[int]:
    if "Any" in categories:
        return [0]
    tmp_categories_indexes = []
    for category in categories:
        tmp_categories_indexes.append(categories_indexes[category])
    return tmp_categories_indexes