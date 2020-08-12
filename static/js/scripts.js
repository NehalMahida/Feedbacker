
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

$(document).ready(function () {
    $('#FacultyId_indi').change(function () {
        //alert("Enter correct Id!!");
        var facultyid = $('#FacultyId_indi').val();
        $.getJSON(
            'get_subject_indi' + '/' + facultyid,
            function (data){
                $('#inputSubject_indi').find('option').remove();
                var option_item = '<option value="Subject">Subject</option>'
                $('#inputSubject_indi').append(option_item);
                //console.log(data);
                if(data.length == 0){
                    alert("Please, Enter Correct Id!!");
                }
                else{
                // Remove old options                
                // Add new items
                $.each(data, function (key, val) {
                    var option_item = '<option value="' + val + '">' + val + '</option>'
                    $('#inputSubject_indi').append(option_item);
                });
            }
            }
        );
    });

    $('#select_indi').click(function () {
        var faculty_id = $('#FacultyId_indi').val();
        var sub = $('#inputSubject_indi').val();
        var data = [faculty_id, sub];
        data = JSON.stringify(data);

        $.getJSON(
            '/getBarChart_indi' + '/' + data,
            function (data) {
                console.log(data);                    
                var ctx = document.getElementById("myBarChart_indi");
                if (window.mybarChart_indi != undefined)
                    window.mybarChart_indi.destroy();
                window.mybarChart_indi = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: data['Question No'],
                        datasets: [
                            {
                                label: "Excellent",
                                backgroundColor: "green",
                                borderColor: "black",
                                borderWidth: 1,
                                data: data.Excellent
                            },
                            {
                                label: "Good",
                                backgroundColor: "blue",
                                borderColor: "black",
                                borderWidth: 1,
                                data: data.Good
                            },
                            {
                                label: "Average",
                                backgroundColor: "purple",
                                borderColor: "black",
                                borderWidth: 1,
                                data: data.Average
                            },
                            {
                                label: "Bad",
                                backgroundColor: "yellow",
                                borderColor: "black",
                                borderWidth: 1,
                                data: data.Bad
                            },
                            {
                                label: "VeryBad",
                                backgroundColor: "red",
                                borderColor: "black",
                                borderWidth: 1,
                                data: data.VeryBad
                            }
                        ]
                    },
                    options: {
                        scales: {
                            xAxes: [{
                                time: {
                                    unit: 'month'
                                },
                                gridLines: {
                                    display: false
                                },
                                ticks: {
                                    maxTicksLimit: 12
                                }
                            }],
                            yAxes: [{
                                ticks: {
                                    min: 0,
                                    max: 200,
                                    maxTicksLimit: 5
                                },
                                gridLines: {
                                    display: true
                                }
                            }],
                        },
                        legend: {
                            display: false
                        }
                    }
                });
            }
        );

    });
}); 