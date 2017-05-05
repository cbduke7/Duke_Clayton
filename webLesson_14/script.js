function validate() {
	var x = document.forms.input.username.value;
	var atPos = x.indexOF("@")
	var dotPos = x.lastIndexOf(".");
	

	if(atPos < 1 || dotPos < atPos+2 || dotPos + 2 > x.length)
		alert("We are unable to process your request. Please correct the following errors...This is not a valid email address!");
	
	else
		alert("Success!")
}

function validate() {
	var y = document.forms.input.passwd.value;
	
	if(y.length < 6)
		alert("Your password does not meet the mininum requirements")
	
	else
		alert("Success!")
}

	
	
	


