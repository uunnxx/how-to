const log = (arg) => console.log(arg);
// log("Hello World"); // Hello World



const getLast = items =>
  items[items.length-1];


// console.log(getLast(['a', 'b', 'c', 'd'])); // d (1 iteration)
// console.log(getLast(['a', 'b', 'c', 'd', 'e', 'f', 'g'])); // g (1 iteration)


const findIndex = (items, match) => {
  for (let i = 0, total = items.length; i < total; i++)
    if (items[i] == match)
      return i;

  return -1;
};

const g = n => n + 1;
const f = n => n * 2;


const doStuff = x => {
  const afterG = g(x);
  const afterF = f(afterG);
  return afterF;
};

// console.log(doStuff(20));

// Every time you write a promise chain, you're composing functions:


// const g = n => n + 1;
// const f = n => n * 2;

const wait = time => new Promise(
  (resolve, reject) => setTimeout(
    resolve,
    time
  )
)

wait(300)
  .then(() => 20)
  .then(g)
  .then(f)
  .then(value => console.log(value))
