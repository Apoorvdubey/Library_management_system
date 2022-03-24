var path = window.location.pathname
   if (path === "/"){
       document.getElementById("dashboard").parentElement.classList.add('active')
   }
  
   if (path === "/users/listUsers/id/"){
       document.getElementById("userManagement").parentElement.classList.add('active')
   }

   if (path === "/bookManagement/listBooks/id/"){
       document.getElementById("bookManagement").parentElement.classList.add('active')
   }