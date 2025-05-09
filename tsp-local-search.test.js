const fs = require('fs');
const { performance } = require('perf_hooks');
import tsp_ls from './tsp-local-search.js'

// Parse CLI arg
const n = parseInt(process.argv[2], 10);
if (!Number.isFinite(n) || n < 0) {
  console.error('Please supply a non-negative integer for <number_of_cities>.');
  process.exit(1);
}

// Random symmetric matrix generator
// maxDistance is the maximum distance allowed between cities
function buildRandomMatrix(size, maxDistance = 10) {
  const m = Array.from({ length: size }, () => Array(size).fill(0));

  for (let i = 0; i < size; ++i) {
    for (let j = i + 1; j < size; ++j) {
      const d = 1 + Math.floor(Math.random() * maxDistance);
      m[i][j] = m[j][i] = d;
    }
  }
  return m;
}

// Generate instance and run algorithm
const matrix = buildRandomMatrix(n);

const t0 = performance.now();
const tourLength = tsp_ls(matrix);
const runtimeSec = (performance.now() - t0) / 1000;

// Log output and append to file
const line = `LS: ${n} number of cities, ${runtimeSec.toFixed(2)} runtime, ${tourLength} tour length\n`;

// Append only
fs.appendFileSync('output.txt', line, 'utf8');
console.log(line.trim());
