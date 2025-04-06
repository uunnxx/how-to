```

LogMessage -> LogFilter -> LogHandler
                               |
            ----------------------------------------
            |                  |                   |
       FileLogHandler  BufferLogHandler    NetworkLogHandler

```


```

LogMessage:

[class.function][severity][payload]

For example:

[Employee.remove()][ERROR][employee does not exist]

```
