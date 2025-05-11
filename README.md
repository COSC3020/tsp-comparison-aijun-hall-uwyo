# Traveling Salesperson Problem -- Empirical Analysis

For this exercise, you'll need to take the code from the TSP Held-Karp and TSP
Local Search exercises. This can be your own implementation or somebody else's.
You will now do an empirical analysis of the implementations, comparing their
performance. Both the Held-Karp and the Local Search algorithms solve the same
problem, but they do so in completely different ways. This results in different
solutions, and in different times required to get to the solution.

Investigate the implementations' empirical time complexity, i.e. how the runtime
increases as the input size increases. *Measure* this time by running the code
instead of reasoning from the asymptotic complexity (this is the empirical
part). Create inputs of different sizes and plot how the runtime scales (input
size on the $x$ axis, time on the $y$ axis). Your largest input should have a
runtime of *at least* an hour. The input size that gets you to an hour will
probably not be the same for the Held-Karp and Local Search implementations.

In addition to the measured runtime, plot the tour lengths obtained by both
implementations on the same input distance matrices. The length of the tour that
Held-Karp found should always be less than or equal to the tour length that
Local Search found. Why is this?

Add the code to run your experiments, graphs, and an explanation of what you did
to this markdown file.

<hr>

<b>Why is Held-Karp less than or equal tour lengths than Local Search</b>

Held-Karp uses a dynamic programming solution that guarantees finding the optimal solution.
Local Search however uses heuristic comparisons for its solution, and makes iterative improvements. However Local Search doesn't explore the entire search space and can get stuck in a local minima due to the `max_no_improve` of 100 I set in my implementation, meaning it could miss a global best tour.

This results in the Held-Karp tours always being less than or equal to the Local Search tour length

<b>Graphs</b>

![image](https://github.com/user-attachments/assets/969a1a85-ecb9-4e44-b4f0-47703e16e948)



![image](https://github.com/user-attachments/assets/af86bcc5-b88e-4c79-ba8a-5bb3d517206a)


<b>Methodology</b>

First I copied over the `code.js` files from both my old tsp-held-karp and tsp-local-search assignment repositories. I am using my own code for benchmarking. Both `code.js` files were renamed respectively to `tsp-held-karp.js` and `tsp-local-search.js` and sit in this repository.

Then I created completely new test files for both `tsp-held-karp.js` and `tsp-local-search.js`, where instead of using the previous test code from their respective repositories, I created a benchmarking function that would allow me to manually run the test file and specify the number of cities as an input parameter. I chose to do manual runs because trying to do all testing at once would end up with me losing
progress due to a crash for a specific run- and I felt that wasn't efficient vs fine tuned single runs where I specify the number of cities as input.

Example: `node tsp-local-search.test.js 10` for running the local search implementation with 10 cities.

After running the benchmark, a line will be appended to a file called `output.txt`. Both HK and LS benchmarking logs will go to this same file. The following information about the runtime is appended to the text file:

`HK: ${n} number of cities, ${runtime in seconds} runtime, ${tourLength} tour length\n`;

or if LS run:

`LS: ${n} number of cities, ${runtime in seconds} runtime, ${tourLength} tour length\n`;

After this initial benchmarking code was setup, I went ahead and did manual runs for HK up until I saw a runtime of over an hour. Once that was complete, I then did the same for LS up until I noticed a significant uptrend in the tour length, which happened only with significantly larger inputs of the number of cities.

Finally, aftering having this finalized logfile that I've also uploaded to this repo as `output.txt`, I ran 2 python scripts to create a graphical representation of the data. 1 graph plotting the time against number of cities, and 1 graph plotting the tour times for both algorithms with the same input matrixes.

For Graph 1, I used `buildRandomMatrix()` as it is uploaded in this repository in order to populate the arrays with random distances, capped by a value of 10 for maxDistance. I did this in order to get a more normalized distribution of values for tour lengths.

For Graph 2 to ensure that both distance matrixes were the same, I used data from runs where I modified the `buildRandomMatrix()` function in both test code files to just use hardcoded incrementing sizes in the for loop. I took out the `Math.random()` basically:
```
function buildRandomMatrix(size, maxDistance = 10) {
  const m = Array.from({ length: size }, () => Array(size).fill(0));

  for (let index = 0; index < size; ++index) {
    for (let index_j = index + 1; index_j < size; ++index_j) {
      const d = index_j * maxDistance;
      m[index][index_j] = m[index_j][index] = d;
    }
  }

  return m;
}
```

- Used chatgpt to help create python scripts that created the graphs off of my output.txt data, specifically for how to create the x and y axis, and how to only label specific points for readability. All other code was written by me.

- Referenced https://nodejs.org/api/perf_hooks.html documentation for perf_hooks library to get
accurate emperical runtime measurements

- Reused code from my tsp-held-karp and tsp-local-search assignment repos.

"I certify that I have listed all sources used to complete this exercise, including the use of any Large Language Models. All of the work is my own, except where stated otherwise. I am aware that plagiarism carries severe penalties and that if plagiarism is suspected, charges may be filed against me without prior notice."
