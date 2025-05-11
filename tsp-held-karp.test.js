const fs = require('fs');
const { performance } = require('perf_hooks');
import tsp_hk from './tsp-held-karp.js'

// Parse CLI arg
const n = parseInt(process.argv[2], 10);
if (Number.isFinite(n) ==  false || n < 0) {
  console.error('Please supply a non-negative integer for <number_of_cities>.');
  process.exit(1);
}

// Random symmetric matrix generator
// maxDistance is the maximum distance allowed between cities
function buildRandomMatrix(size, maxDistance = 10) {
  const m = Array.from({ length: size }, () => Array(size).fill(0));

  for (let index = 0; index < size; ++index) {
    for (let index_j = index + 1; index_j < size; ++index_j) {
      const d = 1 + Math.floor(Math.random() * maxDistance);
      m[index][index_j] = m[index_j][index] = d;
    }
  }

  return m;
}

// Generate instance and run algorithm
const matrix = buildRandomMatrix(n);

const t0 = performance.now();
const tourLength = tsp_hk(matrix);
const runtimeSec = (performance.now() - t0) / 1000;

// Log output and append to file
const line = `HK: ${n} number of cities, ${runtimeSec.toFixed(2)} runtime, ${tourLength} tour length\n`;

// Append only
fs.appendFileSync('output.txt', line, 'utf8');
console.log(line.trim());