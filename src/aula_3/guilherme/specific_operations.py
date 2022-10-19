from msilib.schema import Error
import pandas as pd
import yaml
#df[df.name.str.match(regex)

def filter_column_by_regex(df: pd.DataFrame, config: dict):
    df = df.copy()

    def parse_list_to_regex(l: list):
        return "|".join(l)

    if not config.get('filters').get("title") == None:
        regex = config.get('filters').get("title")
        df = df[df.title.str.contains(regex)]

    if not config.get('filters').get("keywords") == None:
        array = config.get('filters').get("keywords")
        df = df[df.keywords.str.contains(parse_list_to_regex(array))]

    if not config.get('filters').get("abstract") == None:
        regex = config.get('filters').get("abstract")
        df = df[df.abstract.str.contains(regex)]

    if not config.get('filters').get("year") == None:
        array = config.get('filters').get("year")
        df = df[df.year.isin(array)]

    if not config.get('filters').get("type_publication") == None:
        regex = config.get('filters').get("type_publication")
        df = df[df.type_publication.str.contains(regex)]

    if not config.get('filters').get("doi") == None:
        regex = config.get('filters').get("doi")
        df = df[df.doi.str.contains(regex)]

    if not config.get('filters').get("jcs_value") == None:
        data = config.get('filters').get("jcs_value")
        df = df[df.jcs_value == data]

    if not config.get('filters').get("scimago_value") == None:
        data = config.get('filters').get("scimago_value")
        df = df[df.scimago_value == data]

    return df

def export_dataframe(dataframe: pd.DataFrame, config: dict, output_folder: str):
    if config.get("export_format") not in ["json", "csv", "yaml", "xml"]:
        raise Exception("O formato de exportação especificado no arquivo de configuração .yaml não foi reconhecido (json, csv, yaml, xml)")

    EXPORT_TYPE = config.get("export_format")

    if EXPORT_TYPE == "json":
        dataframe.to_json(f"{output_folder}/data.json", orient="records")

    elif EXPORT_TYPE == "csv":
        dataframe.to_csv(f"{output_folder}/data.csv", index=False, sep="|")

    elif EXPORT_TYPE == "yaml":
        data = yaml.dump(dataframe.to_dict(orient="records"))
        open(f"{output_folder}/data.yaml", 'w').write(data)

    elif EXPORT_TYPE == "xml":
        dataframe.to_xml(f"{output_folder}/data.xml", index=False)

    return dataframe
    
      