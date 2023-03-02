(function() {
    // a self contained "namespace"
    console.log(">> Console log")
    // an exposed closure

})(); // execute the function immediately

function Counter(start) {
    var count = start;
    return {
        increment: function() {
            count++;
        },

        get: function() {
            return count;
        }
    }
}

var foo = Counter(4);
foo.increment();
console.log(foo.get()); // 5
