//
//  main.swift
//  day-06-let's-review
//
//  Created by 이윤진 on 2022/01/13.
//

import Foundation
import Darwin

func printEven(arr: [String]) -> String {
    var even = ""
    for i in 0...arr.count-1 {
        if i % 2 == 0 {
            even = even + arr[i]
        }
    }
    return even
}

func printOdd(arr: [String])-> String {
    var odd = ""
    for i in 0...arr.count-1 {
        if i % 2 == 1 {
            odd = odd + arr[i]
        }
    }
    return odd
}

let numStrings = Int(readLine()!)!
for _ in 0...numStrings-1 {
    let inputString = readLine()!

    var arr = [String]()
    for char in inputString {
        arr.append(String(char))
    }
    print(printEven(arr: arr) + " " + printOdd(arr: arr))
}
