var i = 100;

function something() {
	console.log(i);
}
//something();

var x = [1];
function fast_fact(n) {
	if (x[n-1]) {
		return x[n-1];
	}
	for (var i = x.length-1; i < n; i++) {
		var prod = x[i] * (i + 1);
		x.push(prod);
	}
	return x[x.length-1];
}
console.log(fast_fact(4));
console.log(x);