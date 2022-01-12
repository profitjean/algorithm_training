//
//  main.swift
//  day-02-operators
//
//  Created by 이윤진 on 2022/01/12.
//

import Foundation

/*
 * Complete the 'solve' function below.
 *
 * The function accepts following parameters:
 *  1. DOUBLE meal_cost
 *  2. INTEGER tip_percent
 *  3. INTEGER tax_percent
 */

func solve(meal_cost: Double, tip_percent: Int, tax_percent: Int) -> Void {
    // Write your code here
    print(Int(round(meal_cost + meal_cost * Double(tip_percent)/100.0 + meal_cost * Double(tax_percent)/100.0)))
    return 
}

guard let meal_cost = Double((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

guard let tip_percent = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

guard let tax_percent = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

solve(meal_cost: meal_cost, tip_percent: tip_percent, tax_percent: tax_percent)
