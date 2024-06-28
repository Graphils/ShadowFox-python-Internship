def jumping_jacks():
    total_jacks = 100
    completed_jacks= 0
    while completed_jacks < total_jacks:
        print("Perform 10 jumping jacks!({completed_jacks+1}-{completed_jacks+10})")
        completed_jacks += 10
        response = input("Are you tired?(yes/no):")
        if response.lower() == "yes" or response.lower() == "Y":
            response = input("Do you want to skip the remaining sets?(yes/no):")
            if response.lower() == "yes" or response.lower() == "Y":
                print(f"You have completed a total number of {completed_jacks} jumping jacks")
            else:
                print("Congratulation, you completed the workout")
                jumping_jacks()
            