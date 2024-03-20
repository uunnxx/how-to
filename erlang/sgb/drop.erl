-module(drop).
-export([random/1]).
% -import(os, [timestamp/0]).
% -import(calendar, [universal_time/0]).

random(Rate) ->
    maybe_seed(),
    rand:uniform() =< Rate.


maybe_seed() ->
    case get(random_seed) of
        % undefined -> rand:seed(calendar:universal_time());
        % {X,X,X} -> rand:seed(calendar:universal_time());
        undefined -> rand:seed(erlang:timestamp());
        {X, X, X} -> rand:seed(erlang:timestamp());

        _ -> ok
    end.
