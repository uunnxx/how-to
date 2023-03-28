pub fn iteration() {
    // loop {
    //     println!("I loop forever!");
    // }

    // let mut n = 0;
    // while n < 10 {
    //     println!("{}", n);
    //     n = n + 1;
    // }

    for element in 1..10 {
        println!("{}", element);
    }

    let mylist = ["key1", "key2", "key3", "key4"];

    for element in mylist.into_iter() {
        println!("{}", element);
    }
}
