
// JavaScript code that zips list `as` and `bs` using a given function `f`
zipWith: function (f, as, bs) {
  var length = Math.min(as.length, bs.length);
  var zs = [];
  for (var i = 0; i < length; i++) {
    zs[i] = f(as[i], bs[i]);
  }
  return zs;
}
