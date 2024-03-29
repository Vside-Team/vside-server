import requests
import json
import time

headers = {"Content-Type": "application/json; charset=utf-8"}
url = "http://43.200.221.188:8080"
params = {}
category = [
    {"category": "분위기", "keyword": ["아련한", "몽환적인", "어두운", "흥미진진한", "먹먹한", "한적한", "스릴있는", "포근", "따뜻한"]},
    {"category": "장르",
     "keyword": ["에세이", "회귀물", "디스토피아", "SF소설", "단편소설", "웹소설", "커리어", "다큐멘터리", "논픽션", "장편소설", "인문철학", "동화", "문학",
                 "인문"]},
    {"category": "소재",
     "keyword": ["삶의지혜", "정신건강", "위로", "용기", "일하는방식", "번아웃", "갭이어", "진실", "동기부여", "교양", "모험", "폭력", "채식", "방관", "청소년",
                 "가면", "소통", "전쟁", "자아실현", "시골", "여유", "통제", "성장", "불안", "비운", "나만의속도", "호밀빵", "언어", "만남", "비움", "공감",
                 "부끄러움", "꿈", "공존", "휴머노이드", "비참"]},
    {"category": "특징", "keyword": ["쇼펜하우어", "곽재식단편선", "이집트역사", "부커상 수상작", "빛나는이야기"]},
]
contents = [
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/tooSoon/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/tooSoon/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/tooSoon/vside_tooSoon.html",
        "keywords": ["아련한", "에세이", "정신건강"],
        "contentMainKeyword": "삶의지혜",
        "contentTitle": "너무 빨리 지나가버린, \n너무 늦게 깨달아버린",
        "isBrightBg": "true",
        "lighterColor": "#1B312C",
        "darkerColor": "#6D2323",
        "uploadDate": "2022-11-16"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/midnight/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/midnight/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/midnight/vside_midnight.html",
        "keywords": ["몽환적인", "회귀물", "용기"],
        "contentMainKeyword": "위로",
        "contentTitle": "몇 번을 살아내야 우리는 \n후회하지 않을 수 있을까요",
        "isBrightBg": "false",
        "lighterColor": "#221B31",
        "darkerColor": "#333198",
        "uploadDate": "2022-11-16"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/greyMan/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/greyMan/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/greyMan/vside_greyMan.html",
        "keywords": ["SF소설", "단편소설", "웹소설", "어두운"],
        "contentMainKeyword": "디스토피아",
        "contentTitle": "인간이란 존재가 \n밑바닥까지 추락했을 때",
        "isBrightBg": "false",
        "lighterColor": "#1D4644",
        "darkerColor": "#0E463F",
        "uploadDate": "2022-11-16"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/yetAnything/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/yetAnything/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/yetAnything/vside_yetAnything.html",
        "keywords": ["일하는방식", "번아웃", "갭이어"],
        "contentMainKeyword": "커리어",
        "contentTitle": "우리는 아직 \n무엇이든 될 수 있다",
        "isBrightBg": "true",
        "lighterColor": "#664D28",
        "darkerColor": "#6F1E0C",
        "uploadDate": "2022-11-16"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/fish/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/fish/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/fish/vside_fish.html",
        "keywords": ["다큐멘터리", "논픽션", "용기"],
        "contentMainKeyword": "진실",
        "contentTitle": "물고기는 존재하지 않는다",
        "isBrightBg": "true",
        "lighterColor": "#3D164A",
        "darkerColor": "#11415B",
        "uploadDate": "2022-11-16"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/lifePain/main-mage.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/lifePain/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/lifePain/vside_lifePain.html",
        "keywords": ["교양", "인문철학", "쇼펜하우어"],
        "contentMainKeyword": "동기부여",
        "contentTitle": "사는 게 고통일 때",
        "isBrightBg": "true",
        "lighterColor": "#76391F",
        "darkerColor": "#135D7C",
        "uploadDate": "2022-11-30"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/rabbit/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/rabbit/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/rabbit/vside_rabbit.html",
        "keywords": ["단편소설", "곽재식단편선", "디스토피아"],
        "contentMainKeyword": "SF소설",
        "contentTitle": "공상 과학은 어쩌면 \n공상이 아닐지도 모른다",
        "isBrightBg": "true",
        "lighterColor": "#8E8E8E",
        "darkerColor": "#407E70",
        "uploadDate": "2022-11-16"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/ramses/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/ramses/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/ramses/vside_ramses.html",
        "keywords": ["흥미진진한", "이집트역사", "장편소설"],
        "contentMainKeyword": "모험",
        "contentTitle": "당신이 몰랐던 이집트 이야기",
        "isBrightBg": "true",
        "lighterColor": "#522314",
        "darkerColor": "#B85A26",
        "uploadDate": "2022-11-16"
    },

    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/vegetarian/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/vegetarian/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/vegetarian/vside_vegetarian.html",
        "keywords": ["폭력", "장편소설", "채식", "부커상 수상작"],
        "contentMainKeyword": "먹먹한",
        "contentTitle": "공공연한 폭력 앞에 우리는 \n어떤 사람인가요?",
        "isBrightBg": "false",
        "lighterColor": "#1B2131",
        "darkerColor": "#233259",
        "uploadDate": "2022-10-12"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/almond/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/almond/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/almond/vside_almond.html",
        "keywords": ["방관", "청소년", "문학"],
        "contentMainKeyword": "공감",
        "contentTitle": "우리는 아몬드를 갖고 있을까?",
        "isBrightBg": "false",
        "lighterColor": "#6B2222",
        "darkerColor": "#570825",
        "uploadDate": "2022-11-15"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/disqualified/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/disqualified/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/disqualified/vside_disqualified.html",
        "keywords": ["비참", "부끄러움", "문학", "어두운"],
        "contentMainKeyword": "가면",
        "contentTitle": "한 마디로 표현된 인생",
        "isBrightBg": "true",
        "lighterColor": "#B94818",
        "darkerColor": "#993500",
        "uploadDate": "2022-11-16"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/cat/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/cat/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/cat/vside_cat.html",
        "keywords": ["전쟁", "문학", "자아실현"],
        "contentMainKeyword": "소통",
        "contentTitle": "나를 알아가는 과정",
        "isBrightBg": "true",
        "lighterColor": "#05211F",
        "darkerColor": "#0D3B45",
        "uploadDate": "2022-11-07"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/kitchen/main-image1.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/kitchen/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/kitchen/vside_kitchen.html",
        "keywords": ["시골", "한적한", "여유"],
        "contentMainKeyword": "위로",
        "contentTitle": "자연으로 훌쩍 \n떠나고 싶은 그대에게",
        "isBrightBg": "true",
        "lighterColor": "#B4811F",
        "darkerColor": "#055538",
        "uploadDate": "2022-12-21"
    },
    {    # 반영X
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/main-image1.png",
        "coverImgLink": "123",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/vegetarian/vside_vegetarian.html",
        "keywords": ["어두운", "폭력", "스릴있는"],
        "contentMainKeyword": "통제",
        "contentTitle": "당신은 누구의 욕망대로 살고 있습니까?",
        "isBrightBg": "true",
        "lighterColor": "#000000",
        "darkerColor": "#FFFFFF"
    },
    {     # 반영X
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/main-image1.png",
        "coverImgLink": "123",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/vegetarian/vside_vegetarian.html",
        "keywords": ["불안", "문학", "먹먹한"],
        "contentMainKeyword": "성장",
        "contentTitle": "나 자신의 주인은 누구이지? 라는 생각이 들 때",
        "isBrightBg": "true",
        "lighterColor": "#000000",
        "darkerColor": "#FFFFFF"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/forest/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/forest/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/forest/vside_forest.html",
        "keywords": ["인문", "나만의속도", "호밀빵"],
        "contentMainKeyword": "비움",
        "contentTitle": "숲 한복판에서 만난 자유",
        "isBrightBg": "true",
        "lighterColor": "#C5A361",
        "darkerColor": "#766E28",
        "uploadDate": "2022-01-04"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/signLanguage/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/signLanguage/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/signLanguage/vside_signLanguage.html",
        "keywords": ["만남"],
        "contentMainKeyword": "언어",
        "contentTitle": "가장 솔직한 언어와의 만남",
        "isBrightBg": "true",
        "lighterColor": "#E3E4AA",
        "darkerColor": "#137E17",
        "uploadDate": "2022-12-31"
    },
    {
        "imgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/longNight/main-image.png",
        "coverImgLink": "https://s3.ap-northeast-2.amazonaws.com/vside.image/longNight/cover-image.png",
        "contentLink": "https://s3.ap-northeast-2.amazonaws.com/vside.contents/longNight/vside_longNight.html",
        "keywords": ["빛나는이야기", "동화"],
        "contentMainKeyword": "포근",
        "contentTitle": "이 밤이 사무치게 길더라도",
        "isBrightBg": "true",
        "lighterColor": "#8C782F",
        "darkerColor": "#0A5353",
        "uploadDate": "2022-01-04"
    }
]

for keyword in category:
    try:
        response = requests.post(url="http://127.0.0.1:8080/addCategory", json=keyword)
        time.sleep(0.1)
        print("성공")
    except:
        print("실패")

for content in contents:
    try:
        response = requests.post(url="http://127.0.0.1:8080/addContent", json=content)
        time.sleep(0.1)
        print("성공")
    except:
        print("실패")
