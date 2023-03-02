# Question:
I just read about what send does in Ruby and I'm still confused when looking at this code.
(it's from a quiz but its past due date anyways)

```ruby
x = [1,2,3]
x.send :[]=,0,2
x[0] + x.[](1) + x.send(:[],2)
```
I understand that the first line assigns an array to x then I don't understand,
what ```:[] = ,0,2``` does at all and i dont understand why send is needed there I don't get,
what ```x.[](1)``` does and ```x.send(:[],2)``` do on the last line.

# Answers:
## First:
First of all, things like ```[]``` (array index) and ```[]=``` are just methods in Ruby.
```x``` is an Array, and arrays have a ```[]=``` method, which accepts two arguments, an index and a value to set.

Using send lets you pass an arbitrary "message" (method call) to object, with arbitrary parameters.

You could call ```x.send :sort```, for example, to send the "sort" message to the array.
Sort doesn't need any parameters, though, so we don't have to pass anything extra to it.

```x#[]=```, on the other hand, accepts two arguments. Its method can be thought of to look like this:

```ruby
def []=(index, value)
  self.set_value_at_index(index, value)
end
```

So, we can just invoke it with ```send :[]=, 0, 2,``` which is just like calling ```x[0] = 2```. Neat, huh?


## Second answer:

```ruby
# In Ruby, 
a[0] = 2
# is actually syntactic sugar for: 
a.[]=(0, 2).

```
Knowing this, that's what your second line does—it calls the ```[]= ```method with two arguments using metaprogramming,
as you correctly guessed.

This is the same for your third line: ```a[0]``` is syntactic sugar in Ruby for ```x.[](0)```.

The following code is a simpler equivalent to your example:
```ruby
x = [1, 2, 3]
x[0] = 2
x[0] + x[1] + x[2]
```

## Third answer:

Don't worry. Ruby can be a little bit tricky in these cases. Let's examine the code line by line:

```ruby
x = [1,2,3]
x.send :[]=,0,2
x[0] + x.[](1) + x.send(:[],2)
```
### First line
First line is clear to you: it assigns an array of three elements to x. And that's just about it.

### Second line
Second line calls the ```Object#send``` method of ```x``` passing a symbol
(remember that everything that starts with ```:``` is a symbol in ruby) 
```:[]=, 0 (a Fixnum) and 2 (another Fixnum)```.
Now you just have to take a look at what the send method does (as you said you've already done):

Invokes the method identified by symbol, passing it any arguments specified

This means that it will invoke the method identified by ```:[]=``` and pass ```0``` and ```2``` to it.
Now let's take a look at the ```Array#[]= method```.
This method definition (which can be overloaded by you if you need to do so) is:

```ruby
class Array
    # ...
    def []=(a, b)
        # ...
    end
end
```
This method is called by send as ```x.[]=(0, 2)``` which is pretty ugly if you ask me.
That's why Ruby defines a syntactic sugar version: ```x[0] = 2``` and in general:

```ruby
x.[]=(a, b)  -->  x[a] = b
```
In the Array case we also have the following:

```ruby
x.[](a)  -->  x[a]
```
In both cases you are free to call whatever version makes sense to you in the specific context.

### Third line
Now for the third and last line:
```ruby
x[0] + x.[](1) + x.send(:[],2)
```
things gets really tricky. Let's divide it into:
```ruby
x[0]
x.[](1)
x.send(:[], 2)
```
The first one is pretty straight forward. It returns the first element of the array.

The second one is the syntactic sugar that we have seen earlier which can be,
basically be converted into ```x[1]``` which returns the second element of the array.

The third one uses ```Object#send``` to call the method ```[]``` passing ```2``` to it.
Which means that it calls ```x.[](2)``` which means ```x[2]```.

### Conclusion
The code:

```ruby
x = [1,2,3]
x.send :[]=,0,2
x[0] + x.[](1) + x.send(:[],2)
```
can be converted using:
```ruby
x.send(:[]=, a, b)  -->  x.[]=(a, b)
x.send(:[], a)  -->  x.[](a)
x.[]=(a, b)  -->  x[a] = b
x.[](a)  -->  x[a]
```
to:
```ruby
x = [1,2,3]
x[0] = 2
x[0] + x[1] + x[2]
```
which can be reduced to:
```ruby
2 + 2 + 3
```
which results in:
```ruby
7
```


## Fourth:
```send``` is a way to achieve reflection calls in ```ruby```. Thus this line:
```ruby
x.send :[]=,0,2
Is equivalent to:

x[0] = 2
```
You read it that way: 
The name of the method is symbol (in your case ```[]=```) and then you pass in the parameters - ```0 and 2```.


``` 
# source: 
https://stackoverflow.com/questions/12892045/send-method-in-ruby#12892097
```
