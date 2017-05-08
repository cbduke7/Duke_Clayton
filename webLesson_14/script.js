function validateEmail() {
	var atPos = user.indexOF("@");
	var dotPos = user.lastIndexOf(".");
	

	if(atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > user.length)
		alert("We are unable to process your request. Please correct the following errors... This is not a valid email address!");
	
	else
		alert("Success!");
}


function validatePass() {
	if(pass.length < 6)
		alert("We are unable to process your request. Please correct the following errors... Your password does not meet the mininum requirements");
	
	else
		alert("Success!");
}

function validate() {
	var atPos = user.indexOF("@");
	var dotPos = user.lastIndexOf(".");
	
	if(atPos < 1 || dotPos < atPos+2 || dotPos + 2 > user.length || pass.length < 6)
		alert("We are unable to process your request. Please correct the following errors... You did not provide a valid email address and your password does not meet the mininum requirements");
	
	else
		alert("Success");
}	
	
	


