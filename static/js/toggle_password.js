const password_input = document.getElementById('password');
const button_see_password = document.getElementById('togglePassword')


button_see_password.addEventListener("click", () => {    
    if (password_input.type == 'password'){
    
        password_input.type = 'text';        
    }
    else{
        password_input.type = 'password'
    }
})
