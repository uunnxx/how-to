import time
import net.http


resp := http.get('https://vlang.io/utc_now') or {
    println('Failed to fetch data from the server')
    return
}

// t := time.unix(resp.text.int()) // Response.text is deprecated

t := time.unix(resp.body.int())
println(t.format())
