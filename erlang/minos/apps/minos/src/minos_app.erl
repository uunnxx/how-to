%%%-------------------------------------------------------------------
%% @doc minos public API
%% @end
%%%-------------------------------------------------------------------

-module(minos_app).

-behaviour(application).

-export([start/2, stop/1]).

start(_StartType, _StartArgs) ->
    minos_sup:start_link().

stop(_State) ->
    ok.

%% internal functions
