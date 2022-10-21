message=input()

smile = message.count(":-)")
sad = message.count(":-(")

# 어떤 이모티콘도 포함되어 있지 않으면, none 을 출력한다.
if smile==0 and sad==0: 
    print("none")

# 행복한 이모티콘과 슬픈 이모티콘의 수가 동일하게 포함되어 있으면, unsure 를 출력한다.
elif smile==sad: 
    print("unsure")

# 행복한 이모티콘이 슬픈 이모티콘보다 많이 포함되어 있으면, happy 를 출력한다.
elif smile>sad: 
    print("happy")

# 슬픈 이모티콘이 행복한 이모티콘보다 많이 포함되어 있으면, sad 를 출력한다.
elif smile<sad: 
    print("sad")
