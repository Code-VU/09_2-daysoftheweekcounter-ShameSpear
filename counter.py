def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    counts = {}
    final_count = {}
    with open(file_name) as file:
        for line in file:
            if line.startswith("From"):
                words = line.split()
                for word in words:
                    counts[word] = counts.get(word,0) + 1
                # if len(words) > 2:
                #     print(words[2])
                #     days += words[2]
                #     # print(days)
                    # for day in days:
                    #     print(day)
                        # counts[day] = counts.get(day, 0) +1

    for word,count in counts.items():
        if word == "Fri" or word == "Thu" or word == "Sat" or word == "Sun" or word == "Mon" or word == "Wed" or word == "Tue":
            final_count[word] = counts.get(word, count)
    
    print(final_count)



## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
