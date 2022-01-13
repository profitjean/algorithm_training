//
//  main.swift
//  day-05-loops
//
//  Created by 이윤진 on 2022/01/12.
//

import Foundation

guard let n = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

for i in 1...10 {
    print("\(n) x \(i) = \(n*i)")
}
