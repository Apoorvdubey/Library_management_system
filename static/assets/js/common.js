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

