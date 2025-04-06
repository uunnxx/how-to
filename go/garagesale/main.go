package main


import (
    "net/http"
    "log"
    "fmt"
)


func main() {
    h := http.HandlerFunc(Echo)

    log.Println("Listening localhost:8000")

    if err := http.ListenAndServe("localhost:8000", h); err != nil {
        log.Fatal(err)
    }
}


// Echo just tells you about the request you made.
func Echo(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "You asked to", r.Method, r.URL.Path)
}
