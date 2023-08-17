// Duration of your trace, in milliseconds
let TRACE_LENGTH;

// Array of length TRACE_LENGTH with your trace's values
let T;

// Value of performance.now() when you started recording your trace
let start;

const PERIOD_MS = 50;
const ONE_SECOND = 100;
if (PERIOD_MS > ONE_SECOND) throw "Bad PERIOD_MS";

const LINE_SIZE = 16; // in ints

const NUM_LINES = 1000;

function measure_memthroughput() {
  const M = new Array(LINE_SIZE * NUM_LINES);
  const stop = performance.now() + PERIOD_MS;
  let count = 0;
  while (performance.now() < stop) {
    for (let i = 0; i < NUM_LINES; i++) {
      let val = M[i * LINE_SIZE];
    }
    count++;
  }
  return count;
}

function record() {
  console.log("started record function...");

  // Create empty array for saving trace values
  T = new Array(TRACE_LENGTH);

  // Fill array with -1 so we can be sure memory is allocated
  T.fill(-1, 0, T.length);

  // Save start timestamp
  start = performance.now();

  // TODO (Exercise 2-2): Record data for TRACE_LENGTH seconds and save values to T.
  console.log("preparing to recording trace...");
  function iter(i) {
    if (i < TRACE_LENGTH) {
      console.log("scheduling next...");
      setTimeout(() => iter(i+1), ONE_SECOND);
    } else {
      // Once done recording, send result to main thread
      console.log("setting minimum to zero...");
      T = T.map(x => x - Math.min(...T));;
      console.log("sending result...");
      postMessage(JSON.stringify(T));
      console.log("done.")
    }
    console.log(`measure T[${i}]`);
    T[i] = measure_memthroughput();
  };
  console.log("recording trace...");
  iter(0);
}

// DO NOT MODIFY BELOW THIS LINE -- PROVIDED BY COURSE STAFF
self.onmessage = (e) => {
  if (e.data.type === "start") {
    TRACE_LENGTH = e.data.trace_length;
    setTimeout(record, 0);
  }
};

console.log("hello!");
