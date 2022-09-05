#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  console.log('C is fun\n'.repeat(parseInt(process.argv[2])));
}
