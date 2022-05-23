from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from core.models import *
import json
from core.utilities.table_utils import create_columns, create_row_data
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from core.utilities.custom_permissions import CustomPermission


@api_view(["GET"])
@permission_classes([IsAuthenticated, CustomPermission])
def table_data_list(request):
    try:
        table_name = request.GET.get("table_name", None)
        table_obj = Table.objects.get(name=table_name, is_visible=True, is_deleted=False)
        field_list = FieldList.objects.filter(table=table_obj,is_visible=True, is_deleted=False)
        table_data = MasterData.objects.filter(field_name__in=field_list)

        column_defs, add_list = create_columns(field_list)
        row_data = create_row_data(table_data)
        return Response({"Status":True, "columnDefs":column_defs, "rowData":row_data, "add_list":add_list })
    except Exception as error:
        print(str(error))
        return Response({"error":str(error)}, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated, CustomPermission])
def add_row(request):
    try:
        auth_token = request.headers['Authorization']
        user = Token.objects.get(key=auth_token.replace("Token ","")).user
        company = user.profile.company

        # {'table_name':'Project' 'new_row':[{'name': 'dnsvb'}, {'city': 'jhbndj'}, {'address': 'jkncdjks'}]}
        data = json.loads(request.data.get('data'))
        table_name = data.get("table_name", None)
        new_row = data.get("new_row", None)
        
        table_obj = Table.objects.get(name=table_name, is_visible=True, is_deleted=False)
        field_list = FieldList.objects.filter(table=table_obj,is_visible=True, is_deleted=False)

        row_index = None
        for each_field in field_list:
            if row_index == None:
                md_data = MasterData(
                    company = company,
                    field_name = each_field,
                    value = new_row[each_field.name],
                )
                md_data.save()
                row_index = md_data.id
                md_data.row_index = row_index
                md_data.save()
            else:
                md_data = MasterData(
                    company = company,
                    field_name = each_field,
                    value = new_row[each_field.name],
                    row_index = row_index
                )
                md_data.save()

        return Response({"Status":True})
    except Exception as error:
        print(str(error))
        return Response({"error":str(error)}, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated, CustomPermission])
def delete_row(request):
    try:
        row_index = request.GET.get('row_index', None)
        if row_index:
            MasterData.objects.filter(row_index=row_index).delete()
            return Response({"Status":True, "Message":"Deleted a row"})
        else:
            return Response({"Status":False, "Message":"Row Index not found"})

    except Exception as error:
        print(str(error))
        return Response({"error":str(error)}, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, CustomPermission])
def update_row(request):
    try:
        # {"table_name":"Employee","row_data":{"name":"Surabhi","city":"Pune","row_index":"25"}}
        data = json.loads(request.data.get('data'))
        table_name = data.get("table_name", None)
        row_data = data.get("row_data", None)
        row_index = row_data.get('row_index', None)
        if row_index:
            data_list = MasterData.objects.filter(row_index=row_index)
            for each in data_list:
                each.value = row_data[each.field_name.name]
                each.save()
            return Response({"Status":True, "Message":"Data saved successfully"})
        else:
            return Response({"Status":False, "Message":"Row Index not found"})
    except Exception as error:
        print(str(error))
        return Response({"error":str(error)}, status=400)
