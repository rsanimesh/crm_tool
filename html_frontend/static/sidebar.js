$(document).ready(function () {
    $("#name").html(getValue("name"));
    fetchTableNames();
});

function fetchTableNames() {
    var headers = { "Authorization": "Token " + getValue("token") };

    $.ajax({
        url: "/crm/v1/list-table",
        headers: headers,
        type: "GET",
        success: function (result, status, xhr) {
            if (status === "success") {
                loadTablesNames(result);
            }
        }
    });
}

function loadTablesNames(result) {
    const table_menu = result.map((each) => {
        return `<a href="#" onclick="tableDetails(this)" name="${each.name}" tableId="${each.id}" class="w3-bar-item w3-button">${each.name}</a>`;
    })
    $("#tables_names").html(table_menu);
}
