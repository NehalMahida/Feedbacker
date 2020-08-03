
/*$(document).ready(function () {
    // when we click on Semester than 
    $('#inputSemester').change(function () {

        var foodkind = "fruit"//$('#inputSemester').val();

        // Make Ajax Request and expect JSON-encoded data
        $.getJSON(
            '/get_food' + '/' + foodkind,
            function (data) {

                // Remove old options
                $('#inputDepartment').find('option').remove();

                // Add new items
                $.each(data, function (key, val) {
                    var option_item = '<option value="' + val + '">' + val + '</option>'
                    $('#inputDepartment').append(option_item);
                });
            }
        );
    });
});
*/