# call-seq:
#   Enumerator.product(*enums)                   -> enum
#   Enumerator.product(*enums) { |*args| block } -> return value of args[0].each_entry {}
def Enumerator.product(*enums, **nil, &block)
 # TODO: size should be calculated if possible
  return to_enum(__method__, *enums) if block.nil?

  enums.reverse.reduce(block) { |inner, enum|
    ->(*values) {
      enum.each_entry { |value|
        inner.call(*values, value)
      }
    }
  }.call()
end
