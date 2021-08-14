$(document).ready(function (){
    const url = "{% url 'inventory:col_drop' %}"
    $.get(url).then(function(data) {
        $('#id_college').html(data);
    });
})

$("#id_college").change(function refreshDept() {
    const url = $("#id_college").attr("data-dept-url");  // get the url of the `load_cities` view
    const collegeId = $("#id_college").val();  // get the selected country ID from the HTML input
    const collegeName = $("#id_college option:selected").text()
    $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= /persons/ajax/load-cities/ )
        data: {
            'college_id': collegeId       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_cities` view function
            $("#id_depts").html(data);  // replace the contents of the city input with the data that came from the server
            $("#mainCollegeTitle").text("{%trans 'College' %}: " + collegeName);
            /*
            let html_data = '<option value="">---------</option>';
            data.forEach(function (city) {
                html_data += `<option value="${city.id}">${city.name}</option>`
            });
            console.log(html_data);
            $("#id_city").html(html_data);
            */
        }
    });
});

$("#id_AddCollege").click(
    function () {
        const url = $("#collegeModal").attr("data-col-url");
        $.ajax({
            url: url,
            type: 'post',
            success: function (data) {
                $("#collegeModal").html(data.html_form);
            }
        })
    }
)
