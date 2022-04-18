// function verify_supplier() {
//   var distributor = document.verify_form.distributor_name;
//   var company = document.verify_form.company_name;
//   var email = document.verify_form.email;
//   var phone = document.getElementById("Phonenumber");
//   var address = document.verify_form.address;
//   var country = document.verify_form.country;
//   var state = document.verify_form.state;
//   var postalcode = document.verify_form.pincode;
//   var isimark = document.verify_form.isimark;
//   var uploadlogo = document.verify_form.logo;
//   var letters = /^[A-Za-z  ]+$/;
//   var mailformat = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
//   var postalcode = /^\d{5}(-\d{4})?$/.test(str);
//   if (distributor.value.length <= 0) {
//     alert("Distributor name is required");
//     distributor.focus();
//     return false;
//   }
//   if (!distributor.value.match(letters)) {
//     alert("enter alphabets at name");
//     distributor.focus();
//     return false;
//   }
//   if (company.value.length <= 0) {
//     alert("Company name is required");
//     company.focus();
//     return false;
//   }
//   if (!company.value.match(letters)) {
//     alert("enter alphabets at name");
//     company.focus();
//     return false;
//   }
//   if (email.value.length <= 0) {
//     alert("please enter gmail");
//     email.focus();
//     return false;
//   }

//   if (!email.value.match(mailformat)) {
//     alert("invalid gmail");
//     email.focus();
//     return false;
//   }
//   if (phone.value.length == 0) {
//     alert("phone number is required");
//     phone.focus();
//     return false;
//   }
//   if (isNaN(phone.value)) {
//     alert("please enter digits for phonenumber");
//     phone.focus();
//     return false;
//   }
//   if (phone.value.length != 10) {
//     alert("Phonenumber must contain 10 digits");
//     phone.focus();
//     return false;
//   }
//   if (address.value.length <= 0) {
//     alert("write the address it is required");
//     address.focus();
//     return false;
//   }
//   if (country.value.length <= 0) {
//     alert("country is required");
//     country.focus();
//     return false;
//   }
//   if (state.value.length <= 0) {
//     alert("state is required");
//     state.focus();
//     return false;
//   }
//   if (postalcode == "" || postalcode.length != 6) {
//     alert("postalcode should not be empty");
//     return false;
//   }
//   if (isNaN(postalcode)) {
//     alert("Invalid postalcode");
//     return false;
//   }
//   if (isimark.value.length <= 0) {
//     alert("isismark is required");
//     isimark.focus();
//     return false;
//   }
//   if (uploadlogo.value.length == "") {
//     alert("please upload your course photo");
//     uploadlogo.focus();
//     return false;
//   }

//   else {
//     alert("Submitted successfully");
//     return true;
//   }






// }