function validate() {  
    var name = document.reg_form.name;  
    if (name.value.length <= 0) {  
        alert("Name is required");  
        name.focus();  
        return false;  
    }  

}