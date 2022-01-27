//
//  main.swift
//  Swift_Cote
//
//  Created by 이윤진 on 2021/09/02.
//

func checkJobEligibility() {

    var age = 80

    guard age >= 18, age <= 40 else { // 18-40이 아니라면
        print("Not Eligible for Job")
        return
    }

    guard age >= 41, age <= 80 else { // 41-80이 아니라면
        print("next time")
        return
    }
    print("You are eligible for this job")

}

checkJobEligibility()
