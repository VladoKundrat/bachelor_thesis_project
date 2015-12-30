
$(document).ready(function() {
    var table = $('#piece').DataTable( {
        select: true,
        dom: 'fBrtip',
        stateSave: true,
        buttons: [
            {
                extend: 'colvis',
                postfixButtons: [ 'colvisRestore' ],
                columns: ':not(:first-child)'
            }
        ],
        columnDefs: [
            {
                targets: -1,
                visible: false
            }
        ],
        "processing": true,
        "serverSide": true,
        "dataType": "json",
        "pageLength": 15,
        "ajax": "../rest/piece",
        "pagingType": "input",
        "columns": [
        {"className": 'details-control'},
        {"className": 'details-control'},
        {"className": 'details-control'},
        {"className": 'details-control'},
        {"className": 'details-control'},
        {"className": 'details-control'},
        {"className": 'details-control'},
        {"className": 'details-control'},
        {"className": 'details-control'},
        {"className": 'details-control'}
        ]
    });
});


$(document).ready(function() {
    var table = $('#album').DataTable( {
        select: true,
        dom: 'fBrtip',
        //stateSave: true,
        buttons: [
            {
                extend: 'colvis',
                postfixButtons: [ 'colvisRestore' ],
                columns: ':not(:first-child)'
            }
        ],
        columnDefs: [
            {
                "targets":[4],
                "visible": false
            },
            {
                "targets":[5],
                "visible": false
            },
            {
                "targets":[6],
                "visible": false
            },
            {
                "targets":[7],
                "visible": false
            },
            {
                "targets":[8],
                "visible": false
            },
            {
                "targets":[9],
                "visible": false
            },
                                {
                "targets":[10],
                "visible": false
            },
                                {
                "targets":[11],
                "visible": false
            },
                                {
                "targets":[12],
                "visible": false
            },
                                {
                "targets":[13],
                "visible": false
            },
                                {
                "targets":[14],
                "visible": false
            },
                                {
                "targets":[15],
                "visible": false
            },
                                {
                "targets":[16],
                "visible": false
            },
                                {
                "targets":[17],
                "visible": false
            },
                                {
                "targets":[18],
                "visible": false
            },
                                {
                "targets":[19],
                "visible": false
            },
                                {
                "targets":[20],
                "visible": false
            },
                                {
                "targets":[21],
                "visible": false
            },
            {
                "targets":[22],
                "visible": false
            }
        ],
        "pagingType": "input",
        "processing": true,
        "serverSide": true,
        "dataType": "json",
        //"ajax": "{% url 'rest_album' %}",
        "ajax": "../rest/album",
        "pageLength": 15,
        "deferRender": true,
        "columns": [
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'},
            {"className": 'details-control'}
        ]
    });
});

function classFunction(elm) {
        if (elm.indexOf("album") > -1){
            var n = elm.lastIndexOf('_');
            var albumId = elm.substring(n + 1);

            var url = ('../album/detail/999').replace (999, albumId);
        }
        else if (elm.indexOf("piece") > -1){
            var n = elm.lastIndexOf('_');
            var pieceId = elm.substring(n + 1);

            var url = ('../piece/detail/999').replace (999, pieceId);
        }
        $.ajax({
            url: url,
            success: function(data){
                $("#detail_style").html(data);
            }
        })
    }


$(document).ready(function() {
    if(window.location.href.indexOf("piece") > -1){
        $('#piece tbody').on('click', 'tr', function () {
            var pieceId = $(this).find("td:first").text();
            var url = ('../piece/detail/999').replace (999, pieceId);
            go_to_url(url);
        });
    }
    else if (window.location.href.indexOf("album") > -1){
        $('#album tbody').on('click', 'tr', function () {
            var albumId = $(this).find("td:first").text();
            var url =('../album/detail/999').replace (999, albumId);
            go_to_url(url);
        });
    }
});

function go_to_url(url) {
    $.ajax({
        url: url,
        success: function (data) {
            $("#table_style").width("70%");
            $(".hide_button").show();
            $("#detail_style").show();
            $("#detail_style").html(data);
        }
    })
}