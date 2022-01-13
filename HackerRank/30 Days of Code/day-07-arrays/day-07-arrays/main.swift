//
//  main.swift
//  day-07-arrays
//
//  Created by 이윤진 on 2022/01/14.
//

import Foundation

let num = Int(readLine()!)!

let arr = readLine()!.split(separator: " ").map{ Int($0)! }
guard arr.count == num else { fatalError("Bad Input") }

for i in (0...arr.count-1).reversed() {
    print("\(arr[i]) ", terminator: "")
    // terminator default는 \n이라서 ""으로 지정하면 한줄로 표현 가능하다.
}
