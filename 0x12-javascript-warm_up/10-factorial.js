#!/usr/bin/node 
function factorial (number) {
  let result = 1;
  for (let i = 1; i <= number; i++) {
    result = result * i;
  }
  console.log(result);
}
factorial(parseInt(process.argv[2]));
