<?php
// Body Mass Index calculator demo in PHP
// Comments in functions have been omitted here

function calculate_bmi($mass, $length) {
	$cm = $length / 100;
	return $mass / ( $cm * $cm );
}

function dietary_advice($body_mass, $body_length) {
	
	$bmi = calculate_bmi($body_mass, $body_length);
		
	if ($bmi > 30) {
		return 'No more burgers for you!';
	} else {
		return 'All right, one burger will do.';
	}
}

echo dietary_advice(100, 180);
	
?>