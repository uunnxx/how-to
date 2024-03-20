%%%-------------------------------------------------------------------
%% @doc stateful_otp_test public API
%% @end
%%%-------------------------------------------------------------------

-module(stateful_otp_test_app).

-behaviour(application).

-export([start/2, stop/1]).

start(_StartType, _StartArgs) ->
    stateful_otp_test_sup:start_link().

stop(_State) ->
    ok.

%% internal functions
