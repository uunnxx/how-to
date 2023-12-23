defmodule HelloModule do
  def run(str) do
    # str = String.reverse(str)
    # str = String.upcase(str)
    # IO.puts(str)
    # IO.inspect(str)
    str |> String.reverse() |> String.upcase() |> IO.puts()
  end
  
end


# HelloModule.run("Hello, World!")
"Hello, World!" |> HelloModule.run()
