function pushFront(arr, val) {
	for (var i = arr.length; i > 0; i--) {
		arr[i] = arr[i - 1];
	}
	arr[0] = val;
	return arr;
}
//console.log(pushFront([0,1,2], 5));

function popFront(arr) {
	var returnVal = arr[0];
	for (var i = 0; i < arr.length - 1; i++) {
		arr[i] = arr[i + 1];
	}
	arr.length = arr.length - 1;
	console.log(arr);
	return returnVal;
}
//console.log(popFront([0,1,2,3]));

function insertAt(arr, ind, val) {
	for (var i = 0; i < arr.length; i++) {
		if (i === ind) {
			for (var j = arr.length; j > 0; j--) {
				arr[j] = arr[j - 1];
			}
			arr[i] = val;
		}
	}
	return arr;
}
//console.log([0,1,2], 1, 5);







