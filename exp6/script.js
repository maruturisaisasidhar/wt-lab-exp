function checkPrime() {
  const number = parseInt(document.getElementById("numberInput").value);
  const result = document.getElementById("result");
  result.innerHTML = "";

  if (isNaN(number)) {
    result.innerHTML = "Please enter a valid number.";
    return;
  }

  result.innerHTML = `Prime: ${isPrime(number)}`;
}

function checkPalindrome() {
  const number = parseInt(document.getElementById("numberInput").value);
  const result = document.getElementById("result");
  result.innerHTML = "";

  if (isNaN(number)) {
    result.innerHTML = "Please enter a valid number.";
    return;
  }

  result.innerHTML = `Palindrome: ${isPalindrome(number)}`;
}

function calculateFactorial() {
  const number = parseInt(document.getElementById("numberInput").value);
  const result = document.getElementById("result");
  result.innerHTML = "";

  if (isNaN(number)) {
    result.innerHTML = "Please enter a valid number.";
    return;
  }

  result.innerHTML = `Factorial: ${factorial(number)}`;
}

function generateFibonacci() {
  const number = parseInt(document.getElementById("numberInput").value);
  const result = document.getElementById("result");
  result.innerHTML = "";

  if (isNaN(number)) {
    result.innerHTML = "Please enter a valid number.";
    return;
  }

  result.innerHTML = `Fibonacci Series: ${fibonacciSeries(number)}`;
}

function isPrime(num) {
  if (num <= 1) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

function isPalindrome(num) {
  const str = num.toString();
  return str === str.split("").reverse().join("");
}

function factorial(num) {
  if (num < 0) return "Not defined";
  if (num === 0) return 1;
  let fact = 1;
  for (let i = 1; i <= num; i++) {
    fact *= i;
  }
  return fact;
}

function fibonacciSeries(num) {
  if (num < 0) return "Not defined";
  let fibSeries = [0, 1];
  let nextFib = 0;
  while (nextFib <= num) {
    nextFib = fibSeries[fibSeries.length - 1] + fibSeries[fibSeries.length - 2];
    if (nextFib <= num) fibSeries.push(nextFib);
  }
  return fibSeries.join(", ");
}
