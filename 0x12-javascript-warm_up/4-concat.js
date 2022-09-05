#!/usr/bin/node
if (process.argv[3] !== null) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (process.argv[3] === null) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (process.argv[2] === null && process.arg[3] === null) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
