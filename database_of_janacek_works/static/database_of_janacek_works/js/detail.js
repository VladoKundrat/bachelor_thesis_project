if (localStorage.getItem("state") == "closed") // this checks closed/open state and sets subnav accordingly
    $('.subnav').show();
    $('.subnav').parent().click(function () {
        $(this).find('#sub1').toggle(); // This toggles the menu open/close
        // ** Block to remeber state ** //
        if (localStorage.getItem("state") == "open") {
            localStorage.setItem("state", "closed"); // this remembers "open" after user navigates
        } else {
            localStorage.setItem("state", "open"); // this remembers "open" after user navigates
        }
    });
