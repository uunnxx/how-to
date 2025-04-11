class Greeter<T> {
  greeting: T
  constructor(message: T) {
    this.greeting = message
  }
}

let greeter = new Greeter<string>('Hello, world')


# class Greeter:
#     greeter: string
#     
#     def __init__(self, message: str) {
#         self.message = message
#         
#         
# greeter = Greeter('Hello, world')
