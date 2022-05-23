let table_name = null;
let table_add_list = null;

function tableDetails(obj) {
    table_name = $(obj).attr("name");
    tableAPI();
}

function tableAPI() {
    console.log("Load Table: ", table_name);
    var headers = { "Authorization": "Token " + getValue("token") };
    $.ajax({
        url: "/crm/v1/table-data-list?table_name=" + table_name,
        headers: headers,
        type: "GET",
        success: function (result, status, xhr) {
            if (status === "success") {
                console.log(result);
                table_add_list = result.add_list;
                loadTableData(result);
                loadAddModel(result.add_list);
            }
        }
    });
}

function loadTableData(result) {

    $("#myGrid").html("");
    console.log(result);

    // appending action column for edit or delete of row
    result.columnDefs.push({
        headerName: "action",
        minWidth: 150,
        cellRenderer: actionCellRenderer,
        editable: false,
        colId: "action"
    })

    // let the grid know which columns and what data to use
    const gridOptions = {
        columnDefs: result.columnDefs,
        rowData: result.rowData,
        pagination: true,
        paginationPageSize: 10,
        defaultColDef: {
            resizable: true,
        },
        onFirstDataRendered: onFirstDataRendered,
        onCellClicked(params) {
            // Handle click event for action cells
            if (params.column.colId === "action" && params.event.target.dataset.action) {
                let action = params.event.target.dataset.action;

                if (action === "edit") {
                    loadUpdateRowModal(params.node.data);
                }

                if (action === "delete") {
                    deleteRow(params.node.data);
                    params.api.applyTransaction({
                        remove: [params.node.data]
                    });
                }
            }
        }
    };

    function onFirstDataRendered(params) {
        params.api.sizeColumnsToFit();
    }

    // lookup the container we want the Grid to use
    const eGridDiv = document.querySelector('#myGrid');


    // create the grid passing in the div to use together with the columns & data we want to use
    new agGrid.Grid(eGridDiv, gridOptions);

}

function loadAddModel(add_list) {
   
    const add_form = add_list.map((each, index) => {

        if (each.field_type == "text") {
            return (
                `<label class="w3-text-green"><b>${each.field}</b></label>
        <input class="w3-input w3-border w3-light-grey modal-input" type="text" for=${each.field}>`
            )
        }
        else if (each.field_type == "email") {
            return (
                `<label class="w3-text-green"><b>${each.field}</b></label>
            <input class="w3-input w3-border w3-light-grey modal-input" type="email" for=${each.field}>`
            )
        }
        else if (each.field_type == "phone") {
            return (
                `<label class="w3-text-green"><b>${each.field}</b></label>
            <input class="w3-input w3-border w3-light-grey modal-input" type="tel" pattern="[0-9]{10}" for=${each.field}>`
            )
        }
        else if (each.field_type == "dropdown") {
            var field_option = each.field_values.map((e) => {
                return `<option value="${e}">${e}</option>`
            }).join("");
            return (
                `<label class="w3-text-green"><b>${each.field}</b></label>
            <select class="w3-input w3-border w3-light-grey modal-input" for=${each.field}>${field_option}</select>`
            )
        }
    })

    $("#add-modal").html(add_form);
    $("#add-modal").append(`<button onclick="addData()" class="w3-btn w3-green w3-margin-top w3-round" style="width: 50%; margin-left: 25%;">Add</button>`);
    $("#add-btn").show();

}

function addData() {
    const new_row = {}
    $('.modal-input').each(function (i, obj) {
        const rowValue = obj.value;
        const rowName = obj.getAttribute("for");
        new_row[rowName] = rowValue
    });

    var headers = { "Authorization": "Token " + getValue("token") };
    let post_data = JSON.stringify({ "table_name": table_name, "new_row": new_row });

    console.log(post_data);

    $.ajax({
        url: "/crm/v1/add-row",
        headers: headers,
        type: "POST",
        data: { "data": post_data },
        success: function (result, status, xhr) {
            if (status === "success") {
                console.log("Response of add row: ", result);
                tableAPI();
                $("#id01").hide();
            }
        }
    });
}

function deleteRow(rowData) {
    console.log("Delete Data: ", rowData);
    var headers = { "Authorization": "Token " + getValue("token") };

    $.ajax({
        url: `/crm/v1/delete-row?row_index=${rowData.row_index}`,
        headers: headers,
        type: "DELETE",
        success: function (result, status, xhr) {
            if (status === "success") {
                console.log("Response of delete row: ", result);
            }
        },
        error: function (request, status, errorThrown) {
            console.log(errorThrown, status);
        }
    });
}

function loadUpdateRowModal(value_dict){
    const add_form = table_add_list.map((each, index) => {

        if (each.field_type == "text") {
            let value = each.field in value_dict ? value_dict[each.field] : "";
            return (
                `<label class="w3-text-green"><b>${each.field}</b></label>
        <input class="w3-input w3-border w3-light-grey modal-update" type="text" for=${each.field} value=${value}>`
            )
        }
        else if (each.field_type == "email") {
            let value = each.field in value_dict ? value_dict[each.field] : "";
            return (
                `<label class="w3-text-green"><b>${each.field}</b></label>
            <input class="w3-input w3-border w3-light-grey modal-update" type="email" for=${each.field} value=${value}>`
            )
        }
        else if (each.field_type == "phone") {
            let value = each.field in value_dict ? value_dict[each.field] : "";
            return (
                `<label class="w3-text-green"><b>${each.field}</b></label>
            <input class="w3-input w3-border w3-light-grey modal-update" type="tel" pattern="[0-9]{10}" for=${each.field} value=${value}>>`
            )
        }
        else if (each.field_type == "dropdown") {
            let value = each.field in value_dict ? value_dict[each.field] : "";
            var field_option = each.field_values.map((e) => {
                return e === value ? `<option value="${e}" selected>${e}</option>` : `<option value="${e}">${e}</option>`
            }).join("");
            return (
                `<label class="w3-text-green"><b>${each.field}</b></label>
            <select class="w3-input w3-border w3-light-grey modal-update" for=${each.field}>${field_option}</select>`
            )
        }
    })

    $("#view-update-modal-content").html(add_form);
    $("#view-update-modal-content").append(`<input type="text" class="modal-update" for='row_index' value=${value_dict['row_index']} disabled hidden>`);
    $('#view-update-modal').show();
    
}

function updateRow(){
    const row_data = {}
    $('.modal-update').each(function (i, obj) {
        const rowValue = obj.value;
        const rowName = obj.getAttribute("for");
        row_data[rowName] = rowValue
    });

    var headers = { "Authorization": "Token " + getValue("token") };
    let post_data = JSON.stringify({ "table_name": table_name, "row_data": row_data });

    console.log(post_data);

    $.ajax({
        url: "/crm/v1/update-row",
        headers: headers,
        type: "PUT",
        data: { "data": post_data },
        success: function (result, status, xhr) {
            console.log("Response of add row: ", result);
            if (status === "success") {
                tableAPI();
                $("#view-update-modal").hide();
            }
        }
    });
}

function actionCellRenderer() {
    let eGui = document.createElement("div");
    eGui.innerHTML = `
        <button 
        class="w3-btn w3-blue"  
        data-action="edit">
            edit 
        </button>
        <button 
        class="action-button delete"
        data-action="delete">
            delete
        </button>
        `;
    return eGui;
}
