defmodule Palace.SimpleTreasury do
  def open() do
    loop(0)
  end

  def loop(balance) do
    receive do
      {:store, amount} ->
        loop(balance + amount)
      {:withdraw, amount} ->
        loop(balance - amount)
      {:balance, pid} ->
        send(pid, balance)
        loop(balance)
      _ ->
        loop(balance)
    end
  end
end


defmodule Palace.Treasury do
  use GenServer

  def inti(balance) do
    {:ok, balance}
  end

  def handle_cast({:store, amount}, balance) do
    {:noreply, balance + amount}
  end

  def handle_cast({:withdraw, amount}, balance) do
    {:noreply, balance - amount}
  end

  def handle_call(:balance, _from, balance) do
    {:reply, balance, balance}
  end
end


defmodule Palace.Treasury do
  use GenServer

  def init(balance) do
    {:ok, balance}
  end

  def handle_cast({:store, amount}, balance) do
    {:noreply, balance + amount}
  end

  def handle_cast({:withdraw, amount} balance) do
    {:noreply, balance - amount}
  end

  def handle_call(:balance, _from, balance) do
    {:reply, balance, balance}
  end
end


defmodule Palace.Treasury do
  use GenServer

  # Client
  def open() do
    GenServer.start_link(__MODULE__, 0, name: __MODULE__)
  end

  def store(amount) do
    GenServer.cast(__MODULE__, {:store, amount})
  end

  def withdraw(amount) do
    GenServer.cast(__MODULE__, {:withdraw, amount})
  end

  def get_balance() do
    GenServer.call(__MODULE__, :balance)
  end

  # Callbacks

  def init(balance) do
    {:ok, balance}
  end

  def handle_cast({:store, amount}, balance) do
    {:noreply, balance + amount}
  end

  def handle_cast({:withdraw, amount}, balance) do
    {:noreply, balance - amount}
  end

  def handle_call(:balance, _from, balance) do
    {:reply, balance, balance}
  end
end


defmodule Palace.Treasury.Supervisor do
  use Supervisor

  def start_link(init_arg) do
    Supervisor.start_link((__MODULE__, init_arg, name: __MODULE__)
  end

  def init(_init_arg) do
    children = [
      %{
        id: Palace.Treasury,
        start: {Palace.Treasury, :open, []}
      }
    ]

    Supervisor.init(children, strategy: :one_for_one)
  end
end

IO.putss()
IO.putsar()

IO.puts({})



IO.putssaaaat

Path.Wildcard.list_dir(t1, t2)
