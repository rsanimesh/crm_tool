from collections import defaultdict
from turtle import width

def create_columns(columns_list):
    column_defs  = [{"field":col.name,"sortable": True, "filter": True} for col in columns_list]
    add_list = [{"field":col.name,"field_type": col.field_type, "field_values": col.field_values_list} for col in columns_list]
    return column_defs, add_list

def create_row_data(table_data):
    """
    const rowData = [
      { make: "Toyota", model: "Celica", price: 35000 },
      { make: "Ford", model: "Mondeo", price: 32000 },
      { make: "Porsche", model: "Boxster", price: 72000 }
    ];
    """

    row_data_dict = defaultdict(dict)
    for each in table_data:
        row_data_dict[each.row_index][each.field_name.name] = each.validate_value
        row_data_dict[each.row_index]["row_index"] = each.row_index
    return row_data_dict.values()


