# 혜성이는 승엽이의 이모티콘을 귀여운 척이라고 생각해 매우 싫어하므로, 
# 승엽이의 문자가 오면 전체적인 분위기만 판단해서 알려주는 프로그램을 작성하고 싶다.

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

