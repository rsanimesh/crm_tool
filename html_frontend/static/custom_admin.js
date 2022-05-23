$(document).ready(function () {
    $("#modal-company-input").val(getValue("company"));
    fetchFieldData();
});

let table_name = null;
let table_id = null;
let table_data = null;

function fetchFieldData() {
    var headers = { "Authorization": "Token " + getValue("token") };

    $.ajax({
        url: "/crm/v1/list-fields",
        headers: headers,
        type: "GET",
        success: function (result, status, xhr) {
            if (status === "success") {
                table_data = result;
                loadTables();
            }
        }
    });
}

function loadTables() {
    
    $("#myGrid").html("");

    let columnDefs = [
        {"field": "table_name","sortable": true, "filter": true},
        {"field": "name","sortable": true, "filter": true},
        {"field": "field_type","sortable": true, "filter": true},
        {"field": "field_values","sortable": true, "filter": true}
    ]

    let rowData = table_data;
    if (table_name != null){
        rowData = table_data.filter((each)=> {return each.table == table_id});
    }
    
    // let the grid know which columns and what data to use
    const gridOptions = {
        columnDefs: columnDefs,
        rowData: rowData,
        pagination: true,
        paginationPageSize: 10,
        defaultColDef: {
            resizable: true,
        },
        onFirstDataRendered: onFirstDataRendered
    };

    function onFirstDataRendered(params) {
        params.api.sizeColumnsToFit();
    }

    // lookup the container we want the Grid to use
    const eGridDiv = document.querySelector('#myGrid');


    // create the grid passing in the div to use together with the columns & data we want to use
    new agGrid.Grid(eGridDiv, gridOptions);
}

function tableDetails(obj) {
    table_name = $(obj).attr("name");
    table_id = $(obj).attr("tableId");
    loadTables();
}

function createTable(){
    let new_table_name = $("#new-table-name").val();
    let company = getValue("company");
    var headers = { "Authorization": "Token " + getValue("token"), "Content-Type": "application/json" };

    $.ajax({
        url: "/crm/v1/create-table/",
        headers: headers,
        type: "POST",
        data: JSON.stringify({"name":new_table_name, "company":company}),
        success: function (result, status, xhr) {
            if (status === "success") {
                fetchTableNames();
                $("#id01").hide();
            }
        }
    });

}

function createField(){

    let new_field_name = $("#new-field-name").val();
    let new_field_type = $("#new-field-type").val();
    let new_field_value = $("#new-field-value").val();
    let company = getValue("company");
    let headers = { "Authorization": "Token " + getValue("token"), "Content-Type": "application/json" };

    let post_data = JSON.stringify({
            "name": new_field_name,
            "field_type": new_field_type,
            "field_values": new_field_value,
            "company": company,
            "table": table_id,
            "table_name": table_name,
        })
    console.log(post_data);
    console.log(headers);

    $.ajax({
        url: "/crm/v1/create-fields/",
        headers: headers,
        type: "POST",
        data: post_data,
        success: function (result, status, xhr) {
            if (status === "success") {
                fetchFieldData();
                $("#id02").hide();
            }
        }
    });

}
