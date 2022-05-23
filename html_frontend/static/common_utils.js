function logout() {
    var headers = { "Authorization": "Token " + getValue("token") };

    $.ajax({
        url: "/crm/v1/token-logout",
        headers: headers,
        type: "GET",
        success: function (result, status, xhr) {
            if (status === "success") {
                deleteAuth()
                window.location.href = "/";
            }
        },
        error: function(request,status,errorThrown) {
            console.log(errorThrown, status);
            window.location.href = "/";
        }
    })
}

function createItem(key, value) {
    localStorage.setItem(key, value);
}

function getValue(key) {
    return localStorage.getItem(key);
}

function deleteAuth() {
    localStorage.removeItem("token");
    localStorage.removeItem("role");
    localStorage.removeItem("name");
    localStorage.removeItem("company");
}
