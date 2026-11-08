import json
# Rewards and Achievements
# SECTION: Calculate Student Rewards
def calculate_student_rewards(student_id):

    # Load registration records
    with open("data/registrations.json", "r") as file:
        registrations = json.load(file)

    # Count attended events
    events_attended = 0

    for registration in registrations:

        if (registration["student_id"] == student_id
                and registration["attendance"] == "Present"):

            events_attended += 1

    # Calculate points
    total_points = events_attended * 50

    if events_attended >= 5:
        total_points += 100

    if events_attended >= 10:
        total_points += 250

    return events_attended, total_points


# SECTION: Calculate Student Badges
def calculate_student_badges(events_attended):

    badges = []

    if events_attended >= 1:
        badges.append("First Step")

    if events_attended >= 5:
        badges.append("Event Explorer")

    if events_attended >= 10:
        badges.append("Event Champion")

    if events_attended >= 20:
        badges.append("Event Legend")

    return badges


# SECTION: View Student Rewards
def view_my_rewards(student):

    print("\n========================================")
    print("             MY REWARDS")
    print("========================================")

    # Save updated reward information
    save_student_rewards(student["student_id"])

    # Calculate attendance and points
    events_attended, total_points = calculate_student_rewards(
        student["student_id"]
    )
    student_level = calculate_student_level(total_points)
    student_badges = calculate_student_badges(events_attended)

    print("\nStudent:", student["full_name"])
    print("Events Attended:", events_attended)
    print("Total Points:", total_points)
    print("Student Level:", student_level)
    print("\nAchievement Badges:")

    if len(student_badges) == 0:
        print("No badges earned yet.")

    else:
        for badge in student_badges:
            print("-", badge)



# SECTION: Save Student Rewards
def save_student_rewards(student_id):

    # Calculate student's current points
    events_attended, total_points = calculate_student_rewards(student_id)
    student_level = calculate_student_level(total_points)
    student_badges = calculate_student_badges(events_attended)

    # Load existing reward records
    with open("data/rewards.json", "r") as file:
        rewards = json.load(file)

    # Check whether the student already has a reward record
    student_reward = None

    for reward in rewards:

        if reward["student_id"] == student_id:
            student_reward = reward
            break

    # Create a new reward record if one doesn't exist
    if student_reward is None:

        student_reward = {
            "student_id": student_id,
            "events_attended": events_attended,
            "total_points": total_points,
            "student_level": student_level,
            "badges": student_badges
        }

        rewards.append(student_reward)

    else:
        student_reward["events_attended"] = events_attended
        student_reward["total_points"] = total_points
        student_reward["student_level"] = student_level
        student_reward["badges"] = student_badges



    # Save updated reward records
    with open("data/rewards.json", "w") as file:
        json.dump(rewards, file, indent=4)



# SECTION: Calculate Student Level
def calculate_student_level(total_points):

    if total_points >= 2000:
        return "Platinum"

    elif total_points >= 1000:
        return "Gold"

    elif total_points >= 500:
        return "Silver"

    elif total_points >= 250:
        return "Bronze"

    else:
        return "Beginner"
