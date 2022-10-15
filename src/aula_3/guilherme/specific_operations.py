import pandas as pd
#df[df.name.str.match(regex)

def filter_column_by_regex(df: pd.DataFrame, config: dict):
    df = df.copy()

    if not config.get('filters').get("title") == None:
        regex = config.get('filters').get("title")
        df = df[df.title.str.match(regex)]

    if not config.get('filters').get("keywords") == None:
        regex = config.get('filters').get("keywords")
        df = df[df.keywords.str.match(regex)]

    if not config.get('filters').get("abstract") == None:
        regex = config.get('filters').get("abstract")
        df = df[df.abstract.str.match(regex)]

    if not config.get('filters').get("year") == None:
        year = config.get('filters').get("year")
        df = df[df.year == year]

    if not config.get('filters').get("ENTRYTYPE") == None:
        regex = config.get('filters').get("ENTRYTYPE")
        df = df[df.ENTRYTYPE.str.match(regex)]

    if not config.get('filters').get("doi") == None:
        regex = config.get('filters').get("doi")
        df = df[df.doi.str.match(regex)]

    if not config.get('filters').get("jcs_value") == None:
        data = config.get('filters').get("jcs_value")
        df = df[df.jcs_value == data]

    if not config.get('filters').get("scimago_value") == None:
        data = config.get('filters').get("scimago_value")
        df = df[df.scimago_value == data]

    return df
