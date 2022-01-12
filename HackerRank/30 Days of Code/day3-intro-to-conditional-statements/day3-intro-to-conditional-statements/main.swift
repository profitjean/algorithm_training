//
//  main.swift
//  day3-intro-to-conditional-statements
//
//  Created by 이윤진 on 2022/01/12.
//

import Foundation

guard let N = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

if N % 2 == 1 {
    print("Weird")
} else {
    switch N {
    case 6...20:
        print("Weird")
    default:
        print("Not Weird")
    }
}
