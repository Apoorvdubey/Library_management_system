var path = window.location.pathname
   if (path === "/"){
       document.getElementById("dashboard").parentElement.classList.add('active')
   }
  
   if (path === "/users/listUsers/id/"){
       document.getElementById("userManagement").parentElement.classList.add('active')
   }
   if (path === "/users/listUsers/fullName/"){
    document.getElementById("userManagement").parentElement.classList.add('active')
}   
    if (path === "/users/listUsers/email/"){
    document.getElementById("userManagement").parentElement.classList.add('active')
}
    if (path === "/users/listUsers/gender/"){
    document.getElementById("userManagement").parentElement.classList.add('active')
}
    if (path === "/users/listUsers/createdAt/"){
    document.getElementById("userManagement").parentElement.classList.add('active')
}
    if (path === "/users/addUsers/"){
    document.getElementById("userManagement").parentElement.classList.add('active')
}

   if (path === "/bookManagement/listBooks/id/"){
       document.getElementById("bookManagement").parentElement.classList.add('active')
   }
   if (path === "/bookManagement/listBooks/name/"){
    document.getElementById("bookManagement").parentElement.classList.add('active')
}
    if (path === "/bookManagement/listBooks/author/"){
    document.getElementById("bookManagement").parentElement.classList.add('active')
}
    if (path === "/bookManagement/listBooks/price/"){
    document.getElementById("bookManagement").parentElement.classList.add('active')
}
    if (path === "/bookManagement/addBooks/"){
    document.getElementById("bookManagement").parentElement.classList.add('active')
}
    if (path === '/userAdminQueryManagement/listQueries/createdAt/'){
    document.getElementById("userAdminQueryManagement").parentElement.classList.add('active')
}
    if (path === '/userAdminQueryManagement/listQueries/queryStatus/'){
    document.getElementById("userAdminQueryManagement").parentElement.classList.add('active')
}
    if (path === '/donationManagement/listDonations/createdAt/'){
        document.getElementById("donationManagement").parentElement.classList.add('active')
    }
    if (path === '/donationManagement/listLastMonthDonations/createdAt/'){
        document.getElementById("donationManagement").parentElement.classList.add('active')
    }
    if (path === '/donationManagement/listLastMonthDonations/paymentStatus/'){
        document.getElementById("donationManagement").parentElement.classList.add('active')
    }
    if (path === '/donationManagement/listLastMonthDonations/paymentAmount/'){
        document.getElementById("donationManagement").parentElement.classList.add('active')

    }


// ADD BOOK JS

$(document).ready(function () {
    if (window.File && window.FileList && window.FileReader) {
        $("#files").on("change", function (e) {
            $('.image-upload-wrap').css("background", "#F5F5F5");

            var files = e.target.files,
                filesLength = files.length;
            //alert(files.length)
            for (var i = 0; i < filesLength; i++) {
                var f = files[i]
                var fileReader = new FileReader();
                fileReader.onload = (function (e) {
                    var file = e.target;
                    $("<span class=\"pip\">" +
                        "<span class=\"remove\">X</span>" +
                        "<img class=\"imageThumb\" src=\"" + e.target.result + "\" title=\"" + file.name + "\"/>" +
                        "</span>").insertAfter("#files");
                    $(".remove").click(function () {
                        $(this).parent(".pip").remove();

                        //alert($('.pip').length);
                        if ($('.pip').length == 0) {

                            $('.image-upload-wrap').css("background", "rgb(233 244 255)");
                        }
                    });
                    

                });
                fileReader.readAsDataURL(f);
            }
            console.log(files);
        });
    } else {
        alert("Your browser doesn't support to File API")
    }
});

